from tkinter import *

weightTypes = ["Pounds", "Kilograms"]


def calculate():
    if weightType.get() == 'Pounds':
        newWeight = weight.get() / 0.45
    if weightType.get() == 'Kilograms':
        newWeight = weight.get() * 0.45
    units = print_units(weightType.get())
    modifiedWeightLabel = Label(wc,text=str(round(newWeight,2)) + ' ' + units,bg='white',font=('times',15)).grid(row=2,column=2)


def print_units(unit):
    if unit == 'Pounds':
        return 'lb'
    if unit == 'Kilograms':
        return 'kg'


# initialise the window
wc = Tk()
wc.geometry('250x100')
wc.config(background='white')
wc.title('Weight converter')

# create an option menu for your weight
weightType = StringVar(wc)
weightType.set('Type')
menuWeight = OptionMenu(wc, weightType, *weightTypes)
menuWeight.grid(row=1, column=1)
# entry to insert a number for the weight to be converted
weight = IntVar(wc)
weight.set(0)
weightInput = Entry(wc, textvariable=weight, width=10, font=('times',15))
weightInput.grid(row=1, column=2)
# button that calculates the weight
calculateWeight = Button(wc, text='Calculate Weight', command=calculate).grid(row=2, column=1)
# create label that shows the modified weight

wc.mainloop()
