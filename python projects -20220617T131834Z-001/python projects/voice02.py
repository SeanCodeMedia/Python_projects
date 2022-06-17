
import android;
import time;
import os;
import random; 
import glob;
import threading;


class  listener (object): 
    def __init__(self):
     print "called"
     self.standOut()
     
    def standOut (self):
     """docstring for  listener """

     localtime = time.asctime( time.localtime(time.time()) )
    # print "Local current time :", slef.localtime

     droid = android.Android()
     speech = droid.recognizeSpeech();

     os.chdir("/sdcard/download")


     Music = []

     for file in glob.glob("*.mp3"):
      Mus = file
      Music.append(Mus)
      #print Music





 

     



     mus=droid.mediaIsPlaying()

     info=droid.mediaPlayList()


     questions = {


     "how are you":" I am grate thanks", "hi":"how are you",
     "what is the time":"the time is..."+str(localtime), "what's going on":"nothing",
     "who is your creator":"sean peart","vibrate":"vibrating....","pause music":"pauseing music...",
     "play music":"playing music"
     }


     VarableX = speech.result.lower();

     Choose = random.choice(Music)

     print "rand "+Choose

     answering = str(VarableX)

     self.check(VarableX,questions,answering,droid,Choose)


    def listen (self, droid,VarableX,questions,Choose):
     speech = droid.recognizeSpeech();
     print "speech"
     self.check(VarableX,questions,answering,droid,Choose)

     







    def looker (self,ValX,Dro,choosing):

     if (ValX =="vibrate"):
      Dro.vibrate(1000)
     elif (ValX == "pause music"):
      print "pause music..."
      Dro.mediaPlayPause()
     elif (ValX == "play music"):
      print "play music..."
      m=Dro.mediaPlay("/sdcard/download/"+str(choosing))
      print m
      Dro.mediaPlayStart()
      time.sleep(60000)


    def check (self,VarX,quest,ans,dro,chos):

     #print VarableX
     if ( VarX in quest):
      
      print "hellow"

      print VarX

      dro.ttsSpeak(quest[ans])

      self.looker(VarX,dro,chos)
          

     else:   
      print "no working"
      dro.ttsSpeak("sorry i don't understand")
      self.listen(dro)
      threading.Timer(5.0,listen(dro)).start();

#################################


x = listener()
threading.Timer(2.0,listener).start();
#threading.Timer(10.0,listen).start();
