from tkinter import *

weightTypes = ["Pounds", "Kilograms"]

unitTypes = {
    'Kilograms': 1,
    'Tonne': 1000,
    'Pounds': 2.20462,
    'Ounces': 35.274,
    'Milligrams': pow(10, -6),
    'Micrograms': pow(10, -9),
    'Grams': pow(10, -3),
    'Stone': 0.157473,
}


def calculate():
    convertedValue = 0
    if unitTypes.keys().end[weightType.get()] < unitTypes[convertedWeightType.get()]:
        convertedValue = weight.get() * (unitTypes[weightType.get()] / unitTypes[convertedWeightType.get()])
    print(f'initial weight type:{unitTypes[weightType.get()]} converted weight type: '
          f'{unitTypes[convertedWeightType.get()]} converted value: {convertedValue}')
    convertedValue = round(convertedValue,4)
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
weightInput = Entry(wc, textvariable=weight, width=10, font=('times', 15))
weightInput.grid(row=1, column=2)
# create an option menu for the weight to be converted
convertedWeightType = StringVar(wc)
convertedWeightType.set('Tonne')
menuWeight = OptionMenu(wc, convertedWeightType, *unitTypes.keys())
menuWeight.grid(row=2, column=1)
# entry for displaying the converted number
convertedWeight = StringVar(wc)
convertedWeight.set(0)
convertedWeightInput = Entry(wc, textvariable=convertedWeight, width=10, font=('times', 15))
convertedWeightInput.grid(row=2, column=2)

# button that calculates the weight
calculateWeight = Button(wc, text='Calculate Weight', command=calculate).grid(row=3, column=1)

wc.mainloop()
