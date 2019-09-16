import pyperclip

Einglish_letter = list("qwertyuiopasdfghjkl;zxcvbnm,.")

Hebrow_letter = list(("/'קראטוןםפשדגכעיחלךףזסבהנמצתץ"))

text = pyperclip.paste()

newText = []
for c in text:
    if c in Einglish_letter:
        index = Einglish_letter.index(c)
        newText.append(Hebrow_letter[index])
    elif c in Hebrow_letter:
        index = Hebrow_letter.index(c)
        newText.append(Einglish_letter[index])
    else:
        newText.append(c)

stringText = "".join(newText)

pyperclip.copy(newText)
