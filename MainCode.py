from os import path
import pyaudio
import time

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

from check4 import *
from manageDB import *
from detectObj import *

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

                        if strDecode[-3:] == 'end':
                            obj_name = get_object_train(strDecode) #word
                            obj_detect = detect_Object() #
                            if obj_name == obj_detect:  # ckeck speech and pic
                                lenObj = int(lenDB("corpus_Obj.db", "SELECT * FROM object_Train")) # count ROWs
                                obj_check = insert_object_Train(strDecode,lenObj) #check Found objects?

                        elif strDecode[:5] == 'jerry':
                            get_object_command(strDecode)
                            #corpus_Arm

                        elif strDecode[:11] == 'do you know':
                            obj_name = get_object_question(strDecode)
                            obj_find = search_object_Train(obj_name)

                            if obj_find != "None":
                                print "No, I don't know!"
                            else: print "Yes , I know!"

                        elif strDecode[:14] == 'this is how to':
                            get_TrainArm(strDecode)


                except AttributeError:
                    pass
                decoder.start_utt()
    else:
        break
decoder.end_utt()
print('An Error occured :', decoder.hyp().hypstr)