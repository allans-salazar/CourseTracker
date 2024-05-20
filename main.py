import tkinter

def addCourseWindow():
    addCourseWindow = tkinter.Tk()
    addCourseWindow.title("Add New Course")
    addCourseWindow.geometry("300x200")
    

main_window = tkinter.Tk()

main_window.title("Course Tracker")
main_window.geometry("500x200")

AddCourseButton_Frame = tkinter.Frame(main_window)
AddCourseButton = tkinter.Button(AddCourseButton_Frame, height= 2, width=7, text = "Add a Course", command=addCourseWindow)
AddCourseButton.pack()
AddCourseButton_Frame.pack()

tkinter.mainloop()