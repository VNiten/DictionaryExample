numbers = {
    "0": "Cero",
    "1": "Uno",
    "2": "Dos",
    "3": "Tres",
    "4": "Cuatro",
    "5": "Cinco",
    "6": "Seis",
    "7": "Siete",
    "8": "Ocho",
    "9": "Nueve",
}

text = input('Write your number: ')

finalText = ''
for letter in text:
    finalText += numbers[letter] + ' '

print(finalText)
