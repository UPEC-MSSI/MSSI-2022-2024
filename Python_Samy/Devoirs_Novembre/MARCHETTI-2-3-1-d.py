# Samy Marchetti
import sys

#tableau = [3, 6, 8, 5, 10, 3, 7, 6, 3, 2]
i = len(sys.argv) - 1

while i >= (1):
	if(i == (len(sys.argv) - 1)):
		print("["+sys.argv[i]+", ", end = " ")
	if(i != 1) and (i !=(len(sys.argv) - 1)):
		print(sys.argv[i]+", ", end = " ")
	if(i == 1):
		print(sys.argv[i]+"]", end = " ")
	i = i - 1