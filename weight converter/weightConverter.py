from tkinter import *


unitTypes = {
    'Tonnes': pow(10, -3),
    'Kilograms': pow(10, 0),
    'Grams': pow(10, 3),
    'Milligrams': pow(10, 6),
    'Micrograms': pow(10, 9),
}


# converts weight from one type of weight to another
def calculate():
    convertedValue = weight.get() * (unitTypes[convertedWeightType.get()] / unitTypes[weightType.get()])
    convertedWeight.set(convertedValue)


# initialise the window
wc = Tk()
wc.geometry('250x100')
wc.config(background='white')
wc.title('Weight converter')

# create an option menu for the weight to be converted
weightType = StringVar(wc)
weightType.set('Kilograms')
menuWeight = OptionMenu(wc, weightType, *unitTypes.keys())
menuWeight.grid(row=1, column=1)

# entry to insert a number for the weight to be converted
weight = IntVar(wc)
weight.set(0)
weightInput = Entry(wc, textvariable=weight, width=15, font=('times', 15))
weightInput.grid(row=1, column=2)

# create an option menu for the weight to be converted
convertedWeightType = StringVar(wc)
convertedWeightType.set('Tonnes')
menuWeight = OptionMenu(wc, convertedWeightType, *unitTypes.keys())
menuWeight.grid(row=2, column=1)

# entry for displaying the converted number
convertedWeight = StringVar(wc)
convertedWeight.set(0)
convertedWeightInput = Entry(wc, textvariable=convertedWeight, width=15, font=('times', 15))
convertedWeightInput.grid(row=2, column=2)

# button that calculates the weight
calculateWeight = Button(wc, text='Calculate Weight', command=calculate).grid(row=3, column=1)

wc.mainloop()
