from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os, random, datetime
from twython import Twython
from config import *

class Bot:

	def __init__(self):
		self.twitter = Twython(
			tw_app_consumer,
			tw_app_consumer_s,
			kinevion_t,
			kinevion_t_s
		)

		self.file_got = None
		self.random_file_og_name = None

	def __get_time(self):
		time = datetime.datetime.now().time()
		str_time = str(time) # no mostrar
		return str_time[:8]	 # milisegundos

	def __gdrive_auth(self):
		gauth = GoogleAuth()
		gauth.LocalWebserverAuth()
		drive = GoogleDrive(gauth)
		return drive


	def post(self):
		file = open(self.file_got, 'rb')

		if self.random_file_og_name[-3:] == 'mp4':
			file_id = self.twitter.upload_video(media=file, media_type='video/mp4')

		else:
			file_id = self.twitter.upload_media(media=file)

		self.twitter.update_status(status=self.random_file_og_name, media_ids = [file_id['media_id']])
		print(f'Tweet sent: {self.random_file_og_name} | at {self.__get_time()}')

	def get_img(self):
		drive = self.__gdrive_auth()

		file_list = drive.ListFile({'q': f"'{cat_folder_id}' in parents and trashed=false"}).GetList()

		random_file = random.choice(file_list)
		random_file_id = random_file['id']
		random_file_ext = random_file['fileExtension']
		self.random_file_og_name = random_file['title']

		random_file_dl = drive.CreateFile({'id': random_file_id})
		random_file_dl.GetContentFile(f'file.{random_file_ext}')

		self.file_got = f'file.{random_file_ext}'


	def delete_used(self):
		os.remove(self.file_got)
