from os import path
import pyaudio
import time

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

from check4 import *
from manageDB import *


from espeak import espeak
espeak.set_parameter(espeak.Parameter.Pitch, 60)
espeak.set_parameter(espeak.Parameter.Rate, 110)
espeak.set_parameter(espeak.Parameter.Range, 600)
espeak.synth("Hey Guys My name is Jerry")
time.sleep(2)

MODELDIR = "/home/uawsscu/PycharmProjects/DetectML/object_recognition_detection/model_LG"
DATADIR = "/home/uawsscu/PycharmProjects/DetectML/object_recognition_detection/dataLG"

config = Decoder.default_config()
config.set_string('-logfn', '/dev/null')
config.set_string('-hmm', path.join(MODELDIR, 'en-us/en-us'))
config.set_string('-lm', path.join(MODELDIR, 'en-us/en-us.lm.bin'))
config.set_string('-dict', path.join(MODELDIR, 'en-us/cmudict-en-us.dict'))
decoder = Decoder(config)

# Switch to JSGF grammar
jsgf = Jsgf(path.join(DATADIR, 'sentence.gram'))
rule = jsgf.get_rule('sentence.move') #>> public <move>
fsg = jsgf.build_fsg(rule, decoder.get_logmath(), 7.5)
fsg.writefile('sentence.fsg')

decoder.set_fsg("sentence", fsg)
decoder.set_search("sentence")

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
stream.start_stream()

in_speech_bf = False
decoder.start_utt()

STPindex = 0
STPname =""
while True:

    buf = stream.read(1024)
    if buf:
        decoder.process_raw(buf, False, False)

        if decoder.get_in_speech() != in_speech_bf:
            in_speech_bf = decoder.get_in_speech()
            if not in_speech_bf:
                decoder.end_utt()

                try:
                    strDecode = decoder.hyp().hypstr
                    if strDecode != '':
                        print 'Stream decoding result:', strDecode
                        # >>>>>>> END <<<<<<<<<<<<
                        if strDecode[-3:] == 'end':
                            obj_name = get_object_train(strDecode)
                            buff = search_Buff_Detect(1)
                            try :
                                remove_Buff_Detect(1)
                            except :
                                print "Table Buffer NULL"

                            print "Search : ", search_Buff_Detect(1)

                            if(obj_name == buff):
                                print "ADD Object to Table object_Train : ",obj_name
                                lenObj = int(lenDB("corpus_Obj.db", "SELECT * FROM object_Train")) # count ROWs
                                obj_check = insert_object_Train(obj_name,lenObj+1) #check Found objects?

                        # >>>>>>> ARM <<<<<<<<<<<<
                        elif STPindex == 0 and strDecode[:14] == 'this is how to' and strDecode[-4:] == "step":

                            STPindex = int(text2int(strDecode))
                            STPname = get_TrainArm(strDecode)  # grab ball
                            print("SAVE NAME TO Table Main_action")


                        elif STPindex > 0 and strDecode == 'call back step':

                            STPindex -= 1
                            print STPindex, " : ", STPname

                        # >>>>>>> JERRY <<<<<<<<<<<<
                        elif strDecode[:5] == 'jerry':
                            print get_object_command(strDecode)
                            #corpus_Arm
                        
                        
                        # >>>>>>> PASS DO YOU KNOW~??? <<<<<<<<<<<<
                        elif strDecode[:11] == 'do you know':
                            obj_name = get_object_question(strDecode)
                            print(obj_name)
                            obj_find = search_object_Train(obj_name)

                            if obj_find != "None":
                                print "Yes , I know!"
                            else: print "No , I don't know!"



                except AttributeError:
                    pass
                decoder.start_utt()
    else:
        break
decoder.end_utt()
print('An Error occured :', decoder.hyp().hypstr)
