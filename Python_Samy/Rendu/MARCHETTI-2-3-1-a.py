# Samy Marchetti
import sys

#tableau = [3, 6, 8, 5, 10, 3, 7, 6, 3, 2]
i = 1

while i <= (len(sys.argv) - 1):
	if (i == (len(sys.argv) - 1)):
		print(sys.argv[i])
	if (i < (len(sys.argv) - 1)):
		print(sys.argv[i], "# ", end ="")
	i = i + 1