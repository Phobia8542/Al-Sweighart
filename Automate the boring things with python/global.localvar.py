#Lesson 10 (Global and Local variables)
#spam = 42 #Global variable

#def eggs():
    #spam = 42 #local variable(Are nested within a function)

#print(eggs)
#print(spam)
#print ('This says stuff')
#print ('This also says stuff')

#def spam():
    #eggs = 99
    #bacon()
    #Local scope will call bacon function below
    #print(eggs)
    

#def bacon():
    #ham = 101
    #eggs = 0
    #These eggs are different from the one above (Exists in local scope)

#spam()
#Python will check for local variable before checking for global

#These two eggs are seperate
def spam():
    #global eggs
    #You can change the local var(eggs) to the global with a global statement
    eggs = 'Hello'
    print(eggs)
    #This is the nested/local var

eggs = 42
spam()
print(eggs)
#This is a global var