import speech_recognition
import pyttsx3
import requests, json
import calendar
import psutil
import time
import webbrowser
from datetime import date
from dateutil.relativedelta import relativedelta
import os
from googletrans import Translator
from tkinter import *
import datetime
import time
from playsound import playsound
import threading
from threading import *
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import wolframalpha
from functools import reduce
from difflib import SequenceMatcher
import string
import random
import getpass
import numpy as np
import imageio
import scipy.ndimage
import cv2
from tkinter import *
from pytube import YouTube
from tkinter import messagebox
import socket

robot_mouth = pyttsx3.init()
rate = robot_mouth.getProperty('rate')
robot_mouth.setProperty(rate, 160)

robot_ear = speech_recognition.Recognizer()

user_name = getpass.getuser()
host = '/Users/'+user_name+'/Desktop/JV/Media/'


def ipAddress():
	hostname = socket.gethostname()
	ip = socket.gethostbyname(hostname)
	return 'Your IP address is ' + ip

def get_current_location():
	g = geocoder.ip('me')
	return str(g.city)

def is_leap_year(year):
	if calendar.isleap(year) == True:
		return "Yes, it certainly is"
	else: return "No, it's not"

def find_weekday(reply):
	get_rid = ['th', 'rd', 'st', 'nd']
	try:
		for i in get_rid:
			if i in reply:
				reply = reply.replace(i,'')
				break
			else: pass
		the_date = time.strptime(reply, '%Y %B %d')
		return "That's " + time.strftime('%A', the_date)
	except: 
		return "Sorry, say 'weekday' to try again"
	
def open_systemPreferences():
	os.system("open '/Applications/System Preferences.app'")
	return "On"

def open_contacts():
	os.system('open /Applications/Contacts.app')
	return "Here"

def open_chess():
	os.system("open /Applications/Chess.app")
	return "Have fun"

def open_iMovie():
	os.system('open /Applications/iMovie.app')

def open_facebook():
	webbrowser.open_new(r'https://www.facebook.com')
	robot_brain = "Right away, but be mindful about your screen time"
	return robot_brain

def open_netflix():
	webbrowser.open_new(r'https://www.netflix.com')
	robot_brain = "Enjoy your watch!"
	return robot_brain

def open_brackets():
	os.system("open /Applications/Brackets.app")
	return "The IDE at your service"

def open_automator():
	os.system("open /Applications/Automator.app")
	return "Done"

def open_pdfReader():
	os.system("open '/Applications/Adobe Acrobat Reader DC.app'")

def open_youtube():
	webbrowser.open_new(r'https://www.youtube.com')
	robot_brain = "All set"
	return robot_brain

def open_googletranslate():
	webbrowser.open_new(r'https://translate.google.ca/')

def open_messenger():
	webbrowser.open_new(r'https://www.messenger.com')
	robot_brain = "Easy"
	return robot_brain

def open_gmail():
	webbrowser.open_new(r'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
	robot_brain = 'Ready to roll'
	return robot_brain

def open_instagram():
	webbrowser.open_new(r'https://www.instagram.com')
	robot_brain = 'Take care of your eyes'
	return robot_brain


def international_time(you):
	try:
		city = ' '.join([word for word in you.split() if word.istitle()])
		foreign_time = calculate(you)

		return f'My system indicates the time in {city} is {foreign_time}.'
	
	except:
		return "There is an error. I couldn't process your question"

def open_dashboard():
	os.system('open /Applications/Dashboard.app')
	return "Opened"

def open_photos():
	os.system("open /Applications/Photos.app")

def open_googlemap():
	webbrowser.open_new('https://maps.google.com')
	return 'I gotchu'

def open_msexcel():
	os.system("open '/Applications/Microsoft Excel.app'")

def open_msword():
	os.system("open '/Applications/Microsoft Word.app'")

def open_calculator():
	os.system('open /Applications/Calculator.app')

def open_mspp():
	os.system("open '/Applications/Microsoft PowerPoint.app'")

def open_googleChrome():
	try:
		os.system("open '/Applications/Google Chrome.app'")
		return 'Your browser is ready'
	except:
		return "There isn't such app in your computer"

def open_facetime():
	os.system('open /Applications/FaceTime.app')
	return "Yup"

def open_safari():
	try:
		os.system('open /Applications/Safari.app')
		return "Safari is on"
	except:
		return "Safari is disabled"
	
def record():
	os.system("open '/Applications/QuickTime Player.app'")

def open_discord():
	os.system('open /Applications/Discord.app')
	return "Copied"

def open_mail():
	
	os.system('open /Applications/Mail.app')
	return "Here's your mailbox"

def open_dictionary():
	os.system('open /Applications/Dictionary.app')

def open_reminder():
	os.system("open /Applications/Reminders.app")
	return "Yes"

def open_calendar():
	os.system("open /Applications/Calendar.app")
	return 'Just 1 second'

def open_iTunes():
	os.system("open /Applications/iTunes.app")
	return "Switch it up!!"

def openGoogleDrive():
	webbrowser.open_new('https://www.google.com/intl/en/drive/')
	return "Your Google Drive is up"

def open_simpleMind():
	os.system('open /Applications/SimpleMind.app')
	return "Mindmap on"

def news():

	news_url = "https://news.google.com/news/rss"
	Client = urlopen(news_url)
	xml_page = Client.read()
	Client.close()

	soup_page = soup(xml_page, "xml")
	news_list = soup_page.findAll("item")[0:6]
	

	for news in news_list:
		news_link = news.link.text
		webbrowser.open_new(news_link)
	
		
def open_msTeams():
	os.system("open '/Applications/Microsoft Teams.app'")

def open_hotspotShield():
	os.system("open '/Applications/Hotspot Shield.app'")
	return "VPN on"

def storage():
	hdd = psutil.disk_usage('/')
	return "Total: " + str(int(hdd.total / (2**30 * 1.07374))) + ' GB. Used: ' + str(int(hdd.used / (2**30) * 1.07374)) + " GB. Free: " + str(int(hdd.free / (2**30) * 1.07374)) + " GB."

def translate(content):
	translator = Translator()
	translated = translator.translate(content)
	translated = translated.text
	with open("///Users/"+user_name+"/Desktop/translated.txt", 'w') as f:
		f.write(translated)
		f.close()
	
def calculate(you):

	if 'calculate ' in you:
		you = you.replace('calculate ', '')
	try:
		client = wolframalpha.Client('TXV5VL-TURK6K853R')
		query = you
		res = client.query(query)
		output = next(res.results).text
		return f"{output}"
	except:
		return "I don't have an answer"

def open_preview():
	os.system('open /Applications/Preview.app')
	return "Okay"

def create_docx():
	with open('///Users/'+user_name+'/Desktop/new.docx', 'w') as f:
		f.close()
	return	"A new document is set in your Desktop"

def open_fontbook():
	os.system("open '/Applications/Font Book.app'")
	return "Anything else?"

def create_powerpoint():
	with open('///Users/'+user_name+'/Desktop/new.pptx', 'w') as f:
		f.close()
	return "A new presentation is set in your Desktop"

def create_spreadsheet():
	with open("///Users/"+user_name+"/Desktop/new.xls", 'w') as f:
		f.close()
	return "A new spreadsheet is ready in your Desktop"

def random_password():

	lower = string.ascii_lowercase
	upper = string.ascii_uppercase
	numbers = '0123456789'
	symbols = '~`!@#$%^&*()_-+=[]}{\|'

	all = lower + upper + numbers + symbols
	password = ''.join(random.sample(all, 12))

	with open('///Users/'+user_name+'/Desktop/random_password.txt', 'w') as f:
		f.write(password)
		f.close()
	
	return "Your password has been generated in a txt file named 'random_password' located in your Desktop."


def similarity_check(text1, text2):
	match = SequenceMatcher(a = text1.lower(), b = text2.lower())
	result = str(int(match.ratio())*100) + '%'
	return 'Text 1 and Text 2 are ' + result + ' matched.'
 
def image_to_sketch(filepath):
	# take image input and assign variable to it
	img = "/Users/" + user_name + "/Desktop/" + filepath
	
	
	# function to convert image into sketch
	def rgb2gray(rgb):
	# 2 dimensional array to convert image to sketch
		return np.dot(rgb[..., :3], [0.2989, 0.5870, .1140])
	
	
	def dodge(front, back):
	
		# if image is greater than 255 (which is not possible) it will convert it to 255
		final_sketch = front*255/(255-back)
		final_sketch[final_sketch > 255] = 255
		final_sketch[back == 255] = 255
		
		# to convert any suitable existing column to categorical type we will use apect function
		# and uint8 is for 8-bit signed integer
		return final_sketch.astype('uint8')
	
	
	ss = imageio.imread(img)
	gray = rgb2gray(ss)
	
	i = 255-gray
	
	
	# to convert into a blur image
	blur = scipy.ndimage.filters.gaussian_filter(i, sigma=13)
	
	
	# calling the fuction
	r = dodge(blur, gray)
	
	output = "/Users/" + user_name + "/Desktop/sketched.png"
	cv2.imwrite(output, r)

def open_textEdit():
	os.system('open /Applications/TextEdit.app')
	return "Here"

def shopping():
	webbrowser.open_new(r'https://www.amazon.com/')
	webbrowser.open_new(r'https://www.ebay.com/')
	return "Take good care of yourself"

def open_messages():
	os.system('open /Applications/Messages.app')
	return "All set!"

def open_notes():
	os.system('open /Applications/Notes.app')
	return 'Notes are ready in your Desktop'

def doc_word_count(filepath = '///Users/bphan/Desktop/word_count.txt'):
	with open(filepath, 'r') as f:
		data = f.read()
		data.replace(', ',' ')
		return 'The file contains ' + str(len(data.split())) + ' words'

def mic_button_hit():

	while True:
		playsound(host+"button_click.mp3")

		with speech_recognition.Microphone() as mic:
			print("Jarvis: I'm listening")
			robot_ear.adjust_for_ambient_noise(mic)
			audio = robot_ear.record(mic, duration = 4.5)

		print("Jarvis: processing")

		try:
			you = robot_ear.recognize_google(audio)
		except:
			you = ''

		print("Tony: ", you)

		sun = int(time.strftime("%H"))

		if (you == 'Jarvis') or ("hello" in you) or ("what's up" in you):
			responses = ['Yes?', 'Hello?', 'Wassup?']
			robot_brain = random.choice(responses)

		elif ('about' in you or 'who' in you) and 'you' in you:
			robot_brain = "I'm a highly functional problem solver"

		elif ('good morning' in you) or ('good afternoon' in you) or ('good evening' in you) or ('good night' in you):
			if 0 <= sun <= 11:
				robot_brain = "Beautiful day ahead!"
			elif 19 <= sun < 23:
				robot_brain = "Wonderful evening"
			elif 23 <= sun <= 24:
				robot_brain = "It's late, I suggest you take some rest." 
			else: 
				robot_brain = "At your service."

		elif ('chess' in you):
			robot_brain = open_chess()
		
		elif ("contacts" in you):
			robot_brain = open_contacts()

		elif 'IP address' in you:
			robot_brain = ipAddress()

		elif "day is it" in you:

			robot_brain = "It is " + time.strftime("%A, %d/%B/%Y")

		elif you == "what's the time" or you == "what time is it":
			robot_brain = "It's " + time.strftime('%I:%M %p')
		
		elif 'weekday' in you:
			robot_brain = 'Tell me the date'
			print("Jarvis: ", robot_brain)
			robot_mouth.say(robot_brain)
			robot_mouth.runAndWait()

			while True:
				
				
				with speech_recognition.Microphone() as mic:
					print("Jarvis: I'm listening")
					robot_ear.adjust_for_ambient_noise(mic) 
					audio = robot_ear.record(mic, duration = 6)
				
				print("Jarvis: processing")

				try:
					reply = robot_ear.recognize_google(audio)
				except:
					reply = ''

				print("Tony: ", reply)

				if reply:			
					robot_brain = find_weekday(reply)
					break
				else:
					clarification = "Help me determine the date again please?"
					print("Jarvis: ", clarification)
					robot_mouth.say(clarification)
					robot_mouth.runAndWait()

		elif ('dictionary' in you) or ('define' in you):
			open_dictionary()
			robot_brain = "Okay"

		elif ('teams' in you):
			open_msTeams()
			robot_brain = "You're all set"

		elif ('font' in you):
			robot_brain = open_fontbook()

		elif ('iMovie' in you):
			open_iMovie()
			robot_brain = "Your workspace is ready"

		elif you == 'where am I' or 'my location' in you:

			robot_brain = get_current_location()

		elif ('storage' in you):
			robot_brain = storage()

		elif ('record' in you):
			record()
			robot_brain = "Here you go"

		elif ('dashboard' in you):
			robot_brain = open_dashboard()

		elif ('Discord' in you):
			robot_brain = open_discord()

		elif ('mind map' in you):
			robot_brain = open_simpleMind()

		elif ('past' in you or 'future' in you) and ('date' in you or 'day' in you):

			robot_brain = calculate(you)

		elif ('Hotspot Shield' in you):
			robot_brain = open_hotspotShield()
		
		elif ('System Preferences' in you):
			robot_brain = open_systemPreferences()

		elif ('how long' in you):
			robot_brain = calculate(you)	
	
		elif ('brackets' in you):
			robot_brain = open_brackets()

		elif ('Google Drive' in you):
			robot_brain = openGoogleDrive()

		elif (('days' in you) or ('long' in you)) and ('since' in you):
			robot_brain = "Sir, help me reconfirm the start date in the style: year, month, day"
			print("Jarvis: ", robot_brain)
			robot_mouth.say(robot_brain)
			robot_mouth.runAndWait()

			while True:
				
				with speech_recognition.Microphone() as mic:
					print("Jarvis: I'm listening")
					robot_ear.adjust_for_ambient_noise(mic)
					audio = robot_ear.record(mic, duration = 5)
				
				print("Jarvis: processing")
				try:
					reply = robot_ear.recognize_google(audio)
				except:
					reply = ''

				print("Tony: ", reply)
				try:			
					get_rid = ['th','rd','nd','st']
					for i in get_rid:
						if i in reply:
							reply = reply.replace(i,'')
					parsed_time = time.strptime(reply, '%Y %B %d')
					delta = date.today() - date(parsed_time.tm_year, parsed_time.tm_mon, parsed_time.tm_mday)
					robot_brain = "It's been " + str(delta.days) + ' days'
					break
				except:
					clarification = "I'm sorry?"
					print("Jarvis: ", clarification)
					robot_mouth.say(clarification)
					robot_mouth.runAndWait()
		
		elif ("translate" in you) or ("Translate" in you):
			clarification = "Is it gonna be a file or just a sentence?"
			print("Jarvis: ", clarification)
			robot_mouth.say(clarification)
			robot_mouth.runAndWait()

			while True:

				with speech_recognition.Microphone() as mic:
					print("Jarvis: I'm listening")
					robot_ear.adjust_for_ambient_noise(mic)
					audio = robot_ear.record(mic, duration = 3)
				
				print("Jarvis: processing")

				try: 
					rep = robot_ear.recognize_google(audio)
				except:
					rep = ''
				
				print("Tony: ", rep)

				if not rep:
					clarification = "I'm sorry?"
					print("Jarvis: ", clarification)
					robot_mouth.say(clarification)
					robot_mouth.runAndWait()
				else:
					break

			if 'file' in rep:

				with open("///Users/"+user_name+"/Desktop/content.txt", 'w') as f:
					f.close()

				instruction = "Please copy the content of the file into the new txt file I created in your Desktop. Then, come back to tell me you are done."
				print("Jarvis: ", instruction)
				robot_mouth.say(instruction)
				robot_mouth.runAndWait()

				while True:
					with speech_recognition.Microphone() as mic:
						print("Jarvis: I'm listening")
						robot_ear.adjust_for_ambient_noise(mic)
						audio = robot_ear.record(mic, duration = 10)
					
					print("Jarvis: processing")

					try:
						rep = robot_ear.recognize_google(audio)
					except:
						rep = ''
					
					print("Tony: ", rep)

					if ('yes' in rep) or ('done' in rep) or ('completed' in rep) or ('finished' in rep):
						break
					else:
						responses = ['Sir, are you done?', "Should I keep waiting?", "Are you ready?"]
						clarification = random.choice(responses)
						print("Jarvis: ", clarification)
						robot_mouth.say(clarification)
						robot_mouth.runAndWait()
					
				
				with open("///Users/"+user_name+"/Desktop/content.txt", 'r') as f:
					content = f.read()
					translate(content)
				
				os.remove("///Users/"+user_name+"/Desktop/content.txt")

				robot_brain = "The translated version is ready in your Desktop"
			else:
				open_googletranslate()
				robot_brain = "Here you go"

		elif ('text editor' in you):
			robot_brain = open_textEdit()

		elif ('automator' in you):
			robot_brain = open_automator()

		elif ('PDF reader' in you):
			open_pdfReader()
			robot_brain = "It's all set"

		elif ('FaceTime' in you):
			robot_brain = open_facetime()

		elif ('shopping' in you):
			robot_brain = shopping()

		elif  ("common divisor" in you) or ('calculate' in you) or ('number' in you) or ('+' in you) or ('-' in you) or ('*' in you) or ('^' in you) or ('/' in you) or ('factorial' in you) or ('series' in you) or ('convert' in you):
			try:
				robot_brain = calculate(you)
			except:	
				robot_brain = "I couldn't find an answer"
		
		elif ('text' in you) or ('message' in you):
			robot_brain = open_messages()

		elif ('random' in you) and ('number' in you):

			while True:
				
				try:
					start, end = tuple(filter(lambda x: x.isdigit()))
					robot_brain = random.randrange(int(start), int(end))
					break
				except:
					clarification = "What's the range?"
					print("Jarvis: ", clarification)
					robot_mouth.say(clarification)
					robot_mouth.runAndWait()
		
		elif ("password" in you):
			robot_brain = random_password()
		
		elif ('similar' in you) and (('check' in you) or ('determine' in you)):
			
			with open('///Users/'+user_name+'/Desktop/Text1.txt', 'w') as f1, open('///Users/'+user_name+'/Desktop/Text2.txt', 'w') as f2:
				f1.close()
				f2.close()

			instruction = "Help me paste the two text in the txt files I've just created on your Desktop. Afterwards, please come back to tell me you're finished"
			print("Jarvis: ", instruction)
			robot_mouth.say(instruction)
			robot_mouth.runAndWait()

			while True:
				
				with speech_recognition.Microphone() as mic:
					print("Jarvis: I'm listening")
					robot_ear.adjust_for_ambient_noise(mic)			
					audio = robot_ear.record(mic, duration = 20)
				
				print("Jarvis: processing")

				try:
					rep = robot_ear.recognize_google(audio)
				except:
					rep = ''

				print("Tony: ", rep)

				if ('yes' in rep) or ('done' in rep) or ('finished' in rep) or ('completed' in rep):
					break
				else:
					clarification = 'Tony, are you done?'
					print("Jarvis: ", clarification)
					robot_mouth.say(clarification)
					robot_mouth.runAndWait()
			try:
				with open('///Users/'+user_name+'/Desktop/Text1.txt', 'r') as f1:
					text1 = f1.read()
					f1.close()
				
				with open('///Users/'+user_name+'/Desktop/Text2.txt', 'r') as f2:
					text2 = f2.read()
					f2.close()
		
				robot_brain = similarity_check(text1, text2)
				os.remove('///Users/'+user_name+'/Desktop/Text1.txt')
				os.remove('///Users/'+user_name+'/Desktop/Text2.txt')
			except:
				os.remove('///Users/'+user_name+'/Desktop/Text1.txt')
				os.remove('///Users/'+user_name+'/Desktop/Text2.txt')
				robot_brain = "Tony, I noticed you have done something wrong with files. Please state your demand again and do exactly as I instructed"

		elif ('create' in you) and ('document' in you):
			robot_brain = create_docx()
		
		elif ('create' in you) and ('presentation' in you):
			robot_brain = create_powerpoint()
		
		elif ('create' in you) and ('spreadsheet' in you):
			robot_brain = create_spreadsheet()

		elif ('Excel' in you):
			open_msexcel()
			robot_brain = "Done"

		elif ('notes' in you):
			robot_brain = open_notes()

		elif ('Chrome' in you):
			robot_brain = open_googleChrome()
		
		elif ('Safari' in you) or ('browser' in you):
			robot_brain = open_safari()

		elif ('Netflix' in you) or ('watch' in you):
			robot_brain = open_netflix()

		elif ('movie' in you):
			year = str(time.localtime().tm_year)
			you = 'top movies in ' + year + ' IMDB'
			webbrowser.open_new("https://www.google.com/search?q=top+movies+in+"+year)
			robot_brain = "Here are my best suggestions"
			

		elif 'article' in you or 'scrape' in you:
			
			with open('///Users/'+user_name+'/Desktop/url_input.txt', 'w') as f:
				f.close()
			
			instruction = "I've created a txt file on your Desktop. In it, you will put the URLs of your articles on different lines. Afterwards, save the file, close it and come back to tell me you are done."
			print("Jarvis: ", instruction)
			robot_mouth.say(instruction)
			robot_mouth.runAndWait()

			while True:
				
				with speech_recognition.Microphone() as mic:
					print("Jarvis: I'm listening")
					robot_ear.adjust_for_ambient_noise(mic)
					audio = robot_ear.record(mic, duration = 12)

				print("Jarvis: processing")

				try:
					rep = robot_ear.recognize_google(audio)
				except:
					rep = ''
				
				print("Tony: ", rep)
				if ('yes' in rep) or ('done' in rep) or ('finished' in rep) or ('completed' in rep):
					break
				else:
					clarification = 'Are you done?'
					print("Jarvis: ", clarification)
					robot_mouth.say(clarification)
					robot_mouth.runAndWait()
			
			
			try:
				with open('///Users/'+user_name+'/Desktop/url_input.txt', 'r') as f:
					urls = list(map(lambda x: x.replace('\n',''),f.readlines()))
					f.close()
				
				for url in urls:
					url_i = newspaper.Article(url = "%s" % (url), language = 'en')
					url_i.download()
					url_i.parse()
					content = url_i.text
					name = '///Users/'+user_name+'/Desktop/' + str(urls.index(url)) + '.txt'
					with open(name, 'w') as f:
						f.write(content)
						f.close()

				os.remove('///Users/'+user_name+'/Desktop/url_input.txt')
				robot_brain = "All content is uploaded on your Desktop. You're welcome"
			
			except:
				os.remove('///Users/'+user_name+'/Desktop/url_input.txt')
				robot_brain = "I suspect you have done something wrong with the file. Please state your demand again and repeat the process."	

		elif ('photos' in you) and ('open' in you):
			open_photos()
			robot_brain = "Task accomplished"

		elif (('read' in you) and ('book' in you)) or ('audiobook' in you) :
			
			with open('///Users/'+user_name+'/Desktop/audiobook.txt', 'w') as f:
				f.close()
			instruction = "I've created a txt file on your Desktop. Help me put the text in it, then come back to tell me you are done. After that, sit back and listen"
			print("Jarvis: ", instruction)
			robot_mouth.say(instruction)
			robot_mouth.runAndWait()

			while True:
				
				with speech_recognition.Microphone() as mic:
					print("Jarvis: I'm listening")
					robot_ear.adjust_for_ambient_noise(mic)
					audio = robot_ear.record(mic, duration = 10)
				
				print("Jarvis: processing")

				try:
					rep = robot_ear.recognize_google(audio)
				except:
					rep = ''
				print("Tony: ", rep)
				if ('yes' in rep) or ('done' in rep) or ('finished' in rep) or ('completed' in rep):
					break
				else:
					clarification = 'Tony, are you done?'
					print("Jarvis: ", clarification)
					robot_mouth.say(clarification)
					robot_mouth.runAndWait()
				
			try:
				robot_mouth.setProperty(rate, 46)
				with open('///Users/'+user_name+'/Desktop/audiobook.txt', 'r') as f:
					robot_mouth.say(f.read())
					robot_mouth.runAndWait()
					f.close()
				os.remove('///Users/'+user_name+'/Desktop/audiobook.txt')
				robot_brain = "Tony, I've finished reading."
			except:
				os.remove('///Users/'+user_name+'/Desktop/audiobook.txt')
				robot_brain = "Tony, I think you might have done something wrong with the file. Please state your demand again and repeat the process."

		elif ("image" in you) and ('sketch' in you):
			
			with open('///Users/'+user_name+'/Desktop/picture.txt', 'w') as f:
				f.close()
			instruction = "Please place your image in your Desktop. I've created a txt file on your Desktop to let you put the name of the image file including its extension in the file. Afterwards, please come back to tell me you are done."
			print("Jarvis: ", instruction)
			robot_mouth.say(instruction)
			robot_mouth.runAndWait()

			while True:
				
				with speech_recognition.Microphone() as mic:
					print("Jarvis: I'm listening")
					robot_ear.adjust_for_ambient_noise(mic)
					audio = robot_ear.record(mic, duration = 12)
				
				print("Jarvis: processing")
				try:
					rep = robot_ear.recognize_google(audio)
				except:
					rep = ''
				print("Tony: ", rep)
				if ('yes' in rep) or ('done' in rep) or ('finished' in rep) or ('completed' in rep):
					break
				else:
					clarification = 'Tony, are you done?'
					print("Jarvis: ", clarification)
					robot_mouth.say(clarification)
					robot_mouth.runAndWait()
			
			try:
				with open('///Users/'+user_name+'/Desktop/picture.txt', 'r') as f:
					filepath = f.read()
					f.close()
				image_to_sketch(filepath)
				os.remove('///Users/'+user_name+'/Desktop/picture.txt')
				robot_brain = "Sketched version is completed on your Desktop. You're welcome"
			except:
				os.remove('///Users/'+user_name+'/Desktop/picture.txt')
				robot_brain = "Tony, I think you might have done something wrong with the file. Please state your demand again and repeat the process."

		elif ('open' in you) and ('iTunes' in you):
			robot_brain = open_iTunes()
		
		elif ('time is it in' in you) or ("the time in " in you) or ("what is the time in " in you) or ('international' in you):
			robot_brain = international_time(you)

		elif ('file size' in you):
			robot_brain = "Easy. You can do it by a two-finger tap on the file and hitting 'Get info'"

		elif ('copy' in you) and ('file' in you):
			robot_brain = "It's very simple. You can do it by a two-finger tap on the file and hitting 'duplicate'."

		elif (('count' in you) or ('many' in you)) and ('word' in you):
			with open('///Users/bphan/Desktop/word_count.txt', 'w') as f:
				f.close()

			robot_brain = "Please copy the content of the file and paste it in the txt file I have just created in your Desktop. When you are finished, return and inform me"
			print("Jarvis: ", robot_brain)
			robot_mouth.say(robot_brain)
			robot_mouth.runAndWait()

			while True:
				
				with speech_recognition.Microphone() as mic:
					print("Jarvis: I'm listening")
					robot_ear.adjust_for_ambient_noise(mic)
					audio = robot_ear.record(mic, duration = 20)
				
				print("Jarvis: processing")

				try:
					reply = robot_ear.recognize_google(audio)
				except:
					reply = ''
				
				print("Tony: ", reply)

				if ('finished' in reply) or ('done' in reply) or ('completed' in reply) or ('yes' in reply):
					robot_brain = doc_word_count()
					break
				else:
					robot_brain = "Are you ready?"
					print("Jarvis: ", robot_brain)
					robot_mouth.say(robot_brain)
					robot_mouth.runAndWait()



		elif 'leap year' in you:

			while True:
				
				year = int(''.join([x for x in you.split() if x.isdigit()]))
				if year:
					robot_brain = is_leap_year(year) 
					break
				else:
					clarification = "There's something I don't understand. Could you ask me the question again?"
					print("Jarvis: ", clarification)
					robot_mouth.say(clarification)
					robot_mouth.runAndWait()

		elif ('embarrassed' in you):
			robot_brain = "I'm very sorry"

		elif 'weather' in you:
			
			webbrowser.open_new("https://www.google.com/search?q=weather+today")

			robot_brain = "Here is what I've found"

		elif 'calculator' in you:
			robot_brain = open_calculator()

		elif 'Facebook' in you:
			robot_brain = open_facebook()
		
		elif 'open' in you and 'YouTube' in you:
			robot_brain = open_youtube()

		elif 'messenger' in you:
			robot_brain = open_messenger()
		
		elif ' mail' in you:
			robot_brain = open_mail()

		elif 'Gmail' in you:
			robot_brain = open_gmail()
		
		elif 'Instagram' in you:
			robot_brain = open_instagram()
		
		elif ('map' in you) or ('Google Maps' in you):
			robot_brain = open_googlemap()
		
		elif ('direction to' in you) or ('the way to' in you):
			
			to = you.split().index('to')
			destination = ' '.join(you.split()[to+1:])
			ask_vehicle = "What vehicle will you be taking?"
			print("Jarvis: ", ask_vehicle)
			robot_mouth.say(ask_vehicle)
			robot_mouth.runAndWait()

			while True:
				with speech_recognition.Microphone() as mic:
					print("Jarvis: I'm listening")
					robot_ear.adjust_for_ambient_noise(mic)
					audio = robot_ear.record(mic, duration = 2.5)

				try:
					vehicle = robot_ear.recognize_google(audio)
				except:
					vehicle = ''
				if vehicle:
					you = "https://www.google.com/search?q=" + "direction+to+" + '+'.join(destination.split()) + "+by+" + vehicle
				
					break
				else:
					continue

			webbrowser.open_new(you)
			robot_brain = "Here are my recommendations"

		elif ("near me" in you):
			you = "+".join(you.split())
			webbrowser.open_new("https://www.google.com/search?q="+you)
			robot_brain = "Check these out"

		elif ('how far' in you):
			robot_brain = open_googlemap()
		
		elif ('what' in you) and ('address' in you):
			robot_brian = open_googlemap()
		
		elif ("YouTube" in you) and ("download" in you or "convert" in you):
			robot_brain = youtube_converter()

		elif you == '':
			try:
				url = "https://www.google.com"
				timeout = 5
				request = requests.get(url, timeout = timeout)
				robot_brain = "..."
			except (requests.ConnectionError, requests.Timeout) as exception:
				robot_brain = "Unfortunately, I'm disconnected to the Internet and no longer at your service."
				print("Jarvis: ", robot_brain)
				robot_mouth.say(robot_brain)
				robot_mouth.runAndWait()

				break
			

		elif ('wait' in you) or ('hold on' in you) or ('hold up' in you) or ('stand' in you):
			confirmation = "Waiting for your next command"
			print("Jarvis: ", confirmation)
			robot_mouth.say(confirmation)
			robot_mouth.runAndWait()

			while True:
				
				with speech_recognition.Microphone() as mic:
					print("Jarvis: ...")
					robot_ear.adjust_for_ambient_noise(mic) 
					audio = robot_ear.record(mic, duration=3.5)
				
				try:
					reply = robot_ear.recognize_google(audio)
				except:
					reply = ''
				
				print("Tony: ", reply)

				if 'Jarvis' in reply:
					robot_brain = "I'm back"
					break
				else:
					continue
		
		elif ("find") in you and (('folder' in you) or ('file' in you)):
			robot_brain = "Sorry, I respectfully believe it would be much more efficient if you look for it by yourself."

		elif ('open' in you) and (('Microsoft Word' in you) or ('word' in you)):
			open_msword()
			robot_brain = "Sure"

		elif ('PowerPoint' in you):
			open_mspp()
			robot_brain = "Sure"

		elif ('Outlook' in you):
			os.system("open '/Applications/Microsoft Outlook.app'")
			robot_brain = "The mailbox is ready"

		elif ('App Store' in you):
			os.system("open " + "'/Applications/App Store.app'")
			robot_brain = "It's ready"

		elif ('OneNote' in you):
			os.system("open '/Applications/Microsoft OneNote.app'")

		elif ('screenshot' in you):
			os.system('screencapture /Users/'+user_name+'/Desktop/screenshot.jpg')
			robot_brain = "A screenshot is taken and located in your Desktop"

		elif ('alarm' in you) or ('timer' in you) or ('a.m.' in you) or ('p.m.' in you) or ('minute' in you) or ('hour' in you) or ('wake' in you):
			if ('a.m.' in you) or ('p.m.' in you) or ('minute' in you) or ('hour' in you):
				content = "vClock" + you
				webbrowser.open_new("https://vclock.com/")
				robot_brain = "You will need to press the 'Set' button. I can't do that here"
			else:
				robot_brain = "Help me determine the time first"

		elif ('reminder' in you) or ('schedule' in you) or ('task' in you) or ('to do' in you):
			robot_brain = open_reminder()
		
		elif ('calendar' in you) and ('open' in you):
			robot_brain = open_calendar()

		elif ('news' in you):

			robot_brain = "Here are the top news today..."
			news()		

		elif ("play" in you) or ('Play' in you) or ('song' in you) or ('music' in you) or ('tune' in you) or ('make me' in you):
			get_rids = ['play', 'Play']
			you = '+'.join([word for word in you.split() if word not in get_rids])
			webbrowser.open_new("https://www.youtube.com/results?search_query="+you)
			robot_brain = "Enjoy!"

		elif ('leave' in you ) or ('alone' in you) or ('shut' in you) or ('bye' in you) or ('away' in you):
			
			if 0 <= sun <= 11:
				responses = ['Have a good day', "Promptly"]
				robot_brain = random.choice(responses)
			elif 12 <= sun <= 13:
				robot_brain = "I'll see you later"
			elif 14 <= sun <= 17:
				robot_brain = "It's been a pleasure"
			else:
				responses = ['Enjoy the rest of your evening', "If you need me later, I'm here."]
				robot_brain = random.choice(responses)
			
			print("Jarvis: ", robot_brain)
			robot_mouth.say(robot_brain)
			robot_mouth.runAndWait()

			break

		else:	
			if ('what' in you) or ('how' in you) or ('when' in you) or ('where' in you) or ('who' in you) or ('why' in you) or ('which' in you):
				you = "+".join([word for word in you.split()])
				webbrowser.open_new("https://www.google.com/search?q="+you)
				robot_brain = "Here's your result"
			else:
				robot_brain = "I don't understand that. I might have misunderstood you."
		
		print("Jarvis: ", robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()


def youtube_converter():
	converter = Toplevel()
	converter.geometry('220x150')
	converter.title('JV VidConvert')
	converter.resizable(0,0)
	converter.configure(bg = 'black')

	Label(converter, text = "Enter your URL: ", font = ("Avenir", 15), bg = 'black', fg = 'white').place(x = 10, y = 10)
	url = Entry(converter)
	url.place(x = 10, y = 40)

	def download_mp4():
		link = url.get()
		yt = YouTube(link)
		videos = list(yt.streams.all())
		for i in videos:
			if "video" in str(i):
				i.download()
				break

		messagebox.showinfo("Jarvis", "Download is successful. To find the file, input the name of the video on Youtube into spotlight search")

	def download_mp3():
		link = url.get()
		yt = YouTube(link)
		videos = list(yt.streams.all())
		for i in videos:
			if "audio/mp3" in str(i):
				i.download()
				break
			else:
				if "audio/webm" in str(i):
					i.download()
					break
		
		messagebox.showinfo("Jarvis", "Download is successful. To find the file, input the name of the video on Youtube into spotlight search")

	Button(converter, text = "MP4", width = 5, height = 2, command = download_mp4).place(x = 40, y = 93)
	Button(converter, text = "MP3", width = 5, height = 2, command = download_mp3).place(x = 120, y = 93)

	converter.mainloop()


def lock_screen():

	root = Tk()
	root.title('JV')
	root.configure(bg = 'black')
	root.geometry('320x150')
	root.resizable(0,0)

	Label(root, text = user_name, font = ('Avenir', 10), bg = 'black', fg = 'snow').place(x = 5, y = 5)

	Label(root, text = 'Desktop App', font = ("Avenir",10), bg = 'black', fg = 'white').place(x = 122, y = 5)

	Label(root, text = 'Wifi Required', font = ('Avenir', 10), bg = 'black', fg = 'snow').place(x = 245, y = 5)

	button = PhotoImage(file = host + "home_button.png")
	Button(root, image = button, width = 45, height = 45,command = mic_button_hit).place(x = 135, y = 80)

	mainloop()

lock_screen()