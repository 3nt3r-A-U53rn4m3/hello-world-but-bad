import time
from osconsolecmds import clearAboveLine
word = "hello world"

wordlist = list(word)
newwordlist = []
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for letter in wordlist:
  for aletter in alphabet:
    newwordlist.append(aletter)
    print("".join(newwordlist))
    
    if aletter == letter: 
      break
    else:
      newwordlist.pop() 
      time.sleep(0.025)
      clearAboveLine()
      
      
