import os
from time import sleep
import subprocess
import shlex
import telepot

MITRA_TOKEN='349763189:AAEEk5uF9aemhS52Bpr15-yKD_AICJlll5g'
mitra_chat_id="277085902"

prev_delay=0

bot=None

def handle(msg):
    #print msg
    content_type, chat_type, chat_id = telepot.glance(msg) 
    global bot
    if content_type == 'text':
    	command = msg['text']
    	#print 'Got Text: %s ' % command
	
	if command == '/status':
        	#bot.sendPhoto(chat_id, photo=open("/home/nilesh/my_work/telebot/img2.png", "rb"))
        	bot.sendMessage(chat_id, "Nil all looks Good")
    	elif command == '/info':
        	#bot.sendPhoto(chat_id, photo=open("/home/nilesh/my_work/telebot/img1.png", "rb"))        
        	bot.sendMessage(chat_id, "Created By Nilesh Mundphan")
	elif command == '/home':
                bot.sendMessage(chat_id, "Sensors\n----------\nTempreture:\nHumidity  :\nGas Level :\n\nDevices\n-----------\nLights:\nFan   :\nTV    :\nAC    :\n") 
   	else:
		bot.sendMessage(chat_id,command)
 
    elif content_type == 'photo':   	
    	file_id=msg['photo'][2]['file_id']
    	photo_file = bot.getFile(file_id)
        file_path=photo_file['file_path']
    	#download_file("images",file_path)
	print 'Got Image: %s' % file_path
	#show_img(file_path)
    
    elif content_type == 'video':
	file_id=msg['video']['file_id']
        video_file = bot.getFile(file_id)
        file_path=video_file['file_path']
        #download_file("videos",file_path)
        print 'Got Video: %s' % file_path
	#sleep(2)
        #play_vid(file_path)
    
    elif content_type == 'audio':
        file_id=msg['audio']['file_id']
        video_file = bot.getFile(file_id)
        file_path=video_file['file_path']
        #download_file("audios",file_path)
        print 'Got Audio: %s' % file_path
	#sleep(2)
        #play_aud(file_path)
     
    else:
	print msg
	print "Content Type : %s " % (content_type)
	print "I don't understand"	


def telebot_main( stat_msg ):
	global bot
	bot = telepot.Bot(MITRA_TOKEN)
	bot.message_loop(handle)
	bot.sendMessage(mitra_chat_id, "AI TeleBot is Running")
	print stat_msg
	print 'AI TeleBot Is Running'
	while 1:
		sleep(10)

#telebot_main()
