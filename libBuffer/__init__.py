buff1 = ""
buffC = ""
buff2 = ""

def flipBuffers():
    buffC = buff2
    buff2 = buff1
    buff1 = buffC
    buffC = ""

def modifyBuffer(buffer, value):
    if buffer == 1:
        buff1 = value
    elif buffer == 2:
        buff2 = value
    else:
        print("Buffer does not exist.")


