from textblob import TextBlob
#from capture import *
#from Kinect_detect import *


#>>>>>>>>>>>>>>>>>> PASS ThisIs! <<<<<<<<<<<<<<<<<<
def get_object_train(text):
    # CUT "END"
    nounP = ''
    np = False
    print "Train ---Obj---"
    ans = text[0:-3]
    #print "!!" + ans
    b = TextBlob(ans)
    for item in b.noun_phrases:
        #print item
        np = True
        nounP =item

    if(np==False) :
        sentence = b.sentences[0]
        #print sentence

        for word, pos in sentence.tags:
            if pos[0:1] == 'N':
                # CAPTURE
                #cap_ture(word)
                print word + " >>N"
                nounP =word
                break
    return nounP

#>>>>>>>>>>>>>>>> PASS COMMAND! <<<<<<<<<<<<<<<<<<<<
def get_object_command(text):
    print "Command ---Obj---" #Jerry move a ball to the left
    ans = text[6:]
    b = TextBlob(ans)
    sentence = b.sentences[0] #move a ball to the left
    for word, pos in sentence.tags:
        if pos[0:1] == 'N':
            break
    return word

#>>>>>>>>>>>>>>>>>> PASS TrainArm! <<<<<<<<<<<<<<<<
def get_TrainArm(text):
    print "--Verb + Noun--" #this is how to grab a ball
    word = text[15:] #grab a ball
    return word

#>>>>>>>>>>>>>>>>>> PASS Q! <<<<<<<<<<<<<<<<<<
def get_object_question(text):
    print "question--Obj--"
    # CUT "END"
    nounP = ''
    np = False
    b = TextBlob(text)
    for item in b.noun_phrases:
        np = True
        nounP = item

    if (np == False):
        sentence = b.sentences[0]
        for word, pos in sentence.tags:
            if pos[0:1] == 'N':
                nounP = word
                break
    return nounP

#print get_object_question("do you know a red bottle")
#print get_object_command("Jerry move a ball to the left")
#print get_TrainArm("this is how to grab a ball")
print get_object_train("This is a red ball end")