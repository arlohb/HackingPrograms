#!/usr/bin/python3

#used to run shell commands
import os

#used to get command line arguments
import sys

#===========================CONFIG=====================================#
#used to find the pid of the ssh connection
command = "ps auxwww | grep sshd | grep -v grep"

#filename of the output file
fileName = "file.tx"


#===========================FUNCTIONS==================================#

#show the command and output file used
def printInfo():
	print("The command used to find the connection:")
	print("   "+command)
	
	print("The file outputting to:")
	print("   "+fileName+"\n")


#get the pid and user of the connection
def getConnection(info):
	#=========GETTING SSH CONNECTION============#
	#run the command, outputting to a file
	os.system(command+" > "+fileName)
	#open and read the output file
	f = open(fileName, "r")
	output = f.read()
	f.close()

	#=======FORMATTING COMMAND OUTPUT===========#
	#put output in list, removing all spaces
	output = output.split(" ")
	for item in output:
		if item=='':
			output.remove('')
	
	#===============OUTPUT THE RESULTS==========#
	if output==[]:
		if info:
			print("No connection found")
			print("Nothing killed\n")
		#return False for pid and user 
		return False, False
	else:
		#returns pid and user
		return output[1], output[0]


#returns False if key is inputted
def exitCheck(key):
	#if the input is key
	if input()==key:
	#exit the loop
		return False
	else:
		return True


#kill the process with pid
def kill(pid):
	os.system("kill "+pid)


#=============================PROGRAMS=================================#
def killOnCommand():
	printInfo()
	
	#set running to true
	running = True
	#while running
	while running:
		
		pid, user = getConnection(True)
		#if the pid isn't false
		if pid!=False:
			kill(pid)
			#output pid and user
			print("Connection found with PID "+pid+" as "+user)
			print("Killed\n")
		
		running = exitCheck('q')

def monitor():
	printInfo()
	
	#set running to true
	running = True
	#while running
	while running:
		try:
			pid, user = getConnection(False)
			#if the pid isn't false
			if pid!=False:
				#output pid and user
				print("Connection found with PID "+pid+" as "+user)
				answer = input("Kill it? y/n :  ")
				if answer == 'y':
					kill(pid)
		except KeyboardInterrupt:
			break


#==============================RUNNING IT==============================#

try:
	arg = sys.argv[1]
	if arg=='help':
		print("killOnCommand")
		print("monitor")
	elif arg=="killOnCommand":
		killOnCommand()
	elif arg=="monitor":
		monitor()
	else:
		print("Argument not recognised\n run with 'help' to show programs")
except:
	print("Argument not recognised\n run with 'help' to show programs")

