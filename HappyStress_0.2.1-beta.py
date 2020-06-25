#!/usr/bin/python3
"""
HappyStress_0.2.1-beta.py
2020 (C) Nikolas A. Wagner
License: GNU GPLv3

Build_0023

					-- Purpose --
Stress test CPU for its single-threaded performance
 
"""
# ---------------------------------------------------------------------
# if this is the last thing you see in your terminal after a crash, then
# SOMETHING IS VERY WRONG 0_o
print('Compiled without errors! Binary has been executed..')
# ---------------------------------------------------------------------
# get script process start time
import decimal
import time as t
start_time_INIT = t.process_time()

import subprocess as sp
from os import system, get_terminal_size, getcwd

system('clear && printf "Initializing..\n\n"')
t.sleep(0.5)

try: import pyfiglet
except ImportError as err:
	print('{}\n\nLet me just install that for you quick quick :D'.format(err))
	t.sleep(2)

	system('pip3 install pyfiglet==0.7')
	try: import pyfiglet
	except Exception as fatalErr: print(fatalErr)
except Exception as fatalErr: print(fatalErr)

def EXIT(reason):
	global start_time_INIT
	exit_time = get_uptime(start_time_INIT)

	print('\n\n\nFinal Script Uptime: {}'.format(exit_time))
	print('\n\n{}\nGoodbye!\n'.format(reason))

	system('pkill python; pkill python3; history -c')
	if __name__ == '__main__':
		exit()

def INIT():
	global C

	print('INIT(): calculating 426880 * sqrt of 10,005')
	C = 426880 * decimal.Decimal(10005).sqrt()
	print('INIT(): defining global variables..')

try: INIT()
except: EXIT('unexpected error in INIT()..')

scriptName = 'HappyStress_0.2.1-beta.py'; build = 23
copyRight = '2020 (C) Nikolas A. Wagner'
license = 'Distributed with the GNU GPLv3 license'
py3_version = sp.getoutput('python3 --version')
bash_version = sp.getoutput('bash --version | grep version | grep bash')

times = []; file_data = ''; txtPi = ''
final_k = 1; loop_n = 0; n = 0
C = decimal.Decimal(0)

scriptTitle = '\_ HappyStress _/'

# script settings are setup so you can simply add/rm new settings to this
# dictionary, and the menu_userSetup function will handle the changes
defaultSettings = {
	'printPi': True,
	'slowMode': True,
	'Balanced test testCount': 25,
	'Balanced test digits': 150000,
	'ALU test testCount': 15,
	'ALU test digits': 2000000,
	'Save Location': './HappyStress_results/'
}

# ---------------------------------------------------------------------
# defining all remaining functions
print('script: defining functions..')
def MAIN():
	global times, user_settings

	menu_main()

	print('\r\033[KMAIN(): Initialization complete!', end='')
	print('\r\033[KMAIN(): Starting ALU_Spike test..', end='')
	t.sleep(1)
	spiked_test(
		'ALU_Spike',
		'alu-spike_pre',
		54353459,
		834534534,
		426880,
		10005,
		5000000
	)

	refresh_UI(scriptTitle, py3_version, bash_version, True)

	print('\n', '\r\033[KMAIN(): Starting memory access time test..', end='')
	t.sleep(1); times = []
	looped_test(
		'memory access',
		'mem',
		2000,
		42,
		False,
		False
	)

	refresh_UI(scriptTitle, py3_version, bash_version, True)

	print('\r\033[KMAIN(): Starting balanced test..', end='')
	t.sleep(1); times = []
	looped_test(
		'balanced',
		'bal',
		user_settings['Balanced test testCount'],
		user_settings['Balanced test digits'],
		user_settings['slowMode'],
		user_settings['printPi']
		)

	refresh_UI(scriptTitle, py3_version, bash_version, True)

	print('\r\033[KMAIN(): Starting ALU test..', end='')
	times = []
	looped_test(
		'ALU',
		'alu',
		user_settings['ALU test testCount'],
		user_settings['ALU test digits'],
		user_settings['slowMode'],
		user_settings['printPi']
	)

	refresh_UI(scriptTitle, py3_version, bash_version, True)

	print('\r\033[KMAIN(): Starting ALU_Spike test..', end='')
	times = []
	spiked_test(
		'ALU_Spike',
		'alu-spike_post',
		54353459,
		834534534,
		426880,
		10005,
		5000000
	)

	time_since_INIT = get_uptime(start_time_INIT)
	return time_since_INIT

# ---------------------------------------------------------------------
# core functions
def compute_pi(testName, dgts, testCount, slowMode, printPi):
	global final_k, txtPi, loop_n, C, txtPi
	dgts += 1; x = 0

	decimal.getcontext().prec = 1
	decimal.getcontext().prec = dgts

	if slowMode is True:
		C = 426880 * decimal.Decimal(10005).sqrt()
	elif slowMode is False and loop_n == 0:
		C = 426880 * decimal.Decimal(10005).sqrt()

	K = 6.0; M = 1.0; X = 1
	L = 13591409; S = L

	print('\r\033[Kcalculating lastPi...', end='')
	lastPi = decimal.Decimal(C / S)

	for k in range(dgts):
		print('\r\033[Kcalculating M...', end='')
		M = M * (K ** 3 - 16 * K) / ((k + 1) ** 3)
		print('\r\033[Kcalculating L...', end='')
		L += 545140134
		print('\r\033[Kcalculating X...', end='')
		X *= -262537412640768000
		print('\r\033[Kcalculating S...', end='')
		S += decimal.Decimal(M * L) / X
		print('\r\033[Krecalculating Pi...', end='')
		pi = decimal.Decimal(C / S)
		txtPi = pi
		
		if printPi is True:
			print('\r\033[K{}\n\nRunning {} test {} of {}'.format(pi, testName, loop_n + 1, testCount))
		else:
			system('clear')
			print('\r\033[K\n\nRunning {} test {} of {}'.format(testName, loop_n + 1, testCount))

		if x == 0 and slowMode is True:
			uptime = get_uptime(start_time_INIT)
			print('\nScript Uptime: {}'.format(uptime))
			print('calculating k = {}...\n'.format(k))

		if lastPi != pi:
			if slowMode is True:
				print('\nAccuracy improved from k = {}'.format(k), end='')
			final_k = k; lastPi = pi
		else:
			x += 1
			print("\ncompute_pi(): Pi not changed {} time/s\n".format(x), end='')

			if x >= 10:
				if printPi is True:
					system('clear')
					print('\n{}'.format(pi))

				if slowMode is True:
					print("\ncompute_pi(): {} digits of precision achieved in {} iterations!".format(dgts - 1, final_k))
					t.sleep(1)

				system('history -c')
				return pi

def run_compute_pi(testName, dgts, testCount, slowMode, printPi):
	global loop_n

	# get process start time for the test
	startTime = t.process_time()
	result = compute_pi(testName, int(dgts), testCount, slowMode, printPi, )
	uptime = get_uptime(startTime)

	cw_dir = getcwd()
	system('mkdir ./HappyStress_results > /dev/null 2>&1 || exit')

	f = open('./HappyStress_results/pi_final_{}.txt'.format(dgts), 'w+')
	f.write('{}'.format(txtPi)); f.close()
	system('cd {}'.format(cw_dir))

	if slowMode is True and printPi is True:
		print(result)
		print("\nTest #{} took {} seconds\n\n".format(loop_n + 1, uptime))
		t.sleep(2)
	elif slowMode is True and printPi is False:
		print("\nTest #{} took {} seconds\n\n".format(loop_n + 1, uptime))
		t.sleep(2)

	return uptime

def looped_test(testName, tag, testCount, dgts, slowMode, printPi):
	global times, loop_n
	print('Initializing {} test 1 of {}..'.format(testName, testCount), end='')

	start_time_looped = t.process_time()
	avg_time = decimal.Decimal(0)

	for n in range(testCount):
		loop_n = n
		times.append(run_compute_pi(testName, dgts, testCount, slowMode, printPi)) #run_compute_pi() returns uptime of pi calculation
		
		if n < testCount - 1 and slowMode is True:
			print('\rInitializing {} test {} of {}'.format(testName, loop_n + 2, testCount), end='')
	
	test_time = get_uptime(start_time_looped)
	avg_time = round(avg_list(times), 5)
	
	if slowMode is True:
		results = print_loop_results(
			test_time, times, avg_time, testCount, dgts
		)
		print('5.. ', end=''); t.sleep(1)
		print('4.. ', end=''); t.sleep(1)
		print('3.. ', end=''); t.sleep(1)
		print('2.. ', end=''); t.sleep(1)
		print('1.. ', end=''); t.sleep(1)

	store_loop_results(tag, test_time, times, avg_time, testCount, dgts)
	print()

def spiked_test(testName, tag, x, y, n, sqrt, prec):
	start_time_mult = t.process_time()
	print('\r\033[K{}:\n'.format(testName))
	print('\r\033[KCalculating {} * {}'.format(x, y), end='')

	result_mult = mult(x, y)
	test_time = get_uptime(start_time_mult)
	print('\r\033[KCalculated {} in {} seconds!\n'.format(result_mult, test_time))

	#print_spike_results()
	store_spike_results('{}.mult'.format(tag), 'Single repeated-addition test', test_time, x, '*', y, result_mult)

	if n and sqrt is not None:
		start_time_div = t.process_time()
		print('\r\033[KCalculating {} / sqrt of {} (prec = {})'.format(n, sqrt, prec), end='')

		result_div = div(n, sqrt, prec)
		test_time = get_uptime(start_time_div)
		print('\nCalculated the division in {} seconds!\n'.format(test_time))

		#print_spike_results()
		store_spike_results('{}.div'.format(tag), 'High-precision square root test', test_time, x, '/ sqrt of {}'.format(sqrt), y, result_div)

def threaded(testName, tag, testCount):
# 	import threading
# 	thread_mult = threading.Thread(target=mult, args=())
# 	thread_div = threading.Thread(target=div, args=())

	pass

def run_threaded(testName, tag, testCount):
	pass

def threaded_test(testName, tag, testCount):
	pass

# ---------------------------------------------------------------------
# pure functions	
def refresh_UI(scriptTitle, info1, info2, clearScreen):
	global scriptName, build, copyRight, license

	if clearScreen is True:
		system('clear')

	COLS = get_terminal_size().columns
	t = pyfiglet.Figlet(font='big', width=COLS, justify='center')

	print('{} | Build {}'.format(scriptName, str(build)))
	print('{}\n{}'.format(copyRight, '-' * 32))
	print('{}\n{}\n{}\n'.format(info1, info2, '-' * 41))
	print('{}\n\n{}\n'.format(license, '-' * 41))
	print (t.renderText(scriptTitle))

def get_uptime(start_time):
	return t.process_time() - start_time

def avg_list(this_list):
	summed = decimal.Decimal(0)

	for item in this_list:
		try: item = decimal.Decimal(item)
		except: print("\n'item' cannot be coverted to type 'decimal'\n")
		summed += item

	avg = summed / decimal.Decimal(len(this_list))
	return avg

def mult(x, n):
	z = x
	for i in range(n - 1):
		z += x
	return z

def div(n, sqrt, prec):
	decimal.getcontext().prec = 1
	decimal.getcontext().prec = prec

	# suggested values for x, sqrt = 4268809, 10005
	return n / decimal.Decimal(sqrt).sqrt()

# ---------------------------------------------------------------------
# menu functions
def menu_main():
	refresh_UI(scriptTitle, py3_version, bash_version, True)

	print("Press enter to begin or enter 's' to change settings! ", end='')
	r = input()
	print('\033[F\033[K', end='')

	if r == 's':
		menu_userSetup()

def menu_userSetup():
	global user_settings
	selection = None; selected_key = None

	if user_settings is None:
		user_settings = defaultSettings

	refresh_UI('\_ Test Setup _/', py3_version, bash_version, True)

	COLS = get_terminal_size().columns
	print('\n', 'Current Settings:'.center(COLS))

	z = 0
	for setting in user_settings:
		# print('{}. {}: {}'.center(COLS - (COLS // 50)).format(z, setting, user_settings[setting]), end='\r')
		print('{}. {}: {}'.center(COLS - ((len(setting) + len(str(user_settings[setting]))) // 2)).format(z, setting, user_settings[setting]), end='\r')
		z += 1

	print("\n Enter '-1' to return\n", 'Which setting would you like to set?'.center(COLS), end='')
	try: selection = int(input('{}'.format(' ' * (COLS // 2))))
	except KeyboardInterrupt: EXIT('Detected KeyboardInterrupt..')
	except:
		print('\n', 'Oops. That input is invalid!'.center(COLS))
		t.sleep(1.5)
		menu_userSetup(); return 1

	# the tuple function is used to return the key string according to its unordered index
	try: selected_key = tuple(user_settings.items())[selection][0]
	except KeyboardInterrupt: EXIT('Detected KeyboardInterrupt..')
	except:
		print('\n', 'That is not an available option!'.center(COLS))
		t.sleep(1.5)
		menu_userSetup(); return 1

	if selection == -1:
		MAIN(); exit()
	elif selection < -1:
		print('\n', 'That is not an available option!'.center(COLS))
		t.sleep(1.5)
		menu_userSetup(); return 1

	refresh_UI('\_ Test Setup _/', py3_version, bash_version, True)

	COLS = get_terminal_size().columns
	print('\n', 'Ok, {} selected!'.center(COLS - (COLS // 50)).format(selected_key))
	print('Type in your new setting:'.center(COLS))
	new_set = input('{}'.format(' ' * (COLS // 2)))

	if new_set.find('true') and new_set.find('t') != -1:
		new_set = True
	elif new_set.find('false') and new_set.find('f') != -1:
		new_set = False

	if new_set is not None or '':
		user_settings[selected_key] = new_set
		print('\n', '{} has been set to {}!'.center(COLS - (COLS // 50)).format(selected_key, new_set))
		t.sleep(1.5)
	else:
		print('\n', 'Oops. That input is invalid!'.center(COLS))
		t.sleep(1.5)
		menu_userSetup()

	refresh_UI('\_ Test Setup _/', py3_version, bash_version, True)
	COLS = get_terminal_size().columns

	print('\n', 'Current Settings:'.center(COLS))

	z = 0
	for setting in user_settings:
		print('{}. {}: {}'.center(COLS - (COLS // 50)).format(z, setting, user_settings[setting]), end='\r')
		z += 1

	menu_userSetup(); return

	MAIN(); return 1

# ---------------------------------------------------------------------
# other impure functions
def print_loop_results(totTime, testTimes, avgTime, testCount, dgts):
	global start_time_INIT
	script_time = get_uptime(start_time_INIT)

	print('\n\nRESULTS:\n{}'.format('-' * 7))
	result = 'Script Uptime: {}\n'.format(script_time)
	result += str(print('Tests performed: {}\nTotal elapsed time: {} seconds\n'.format(testCount, round(totTime, 5))))
	result += str(print('This computer takes {} seconds on average to calculate {} digits of pi!\n'.format(avgTime, dgts)))
	result += str(print('\nTest Times:\n{}'.format('-' * 12)))

	z = 1
	for i in times:
		if z < 10:
			result += str(print('Test 0{}: {}'.format(z, i)))
			z += 1
		elif z < 100:
			result += str(print('Test {}: {}'.format(z, i)))
			z += 1
		elif z < 1000:
			result += str(print('T#  {}: {}'.format(z, i)))
			z += 1
		else:
			result += str(print('T# {}: {}'.format(z, i)))
			z += 1

	return result

def print_spike_results(tag, desc, totTime, x, sym, y, result):
	pass
	global start_time_INIT

	print('\n\nRESULTS:\n{}'.format('-' * 7))
	result += 'Script Uptime: {}\n'.format(script_time)
	result = str(print('Tests performed: {}\nTotal elapsed time: {} seconds\n'.format(testCount, round(totTime, 5))))
	result += str(print('This computer takes {} seconds on average to calculate {} digits of pi!\n'.format(avgTime, dgts)))
	result += str(print('\nTest Times:\n{}'.format('-' * 12)))

	z = 1
	for i in times:
		if z < 10:
			result += str(print('Test 0{}: {}'.format(z, i)))
			z += 1
		elif z < 100:
			result += str(print('Test {}: {}'.format(z, i)))
			z += 1
		elif z < 1000:
			result += str(print('T#  {}: {}'.format(z, i)))
			z += 1
		else:
			result += str(print('T# {}: {}'.format(z, i)))
			z += 1
	script_time = get_uptime(start_time_INIT)
	return result

def store_loop_results(tag, totTime, testTimes, avgTime, testCount, dgts):
	global start_time_INIT
	script_time = get_uptime(start_time_INIT)

	cw_dir = getcwd()
	system('mkdir ./HappyStress_results > /dev/null 2>&1 || exit')

	fID = str(int(t.process_time()))
	f = open('./HappyStress_results/piStress_{}_{}.txt'.format(tag, fID[:-6:-1]), 'w+')
	f.write('Script Uptime: {}\n'.format(script_time))
	f.write('Tests Performed: {}\n'.format(testCount))
	f.write('Pi Digits (calculated per test): {}\n\n'.format(dgts))

	f.write('Test Time (total): {}\n'.format(totTime))
	f.write('Test Time (average): {}\n\n'.format(avgTime))
	f.write('Times:\n')

	z = 1
	for i in testTimes:
		if z < 10:
			f.write('Test 0{}: {}\n'.format(z, i))
			z += 1
		elif z < 100:
			f.write('Test {}: {}\n'.format(z, i))
			z += 1
		elif z < 1000:
			f.write('T#  {}: {}\n'.format(z, i))
			z += 1
		else:
			f.write('T# {}: {}\n'.format(z, i))
			z += 1

	f.close()
	system('cd {}'.format(cw_dir))

def store_spike_results(tag, desc, totTime, x, sym, y, result):
	global start_time_INIT
	script_time = get_uptime(start_time_INIT)

	cw_dir = getcwd()
	system('mkdir ./HappyStress_results > /dev/null 2>&1 || exit')

	fID = str(int(t.process_time()))
	f = open('./HappyStress_results/piStress_{}_{}.txt'.format(tag, fID[:-6:-1]), 'w+')
	f.write('Script Uptime: {}\nTest Time (total): {}\n'.format(script_time, totTime))
	f.write('{}\n\n'.format(desc))

	if tag.find('.div') != -1:
		f.write('Calculation Performed: {} {} = {}\n'.format(x, sym, result))
	elif tag.find('.mult') != -1:
		f.write('Calculation Performed: {} {} {} = {}\n'.format(x, sym, y, result))

	f.close(); system('cd {}'.format(cw_dir))

# ---------------------------------------------------------------------
# try running MAIN, catch exceptions, finally exit()
print('script: functions are all defined. try-catching MAIN()..\n\n')
try:
	upTime = MAIN()
	if upTime:
		EXIT('Thanks for using HappyStress!')
	else:
		EXIT('unexpected error in MAIN()..')		
except KeyboardInterrupt:
	EXIT('Detected KeyboardInterrupt..')
#except NameError as error:
	EXIT('Detected NameError\n\n{}..'.format(error))

if __name__ == '__main__':
	exit()
