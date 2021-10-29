import random  # importing random module

def game(c,y):
# checking condition when computer turn = your turn
    if c==y:
        return "tie"
#checking condition when computer chooses stone
    elif c=="s":
        if y=="p":
            return "you win!"
        else:
            return "you loose!"
#checking condition when computer chooses paper
    elif c=="p":
        if y=="sc":
            return "you win!"
        else:
            return "you loose!"
#checking condition when computer chooses scissor
    elif c=="sc":
        if y=="s":
            return "you win!"
        else:
            return "you loose!"
#taking input from computer by random module
print("computer turn: stone(s) paper(p) scissor(sc):-")
rand=random.randint(0,2)
if rand==0:
    c="s" 
elif rand==1:
    c="p"
else:
    c="sc"
#taking input from user
y=input("your turn: stone(s),paper(p),scissor(sc):-")
#putting c,y value in game function
a=game(c,y)
#printing what computer chooses and what is choosen by you
print(f"computer chooses {c}")
print(f"you chooses {y}")
#printing final result whether u win or loose
print(a)