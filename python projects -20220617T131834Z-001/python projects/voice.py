
import android; 

droid = android.Android();


answer = {
	

"hello":"hi"


}


questions ["what is your name", "how are you today"]


speech = droid.recognizeSpeech();

#print speech.result
#droid.ttsSpeak( "you just said"+str(speech.result))

talk = str(speech.result)
print "hellow "		

def checkQuestion():
    print "hellow+"
    if (talk == answer["hello"]): 
     print "hellow-"
     
     droid.ttsSpeak("how are you today?")

    else:
     droid.makeToast("something is wrong with the funcion")
     print "hellow_0"


checkQuestion();

droid = android.Android();