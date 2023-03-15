import pandas as PD
import csv 
import webbrowser

#Function
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
        svalue = int(entry_value_array.get())
        if x == "" :
            label_selected_file.configure(text="Wrong file selected")
        else :
            with open(x) as OriginalData :
                newData = csv.reader(OriginalData)
                array = list(newData)
            spaceDelete = array[-(len(array) - 1):-1]
            backArray = spaceDelete[-(svalue):]
            PD.DataFrame(backArray).to_csv(x, index_label=False, header= False,index=False)
            PD.DataFrame(backArray).to_csv("CopyData" + str(FilterSystem.numbering) + ".csv", index_label=False, header= False,index=False)
            FilterSystem.numbering += 1
            FilterSystem.file = ""
            label_selected_file.configure(text = "Convert Success")
    def Devloper():
        webbrowser.open_new("https://github.com/Eundoe/eundoe-PythonLab")

