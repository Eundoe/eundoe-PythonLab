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

    def FilteringMk4() : 
        x = FilterSystem.file
        realname = os.path.split(x)
        svalue = int(entry_value_array.get())
        if not os.path.exists("./ConvertedData"):
            os.makedirs('./ConvertedData')
        if not os.path.exists("./CopyData"):
            os.makedirs('./CopyData')
        if x == "" :
            label_selected_file.configure(text="Wrong file selected")
        else :
            with open(x) as OriginalData :
                newData = csv.reader(OriginalData)
                array = list(newData)
            spaceDelete = array[-(len(array) - 1):-1]
            backArray = spaceDelete[-(svalue + 500): -(svalue)]
            PD.DataFrame(backArray).to_csv("./ConvertedData/" + realname[1], index_label=False, header= False,index=False)
            PD.DataFrame(backArray).to_csv("./CopyData/Copied" + str(FilterSystem.numbering) + ".csv", index_label=False, header= False,index=False)
            FilterSystem.numbering += 1
            FilterSystem.file = ""
            label_selected_file.configure(text = "Convert Success get 500 data!")
            if os.path.exists(x):
                os.remove(x)
    def Devloper():
        webbrowser.open_new("https://github.com/Eundoe/eundoe-PythonLab")
