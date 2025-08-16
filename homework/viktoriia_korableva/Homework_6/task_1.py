text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
text_list = text.split()
new_text_list = []

for word in text_list:
    if word[-1] in [",", "."]:
        new_word = word[:-1] + "ing" + word[-1]
    else:
        new_word = word + "ing"
    new_text_list.append(new_word)

new_text = " ".join(new_text_list)
print(new_text)
