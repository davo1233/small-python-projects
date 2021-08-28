from tkinter import *

unitTypes = {
    'Tonnes': pow(10, -3),
    'Kilograms': pow(10, 0),
    'Grams': pow(10, 3),
    'Milligrams': pow(10, 6),
    'Micrograms': pow(10, 9),
    'Pounds': 2.20462,
    'Ounces': 35.274,
    'Imperial Ton': 0.000984207,
    'US Ton': 0.00110231,
    'Stone': 0.157473,
}


# converts weight from one type of weight to another
def calculate():
    try:
        convertedValue = weight.get() * (unitTypes[convertedWeightType.get()] / unitTypes[weightType.get()])
        convertedWeight.set(convertedValue)
    except TclError:
        newWindow = Tk()
        newWindow.geometry("155x40")
        newWindow.title('Error')
        newWindow.config(bg='white')
        newWindow.resizable(False, False)
        Label(newWindow, bg='white', text='Please enter a number.', font=('helvetica',10,'bold')).grid(row=1,column=1)


# initialise the window
wc = Tk()
wc.geometry('250x100')
wc.config(background='white')
wc.title('Weight converter')
wc.resizable(False, False)

# create an option menu for the weight to be converted
weightType = StringVar(wc)
weightType.set('Kilograms')
menuWeight = OptionMenu(wc, weightType, *unitTypes.keys())
menuWeight.grid(row=1, column=1)

# entry to insert a number for the weight to be converted
weight = IntVar(wc)
weight.set(0)
weightInput = Entry(wc, text='Input',textvariable=weight, width=15, font=('times', 15))
weightInput.grid(row=1, column=2)

# create an option menu for the weight to be converted
convertedWeightType = StringVar(wc)
convertedWeightType.set('Tonnes')
menuWeight = OptionMenu(wc, convertedWeightType, *unitTypes.keys())
menuWeight.grid(row=2, column=1)

# entry for displaying the converted number
convertedWeight = StringVar(wc)
convertedWeight.set("Output")
convertedWeightInput = Entry(wc, textvariable=convertedWeight, width=15, font=('times', 15))
convertedWeightInput.grid(row=2, column=2)

# button that calculates the weight
calculateWeight = Button(wc, text='Calculate Weight', command=calculate).grid(row=3, column=1)

wc.mainloop()
