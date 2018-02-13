
def text_STEP(text):
    text = text.split()
    STEP = ""
    for i in range(-2,0):
        STEP = STEP + " " + text[i]
        #print STEP+".."
    return STEP

def cut_STEP(text):
    STEP = text_STEP(text)
    test = text.split(STEP,1)[0]
    return test


test ="This is how to grab ball three step"

print cut_STEP(test)

