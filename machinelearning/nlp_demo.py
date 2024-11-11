import contractions



text = "I read this book for the first time in 1987, and it's still one of my favorites !"

fixed = contractions.fix(text)
print(fixed)