
#a fun multiple choice quiz

#this line keeps initial score
score=0

#for style??
print("-----------------------------------------------------)")
#asks a question about a book, and needs user input
quest_1 = input("1. Who wrote the book, Crime and 'Punishment?'? \
                \n A)Fyodor Dostoevsky \
                \n B)Herman Hesse   \
                \n C)Lucy Maude Montgomery \
                \n D)Herman Melville \
                \n <" )
if quest_1 == "A" or "a":
    print("correct!")
    score=score+1
else:
    print("Incorrect")

print("-----------------------------------------------------)")
#ask question 2,need user input
quest_2 = input("2. Who's NOT a character in hit game Limbus Company? \
                \n A)Gregor samsa (The metamorphosis)\
                \n B)Emil Sinclair (Demian:The story o Emil Sinclaire's youth)\
                \n C)Hong Lu (Dream of the Red chamber)\
                \n D)Anne Shirley(Anne of Green Gables) \
                \n <")
if quest_2 == "C" or "c":
    print("correct!")
    score=score+1
else:
    print("Incorrect")

print("-----------------------------------------------------)")
#ask question 3,need user input
quest_3 = input("3. Which game has Mili (The indie band) Not provided music for? \
                \n A)Library of Ruina \
                \n B)Limbus Company \
                \n C) ENDER LILIES:quietus of the knights \
                \n D)Gris \
                \n <")
if quest_3 == "D" or "d":
    print("correct!")
    score=score+1
else:
    print("Incorrect")

print("-----------------------------------------------------)")
#ask question 3,need user inputc

quest_4=input("What drink invoves the use of rice and cinnamon? \
              \n A) Horchata \
              \n B)Colada Morada \
              \n C)Chicha de Piña \
              \n D)jugo de sandia \
              \n <")

if quest_4 == "A" or "a":
    print("correct!")
    score=score+1
else:
    print("Incorrect")

#PRINTS FINAL SCORE
print("Final score: " + str(score))

#these chunks are for an additional bit o personality for the quiz.it determines a response depending of the total score
if score == 0:
    print("Oh well. try again")

elif score == 4:
    print("amazing!")

else:
    print("almost there")