from gtts import gTTS
import os

print("This is a Python-based Text-To-Speech program using Google TTS...")
print("""Please choose a language (use language number): 
1 - American English
2 - UK English
3 - Irish English
4 - Spain Spanish
5 - American Spanish
6 - French
""")

# Repeats loop until a valid choice is made
while True:
    choice = input("Enter language number: ")
    if choice.isdigit() and 1 <= int(choice) <= 6:
        lang_choice = int(choice)
        break
    else:
        print("Invalid input, please choose one of the options listed above...")

# Checks which language was chosen
if lang_choice == 1:
    language = 'en'
    accent = 'us'
elif lang_choice == 2:
    language = 'en'
    accent = 'co.uk'
elif lang_choice == 3:
    language = 'en'
    accent = 'ie'
elif lang_choice == 4:
    language = 'es'
    accent = 'es'
elif lang_choice == 5:
    language = 'es'
    accent = 'us'
elif lang_choice == 6:
    language = 'fr'
    accent = 'fr'

# Takes user text to be used in audio
text = input("Enter text to speak here: ")

# Create a gTTS object with the text and language
speech = gTTS(text=text, lang=language, tld=accent, slow=False)

# Name the file
filename = input("Choose a name for this audio file: ")

# Save the converted audio to a file
speech.save(filename + ".mp3")
# Play the audio file using the OS default player
os.system(filename + ".mp3")
