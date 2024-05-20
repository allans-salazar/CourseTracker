import tkinter

global maxWindows # counts for the max number of windows
maxWindows = 1

#Window pop-up to add information for a new Course 
class addCourseWindow(tkinter.Toplevel): 
    def __init__(self):
        super().__init__()
        self.title("Add New Course")
        self.geometry("300x200")
        tkinter.Label(self, text = "Hello").pack()
        self.protocol("WM_DELETE_WINDOW", self.closed)

    #Functions for addCourseWindow
    def closed(self):
        global maxWindows
        maxWindows-=1
        self.destroy()

#Functions for main_window
def createWindow():
    global maxWindows 

    if maxWindows < 2:
        maxWindows+=1
        newWindow = addCourseWindow()

#Main Window 
main_window = tkinter.Tk()

main_window.title("Course Tracker")
main_window.geometry("500x200")

AddCourseButton_Frame = tkinter.Frame(main_window)
AddCourseButton = tkinter.Button(AddCourseButton_Frame, height= 2, width=7, text = "Add a Course", command=createWindow)
AddCourseButton.pack()
AddCourseButton_Frame.pack()

tkinter.mainloop()