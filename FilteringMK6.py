from tkinter import *
from tkinter import filedialog
import pandas as PD
import csv 
import webbrowser
import os
import matplotlib.pyplot as plt

#Function
class FilterSystem(object):
    file = ''
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
            with open(filename) as GraphData:
                visualData = list(csv.reader(GraphData))
                listData = visualData[-(len(visualData)) : -1]
                zdirData = []
                for item in listData :
                    result = list(item)
                    zdirData.append(float(result[2]))
            plt.figure(figsize=(11,6))
            plt.title(os.path.split(filename)[1] + 'Z dir Graph')
            plt.plot(zdirData)
            plt.show()

    def FilteringMk5() : 
        x = FilterSystem.file
        realname = os.path.split(x)
        svalue = int(entry_value_array.get())
        if not os.path.exists("./ConvertedData"):
            os.makedirs('./ConvertedData')
        if x == "" :
            label_selected_file.configure(text="Wrong file selected")
        else :
            with open(x) as OriginalData :
                newData = csv.reader(OriginalData)
                array = list(newData)
            spaceDelete = array[-(len(array) - 1):-1]
            backArray = spaceDelete[-(svalue + 500): -(svalue)]
            PD.DataFrame(backArray).to_csv("./ConvertedData/" + realname[1], index_label=False, header= False,index=False)
            FilterSystem.file = ""
            label_selected_file.configure(text = "Convert Success get 500 data!")
            if os.path.exists(x):
                os.remove(x)
    def Devloper():
        webbrowser.open_new("https://github.com/Eundoe/eundoe-PythonLab")
