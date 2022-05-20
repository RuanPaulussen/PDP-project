from tkinter import *

def next_question():
    line = file.readline().strip()
    if line:
        list = line.split(",")
        if int(current_level) == int(list[2]):
            imported_question = list[0]
            global imported_answer
            imported_answer = list[1]
            Question.set(imported_question)
        elif int(current_level) <= highest_level:
            next_question()
        else:
            main.configure(bg="green")
            Question.set("You Won")
    else:
        file.seek(0)
        next_question()

def submit (event):
    given_answer = Answer.get()
    global current_level
    if given_answer.lower() == imported_answer.lower():
        main.configure(bg="lightgreen")
        current_level += 0.2
    else:
        main.configure(bg="red")
        if current_level >= 1.2:
            current_level -= 0.2
        else:
            current_level = 1
    Level.set(round(current_level,1))
    Answer.set("")
    next_question()
def Submit ():
    given_answer = Answer.get()
    global current_level
    if given_answer.lower() == imported_answer.lower():
        main.configure(bg="lightgreen")
        current_level += 0.1
    else:
        main.configure(bg="red")
        if current_level >= 1.2:
            current_level -= 0.2
        else:
            current_level = 1
    Level.set(round(current_level,1))
    Answer.set("")
    next_question()


highest_level = 1
with open("Questions.txt") as file :
    line = file.readline().strip()
    while line:
        list = line.split(",")
        if int(highest_level) < int(list[2]):
            highest_level = int(list[2])
        line = file.readline().strip()
current_level = 1


root = Tk()
main = Frame(root, bg="white", width=1000, height=500)
main.pack()

Question = StringVar()
file = open("Questions.txt")

line = file.readline().strip()
list = line.split(",")
if current_level == int(list[2]):
    imported_question = list[0]
    imported_answer = list[1]
    Question.set(imported_question)
else:
    next_question()


Questionlabel = Label(main, textvariable=Question, font=("Arial", 20))
Questionlabel.place(anchor=CENTER, relx=0.5, rely=0.4)

Answer = StringVar()
answerField = Entry(main, textvariable=Answer)
answerField.bind('<Return>',submit)
answerField.place(anchor=CENTER, relx=0.5, rely=0.5)

submit = Button(main, text="Enter", font=("Arial", 15), command=Submit)
submit.place(anchor=CENTER, relx=0.5, rely=0.6)

Level = StringVar()
Level.set(round(current_level, 1))
levelLabel = Label(main, textvariable=Level, font=("Arial", 20))
levelLabel.place(anchor=CENTER, relx=0.9, rely=0.1)

mainloop()