#1 .Generate Random password of Varying length: print the generated password that matches the user requested 
#2 . order of characters within the password must be random 
#3. Generate Random Password of Fixed Length of 6 chars.It must have atleast 2 alphabets, 1 number and 1 spl character. 
import random
# alphabet - a-z
alpha = ['a','b','c', 'd', 'e', 'f']
# num 1-9
num = ['1','2','4','6']
# all 
charp = ['$','%', '$', '#', '%']


# user input : Ask user to enter the size of password they want to be generated min num 5 chatracter . 
# then generate a random password that coinsists of 2 alphabets 2 signs and 1 number 

countChar = int (input("Enter the size of password you want min is 5 chars "))
print( "you want password of size",countChar,"we will share shortly" )
userpwdCount = 0 
userpassword = [] 
whileloop =0
while userpwdCount < countChar: 
    whileloop +=  1 
    print(whileloop, "is the while loop count")
    
    userpassword.append( random.choice(alpha))
    userpassword.append(random.choice(alpha))
    userpwdCount = userpwdCount+ 2
    userpassword.append(random.choice(num))
    userpwdCount= userpwdCount+1 
    userpassword.append(random.choice(charp))
    userpassword.append(random.choice(charp))
    userpwdCount= userpwdCount+2
    print(userpwdCount)
generatedpassword = ""
for i in userpassword: 
    generatedpassword = generatedpassword+i
print(generatedpassword)
