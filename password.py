import json
import random

f = open('config.json')

# Load Config File
def load(file):

    data = json.load(file)

    global num_option
    num_option = data['settings'][0]['numbers']

    global cap_words_option
    cap_words_option = data['settings'][0]['cap_words']

    global passw_len
    passw_len = data['settings'][0]['lenght']

    file.close()

load(f)

passw_letters = "qwertyuiopasdfghjklzxcvbnm"
passw_cap_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
passw_nums = "1234567890"

# Share Of Each Content in password
passw_letters_share = int(passw_len / 2) # 25%
passw_cap_letters_share = int(passw_letters_share / 2) # 25%
passw_nums_share = int(passw_len / 2) # 50%

# Take Letters From Lists & Make Word
word = random.sample(passw_letters, passw_letters_share)
cap_word = random.sample(passw_cap_letters, passw_cap_letters_share)
num_word = random.sample(passw_nums, passw_nums_share)

# Convert Words To Strings
string_word = ''
for i in range(passw_letters_share):
    string_word += word[i]

string_cap_words = ''
for i in range(passw_cap_letters_share):
    string_cap_words += cap_word[i]

string_num_words = ''
for i in range(passw_nums_share):
    string_num_words += num_word[i]


print(string_word + string_num_words + string_cap_words)