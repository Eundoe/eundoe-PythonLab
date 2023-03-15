from tkinter import *
from tkinter import filedialog
import pandas as PD
import csv 
import webbrowser

class FilterSystem(object):
    file = ''
    numbering = 0
    def FindFiles() :
        filename = filedialog.askopenfilename(initialdir='./',
                                          title= "Select CSV files",
                                          filetypes=(("CSV files",
                                                      "*.csv*"),
                                                      ("all files", "*.*")))
        FilterSystem.file = filename
        if FilterSystem.file == "":
            pass
        else:
            label_selected_file.configure(text = "Selected File : " + filename)

    def FilteringMk3() : 
        x = FilterSystem.file
        if x == "" :
            label_selected_file.configure(text="Wrong file selected plz confirm again")
        else :
            with open(x) as OriginalData :
                newData = csv.reader(OriginalData)
                array = list(newData)
            spaceDelete = array[-(len(array) - 1):-1]
            backArray = spaceDelete[-50:]
            PD.DataFrame(backArray).to_csv(x, index_label=False, header= False,index=False)
            PD.DataFrame(backArray).to_csv("CopyData" + str(FilterSystem.numbering) + ".csv", index_label=False, header= False,index=False)
            FilterSystem.numbering += 1
            FilterSystem.file = ""
            label_selected_file.configure(text = "Convert Success plz confirm")
    def Devloper():
        webbrowser.open_new("https://github.com/Eundoe/Eundoe")



window = Tk()
# windows
window.title('Filtering MK3 by EUNDOE')
window.geometry("500x150")
window.config(background="white")
window.resizable(False, False)

# GUI
label_selected_file = Label(window, text= "Select file plz",
                            fg="red", font= ('Arial',14))
button_find_file = Button(window, text = "Load File",
                          command= FilterSystem.FindFiles)
button_convert_file= Button(window, text = "Convert",
                          command= FilterSystem.FilteringMk3)
label_github_check = Label(window, text="Confirm Github", font=('Arial',8), fg='blue', background='white',
                           cursor= "hand2")

#Prettier 

label_selected_file.pack(pady=20, ipady=5, ipadx=10)
button_find_file.place(width=80,x=30,y=80, height=30)
button_convert_file.place(width=80,x=130,y=80, height=30)
label_github_check.place(x= 350, y=130)
label_github_check.bind("<Button-1>", lambda e: FilterSystem.Devloper())




window.mainloop()