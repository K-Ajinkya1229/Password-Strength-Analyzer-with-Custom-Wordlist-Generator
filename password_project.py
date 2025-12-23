from zxcvbn import zxcvbn

print("=== PASSWORD STRENGTH ANALYZER ===")

password = input("Enter a password to check strength: ")
result = zxcvbn(password)
score = result['score']

if score <= 1:
    print("Password Strength: WEAK")
elif score == 2:
    print("Password Strength: MEDIUM")
else:
    print("Password Strength: STRONG")

print("\n=== WORDLIST GENERATOR ===")

name = input("Enter your name: ")
year = input("Enter your birth year: ")
pet = input("Enter pet name: ")

words = []
base_words = [name, pet]
suffixes = ["123", "@", "!", year]

for word in base_words:
    for suffix in suffixes:
        words.append(word + suffix)
        words.append(word.capitalize() + suffix)
        words.append(word + year)

with open("wordlist.txt", "w") as file:
    for w in words:
        file.write(w + "\n")

print("\nWordlist successfully saved as wordlist.txt")
print("PROJECT COMPLETED SUCCESSFULLY")
