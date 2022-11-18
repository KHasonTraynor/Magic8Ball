import magic
import time

words= ['How','What','Will',"Who",'Where','When','Why','Are','Can','Which','Whose','If','Am','Could','Would','Did','Do']

print("""
      _.a$$$$$a._
     ,$$$$$$$$$$$$$.
   ,$$$$$$$$$$$$$$$$$.
  d$$$$$$$$$$$$$$$$$$$b
 d$$$$$$$$~'"`~$$$$$$$$b
($$$$$$$p   _   q$$$$$$$)
$$$$$$$$   (_)   $$$$$$$$
$$$$$$$$   (_)   $$$$$$$$
($$$$$$$b       d$$$$$$$)
 q$$$$$$$$a._.a$$$$$$$$p
  q$$$$$$$$$$$$$$$$$$$p
   `$$$$$$$$$$$$$$$$$'
     `$$$$$$$$$$$$$'
       `~$$$$$$$~'
""")
time.sleep(1.0)
print("Hello wanderer!")
time.sleep(1.50)
question= input("What answer can I find for you today?  ")
question = question.capitalize()

while not question.startswith(tuple(words)) or len(question) < 6:
    print ("Hmm, I dont see a question please try again")
    question= input("What answer can I find for you today?(yes or no questions)   ")
    question = question.capitalize()

if question.startswith(tuple(words)):
    magic.MagicBall()