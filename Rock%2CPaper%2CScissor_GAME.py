
# coding: utf-8

# In[9]:

from random import randint


def A():
    print("WELCOME To Rock__Paper__ScissoR. Lets Play: ")
    print("Harshil vs You")

def game():
    
    You = input("Enter your word: ")
    A = ['rock','paper','paper']
    Harshil = A[randint(0,2)]
    print("Harshil chooses: ",Harshil)

    if Harshil == "rock" and You == "rock":
        print("It's a TIE!!")
        print("Wanna try again??")
    
    elif Harshil == "rock" and You == "paper":
        print("You win!!!")
        
    elif Harshil == "rock" and You == "scissor":
        print("Harshil wins. You loose!!!")
        
    elif Harshil == "paper" and You == "rock":
        print("Harshil wins. You loose!!!")
        
    elif Harshil == "paper" and You == "paper":
        print("It's a TIE!!!")
        print("Wanna try again??")
        
    elif Harshil == "paper" and You == "scissor":
        print("You win!!!")
        
    elif Harshil == "scissor" and You == "rock":
        print("You win!!!")
        
    elif Harshil == "scissor" and You == "paper":
        print("Harshil wins. You loose!!!")
        
    elif Harshil == "scissor" and You == "scissor":
        print("Its a TIE!!!")
        print("Wanna try again??")
   
    else:
        print("Enter correct input")
        
if __name__ == "__main__":
    
    A()
    game()
    

