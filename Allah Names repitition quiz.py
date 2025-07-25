# This program is made to memorise the 99 names of Allah through repetition.

import random

names1 = {
    1: "Ar-Rahman",
    2: "Ar-Raheem",
    3: "Al-Malik",
    4: "Al-Quddus",
    5: "As-Salam",
    6: "Al-Mu’min",
    7: "Al-Muhaimin",
    8: "Al-Aziz",
    9: "Al-Jabbar",
    10: "Al-Mutakabbir"
}

names2 = {
    11: "Al-Khaliq",
    12: "Al-Bari",
    13: "Al-Musawwir",
    14: "Al-Ghaffar",
    15: "Al-Qahhar",
    16: "Al-Wahhab",
    17: "Ar-Razzaq",
    18: "Al-Fattah",
    19: "Al-‘Aleem",
    20: "Al-Qaabid"
}


names3 = {
    21: "Al-Baasit",
    22: "Al-Khaafid",
    23: "Ar-Raafi",
    24: "Al-Mu’izz",
    25: "Al-Mudhill",
    26: "As-Sami",
    27: "Al-Baseer",
    28: "Al-Hakam",
    29: "Al-‘Adl",
    30: "Al-Lateef"
}

names4 = {
    31: "Al-Khabeer",
    32: "Al-Haleem",
    33: "Al-‘Azeem",
    34: "Al-Ghafoor",
    35: "Ash-Shakoor",
    36: "Al-‘Aliyy",
    37: "Al-Kabeer",
    38: "Al-Hafeez",
    39: "Al-Muqeet",
    40: "Al-Haseeb"
}

names5 = {
    41: "Al-Jaleel",
    42: "Al-Kareem",
    43: "Ar-Raqeeb",
    44: "Al-Mujeeb",
    45: "Al-Waasi",
    46: "Al-Hakeem",
    47: "Al-Wadood",
    48: "Al-Majeed",
    49: "Al-Ba’ith",
    50: "Ash-Shaheed"
}
names6 = {
    51: "Al-Haqq",
    52: "Al-Wakeel",
    53: "Al-Qawiyy",
    54: "Al-Mateen",
    55: "Al-Waliyy",
    56: "Al-Hameed",
    57: "Al-Muhsee",
    58: "Al-Mubdi",
    59: "Al-Mueed",
    60: "Al-Muhyi"
}
dict7 = {
    61: "Al-Mumeet",
    62: "Al-Hayy",
    63: "Al-Qayyoom",
    64: "Al-Waajid",
    65: "Al-Maajid",
    66: "Al-Waahid",
    67: "Al-Ahad",
    68: "As-Samad",
    69: "Al-Qaadir",
    70: "Al-Muqtadir"
}


names8 = {
    71: "Al-Muqaddim",
    72: "Al-Mu’akhkhir",
    73: "Al-Awwal",
    74: "Al-Aakhir",
    75: "Az-Zaahir",
    76: "Al-Baatin",
    77: "Al-Waali",
    78: "Al-Muta’ali",
    79: "Al-Barr",
    80: "At-Tawwaab"
}

names9 = {
    81: "Al-Muntaqim",
    82: "Al-‘Afuww",
    83: "Ar-Ra’uf",
    84: "Maalik-ul-Mulk",
    85: "Dhul-Jalaali-Wal-Ikram",
    86: "Al-Muqsit",
    87: "Al-Jaami",
    88: "Al-Ghaniyy",
    89: "Al-Mughni",
    90: "Al-Maani"
}

names10 = {
    91: "Ad-Daarr",
    92: "An-Naafi",
    93: "An-Noor",
    94: "Al-Haadi",
    95: "Al-Badee’",
    96: "Al-Baaqi",
    97: "Al-Waarith",
    98: "Ar-Rasheed",
    99: "As-Saboor"
}



meanings1 = {
    1: "Nihayat Reham Karne Wala",
    2: "Behad Meharbaan",
    3: "Har Cheez Ka Malik",
    4: "Har Aib Se Pak",
    5: "Salamati Dene Wala",
    6: "Aman Dene Wala",
    7: "Nigraani Karne Wala",
    8: "Sab Par Ghalib",
    9: "Har Kami Ko Poora Karne Wala",
    10: "Buzurgi Dikhane Wala"
}

meanings2 = {
    11: "Paida Karne Wala",
    12: "Bina Naqsh Banane Wala",
    13: "Soorat Banane Wala",
    14: "Bahut Zyada Maaf Karne Wala",
    15: "Zabardast Ghalib",
    16: "Bina Maange Dene Wala",
    17: "Rizq Dene Wala",
    18: "Faisla Karne Wala",
    19: "Har Cheez Ka Ilm Rakhne Wala",
    20: "Tang Karne Wala"
}

meanings3 = {
    21: "Kushada Karne Wala",
    22: "Girane Wala",
    23: "Buland Karne Wala",
    24: "Izzat Dene Wala",
    25: "Zillat Dene Wala",
    26: "Sab Sunne Wala",
    27: "Sab Dekhne Wala",
    28: "Behtareen Faisla Karne Wala",
    29: "Insaaf Karne Wala",
    30: "Bareek Feham, Narm Dil"
}

meanings4 = {
    31: "Har Baat Se Waqif",
    32: "Bohat Bardasht Karne Wala",
    33: "Nihayat Azeem",
    34: "Maaf Karne Wala",
    35: "Shukar Qubool Karne Wala",
    36: "Nihayat Buland",
    37: "Bohat Buzurg",
    38: "Hifazat Karne Wala",
    39: "Har Cheez Ka Rizq Dene Wala",
    40: "Hisaab Lene Wala"
}

meanings5 = {
    41: "Azmat Wala",
    42: "Nihayat Karam Karne Wala",
    43: "Har Cheez Par Nigraani Karne Wala",
    44: "Du’a Sunne Wala",
    45: "Har Cheez Ko Ghairne Wala",
    46: "Hakeem-o-Dana",
    47: "Muhabbat Karne Wala",
    48: "Buzurgi Wala",
    49: "Zinda Karne Wala",
    50: "Har Cheez Ka Gawah"
}

meanings6 = {
    51: "Haqeeqat Wala",
    52: "Kaafi Hone Wala",
    53: "Nihayat Taqatwar",
    54: "Mazboot",
    55: "Madadgaar",
    56: "Tareef Ke Laayak",
    57: "Har Cheez Ka Ginnah Rakhne Wala",
    58: "Ibtida Karne Wala",
    59: "Dobara Paida Karne Wala",
    60: "Zindagi Dene Wala"
}

meanings7 = {
    61: "Mout Dene Wala",
    62: "Zinda Rehne Wala",
    63: "Har Cheez Ko Qaim Rakhne Wala",
    64: "Paida Karne Wala",
    65: "Buzurgi Wala",
    66: "Akele Pan Wala",
    67: "Wahid, La Shareek",
    68: "Be Niyaz",
    69: "Qudrat Rakhnay Wala",
    70: "Taqat Ka Malik"
}

meanings8 = {
    71: "Aagay Badhane Wala",
    72: "Peechay Karne Wala",
    73: "Pehla",
    74: "Aakhri",
    75: "Zahir Hone Wala",
    76: "Chhupa Hua",
    77: "Har Cheez Par Hukumat Karne Wala",
    78: "Nihayat Buland-o-Bala",
    79: "Nekiyan Dene Wala",
    80: "Tauba Qubool Karne Wala"
}

meanings9 = {
    81: "Badla Lene Wala",
    82: "Maaf Karne Wala",
    83: "Nihayat Meharbaan",
    84: "Har Mulk Ka Malik",
    85: "Jalal aur Karam Wala",
    86: "Insaaf Karne Wala",
    87: "Jama Karne Wala",
    88: "Be Niyaz",
    89: "Ameer Banane Wala",
    90: "Rokne Wala"
}

meanings10 = {
    91: "Nuqsan Dene Wala",
    92: "Faida Dene Wala",
    93: "Roshni Dene Wala",
    94: "Hidayat Dene Wala",
    95: "Naya Ijaad Karne Wala",
    96: "Hamesha Rehne Wala",
    97: "Sab Ka Waaris",
    98: "Seedha Raasta Dikhane Wala",
    99: "Sabr Karne Wala"
}


# This will get an input from the user that will return variables that can used instead of dictionary names later.
user = int(input("Enter number: "))

def input_user(user):
    n = "names" + str(user)
    m = "meanings" + str(user)
    print(n)
    print(m)
    return n, m  # Returning both variables

namesx, meaningsx = input_user(user)

# This is a random dictionary selector when the user has memorised all the names and meanings
# This can be used as an input to input_user(random_dict_selector()) so that
# it returns 2 names and meaning corresponding random dictionaries

def random_dict_selector():
    i=random.randint(0,10)
    return i


# This function will generate a random number that can be inserted instead of index to randomize the keys of
# dictionaries.
def dict_index_selector():
    i=random.randint(0,10)
    return i

def option_generator(meaningsx):
    option1= meaningsx.get(dict_index_selector())
    pass

