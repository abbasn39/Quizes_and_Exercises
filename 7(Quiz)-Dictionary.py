#Create a dictionary with 5 words and their meanings, the user will enter the word and the program will return its meaning.
# Assume that the user will as only one fo the five already given words.

PersonalDict={"Ephemeral":"Adjective — Lasting for a very short time.",
              "Quagmire":"Noun — A difficult, complex, or hazardous situation.",
              "Serendipity":"Noun — The occurrence of events by chance in a happy or beneficial way.",
              "Zephyr":"Noun — A soft, gentle breeze.",
              "Lugubrious":"Adjective — Looking or sounding sad and dismal.",}

print("please enter your word")
inputWord=input()
print("The meaning of the word is:")
print(PersonalDict.get(inputWord))

