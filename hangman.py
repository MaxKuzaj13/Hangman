# import liberes
import os
import string
import requests
from random import randint
from datetime import datetime

# Can use class

'''
# class InvalidInputError(Except):
#	pass
	# raise InvalidInputError("Need a ... not number") """'''


def import_www():
	url = 'https://learn.code.cool/media/progbasics/countries-and-capitals.txt'
	r = requests.get(url)
	# r.encoding = 'cp1250'
	# print(r.text)
	return r.text


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
		sex_p = "Jesteś kobietą"
	else:
		sex_p = 'Jesteś mężczyzną'
	return sex_p


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
	test_value = True
	while test_value == True:
		lether = input('proszę podaj litere: ').lower()
		if len(lether) == 1 and lether in list(string.ascii_lowercase):
			test_value = False
		elif lether == 'exit' or lether == 'wyjscie' or lether == 'wyjście' or lether == '|':
			test_value = False
		else:
			print('podaj prawidłową litere')
			test_value = True

	return lether


def saving_result(life, name_player, start_time, answer):
	now = datetime.now()
	delta_time = (start_time-now).seconds
	try:
		f = open("hangman.txt", "a+")
	except:
		f = open("hangman.txt", "w+")

	line_add = name_player + ' | ' + now.strftime("%d-%b-%Y %H:%M:%S") + ' | ' + str(life) + ' | ' + str(delta_time) + ' | ' + answer + '\n'
	f.write(line_add)
	write_result()
	f.close()


def write_result():
	f = open("hangman.txt", "r")
	print('najlepsze wyniki: ')
	for line in f:
		print(line)


def main():
	os.system('clear')
	start_time = datetime.now()
	name_player = insert_name()
	sex_p = sex(name_player)
	answ = import_www()
	print(sex_p)
	answ_list = import_password_to_list(answ)
	ran_pass = random_password(answ_list)
	life = 5
	# do dodania import
	answer = ran_pass.lower()
	# answer_hide
	print(name_player + ' możesz zgadywać nasze hasło:')
	answer_hide = encripting(answer)

	while life > 0:
		lether = leteher_input()
		if sex_p == "Jesteś kobietą":
			print('Wybrałaś: ' + str(lether))
		else:
			print('Wybrałeś: ' + str(lether))

		answer_hide, life = checking_letters(answer_hide, answer, lether, life)
		
		if lether == 'exit' or lether == 'wyjscie' or lether == 'wyjście':
			break

		check_how_meny_lethers_left = answer_hide.count('*')

		if check_how_meny_lethers_left == 0:
			if sex_p == "Jesteś kobietą":
				print('Wygrałaś {} gratulacje'.format(name_player))
			else:
				print('Wygrałeś {} gratulacje'.format(name_player))
			# Wprowadzic zapis
			
			saving_result(life, name_player, start_time, answer)
			break

		print('Pozostało prób : ' + str(life))

	write_result()
	if life == 0:
		if sex_p == "Jesteś kobietą":
			print('przegrałaś {} zagraj jeszcze raz'.format(name_player))
		else:
			print('przegrałeś {} zagraj jeszcze raz'.format(name_player))


if __name__ == "__main__":
	main()
