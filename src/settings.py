# -*- coding: utf-8 -*-

"""
This is the file place to setting the application before you try to run it!
"""

class Settings:
	def __init__(self):
		# -> Main setting.
		# Your authentication token.
		self.AUTH_TOKEN = "EteEct6twcjPtQoAz7o7.bI+n8Uc+KCrHRjit/sE4HW.W5mxJT+7buppZAwD8ZxmUF3ceLpnhXUGh5zOGPOR+20="

		# -> Youtube video downloader setting.
		# Integrate with your site url + the path for saving the downloaded videos.
		self.SITE_URL = "http://yoursite.com/DIRECTORY" #your address site to see the saved videos, eg: http://site.com/videos/.
		self.SITE_PATH = "YOUR_PATH" #path/directory to save the videos, eg: /home/user/public_html/videos/.

		# -> Welcome Message when you are accepted the invite groups.
		self.WELCOME_MESSAGE = '\
		Makasih Anjing Sudah Di Undang, BOT Created by Bayu Lingga ^_^\
		"!bothelp" untuk melihat perintah yang tersedia.'

		# -> Auto reply setting.
		# Replacing "simi" words to another words.
		self.REPLACEMENT_CALL = "Bayu lingga"

		# -> Not Important setting.
		# Have another account? you can set it for your secondary account, it will called you/the others account as a boss.
		self.HERE_IAM_YOUR_BOSS = "NTR|Zero Cool" 
