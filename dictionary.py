numbers = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}

text = input('Write your number: ')

finalText = ''
for letter in text:
    finalText += numbers[letter] + ' '

print(finalText)
