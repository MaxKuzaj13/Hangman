# import liberes
import os
import string
import requests
from random import randint
from datetime import datetime

exit_code = ['exit', 'wyjscie', 'wyjście', 'quit', '|']
LIFE = 5


def import_www():
	try:
		url = 'https://learn.code.cool/media/progbasics/countries-and-capitals.txt '
		r = requests.get(url)
		comment = r.text
	except:
		print("wystąpił problem z połaczeniem z baza danych sprubuj później")
		exit()
		comment = 'wyjscie'
	return comment


def import_password_to_list(answ):
	answ_list = answ.split('\n')
	return answ_list


def random_password(answ_list):
	ran_num = randint(0, len(answ_list))
	ran_pass = answ_list[ran_num]
	return ran_pass


def insert_name():
	name_player = input('Wpisz swoje imię: ')
	return name_player


def sex(name_player):
	if list(name_player)[-1] == 'a':
		sex_man = False
	else:
		sex_man = True
	return sex_man


def checking_letters(answer_hide, answer, lether, life):
	if lether not in list(answer):
		print('pudło')
		life = life - 1
		print(''.join(answer_hide))

	else:
		print('trafiony')
		# jeżeli trafione to dodaj literę
		for i in range(len(answer_hide)):
			if answer[i] == lether:
				answer_hide[i] = lether

		print(''.join(answer_hide))
	return answer_hide, life


def encripting(answer):
	answer_hide = []
	for a in range(len(answer)):
		if answer[a] == ' ':
			answer_hide.append(' ')
		elif answer[a] == '|':
			answer_hide.append('|')
		else:
			answer_hide.append('*')
	print(''.join(answer_hide))
	print('', end='\n')
	return answer_hide


def leteher_input():
	while True:
		lether = input('proszę podaj litere: ').lower()
		if len(lether) == 1 and lether in list(string.ascii_lowercase):
			break
		elif lether in exit_code:
			break
		else:
			print('podaj prawidłową litere')

	return lether


def saving_result(life, name_player, start_time, answer):
	now = datetime.now()
	delta_time = (start_time - now).seconds
	try:
		f = open("hangman.txt", "a+")
	except:
		f = open("hangman.txt", "w+")

	line_add = name_player + ' | ' + now.strftime("%d-%b-%Y %H:%M:%S") + ' | ' + str(life) + ' | ' + str(
		delta_time) + ' | ' + answer + '\n'
	f.write(line_add)
	write_result()
	f.close()


def write_result():
	f = open("hangman.txt", "r")
	print('najlepsze wyniki: ')
	for line in f:
		print(line)


def testing_sex(sex_man):
	test_sex = 'n'
	while not test_sex == 't':

		if sex_man is True:
			test_sex = input("Jesteś Mężczyzną? wybierza 't' aby potwierdzić i 'n' aby zaprzeczyć \n").lower()
			if test_sex == 'n':
				sex_man = False
			else:
				pass
		else:
			test_sex = input("Jesteś Kobietą? wybierza 't' aby potwierdzić i 'n' aby zaprzeczyć \n").lower()
			if test_sex == 'n':
				sex_man = True
			else:
				pass
	return sex_man


def print_if_left_zero(life, sex_man, name_player):
	if life == 0:
		if sex_man is False:
			print('przegrałaś {} zagraj jeszcze raz \n'.format(name_player))
		else:
			print('przegrałeś {} zagraj jeszcze raz \n'.format(name_player))


def main():
	os.system('clear')
	start_time = datetime.now()
	name_player = insert_name()
	sex_man = sex(name_player)

	sex_man = testing_sex(sex_man)
	answ = import_www()

	answ_list = import_password_to_list(answ)
	ran_pass = random_password(answ_list)
	life = LIFE
	# do dodania import
	answer = ran_pass.lower()
	# answer_hide
	print(name_player + ' możesz zgadywać nasze hasło (hasło jest w języku angielskim i zawiera nazwę stolicy oraz nazwe państwa w którym się znajduje:')
	answer_hide = encripting(answer)

	while life > 0:
		lether = leteher_input()
		os.system('clear')
		print('Wybrałaś: ' if sex_man is False else 'Wybrałeś: ' + lether)

		answer_hide, life = checking_letters(answer_hide, answer, lether, life)

		if lether in exit_code:
			break

		check_how_meny_lethers_left = answer_hide.count('*')

		if not check_how_meny_lethers_left:
			if sex_man is False:
				print('Wygrałaś {} gratulacje'.format(name_player))
			else:
				print('Wygrałeś {} gratulacje'.format(name_player))
			# Wprowadzic zapis

			saving_result(life, name_player, start_time, answer)
			break

		print('Pozostało prób : ' + str(life))
		print()
	print_if_left_zero(life, sex_man, name_player)

	write_result()


if __name__ == "__main__":
	main()
