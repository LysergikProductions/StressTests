#!/usr/bin/python3
"""
binet.py | Build_0002
2020 (C) Nikolas A. Wagner
License: GNU GPLv3

	-- Purpose --
Calculate Nth digit of Pi
 
"""
# ---------------------------------------------------------------------
print('Compiled without errors! Binary has been executed..')
# ---------------------------------------------------------------------

import time as t
start_time_INIT = t.time()

import decimal as d
import subprocess as sp
from os import system, path

system('clear && printf "Initializing..\n\n"')

# ---------------------------------------------------------------------
def EXIT(reason):
	global start_time_INIT

	exit_time = get_uptime(start_time_INIT)

	print('\n\n\nFinal Script Uptime: {}\n\n'.format(exit_time))
	if reason is not None:
		print('Error:\n{}\n\nGoodbye!\n'.format(reason))

	system('pkill python; pkill python3; history -c')
	exit()

build = 2
scriptName = path.basename(__file__)
copyRight = '2020 (C) Nikolas A. Wagner'
license = 'Distributed with the GNU GPLv3 license'

py3_version = sp.getoutput('python3 --version')
bash_version = sp.getoutput(
	'bash --version | grep version | grep bash'
)

prec = 1000000
phi = d.Decimal(0)

def INIT():
	global phi

	print(
		'\r\033[KCalculating golden ratio to precision of {}'
		.format(prec),
		end=''
	)
	phi = compute_golden(prec)
	system('clear')

# ---------------------------------------------------------------------
print('\r\033[Kscript: defining functions..', end='')
def MAIN():
	INIT(); system('clear')

	while True:
		print('\nEnter any number position of the fib sequence:')
		try: n = int(input())
		except ValueError as err:
			EXIT(err)

		try: int(n)
		except ValueError:
			try: float(n)
			except ValueError as err:
				#print('user entered string'); t.sleep(1) #DEBUG LINE
				EXIT(err)
			else:
				#print('user entered float'); t.sleep(1) #DEBUG LINE
				n = d.Decimal(n)
				print("Can't accept floats atm sorry")
				continue
		except:
			EXIT(error)
		else:
			#print('user entered int'); t.sleep(1) #DEBUG LINE
			pass

		strN = str(n)
		if '.' not in strN:
			if strN[-1] == '1' and int(n) != 11:
				suff = 'st'
			elif strN[-1] == '2' and int(n) != 12:
				suff = 'nd'
			elif strN[-1] == '3' and int(n) != 13:
				suff = 'rd'
			else:
				suff = 'th'
		else:
			suff = ' th'

		answer = compute_binet(d.Decimal(phi), n)

		if round(answer) == 0:
				answer = 0

		system('clear')
		print(
			'\nThe {}{} number of the Fibonacci sequence is:\n\n{}\n'
			.format(
				n, suff, round(answer)
			)
		)
	
	return 1

# ---------------------------------------------------------------------
# core functions
def compute_golden(x):
	d.getcontext().prec = x
	return (d.Decimal(5).sqrt() + 1) / d.Decimal(2)

def compute_binet(gold, n):
	if n < 1000:
		precbin = 1000
	else:
		precbin = abs(n)

	d.getcontext().prec = precbin

	numerator = (
		d.Decimal(gold ** n) -\
		(d.Decimal(-1 / gold) ** n)
	)
	denominator = d.Decimal(5).sqrt()

	return numerator / denominator

# ---------------------------------------------------------------------
# pure functions	
def get_uptime(start_time):
	return t.time() - start_time

# ---------------------------------------------------------------------
# impure functions
def impure_function1():
	pass

# ---------------------------------------------------------------------
# try running MAIN, catch exceptions, finally exit()
print('\r\033[Kscript: functions are all defined. try-catching MAIN()..', end='')

try: upTime = MAIN()		
except KeyboardInterrupt:
	EXIT('Detected KeyboardInterrupt..')
except NameError as error:
	EXIT('Detected NameError\n\n{}..'.format(error))
else:
	if upTime is not False:
		EXIT(None)
	else:
		EXIT('unexpected error in MAIN()..')

if __name__ == '__main__':
	exit()