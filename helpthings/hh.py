import os 

for t in range(2):
	os.fork()
	print('-')
