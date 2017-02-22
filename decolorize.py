from PIL import Image
import praw
import urllib.request
import pyimgur
from linecache import getline
from os import remove
from os import path
from os import execl
from sys import exit
from time import sleep
line = getline('count.txt',1)
user = "changethis"
pass= "changethis"
num = int(line)
num+=1
count = open("count.txt","w")
count.write(str(num))
clientid = "changethis" 
clientsecret = "changethis"
r = praw.Reddit(user_agent='DecolorizesBwPics')
r.login(user,pass,disable_warning=True)
inbox = r.get_unread(True,True)
im = pyimgur.Imgur(clientid)
def main():
 while True:
   for message in inbox:
     r.get_unread(True,True)
     if "!decolorizeme" in message.body and "imgur" in message.body and ".png" in message.body or ".jpg" in  message.body:
      split = message.body.split()[1]
      print("Downloading "+(split))
      contents = urllib.request.urlopen(split)
      f = open("temp.png","w")
      f.close()
      f = open("temp.png","r+b")
      f.write(bytes(contents.read()))
      print("Downloaded "+split)
      bwimage = Image.open(f)
      bwimage = bwimage.convert('L')
      bwimage.save(str(num)+".png")
      path = str(num)+".png"
      upload = im.upload_image(path, title="Image")
      print(str(upload.link+"\r\n"))
      message.reply(str(upload.link)+" Here is your decolored image")
      remove(path)
      message.mark_as_read()
      sleep(60)
      main()
main()

