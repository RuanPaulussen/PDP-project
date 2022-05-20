from tkinter import *

def submit():
    if Question.get() != "" and Answer.get() != "" and Level.get().isdigit():
        with open("Questions.txt","a") as file:
            file.write(Question.get() + "," + Answer.get() + "," + Level.get() + "\n")
        Level.set("")
        Question.set("")
        Answer.set("")
    else:
        print("yes")

root = Tk()
main = Frame(root, bg="white", width=500, height=500)
main.pack()

Question = StringVar()
QuestionFrame = Frame(main)
Questionfield = Entry(QuestionFrame, textvariable=Question,width= 50)
Questionfield.grid(row=1)
QuestionLabel = Label(QuestionFrame, text="Question")
QuestionLabel.grid(row=0)
QuestionFrame.place(anchor=CENTER, relx=0.5, rely=0.4)

Answer = StringVar()
answerframe = Frame(main)
answerfield= Entry(answerframe, textvariable=Answer)
answerfield.grid(row=1)
answerlabel = Label(answerframe, text="Answer")
answerlabel.grid(row=0)
answerframe.place(anchor=CENTER, relx=0.5, rely=0.5)

Level = StringVar()
levelframe = Frame(main)
levelfield= Entry(levelframe, textvariable=Level)
levelfield.grid(row=1)
levellabel = Label(levelframe, text="Level")
levellabel.grid(row=0)
levelframe.place(anchor=CENTER, relx=0.5, rely=0.6)

submit = Button(main, text="Enter", font=("Arial", 15), command=submit)
submit.place(anchor=CENTER, relx=0.5, rely=0.7)

mainloop()