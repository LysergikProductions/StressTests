"""
pi.py
# 2020 (C) Nikolas A. Wagner
# License: GNU GPLv3

# Build_005

                   -- Purpose --
 Stress test CPU for its sigle-threaded performance
 
 """

import os; import sys
import decimal; import time
startTime = time.time()
txtPi = ""; final_k = 1; its = 1
decimalArgs = decimalArgs = decimal.Decimal(0)

def INIT():
	global decimalArgs
	os.system('clear && printf "Initializing..\n"')
	try:
		args = int(sys.argv[1]); print(args)
		decimalArgs = decimal.Decimal(args)
	except:
		print("""I can't do that! I need a single number with no extra symbols!\n""")
	finally:
		if decimalArgs < 1:
			decimalArgs = 1
		elif decimalArgs > 10000000:
			decimalArgs = 10000000
		elif not decimalArgs:
			print('you need to enter a number!')

INIT()

def getUptime():
	return time.time() - startTime

def compute_pi(n):
	decimal.getcontext().prec = n + 1
	global final_k

	its = n; n += 11
	x = 0
	C = 426880 * decimal.Decimal(10005).sqrt()

	K = 6.0; M = 1.0; X = 1
	L = 13591409; S = L

	for k in range(1, n):
		print('calculating..')
		lastPi = C / S
		M = M * (K ** 3 - 16 * K) / ((k + 1) ** 3)
		L += 545140134
		X *= -262537412640768000
		S += decimal.Decimal(M * L) / X
		pi = C / S

		os.system('clear')
		print('{0}\n'.format(pi))

		if lastPi != pi:
			print('Accuracy improved from iteration {0}'.format(k))
			final_k = k
		else:
			x += 1
			print("Pi not changed {0} time/s".format(x))

			if x >= int(10):
				os.system('history -c && clear')
				print(pi)
				print("\n{0} digits of precision achieved in {1} iterations!".format(its, final_k))

				global txtPi; txtPi = str(pi)
				return ""

def MAIN():
	result = compute_pi(int(decimalArgs)); print(result)
	f = open('pi.txt', 'w+'); f.write(txtPi)

	uptime = str(getUptime())
	print("This took {0} seconds\n".format(uptime))

MAIN()