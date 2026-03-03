import random
from wordfreq import top_n_list
words = top_n_list("en", 5000)
words = [i for i in words if 5 <= len(i) <= 6 and not i.isdigit()]
def scramble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)
score=0
list1=[]
n=int(input("Enter Number of Rounds: "))
for i in range(0,n):
    x=random.choice(words)
    list1.append(x)
for i in range(0,n):
    attempts=3
    a=scramble_word(list1[i])
    print("Unscranble this Word:",a)
    while attempts>0:
        guess=input("Enter Your Guess: ").lower()
        if guess==list1[i]:
            print("✅ Correct! You win this round..!!!")
            score+=1
            break
        else:
            attempts=attempts-1
            if attempts>0:
                print(f"❌ Incorrect! Attempts left: {attempts}")
            else:
                print("❌ No attempts left..!!!")
    if guess!=list1[i]:
        print("The correct word is :",list1[i])
    print()
print("\n===== GAME OVER =====")
print("Your final score:", score, "/", n)