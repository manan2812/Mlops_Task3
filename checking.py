programfile = open('/root/mlopsws/machine_learning.py','r')	#connecting to the code file
code = programfile.read()				#reading the code file

if 'keras' or 'tensorflow' in code:			#because keras or tensorflow keyword is a must for a deep learning program
	if 'Conv2D' in code:				#beacuse if a code is of CNN conv2D layer is a must 
		print('OK')
	else:
		print('not OK')
else:
	print('NOT A NEURAL NETWORK')
