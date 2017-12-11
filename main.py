#!/usr/bin/python
import telebot
import thread
import time

def main():
	print "Starting AI Serive"
	time.sleep(2)
	try:
   		thread.start_new_thread( telebot.telebot_main, ("Telebot-Thread", ) )
	except:
   		print "Error: unable to start thread"
		#telebot.telebot_main()
	print 'AI In Main Loop'
	while True:
		pass
  
if __name__== "__main__":
  	main()

