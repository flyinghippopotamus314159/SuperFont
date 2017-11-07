""""
SuperFont

Created by FlyingHippopotamus314159 under a GNU Public Liscence v3.0 (GNU GLPv3)

Commands:
-init_prog() initalises program
-font_init() initalises a new compressed font. font compression not currently available
-make_chr()  make a new character
-create_text() creates a text 
""""
import os, shutil
def font_init(font_file,font_import):
    file=open(str(font_file+".uiff"), "r")
    os.makedirs(str("fonts/"+font_import))
    fileRead=str(file.read())
    for i in range(200):
        fontLetters=fileRead.split(";")
        print(fontLetters)
        file.close()
        newfile=open(str(str("fonts/"+font_import)+"/"+str(str(i)+".f0nt")), "w")
        newfile.write(fontLetters[i])
    newnewfile=open(str("fonts/"+font_import+"//exist"),"w")
    newnewfile.write("y")
def init_prog():
    if not os.path.exists("fonts"):
        os.makedirs("fonts")
        file.close()
    else:
        procceed=input("Procceeding will delete all saved fonts. To procceed, press y>>>")
        if procceed=="y":
            shutil.rmtree("fonts", ignore_errors=False, onerror=None)
            os.makedirs("fonts")                    
def make_chr(font_name,chr_name,width):
    try:
        file=open(str("fonts/"+font_name+"//exist.f0nt"),"w")
        file.write("y")
    except:
        os.makedirs(str("fonts/"+font_name))
        file=open(str("fonts/"+font_name+"//exist.f0nt"),"w")
        file.write("y")
    letter=[]
    n=0
    writeToFile=""
    try:
        centreOffset=int(width)
    except:
        centreOffset=10
    while n<10:
        line=input(">")
        line=line.center(centreOffset)
        line=line+":"
        writeToFile=writeToFile+line
        n=n+1
    file=open(str("fonts/"+font_name+str("/"+str(ord(str(chr_name)))+".f0nt")), "w")
    file.write(writeToFile)
    print(writeToFile)
    file.close()
def create_text(text,font_name,file_name):
    letter=[]
    for i in range(len(text)):
        letter.append(str(text)[i])
    fileReadFull=[]
    for i in range(len(letter)):
        file=open(str("fonts/"+font_name+str("/"+str(ord(letter[i]))+".f0nt")),"r")
        fileRead=str(file.read())
        fileReadList=fileRead.split(":")
        fileReadFull.append(fileReadList)
        file.close()
    for i in range(10):
        n=0
        output=""
        while n<len(letter):
            output=output+fileReadFull[n][i]
            n=n+1
        print(output)
        if file_name!="n":
            try:
                file=open(file_name,"w")
                file.write(output)
                file.close()
            except:
                return("ERROR:could not write to file")
