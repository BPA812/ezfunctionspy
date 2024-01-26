def LoopPrintLine(text,times):
    for i in range(times):
        print(text)
def PiDigits():
    return 3.1415926535
def GameMakerDialog(speakerName,dialog,quotemarks):
    print(speakerName + ':')
    print("-"*20)
    if quotemarks == '1':
        print("'" + dialog + "'")
    else:
        print(dialog)
    print("-"*20)