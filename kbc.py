questions = ["what is the captial of india?","what is the capitial of Maharashtra?","What is capital of USA?"]
answers = ["Delhi","Mumbai","Washington DC"]
options = [["Mumbai","Delhi","Kolkata","Bangalore"],
           ["Latur","Satara","Pune","Mumbai"],
           ["New York","Washington DC","LA","Miami"]
           ]
prize = [10,100,1000]

sum = 0

for i in range(len(questions)):
    print(questions[i])
    print(options[i])
    ans = str(input("your answer is : "))
    print(ans)
    if ans == answers[i]:
        sum = sum+prize[i]
        print("Congratulations you won : ",sum)
    else:
        print("Sorry you failed it and won nothing")
        break


