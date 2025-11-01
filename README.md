# FAKEMON

I put this on here because its the first proper project I ever did, and I think it was cool considering how new I was to programming. What I find quite funny now is the 2000 line script of animations that I hand typed (I have no idea how I got the motivation to do that). There are definitely a couple of bugs but most of them seem to be very specific.  
  
You get given a random team of pokemon with a random set of moves (the only logic for picking the moves was the type of the move). You then either battle a wild pokemon or a trainer. Winning gives you points and it's game over if you lose the battle. I added pokeballs to catch the wild pokemon to replace one of your party members, and there are also things like status effects and items.

---

Due to os.system() requiring different arguments to clear the terminal on macOS / linux compared to windows, ensure you find and replace before running:
  
> `os.system('clear')` for macOS and linux  

> `os.system('cls')` for windows  

(Make sure to do this in all the files)
