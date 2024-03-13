
import sys
HOutput="";
instruction=sys.argv[1]
if instruction == '-a': #test the first comman argument
    #this section test each known operator and adds it to our hex output
    if sys.argv[2] == "'add":
        HOutput=HOutput+"00"
    elif sys.argv[2] == "'addi":
        HOutput=HOutput+"08"
    elif sys.argv[2] == "'sub":
        HOutput=HOutput+"00"
    elif sys.argv[2] == "'sll":
        HOutput=HOutput+"00"
    elif sys.argv[2] == "'srl":
        HOutput=HOutput+"00"
    elif sys.argv[2] == "'lw":
        HOutput=HOutput+"23"
    elif sys.argv[2] == "'sw":
        HOutput=HOutput+"2b"
    #this section loops 3 times to test each input
    for i in range(3,6):
        #check if current argument is zero register
        if sys.argv[i]=="$zero'" or sys.argv[i]=="$zero,":
            HOutput=HOutput+"00"
        
        #check if current argument is Assembly Temporary register
        elif sys.argv[i]=="$at'" or sys.argv[i]=="$at,":
            HOutput=HOutput+"01"
        
        #check if current argument is Expression Evaluation register
        elif sys.argv[i]=="$v0'" or sys.argv[i]=="$v0,":
            HOutput=HOutput+"02"
        elif sys.argv[i]=="$v1'" or sys.argv[i]=="$v1,":
            HOutput=HOutput+"03"
        
        #check if current argument is Argument register
        elif sys.argv[i]=="$a0'" or sys.argv[i]=="$a0,":
            HOutput=HOutput+"04"
        elif sys.argv[i]=="$a1'" or sys.argv[i]=="$a1,":
            HOutput=HOutput+"05"
        elif sys.argv[i]=="$a2'" or sys.argv[i]=="$a2,":
            HOutput=HOutput+"06"
        elif sys.argv[i]=="$a3'" or sys.argv[i]=="$a3,":
            HOutput=HOutput+"07"
        
        #check if current argument is first set of temp register
        elif sys.argv[i]=="$t0'" or sys.argv[i]=="$t0,":
            HOutput=HOutput+"08"
        elif sys.argv[i]=="$t1'" or sys.argv[i]=="$t1,":
            HOutput=HOutput+"09"
        elif sys.argv[i]=="$t2'" or sys.argv[i]=="$t2,":
            HOutput=HOutput+"0a"
        elif sys.argv[i]=="$t3'" or sys.argv[i]=="$t3,":
            HOutput=HOutput+"0b"
        elif sys.argv[i]=="$t4'" or sys.argv[i]=="$t4,":
            HOutput=HOutput+"0c"
        elif sys.argv[i]=="$t5'" or sys.argv[i]=="$t5,":
            HOutput=HOutput+"0d"
        elif sys.argv[i]=="$t6'" or sys.argv[i]=="$t6,":
            HOutput=HOutput+"0e"
        elif sys.argv[i]=="$t7'" or sys.argv[i]=="$t7,":
            HOutput=HOutput+"0f"
        
        #check if current argument is Save register
        elif sys.argv[i]=="$s0'" or sys.argv[i]=="$s0,":
            HOutput=HOutput+"10"
        elif sys.argv[i]=="$s1'" or sys.argv[i]=="$s1,":
            HOutput=HOutput+"11"
        elif sys.argv[i]=="$s2'" or sys.argv[i]=="$s2,":
            HOutput=HOutput+"12"
        elif sys.argv[i]=="$s3'" or sys.argv[i]=="$s3,":
            HOutput=HOutput+"13"
        elif sys.argv[i]=="$s4'" or sys.argv[i]=="$s4,":
            HOutput=HOutput+"14"
        elif sys.argv[i]=="$s5'" or sys.argv[i]=="$s5,":
            HOutput=HOutput+"15"
        elif sys.argv[i]=="$s6'" or sys.argv[i]=="$s6,":
            HOutput=HOutput+"16"
        elif sys.argv[i]=="$s7'" or sys.argv[i]=="$s7,":
            HOutput=HOutput+"17"
        
        #check if current argument is second set of temp register
        elif sys.argv[i]=="$t8'" or sys.argv[i]=="$t8,":
            HOutput=HOutput+"18"
        elif sys.argv[i]=="$t9'" or sys.argv[i]=="$t9,":
            HOutput=HOutput+"19"
        
        #check if current argument is kernal register
        elif sys.argv[i]=="$k0'" or sys.argv[i]=="$k0,":
            HOutput=HOutput+"1a"
        elif sys.argv[i]=="$k1'" or sys.argv[i]=="$k1,":
            HOutput=HOutput+"1b"
        
        #check if current argument is pointer register
        elif sys.argv[i]=="$gp'" or sys.argv[i]=="$gp,":
            HOutput=HOutput+"1c"
        elif sys.argv[i]=="$sp'" or sys.argv[i]=="$sp,":
            HOutput=HOutput+"1d"
        elif sys.argv[i]=="$fp'" or sys.argv[i]=="$fp,":
            HOutput=HOutput+"1e"
            
        #check if current argument is Return address register
        elif sys.argv[i]=="$ra'" or sys.argv[i]=="$ra,":
            HOutput=HOutput+"1f"
        
elif sys.argv[1]=='-m': #test the first command argument
    HOutput=HOutput+"'"
    tempString=sys.argv[2]
    #this section test the first two character of the string  to the known operators and adds it to our string output
    if tempString[1] == "2" and tempString[2]=="0":
        HOutput=HOutput+"add "
    elif tempString[1] == "0" and tempString[2]=="8":
        HOutput=HOutput+"addi "
    elif tempString[1] == "2" and tempString[2]=="2":
        HOutput=HOutput+"sub "
    elif tempString[1] == "0" and tempString[2]=="0":
        HOutput=HOutput+"sll "
    elif tempString[1] == "0" and tempString[2]=="2":
        HOutput=HOutput+"srl "
    elif tempString[1] == "2" and tempString[2]=="3":
        HOutput=HOutput+"lw "
    elif tempString[1] == "2" and tempString[2]=="b":
        HOutput=HOutput+"sw "
    i=3
    while i<=8:
        j=i+1 #an easy variable to help measure the next number
        #check if current argument is zero register
        if tempString[i]=="0" and tempString[j]=="0":
            HOutput=HOutput+"$zero"
        
        #check if current argument is Assembly Temporary register
        elif tempString[i]=="0" and tempString[j]=="1":
            HOutput=HOutput+"$at"
        
        #check if current argument is Expression Evaluation register
        elif tempString[i]=="0" and tempString[j]=="2":
            HOutput=HOutput+"$v0"
        elif tempString[i]=="0" and tempString[j]=="3":
            HOutput=HOutput+"$v1"
        
        #check if current argument is Argument register
        elif tempString[i]=="0" and tempString[j]=="4":
            HOutput=HOutput+"$a0"
        elif tempString[i]=="0" and tempString[j]=="5":
            HOutput=HOutput+"$a1"
        elif tempString[i]=="0" and tempString[j]=="6":
            HOutput=HOutput+"$a2"
        elif tempString[i]=="0" and tempString[j]=="7":
            HOutput=HOutput+"$a3"
        
        #check if current argument is first set of temp register
        elif tempString[i]=="0" and tempString[j]=="8":
            HOutput=HOutput+"$t0"
        elif tempString[i]=="0" and tempString[j]=="9":
            HOutput=HOutput+"$t1"
        elif tempString[i]=="0" and tempString[j]=="a":
            HOutput=HOutput+"$t2"
        elif tempString[i]=="0" and tempString[j]=="b":
            HOutput=HOutput+"$t3"
        elif tempString[i]=="0" and tempString[j]=="c":
            HOutput=HOutput+"$t4"
        elif tempString[i]=="0" and tempString[j]=="d":
            HOutput=HOutput+"$t5"
        elif tempString[i]=="0" and tempString[j]=="e":
            HOutput=HOutput+"$t6"
        elif tempString[i]=="0" and tempString[j]=="f":
            HOutput=HOutput+"$t7"
        
        #check if current argument is Save register
        elif tempString[i]=="1" and tempString[j]=="0":
            HOutput=HOutput+"$s0"
        elif tempString[i]=="1" and tempString[j]=="1":
            HOutput=HOutput+"$s1"
        elif tempString[i]=="1" and tempString[j]=="2":
            HOutput=HOutput+"$s2"
        elif tempString[i]=="1" and tempString[j]=="3":
            HOutput=HOutput+"$s3"
        elif tempString[i]=="1" and tempString[j]=="4":
            HOutput=HOutput+"$s4"
        elif tempString[i]=="1" and tempString[j]=="5":
            HOutput=HOutput+"$s5"
        elif tempString[i]=="1" and tempString[j]=="6":
            HOutput=HOutput+"$s6"
        elif tempString[i]=="1" and tempString[j]=="7":
            HOutput=HOutput+"$s7"
        
        #check if current argument is second set of temp register
        elif tempString[i]=="1" and tempString[j]=="8":
            HOutput=HOutput+"$t8"
        elif tempString[i]=="1" and tempString[j]=="9":
            HOutput=HOutput+"$t9"
        
        #check if current argument is kernal register
        elif tempString[i]=="1" and tempString[j]=="a":
            HOutput=HOutput+"$k0"
        elif tempString[i]=="1" and tempString[j]=="b":
            HOutput=HOutput+"$k1"
        
        #check if current argument is pointer register
        elif tempString[i]=="1" and tempString[j]=="c":
            HOutput=HOutput+"$gp"
        elif tempString[i]=="1" and tempString[j]=="d":
            HOutput=HOutput+"$sp"
        elif tempString[i]=="1" and tempString[j]=="e":
            HOutput=HOutput+"$fp"
            
        #check if current argument is Return address register
        elif tempString[i]=="1" and tempString[j]=="f":
            HOutput=HOutput+"$ra"
        
        i=i+2
        if i<=7:
            HOutput=HOutput+", "
        else:
            HOutput=HOutput+"' "
else:
    print("Command Not accepted")
    
print(HOutput)
