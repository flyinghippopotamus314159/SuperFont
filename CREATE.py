""""
SuperFont

Created by FlyingHippopotamus314159 under a GNU Public Liscence v3.0 (GNU GLPv3)

Commands:
-init_prog() initalises program
-make_chr()  make a new character
""""
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
def init_prog():
    if not os.path.exists("fonts"):
        os.makedirs("fonts")
        file.close()
    else:
        procceed=input("Procceeding will delete all saved fonts. To procceed, press y>>>")
        if procceed=="y":
            shutil.rmtree("fonts", ignore_errors=False, onerror=None)
            os.makedirs("fonts") 
#compiles fonts into a single file:
##def compile_font(font,export_name):
##    font_content=[]#creates a list with 200 empty strings
##    for i in range(200):
##        font_content.append("")
##        file=open(str("fonts/"+font+str("/"+str(i)+".f0nt")),"r")
##        font_content[i]=file
##        file.close()
##    file=open(str(export_name+".uiff"),"w")
##    file_content=""
##    for i in range(200):
##        font_content.append(str(str(font_content[i])+";"))
##    file.write(file_content)
##    file.close()
