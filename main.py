import animations as animations
import math
import os
# mac = os.system('cls')
# windows = os.system('cls')
import random
import time

black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m" #text colours
white = "\033[0;37m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"
orange = "\033[38;2;255;165;0m"
bold = "\u001b[1m"
reset = "\u001b[0m"

typeTable = { #a dictionary with attacking type match-ups e.g. flying attacking
    "Null" :{
        0 : [0],
        0.5 : [0],
        1 : [0],
        2 : [0],
        "c": white,
        "hc": "\033[48;2;255;255;255m",
        "move" : [0]
    },

    "Normal" : {
        0 : ["Ghost"],
        0.5 : ["Rock","Steel"],
        1 : ["Normal","Fighting","Flying","Poison","Ground","Bug","Fire","Water","Grass","Electric","Psychic","Ice","Dragon","Dark","Fairy"],
        2 : [0],
        "c": "\033[38;2;168;167;122m",
        "hc": "\033[48;2;168;167;122m",
        "move":["Normal","Fighting","Flying","Poison","Ground","Bug","Fire","Water","Grass","Electric","Psychic","Ice","Dark","Fairy"]
    },

    "Fighting" : {
        0 : ["Ghost"],
        0.5 : ["Flying","Poison","Bug","Psychic","Fairy"],
        1 : ["Fighting","Ground","Fire","Water","Grass","Electric","Dragon"],
        2 : ["Normal","Rock","Steel","Ice","Dark"],
        "c": "\033[38;2;187;85;68m",
        "hc": "\033[48;2;187;85;68m",
        "move":["Fighting","Ground","Fire","Grass","Electric","Normal","Rock","Steel","Dark","Ghost","Poison","Bug"]
    },

    "Flying" :{
        0 : [0],
        0.5 : ["Rock","Steel","Electric"],
        1 : ["Normal","Flying","Poison","Ground","Ghost","Fire","Water","Psychic","Ice","Dragon","Dark","Fairy"],
        2 : ["Fighting","Bug","Grass"],
        "c": "\033[38;2;136;153;255m",
        "hc": "\033[48;2;136;153;255m",
        "move" : ["Normal","Flying","Poison","Ghost","Fire","Psychic","Ice","Dragon","Steel","Electric"]
    },

    "Poison" :{
        0 : ["Steel"],
        0.5 : ["Poison","Ground","Rock","Ghost"],
        1 : ["Normal","Fighting","Flying","Bug","Fire","Water","Electric","Psychic","Ice","Dragon","Dark"],
        2 : ["Grass","Fairy"],
        "c": "\033[38;2;163;62;161m",
        "hc": "\033[48;2;163;62;161m",
        "move" : ["Poison","Ground","Rock","Normal","Fighting","Bug","Fire","Electric","Psychic","Dark","Grass"]
    },

    "Ground" :{
        0 : ["Flying"],
        0.5 : ["Fug","Frass"],
        1 : ["Formal","Fighting","Ground","Ghost","Water","Psychic","Ice","Dragon","Dark","Fairy"],
        2 : ["Poison","Rock","Steel","Fire","Electric"],
        "c": "\033[38;2;197;167;76m",
        "hc": "\033[48;2;197;167;76m",
        "move" : ["Ground","Rock","Normal","Fire","Psychic","Ice","Dark","Steel"]
    },

    "Rock" :{
        0 : [0],
        0.5 : ["Fighting","Ground","Steel"],
        1 : ["Normal","Poison","Rock","Ghost","Water","Grass","Electric","Psychic","Dragon","Dark","Fairy"],
        2 : ["Flying","Bug","Fire","Ice"],
        "c": "\033[38;2;187;170;102m",
        "hc": "\033[48;2;187;170;102m",
        "move" : ["Poison","Ground","Rock","Normal","Fighting","Fire","Psychic","Ice","Dark","Grass","Steel"]
    },

    "Bug" :{
        0 : [0],
        0.5 : ["Fighting","Flying","Posion","Ghost","Steel","Fire","Fairy"],
        1 : ["Normal","Ground","Rock","Bug","Water","Electric","Ice","Dragon"],
        2 : ["Grass","Psychic","Dark"],
        "c": "\033[38;2;170;187;34m",
        "hc": "\033[48;2;170;187;34m",
        "move" : ["Poison","Normal","Bug","Water","Dark","Grass","Fairy"]
    },

    "Ghost" :{
        0 : ["Normal"],
        0.5 : ["Dark"],
        1 : ["Fighting","Flying","Poison","Ground","Rock","Bug","Steel","Fire","Water","Grass","Electric","Ice","Dragon","Fairy"],
        2 : ["Ghost","Psychic"],
        "c": "\033[38;2;102;102;187m",
        "hc": "\033[48;2;102;102;187m",
        "move" : ["Poison","Ghost","Normal","Psychic","Dark"]
    },

    "Steel" :{
        0 : [0],
        0.5 : ["Steel","Fire","Water","Electric"],
        1 : ["Normal","Fighting","Flying","Poison","Ground","Bug","Ghost","Grass","Psychic","Dragon","Dark"],
        2 : ["Rock","Ice","Fairy"],
        "c": "\033[38;2;170;170;187m",
        "hc": "\033[48;2;170;170;187m",
        "move" : ["Ground","Rock","Ghost","Normal","Fighting","Fire","Electric","Dragon","Dark","Fairy","Steel"]
    },

    "Fire" :{
        0 : [0],
        0.5 : ["Rock","Fire","Water","Dragon"],
        1 : ["Normal","Fighting","Flying","Poison","Ground"],
        2 : ["Bug","Steel","Grass","Ice"],
        "c": "\033[38;2;255;68;34m",
        "hc": "\033[48;2;235;68;34m",
        "move" : ["Rock","Normal","Fighting","Fire","Psychic","Dragon","Dark","Steel"]
    },

    "Water" :{
        0 : [0],
        0.5 : ["Water","Grass","Dragon"],
        1 : ["Normal","Fighting","Flying","Poison","Bug","Ghost","Steel","Electric","Psychic","Ice","Dark","Fairy"],
        2 : ["Ground","Rock","Fire"],
        "c": "\033[38;2;50;150;250m",
        "hc": "\033[48;2;50;150;250m",
        "move" : ["Rock","Normal","Fighting","Flying","Water","Psychic","Ice","Fairy"]
    },

    "Grass" :{
        0 : [0],
        0.5 : ["Flying","Poison","Bug","Steel","Fire","Grass","Dragon"],
        1 : ["Normal","Fighting","Ghost","Electric","Psychic","Ice","Dark","Fairy"],
        2 : ["Ground","Rock","Water"],
        "c": "\033[38;2;119;204;85m",
        "hc": "\033[48;2;119;204;85m",
        "move" : ["Poison","Ground","Rock","Normal","Fighting","Bug","Dark","Grass","Fairy"]
    },

    "Electric" :{
        0 : ["Ground"],
        0.5 : ["Grass","Electric","Dragon"],
        1 : ["Normal","Fighting","Poison","Rock","Bug","Ghost","Steel","Fire","Psychic","Ice","Dark","Fairy"],
        2 : ["Flying","Water"],
        "c": "\033[38;2;254;203;51m",
        "hc": "\033[48;2;254;203;51m",
        "move" : ["Poison","Normal","Fighting","Electric","Dark","Fairy","Steel"]
    },

    "Psychic" :{
        0 : ["Dark"],
        0.5 : ["Steel","Psychic"],
        1 : ["Normal","Flying","Ground","Rock","Bug","Ghost","Fire","Water","Grass","Electric","Ice","Dragon","Fairy"],
        2 : [0],
        "c": "\033[38;2;220;100;135m",
        "hc": "\033[48;2;220;100;135m",
        "move" : ["Poison","Rock","Ghost","Normal","Fighting","Water","Psychic","Ice","Grass","Fairy"]
    },

    "Ice" :{
        0 : [0],
        0.5 : ["Steel","Fire","Water","Ice"],
        1 : ["Normal","Fighting","Poison","Rock","Bug","Ghost","Electric","Psychic","Dark","Fairy"],
        2 : ["Flying","Ground","Grass","Dragon"],
        "c": "\033[38;2;102;204;255m",
        "hc": "\033[48;2;102;204;255m",
        "move" : ["Poison","Rock","Normal","Water","Psychic","Ice","Dark","Fairy","Steel"]
    },

    "Dragon" :{
        0 : ["Fairy"],
        0.5 : ["Steel"],
        1 : ["Normal","Fighting","Flying","Poison","Ground","Rock","Bug","Ghost","Fire","Water","Grass","Electric","Psychic","Ice","Dark"],
        2 : ["Dragon"],
        "c": "\033[38;2;119;102;238m",
        "hc": "\033[48;2;119;102;238m",
        "move":["Normal","Fighting","Flying","Poison","Ground","Rock","Bug","Ghost","Fire","Water","Grass","Electric","Psychic","Ice","Dark","Dragon"]
    },

    "Dark" :{
        0 : [0],
        0.5 : ["Fighting","Dark","Fairy"],
        1 : ["Normal","Flying","Poison","Ground","Rock","Bug","Steel","Fire","Water","Grass","Electric","Ice","Dragon"],
        2 : ["Ghost","Psychic"],
        "c": "\033[38;2;119;85;68m",
        "hc": "\033[48;2;119;85;68m",
        "move" : ["Poison","Rock","Ghost","Normal","Fighting","Bug","Dark","Grass","Steel"]
    },

    "Fairy" :{
        0 : [0],
        0.5 : ["Poison","Steel","Fire"],
        1 : ["Normal","Flying","Ground","Rock","Bug","Ghost","Water","Grass","Electric","Psychic","Ice","Fairy"],
        2 : ["Fighting","Ice","Dark","Dragon"],
        "c": "\033[38;2;238;153;238m",
        "hc": "\033[48;2;238;153;238m",
        "move" : ["Rock","Normal","Bug","Water","Psychic","Ice","Grass","Fairy"]
    },
}

balls = {
  "pokeball" : [1,red],
  "great ball" : [1.5,blue],
  "ultra ball" : [2,black],
  "quick ball" : [1,yellow], #effectiveness of 5 if first move,4 if second move, 3 if third move
  "master ball" : [255,magenta],
  "net ball" : [1,green], #effectiveness 3.5 if bug type
  "dive ball" : [1,blue], #effectiveness 3.5 if water type
  "timer ball" : [1,white], #effectiveness increases as number of turns also increases
  "fast ball" : [1,yellow], #effectiveness 4 if opponent base speed stat >100
}
#have methods for the catching that returns caught or broken out (maybe a separate one for net and dive balls etc.)
#DONT FORGET ABOUT INFORMATION FOR MOVES

class bag():
  def __init__(self):
    self.revive = [6,"revive"]
    self.potion = [20,"potion"]
    self.superPotion = [10,"super potion"]
    self.hyperPotion = [5,"hyper potion"]
    self.fullRestore = [2,"full restore"]
    
    self.burnHeal = [2,"burn heal"]
    self.antidote = [2,"antidote"]
    self.paralyseHeal = [2,"paralyse heal"]
    self.oranBerry = [30,"oran berry"]

    self.pokeball = [10,"pokeball"]
    self.greatball = [6,"great ball"]
    self.ultraball = [3,"ultra ball"]
    self.quickball = [2, "quick ball"]
    self.masterball = [1,"master ball"]
    self.netball = [2,"net ball"]
    self.diveball = [2,"dive ball"]
    self.timerball = [2,"timer ball"]
    self.fastball = [2,"fast ball"]

  def usePotion(self,currentPk,potionType,pkList,oppCurrentPk): #self is the currentPk
    match potionType:
      case "poition":
        amountToHeal = 60
      case "super":
        amountToHeal = 120
      case "hyper":
        amountToHeal = 200
    
    partyPrint(pkList,True,"full",False)
    carryOn = False
    while carryOn is False:
      print("Which pokemon would you like to heal?")
      healChoice = int(input("Number >> "))
      if pkList[healChoice].currentHp <= 0:
        print(red+"This pokemon has fainted"+reset)
      else:
        carryOn = True
    hp = pokemon.getHP(pkList[healChoice-1])
    if pkList[healChoice-1].name == currentPk.name:
      healed = hp - pkList[healChoice-1].currentHp if pkList[healChoice-1].currentHp + amountToHeal > hp else amountToHeal
      os.system('cls')
      animations.health(self,trainerPkAlive,currentPk.currentHp,hp,healed,battleStatsDisplay,oppCurrentPk,oppPkAlive,typeTable,"opp",oppType,green,False)
    else:
      print(pkList[healChoice-1].name+"'s health has been restored")
    
    if pkList[healChoice-1].currentHp >= (pokemon.getHP(pkList[healChoice-1]) - amountToHeal):
      pokemon.resetHP(pkList[healChoice-1])
    else:
      pkList[healChoice-1].currentHp += amountToHeal
  
  def useRevive(self,pkList,trainerPkAlive): 
    partyPrint(pkList,True,"compact",False)
    carryOn = False
    while carryOn is False:
      print("Which pokemon would you like to revive?")
      pkRes = int(input("Number >> "))
      if pkList[pkRes-1].currentHp > 0:
        print(red+"This pokemon is still alive"+reset)
      else:
        carryOn = True
    pokemon.resetHP(pkList[pkRes-1])
    print(pkList[pkRes-1]+" has been revived")
    trainerPkAlive += 1
    return trainerPkAlive
  
  def useFullRestore(self,currentPk,pkList,oppCurrentPk): #self is currentPk
    partyPrint(pkList,True,"full",False)
    carryOn = False
    while carryOn is False:
      print("Which pokemon would you like to heal?")
      healChoice = int(input("Number >> "))
      if pkList[healChoice].currentHp <= 0:
        print(red+"This pokemon has fainted"+reset)
      else:
        carryOn = True

    hp = pokemon.getHP(pkList[healChoice-1])
    if pkList[healChoice-1].name == currentPk.name:
      healed = hp - pkList[healChoice-1].currentHp
      os.system('cls')
      animations.health(currentPk,trainerPkAlive,currentPk.currentHp,hp,healed,battleStatsDisplay,oppCurrentPk,oppPkAlive,typeTable,"opp",oppType,green,False)

    print(pkList[healChoice-1].name+"'s health has been restored")
    pokemon.resetHP(pkList[healChoice-1])

    match pkList[healChoice-1].status:
      case "Burned":
        print(pkList[healChoice-1].name+"'s burn has been healed")
      case "Poisoned":
        print(pkList[healChoice-1].name+"'s poison has been healed")
      case "Paralysed":
        print(pkList[healChoice-1].name+"'s paralysis has been healed")
    pkList[healChoice-1].status = "None"
    
  def useStatusHeal(self,pkList):
    partyPrint(pkList,True,"compact",False)
    carryOn = False
    while carryOn is False:
      print("Which pokemon would you like to heal?")
      healChoice = int(input("Number >> "))
      if pkList[healChoice].currentHp <= 0:
        print(red+"This pokemon has fainted"+reset)
      else:
        carryOn = True
    
    match pkList[healChoice-1].status:
      case "Burned":
        print(pkList[healChoice-1].name+"'s burn has been healed")
      case "Poisoned":
        print(pkList[healChoice-1].name+"'s poison has been healed")
      case "Paralysed":
        print(pkList[healChoice-1].name+"'s paralysis has been healed")
    pkList[healChoice-1].status = "None"

class pokemon(bag):
  def __init__(self,name="",type1="",type2="",hp="",a="",d="",sA="",sD="",sp=""): #creating a class about the pokemon
    self.name = name
    self.type1 = type1
    self.type2 = type2
    self.__hp = (int(hp) * 2) + 110
    self.__attack = int(a) * 2 
    self.__defence = int(d)
    self.__sAttack = int(sA)
    self.__sDefence = int(sD)
    self.speed = int(sp)
    self.currentHp = self.__hp
    self.currentSp = self.speed
    self.currentAtt = self.__attack
    self.currentDef = self.__defence
    self.currentSpDef = self.__sDefence
    self.currentSpAtt = self.__sAttack
    self.status = "None"
    self.paralysedTurns = 0
    self.burnTurns = 0
    self.poisonTurns = 0

  def getHP(self):
    return self.__hp

  def resetHP(self):
    self.currentHp = self.__hp

  def resetStats(self):
    self.currentAtt = self.__attack
    self.currentDef = self.__defence
    self.currentSp = self.speed
    self.currentSpDef = self.__sDefence
    self.currentSpAtt = self.__sAttack
    self.status = ""

  def assignMoves(self,m1n="",m1t="",m1p=0,m1s="",m2n="",m2t="",m2p=0,m2s="",m3n="",m3t="",m3p=0,m3s="",m4n="",m4t="",m4p=0,m4s=""):
    self.move1n = m1n
    self.move1t = m1t
    self.move1p = m1p
    self.move1s = m1s
    self.move2n = m2n
    self.move2t = m2t
    self.move2p = m2p
    self.move2s = m2s
    self.move3n = m3n
    self.move3t = m3t
    self.move3p = m3p
    self.move3s = m3s
    self.move4n = m4n
    self.move4t = m4t
    self.move4p = m4p
    self.move4s = m4s

  def printWild():
    print(r"""

                    ..:---:.
               .+%%%%%%%%%%%%%%%+..
            .*%%%%#=:.......:=#%%%%#:.
          :%%%%=.               .=%%%%:.
        .#%%%:                    .:#%%#.
       :%%@-                         -%%%-
      :%%%.                           .#%@-.
     .%%%:           .:=+=:.           .%%%.
     +%%-         .+%%%%%%%%%+.         :%%+.
    .%%%.        :%%@*:   :*%%%:        .#%%.
    :%%%+++-:...:%%%.       .%%@:...:-+++%%@:
    :%%@@%%%%%%%%%%=         -%%%%%%%%%%@@%@:
    .%%#.  ...:-+%%*        .*%%*-:...  .#%%.
     +%%-       .%%%+.     .=%%%.       :%@+.
     .%%%.       .+@%%#=-=#%%%*.       .%%%.
      -%%%.        .+#%@%@%#+.       ..#%@-.
       :%%%-           .            .-%%%-
        .#%%%:.                   .:#%@#.
         .:%%%%-..             ..-%%@%:
           ..#%@%%#-.........-#@%@%#:
              ..+%%@%%%%%%%%@@%%*..
                   ...:---:...


    """)
    print("A wild pokemon appeared!")

  def getOppName():
    print(r"""
              @*+*
            *+++++++*
           %+==+-++++#
           *+-----=++#
           *#:+--+:=+*#
             -.-:::+%
             ==-==-=
           *---=--===#%    ##%
          #=:==#-++=:*#%   +-+#
          %+==:--==-+##%   %#%
         %#*+=:--====**#% +-:-+
         *+*++--+++*+*--*+:---+
        +..=++=-++++=*=.-=:=-#
        +.:+++--++++*++--
        #*******#####++*
        %+=----=-----%%
        *======*======
         *==-==%+----=#
         *---== +======
         *-====  ==-==+
         #=-=-=  %=--==*
          +-==+@  *===+*
          *+=++   *++++++
          +++++#   #+++++*
          *+++++   %*++=+*
        #*++*++@   #++++**
        #++++*+@   #++++++*
      *+++*#*##     **++*+#
      +===*         +++***
                     #+++*

        """)
    with open("opponentPrefixes.txt") as file:
      tempList = list([line.split(",") for line in file]) #putting all the moves into tempList split by ','
      oppPrefix = random.sample(tempList,1)
    del tempList
    with open("opponentNames.txt") as file:
      tempList = list([line.split(",") for line in file])
      oppName = random.sample(tempList,1)
    del tempList
    oppName = str(oppPrefix[0][0]) + " " + str(oppName[0][0])
    print("You are challenged by " + oppName + "!", end = ' ', flush = True)
    return oppName

  def sendOutOpp(self,oppName):
    print(bold + oppName + " sent out " + self.name + reset)

  def sendOut(self):
    print(bold + "\nYou sent out " + self.name + reset)

  def assignStatus(self,movePower,oppCurrentPk):
    match int(movePower):
      case -1:
        if oppCurrentPk.status == "None":
          oppCurrentPk.status = "paralysed"
          oppCurrentPk.paralysedTurns = 1
          print(bold + oppCurrentPk.name + " has been "+yellow+"paralysed"+reset)
        else:
          print(bold + "But it failed!")
        time.sleep(0.5)

      case -2:
        if oppCurrentPk.status == "None":
          oppCurrentPk.status = "burned"
          oppCurrentPk.burnTurns = 1
          print(bold + oppCurrentPk.name + " has been "+red+"burned"+reset)
        else:
          print(bold + "But it failed!")
        time.sleep(0.5)

      case -4:
        if oppCurrentPk.status == "None":
          oppCurrentPk.status = "poisoned"
          oppCurrentPk.poisonTurns = 1
          print(bold + oppCurrentPk.name + " has been "+magenta+"poisoned"+reset)
        else:
          print(bold + "But it failed!")
        time.sleep(0.5)

      case -5:
        if self.currentAtt == 3*self.__attack:
          print(bold + self.name + "'s attack is maxed out")
        else:
          if self.currentAtt + 0.5*self.__attack > 3*self.__attack:
            self.currentAtt = 3*self.__attack
          else:
            self.currentAtt += 0.5*self.__attack
          print(bold + self.name + "'s "+red+"attack rose"+reset)
        time.sleep(0.5)

      case -6:
        if self.currentAtt == 3*self.__attack:
          print(bold + self.name + "'s attack is maxed out")
        else:
          if self.currentAtt + self.__attack > 3*self.__attack:
            self.currentAtt = 3*self.__attack
          else:
            self.currentAtt += self.__attack
          print(bold + self.name + "'s "+red+"attack sharply rose"+reset)
        time.sleep(0.5)

      case -7:
        if self.currentAtt == 3*self.__attack or self.currentHp < 0.5*self.__hp:
          print(bold + "But it failed!")
        else:
          self.currentHp -= 0.5*self.__hp
          animations.health(self,trainerPkAlive,self.currentHp,self.__hp,(0.5*self.__hp),battleStatsDisplay,oppCurrentPk,oppPkAlive,typeTable,"opp",oppType,red,True)
          self.currentAtt = 3*self.__attack
          print(bold + self.name + "'s "+red+"attack drastically rose"+reset)
        time.sleep(0.5)

      case -8:
        if self.currentDef == 3*self.__defence:
          print(bold + self.name + "'s defence is maxed out")
        else:
          if self.currentDef + self.__defence > 3*self.__defence:
            self.currentDef = 3*self.__defence
          else:
            self.currentDef += self.__defence
          print(bold + self.name + "'s "+red+"defence sharply rose"+reset)
        time.sleep(0.5)

      case -9:
        if self.currentDef == 3*self.__defence:
          x = self.name + "'s defence is maxed out"
        else:
          if self.currentDef + 0.5*self.__defence > 3*self.__defence:
            self.currentDef = 3*self.__defence
          else:
            self.currentDef += 0.5*self.__defence
          x = self.name + "'s "+red+"defence rose"+reset
        if self.currentAtt == 3*self.__attack:
          print(bold + self.name + "'s attack is maxed out")
        else:
          if self.currentAtt + 0.5*self.__attack > 3*self.__attack:
            self.currentAtt = 3*self.__attack
          else:
            self.currentAtt += 0.5*self.__attack
          print(bold + self.name + "'s "+red+"attack rose"+reset+" and " + x)
        time.sleep(0.5)

      case -10:
        if self.currentSp == 3*self.speed:
          print(bold + self.name + "'s speed is maxed out")
        else:
          if self.currentSp + self.speed > 3*self.speed:
            self.currentSp = 3*self.speed
          else:
            self.currentSp += self.speed
          print(bold + self.name + "'s "+red+"speed sharply rose"+reset)
        time.sleep(0.5)

      case -11:
        if self.currentSpDef == 3*self.__sDefence:
          print(bold + self.name + "'s defence is maxed out")
        else:
          if self.currentSpDef + self.__sDefence > 3*self.__sDefence:
            self.currentSpDef = 3*self.__sDefence
          else:
            self.currentSpDef += self.__sDefence
          print(bold + self.name + "'s "+red+"defence sharply rose"+reset)
        time.sleep(0.5)

      case -13:
        if self.currentSpDef == 3*self.__sDefence:
          x = self.name + "'s defence is maxed out"
        else:
          if self.currentSpDef + 0.5*self.__sDefence > 3*self.__sDefence:
            self.currentSpDef = 3*self.__sDefence
          else:
            self.currentSpDef += 0.5*self.__sDefence
          x = self.name + "'s "+red+"defence rose"+reset
        if self.currentSpAtt == 3*self.__sAttack:
          print(bold + self.name + "'s attack is maxed out")
        else:
          if self.currentSpAtt + 0.5*self.__sAttack > 3*self.__sAttack:
            self.currentSpAtt = 3*self.__sAttack
          else:
            self.currentSpAtt += 0.5*self.__sAttack
          print(bold + self.name + "'s "+red+"attack rose"+reset+" and " + x)
        time.sleep(0.5)

      case -14:
        if self.currentDef == 3*self.__defence:
          print(bold + self.name + "'s defence is maxed out")
        else:
          self.currentDef = 3*self.__defence
          print(bold + self.name + "'s "+red+"attack drastically rose"+reset)
        time.sleep(0.5)

      case -15:
        if self.currentDef == self.__defence - 3*self.__defence:
          print(bold + "But it failed!")
        else:
          if self.currentDef - 0.5*self.__sDefence < self.__defence - 3*self.__defence:
            self.currentDef = self.__defence - 3*self.__sDefence
          else:
            self.currentDef -= 0.5*self.__defence
          print(bold + oppCurrentPk.name + "'s "+blue+"defence fell"+reset)
        time.sleep(0.5)

      case -16:
        pokemon.resetStats(self)
        print(bold + self.name + "'s stats have been reset!")
        time.sleep(0.5)

      case -17:
        if self.currentHp == self.__hp:
          print(bold + "But it failed!")
        else:
          if self.currentHp < (self.__hp // 2):
            animations.health(self,trainerPkAlive,self.currentHp,0.5*self.__hp,battleStatsDisplay,oppCurrentPk,oppPkAlive,typeTable,"opp",oppType,bright_green,False)
            self.currentHp += 0.5*self.__hp
          else:
            animations.health(self,trainerPkAlive,self.currentHp,self.__hp-self.currentHp,battleStatsDisplay,oppCurrentPk,oppPkAlive,typeTable,"opp",oppType,bright_green,False)
            self.currentHp = self.__hp
          print(bold + self.name + "'s "+green+"hp has been restored"+reset)
        time.sleep(0.5)

  def statusEffect(self,oppCurrentPk,affected):
    print(bold)
    os.system('cls')
    match self.status:
      case "None":
        self.currentSp = self.speed

      case "paralysed":
        self.currentSp = self.speed/2
        self.paralysedTurns += 1
        if self.paralysedTurns == 6:
          self.status = "None"
        time.sleep(0.5)
        os.system('cls')

      case "burned":
        print(self.name + " was hurt by "+red+"burn"+reset)
        time.sleep(0.5)
        os.system('cls')
        animations.health(self,trainerPkAlive,self.currentHp,self.__hp,(0.0625*self.__hp),battleStatsDisplay,oppCurrentPk,oppPkAlive,typeTable,affected,oppType,bright_red,True)
        self.currentHp = self.currentHp - (0.0625 * self.__hp)
        self.burnTurns += 1
        if self.burnTurns == 6:
          self.status = "None"
        time.sleep(0.5)
        os.system('cls')

      case "poisoned":
        print(self.name + " was hurt by "+magenta+"poison"+reset)
        time.sleep(0.5)
        os.system('cls')
        animations.health(self,trainerPkAlive,self.currentHp,self.__hp,((self.poisonTurns*0.0625) * self.__hp),battleStatsDisplay,oppCurrentPk,oppPkAlive,typeTable,affected,oppType,magenta,True)
        self.currentHp = self.currentHp - ((self.poisonTurns*0.0625) * self.__hp)
        self.poisonTurns += 1
        time.sleep(0.5)
        os.system('cls')

  def damageDealt(self,damageDone,oppCurrentPk,trainerPkAlive,oppPkAlive,affected,BSD):
    if overallMoveEff == 2:
      print(bold + "It was SUPER EFFECTIVE" +"(-"+str(round(damageDone))+"hp)"+ reset)
    elif overallMoveEff == 0.5:
      print(bold + "It was NOT VERY EFFECTIVE" +"(-"+str(round(damageDone))+"hp)"+ reset)
    elif overallMoveEff == 0:
      print(bold + "It had NO EFFECT" +"(-"+str(round(damageDone))+"hp)"+ reset)
    else:
      print("(-"+str(round(damageDone))+"hp)")
    time.sleep(1.3)
    is0 = False
    if self.currentHp - damageDone < 0:
      damageDone = self.currentHp
      is0 = True
    os.system('cls')
    animations.health(self,trainerPkAlive,self.currentHp,self.__hp,damageDone,battleStatsDisplay,oppCurrentPk,oppPkAlive,typeTable,affected,oppType,red,True)

    if is0 is False:
      self.currentHp = self.currentHp - damageDone
    else:
      self.currentHp = 0

def main(restart):
  if restart == False:
    title()

  pkList = []
  pkList = partySetup("trainer") #creating 6 pokemon and adding them to pkList
  partyMoveSelector(pkList) #assigning moves to the pokemon objects

  global isTitle
  isTitle = True
  partyPrint(pkList,False,"countdown",True) #does title print one parameters:(list, printHP,type,isTitle)
  isTitle = False

  trainersBeat = 0
  wildsBeat = 0
  global trainer
  trainer = bag()

  global points
  points = 0
  result = "again"
  while result == "again" or result == "ran" or result == "win" or result == "catch":
    result = battleInit(pkList,trainer)
    if result == "win":
      if oppType == "trainer":
        trainersBeat += 1
        points += math.ceil(numOppPk / 2)
      else:
        wildsBeat += 1
        points += 1
      os.system('cls')
      print("")

  os.system('cls')
  print(bold + "You blacked out..." + reset)
  time.sleep(1)
  os.system('cls')
  print(red + r"""

  ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗████████╗
  ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝╚══██╔══╝
   ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗   ██║
    ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║   ██║
     ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║   ██║
     ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝   ╚═╝
  """ + reset)
  print(r"""
  - You managed to beat:
     - """+str(trainersBeat)+""" trainers
     - and """+str(wildsBeat)+""" wild fakémon
  - This means that your score was """+str(points)+"""
  """)
  input("Restart (enter anything) >> ")
  os.system('cls')
  main(True)

def title(): #make title slowly fade in up/down
  ys = "\033[38;2;199;160;8m"
  y = "\033[38;2;245;194;66m"
  
  for i in range(0,8):
    if i % 2 == 0:
      print()
    print("\033[38;2;245;194;66m" + r"""

      ███████"""+ys+"""╗"""+y+""" █████"""+ys+"""╗"""+y+""" ██"""+ys+"""╗"""+y+"""  ██"""+ys+"""╗"""+y+"""███████"""+ys+"""╗"""+y+"""███"""+ys+"""╗"""+y+"""   ███"""+ys+"""╗"""+y+""" ██████"""+ys+"""╗"""+y+""" ███"""+ys+"""╗"""+y+"""   ██"""+ys+"""╗
      """+y+"""██"""+ys+"""╔════╝"""+y+"""██"""+ys+"""╔══"""+y+"""██"""+ys+"""╗"""+y+"""██"""+ys+"""║"""+y+""" ██"""+ys+"""╔╝"""+y+"""██"""+ys+"""╔════╝"""+y+"""████"""+ys+"""╗"""+y+""" ████"""+ys+"""║"""+y+"""██"""+ys+"""╔═══"""+y+"""██"""+ys+"""╗"""+y+"""████"""+ys+"""╗"""+y+"""  ██"""+ys+"""║
      """+y+"""█████"""+ys+"""╗"""+y+"""  ███████"""+ys+"""║"""+y+"""█████"""+ys+"""╔╝"""+y+""" █████"""+ys+"""╗"""+y+"""  ██"""+ys+"""╔"""+y+"""████"""+ys+"""╔"""+y+"""██"""+ys+"""║"""+y+"""██"""+ys+"""║"""+y+"""   ██"""+ys+"""║"""+y+"""██"""+ys+"""╔"""+y+"""██"""+ys+"""╗"""+y+""" ██"""+ys+"""║
      """+y+"""██"""+ys+"""╔══╝"""+y+"""  ██"""+ys+"""╔══"""+y+"""██"""+ys+"""║"""+y+"""██"""+ys+"""╔═"""+y+"""██"""+ys+"""╗"""+y+""" ██"""+ys+"""╔══╝"""+y+"""  ██"""+ys+"""║╚"""+y+"""██"""+ys+"""╔╝"""+y+"""██"""+ys+"""║"""+y+"""██"""+ys+"""║"""+y+"""   ██"""+ys+"""║"""+y+"""██"""+ys+"""║╚"""+y+"""██"""+ys+"""╗"""+y+"""██"""+ys+"""║
      """+y+"""██"""+ys+"""║"""+y+"""     ██"""+ys+"""║"""+y+"""  ██"""+ys+"""║"""+y+"""██"""+ys+"""║"""+y+"""  ██"""+ys+"""╗"""+y+"""███████"""+ys+"""╗"""+y+"""██"""+ys+"""║ ╚═╝"""+y+""" ██"""+ys+"""║╚"""+y+"""██████"""+ys+"""╔╝"""+y+"""██"""+ys+"""║ ╚"""+y+"""████"""+ys+"""║
      ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
  """ + reset)
    if i % 2 != 0:
      print("")
    print(r"""
    - Win battles to earn points
    - If you lose, your points are your final score and you are done
    - Wild pokemon - 1 point
    - Trainer - points = num of pokemon / 2 (rounded up)

                             Pokemon types
   """+"\033[48;2;168;167;122m"+""" Normal """+"\033[48;2;187;85;68m"+""" Fighting """+"\033[48;2;136;153;255m"+""" Flying """+"\033[48;2;163;62;161m"+""" Poison """+"\033[48;2;197;167;76m"+""" Ground """+"\033[48;2;187;170;102m"+""" Rock """+"\033[48;2;170;187;34m"+""" Bug """+"\033[48;2;102;102;187m"+""" Ghost """+"\033[48;2;170;170;187m"+""" Steel """+reset+"""
    """+"\033[48;2;255;68;34m"+""" Fire """+"\033[48;2;50;150;250m"+""" Water """+"\033[48;2;119;204;85m"+""" Grass """+"\033[48;2;254;203;51m"+""" Electric """+"\033[48;2;220;100;135m"+""" Psychic """+"\033[48;2;102;204;255m"+""" Ice """+"\033[48;2;119;102;238m"+""" Dragon """+"\033[48;2;119;85;68m"+""" Dark """+"\033[48;2;238;153;238m"+""" Fairy """ + reset+"""
     """)
    if i != 7:
      print(bold + "LOADING...")
      time.sleep(1)
      os.system('cls')
    else:
      time.sleep(1)
  input("Enter anything to continue >> "+reset)
  os.system('cls')

def partyPrint(list,printHP,type,isTitle):
  moves = []
  if type == "countdown":
    if isTitle is True:
      print("You have received the following fakémon:\n ")
    print("-----------------------------------------------------------------------")
    for i in range(0,len(list)):
      moves = [[list[i].move1t,list[i].move1n],
               [list[i].move2t,list[i].move2n],
               [list[i].move3t,list[i].move3n],
               [list[i].move4t,list[i].move4n]]
      print(list[i].name) #printing the name of the pokemon
      print(typeTable[list[i].type1]["hc"] +" "+list[i].type1+" "+reset,end="",flush=True)
      if list[i].type2 != "Null":
        print(" "+typeTable[list[i].type2]["hc"] +" "+list[i].type2+" " + reset)
      else:
        print("")
      print()
      for j in range(0,4):
        print(typeTable[moves[j][0]]["c"] + "● " + reset + moves[j][1] + "     ",end="",flush=True)
      print("")
      print("-----------------------------------------------------------------------")
      time.sleep(1.5) #revals the pokemon

    for k in range(0,3):
      os.system('cls')
      if isTitle is True:
        print("You have received the following fakémon:\n ")
      print("-----------------------------------------------------------------------")
      for i in range(0,len(list)):
        moves = [[list[i].move1t,list[i].move1n],[list[i].move2t,list[i].move2n],[list[i].move3t,list[i].move3n],[list[i].move4t,list[i].move4n]]
        print(list[i].name) #printing the name of the pokemon
        print(typeTable[list[i].type1]["hc"] +" "+list[i].type1+" "+reset,end="",flush=True)
        if list[i].type2 != "Null":
          print(" "+typeTable[list[i].type2]["hc"] +" "+list[i].type2+" "+reset)
        else:
          print("")
        print()
        for j in range(0,4):
          print(typeTable[moves[j][0]]["c"] + "● " + reset + moves[j][1] + "     ",end="",flush=True)
        print("")
        print("-----------------------------------------------------------------------")
      print("\n                             < " + str(3-k) + " >")
      time.sleep(1) #does the countdown

  elif type == "compact":

    longestNameLen = 0
    for j in range(0,len(list)):
      if len(list[j].name) > longestNameLen:
        longestNameLen = len(list[j].name)
    
    print("-----------------------------------------------------------------------")
    for i in range(0,len(list)):
      typeSpace = (longestNameLen+2) - len(list[i].name)
      print(white + str(i+1)+ ". " + list[i].name + (typeSpace*" ") + typeTable[list[i].type1]["hc"] +" "+ list[i].type1+" "+reset,end="",flush=True)
      if list[i].type2 != "Null":
        print(typeTable[list[i].type2]["hc"] +" "+list[i].type2+" "+reset) #otherwise print both
      else:
        print("")
      time.sleep(0.1)
    print(white + "-----------------------------------------------------------------------")

  if type == "full":
    for i in range(0,len(list)):
      moves = [[list[i].move1t,list[i].move1n],[list[i].move2t,list[i].move2n],[list[i].move3t,list[i].move3n],[list[i].move4t,list[i].move4n]]
      print(str(i+1)+ ". " + list[i].name) #printing the name of the pokemon
      print(typeTable[list[i].type1]["hc"] +" "+list[i].type1+" "+reset,end="",flush=True)
      if list[i].type2 != "Null":
        print(" " + typeTable[list[i].type2]["hc"] +" "+list[i].type2+" "+reset)
      else:
        print("")
  
      if list[i].status == "paralysed":
        print("\033[48;2;254;203;51m" + " Paralysed " + reset)
      elif list[i].status == "poisoned":
        print("\033[48;2;163;62;161m" + " Poisoned " + reset)
      elif list[i].status == "burned":
        print("\033[48;2;235;68;34m" + " Burned " + reset)
      else:
        print()

      if printHP is True:
        HPPrint(list[i],"noLoading")
        print()
      print()
      for j in range(0,4):
        print(typeTable[moves[j][0]]["c"] + "● " + reset + moves[j][1] + "     ",end="",flush=True)
      print("")
      print("-----------------------------------------------------------------------")
  del moves

def HPPrint(pk,loadingBars):
  hp = pokemon.getHP(pk)
  percent = pk.currentHp / hp #what % of the maxhp is the currenthp
  greenbars = math.ceil(20 * percent)  #formula for woking out how many + is needed for hp
  redbars = 20 - greenbars

  if pk.currentHp <= (hp / 4):
    colour = red
  elif pk.currentHp <= hp / 2:
    colour = orange
  else:
    colour = green

  print(colour +  greenbars*"█" + bright_black + redbars*"█" + reset,end='', flush=True)
  printingHp = int(math.ceil(pk.currentHp))
  spaces = 3-len(str(printingHp))
  print(" " + str(printingHp) + (spaces*" "), end="", flush=True)

def partySetup(choice):
  with open("pokemon.txt") as textfile:
    tempList = [line.split() for line in textfile]
  pokeList = random.sample(tempList, 6) #takes 6 random pokemon from the pokemon.txt  
  
#pokemon(name, type1, type2, hp, att, def, sAtt, sDef, spd)
  global oppType

  if choice == "trainer":
    position1 = pokemon(*pokeList[0])
    position2 = pokemon(*pokeList[1])
    position3 = pokemon(*pokeList[2])
    position4 = pokemon(*pokeList[3])
    position5 = pokemon(*pokeList[4])
    position6 = pokemon(*pokeList[5])
    return [position1, position2, position3, position4, position5, position6]

  elif choice > 1:
    oppType = "trainer"#trainer opp
    oppPosition1 = pokemon(*pokeList[0])
    oppPosition2 = pokemon(*pokeList[1])
    oppPosition3 = pokemon(*pokeList[2])
    oppPosition4 = pokemon(*pokeList[3])
    oppPosition5 = pokemon(*pokeList[4])
    oppPosition6 = pokemon(*pokeList[5])
    opponentPartyList = [oppPosition1,oppPosition2,oppPosition3,oppPosition4,oppPosition5,oppPosition6]

    if points < 10:
      numPk = random.randint(1,3)
    elif points <= 15 and points >= 10:
      numPk = random.randint(1,5)
    elif points <= 20 and points >= 15:
      numPk = random.randint(3,6)
    else:
      numPk = 6

    if numPk < 6:
      for k in range(0,(6-numPk)): #the higher the number is the more pokemon in the party, 5 = 5 pokemon in party
        opponentPartyList.pop()

    return opponentPartyList

  else: #wild
    oppType = "wild"
    randomWildPkm = random.sample(tempList,1)
    wildpk = pokemon(*randomWildPkm[0])

    with open("moves.txt") as file:
      tempList = [line.split(",") for line in file] #putting all the moves into tempList split by ','
      temp2List = []
      for j in range(0,len(tempList)): #for each move in the tempList
        if tempList[j][1] in typeTable[wildpk.type1]["move"] or tempList[j][1] in typeTable[wildpk.type2]["move"]:
          duplicate = False
          for k in range(0,len(temp2List)):
            if tempList[j][0] == temp2List[k][0]: #checking whether the pokemon already has the move or not
              duplicate = True
          if duplicate is False:
            temp2List.append(tempList[j]) #adding the eligible ones to a second temp list
    l = random.sample(temp2List,4) #taking 4 random ones
    wildpk.assignMoves(l[0][0],l[0][1],l[0][2],l[0][3],
                       l[1][0],l[1][1],l[1][2],l[1][3],
                       l[2][0],l[2][1],l[2][2],l[2][3],
                       l[3][0],l[3][1],l[3][2],l[3][3])
    del l
    del tempList
    del temp2List
    list = [wildpk]
    return list

def partyMoveSelector(list): #when called originally, list is pkList
    for i in range(0,len(list)): #per pokemon
      with open("moves.txt") as file:
        tempList = [line.split(",") for line in file] #putting all the moves into tempList split by ','
        temp2List = []
        for j in range(0,len(tempList)): #for each move in the tempList
          if tempList[j][1] in typeTable[list[i].type1]["move"] or tempList[j][1] in typeTable[list[i].type2]["move"]:
            duplicate = False
            for k in range(0,len(temp2List)):
              if tempList[j][0] == temp2List[k][0]: #checking whether the pokemon already has the move or not
                duplicate = True
            if duplicate is False:
              temp2List.append(tempList[j]) #adding the eligible ones to a second temp list
      l = random.sample(temp2List,4) #taking 4 random ones
      list[i].assignMoves(l[0][0],l[0][1],l[0][2],l[0][3],
                          l[1][0],l[1][1],l[1][2],l[1][3],
                          l[2][0],l[2][1],l[2][2],l[2][3],
                          l[3][0],l[3][1],l[3][2],l[3][3]) #calling the assign moves method in the pokemon class
      del l
      del tempList
      del temp2List

def battleInit(pkList,trainer):
  for j in range(0,6):
    pokemon.resetHP(pkList[j])
    pokemon.resetStats(pkList[j])
  attemptedEscape = 0
  if points == 0:
    choice = 1
  else:
    choice = random.randint(1,4)
  oppPartyList = []
  oppPartyList = partySetup(choice)
  partyMoveSelector(oppPartyList)
  os.system('cls')

  global numOppPk
  numOppPk = len(oppPartyList)

  if choice == 1:
    animations.longGrass(points)
  else:
    animations.trainerLongGrass(points)

  oppName = ""
  if choice != 1:
    oppName = pokemon.getOppName()
    greyCircles = 6 - len(oppPartyList)
    redCircles = 6 - greyCircles
    while redCircles > 0:
      print(red + "●", end='', flush=True)
      redCircles -= 1
      time.sleep(0.013)
    while greyCircles > 0:
      print(bright_black + "●", end='', flush=True)
      greyCircles -= 1
      time.sleep(0.013)
  else:
    pokemon.printWild()
  print(" ")
  print(white + "\nYour fakémon: ")
  partyPrint(pkList,False,"compact",False)

  carryOn = False
  while carryOn is False:
    try:
      currentPkIndex = int(input("\nPick the pokemon to start the battle with (the number) >> "))-1
      if currentPkIndex <= 5 and currentPkIndex >= 0:
        carryOn = True
        currentPk = pkList[currentPkIndex]
    except ValueError:
      print(red + "That is not a number" + reset)

  os.system('cls')
  statusMovesUsed = 0
  global trainerPkAlive
  trainerPkAlive = 6
  global oppPkAlive
  oppPkAlive = len(oppPartyList)
  oppCurrentPkIndex = random.randint(0,len(oppPartyList)-1)
  oppCurrentPk = oppPartyList[oppCurrentPkIndex]
  if choice != 1:
    pokemon.sendOutOpp(oppPartyList[oppCurrentPkIndex],oppName)
  else:
    print(bold + "A wild " + oppPartyList[0].name + " appeared!")
  time.sleep(1.3)
  os.system('cls')
  pokemon.sendOut(currentPk)
  time.sleep(1.3)
  os.system('cls')
  if oppType == "trainer":
    animations.battleInitialGraphic(typeTable[currentPk.type1]["c"],typeTable[oppCurrentPk.type1]["c"])
  else:
    animations.wildBattleInitialGraphic(typeTable[currentPk.type1]["c"],typeTable[oppCurrentPk.type1]["c"],battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]],False)
  os.system('cls')
  carryOn = True
  result = [currentPk,oppCurrentPk]
  global numTurns
  numTurns = 1
  while carryOn is True:
    result = battleTurn(result[0],result[1],attemptedEscape,statusMovesUsed,pkList,oppName,trainerPkAlive,oppPkAlive,trainer,oppPartyList,numTurns)
    numTurns += 1
    if result != None:
      if result[0] in ("loss", "win", "ran","catch"):
        if result[0] == "win" and oppType == "trainer":
          print(bold + "You defeated " + oppName + "!" + reset)
          time.sleep(1)
          os.system('cls')
        elif result[0] == "win" and oppType == "wild":
          print("You defeated the wild " + oppCurrentPk.name)
          time.sleep(1.5)
          os.system('cls')
        if result != "loss":
          print(bold+"Your pokemon have been healed")
          time.sleep(1.5)
          os.system('cls')
          print("All stat changes and status effects have been reset")
          time.sleep(1.5)
          os.system('cls')
          input("Enter anything to continue >> ")
          carryOn = False
        return result[0]

def battleStatsDisplay(currentPk,pkAlive):
  print(reset + "|--------------------------|")
  print("| " + currentPk.name + " ", end="", flush=True)
  if currentPk.status == "paralysed":
    print("\033[48;2;254;203;51m" + " Paralysed " + reset + (13-len(currentPk.name))*" " + "|")
  elif currentPk.status == "poisoned":
    print("\033[48;2;163;62;161m" + " Poisoned " + reset + (14-len(currentPk.name))*" " + "|")
  elif currentPk.status == "burned":
    print("\033[48;2;235;68;34m" + " Burned " + reset + (16-len(currentPk.name))*" " + "|")
  else:
    print((24-len(currentPk.name))*" " + "|")
  print("| ", end = "", flush = True)
  HPPrint(currentPk,"noLoading")
  print(reset + " |")

  greyCircles = 6 - pkAlive
  redCircles = 6 - greyCircles
  print("| ", end="",flush=True)
  while redCircles > 0:
    print(red + "●", end='', flush=True)
    redCircles -= 1
  while greyCircles > 0:
    print(bright_black + "●", end='', flush=True)
    greyCircles -= 1
  print(reset + 19*" " + "|")
  print("|--------------------------|")

def battleTurn(currentPk,oppCurrentPk,attemptedEscape,statusMovesUsed,pkList,oppName,trainerPkAlive,oppPkAlive,trainer,oppPartyList,numTurns):
  print("You:")
  battleStatsDisplay(currentPk, trainerPkAlive)
  print("\nOpponent:")
  battleStatsDisplay(oppCurrentPk,oppPkAlive)
  animations.battleTurnGraphic(balls,trainer,oppType,"selection",typeTable[currentPk.type1]["c"], typeTable[oppCurrentPk.type1]["c"],None,None,typeTable)
  carryOn = False
  battleChoice = 5
  while carryOn is False:
    try:
      battleChoice = int(input("Number >> "))
      if battleChoice <= 5 and battleChoice >= 0:
        carryOn = True
    except ValueError:
      print(red + "That is not a number" + reset)
  match battleChoice:
    case 1:
      moveUsed = battleAttack(currentPk,oppCurrentPk)
    case 2:
      os.system('cls')
      trainerPkAlive = battleBag(trainer,pkList,currentPk,oppCurrentPk,trainerPkAlive)
      cpuBattle(oppCurrentPk,currentPk,statusMovesUsed,trainerPkAlive,oppPkAlive)
    case 3:
      currentPk = battleFakemon(pkList,oppCurrentPk,statusMovesUsed,currentPk,attemptedEscape,oppName,oppPartyList,trainerPkAlive,oppPkAlive)
      cpuBattle(oppCurrentPk,currentPk,statusMovesUsed,trainerPkAlive,oppPkAlive)
    case 4:
      print()
      if oppType == "wild":
        attemptedEscape += 1
        probability = (((currentPk.speed * 128)/oppCurrentPk.speed) + 30 * attemptedEscape) % 256
        rInt = random.randint(1,256)

        if rInt <= probability:
          print(bold + green + "You got away safely" + reset)
          os.system('cls')
          return ["ran"]
        else:
          print(bold + red + "You couldn't get away!" + reset)
          time.sleep(2)
          os.system('cls')
          cpuBattle(oppCurrentPk,currentPk,statusMovesUsed,trainerPkAlive,oppPkAlive)
      else:
        print(bold + red + "You can't run from a trainer!" + reset)
        time.sleep(2)
        os.system('cls')
    case 5:
      if oppType == "wild":
        caught = battleCatch(currentPk,oppCurrentPk,trainer,pkList,numTurns)
        if caught is True:
          return ["catch"]
        else:
          cpuBattle(oppCurrentPk,currentPk,statusMovesUsed,trainerPkAlive,oppPkAlive)
          os.system('cls')
          time.sleep(1)
          pokemon.statusEffect(currentPk,oppCurrentPk,"opp")
          pokemon.statusEffect(oppCurrentPk,currentPk,"trainer")
          os.system('cls')
          return [currentPk,oppCurrentPk]
      else:
        print(bold + red + "You cannot catch another trainers pokemon!" + reset)
        os.system('cls')

  
  if battleChoice == 1 and len(moveUsed) != 0:
    if currentPk.speed > oppCurrentPk.speed:
      pkCol1 = typeTable[currentPk.type1]["c"]
      pkCol2 = typeTable[oppCurrentPk.type1]["c"]
      os.system('cls')
      print(bold+"You:"+reset)
      battleStatsDisplay(currentPk, trainerPkAlive)
      print()
      print(bold+"Opponent:"+reset)
      battleStatsDisplay(oppCurrentPk, oppPkAlive)
      animations.battleTurnGraphic(balls,trainer,oppType,None,typeTable[currentPk.type1]["c"], typeTable[oppCurrentPk.type1]["c"],None,None,typeTable)
      print("\n"+bold + moveUsed[4] + reset)
      time.sleep(1.5)
      os.system('cls')
      if moveUsed[3] == "st": #status move or not
        if int(moveUsed[2]) in [-1,-2,-4,-15]: #self or not
          if oppType == "wild":
            animations.wildStatus("opp",pkCol1,pkCol2,battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
          else:
            animations.status("opp",pkCol1,pkCol2,battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
  
        else:
          if oppType == "wild":
            animations.wildStatus("self",pkCol1,pkCol2,battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
          else:
            animations.status("self",pkCol1,pkCol2,battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
        pokemon.assignStatus(currentPk,moveUsed[2],oppCurrentPk)
        print(reset)
      else:
        if oppType == "wild":
          animations.wildYouAttack(pkCol1,pkCol2,typeTable[moveUsed[1]]["c"],battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
        else:
          animations.youAttack(pkCol1,pkCol2,typeTable[moveUsed[1]]["c"],battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
        time.sleep(0.2)
        damageDone = damageCalculation(moveUsed,currentPk,oppCurrentPk)
        pokemon.damageDealt(oppCurrentPk,damageDone,currentPk,oppPkAlive,trainerPkAlive,"trainer",battleStatsDisplay)
      time.sleep(3)
      os.system('cls')
      if oppCurrentPk.currentHp > 0:
        cpuBattle(oppCurrentPk,currentPk,statusMovesUsed,trainerPkAlive,oppPkAlive)
      else:
        print(bold+"You:"+reset)
        battleStatsDisplay(currentPk, trainerPkAlive)
        print()
        print(bold+"Opponent:"+reset)
        battleStatsDisplay(oppCurrentPk, oppPkAlive)
        animations.battleTurnGraphic(balls,trainer,oppType,None,typeTable[currentPk.type1]["c"], typeTable[oppCurrentPk.type1]["c"],None,None,typeTable)
        print(bold + oppCurrentPk.name + red + " has fainted!" + reset)
        time.sleep(1)
        oppPkAlive -= 1
        if oppPkAlive >= 1:
          oppCurrentPk = cpuSwitch(currentPk,oppCurrentPk,oppName,oppPartyList)
        else:
          if oppType == "wild":
            animations.wildDefeat(typeTable[currentPk.type1]["c"],typeTable[oppCurrentPk.type1]["c"],battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
          else:
            animations.oppTrainerWithdraw(typeTable[currentPk.type1]["c"],typeTable[oppCurrentPk.type1]["c"],battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
          return ["win"]

    else:
      cpuBattle(oppCurrentPk,currentPk,statusMovesUsed,trainerPkAlive,oppPkAlive)
      time.sleep(3)
      if currentPk.currentHp > 0:
        pkCol1 = typeTable[currentPk.type1]["c"]
        pkCol2 = typeTable[oppCurrentPk.type1]["c"]
        os.system('cls')
        
        print(bold+"You:"+reset)
        battleStatsDisplay(currentPk, trainerPkAlive)
        print()
        print(bold+"Opponent:"+reset)
        battleStatsDisplay(oppCurrentPk, oppPkAlive)
        animations.battleTurnGraphic(balls,trainer,oppType,None,typeTable[currentPk.type1]["c"], typeTable[oppCurrentPk.type1]["c"],None,None,typeTable)
        
        print(bold + moveUsed[4] + reset)
        time.sleep(1.5)
        os.system('cls')
        print(bold+"You:"+reset)
        battleStatsDisplay(currentPk, trainerPkAlive)
        print()
        print(bold+"Opponent:"+reset)
        battleStatsDisplay(oppCurrentPk, oppPkAlive)
        animations.battleTurnGraphic(balls,trainer,oppType,None,typeTable[currentPk.type1]["c"], typeTable[oppCurrentPk.type1]["c"],None,None,typeTable)
        if moveUsed[3] == "st": #status move or not
          if int(moveUsed[2]) in [-1,-2,-4,-15]: #self or not
            if oppType == "wild":
              animations.wildStatus("opp",pkCol1,pkCol2,battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
            else:
              animations.status("opp",pkCol1,pkCol2,battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
  
          else:
            if oppType == "wild":
              animations.wildStatus("self",pkCol1,pkCol2,battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
            else:
              animations.status("self",pkCol1,pkCol2,battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
          pokemon.assignStatus(currentPk,moveUsed[2],oppCurrentPk)
          print(reset)
        else:
          if oppType == "wild":
            animations.wildYouAttack(pkCol1,pkCol2,typeTable[moveUsed[1]]["c"],battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
          else:
            animations.youAttack(pkCol1,pkCol2,typeTable[moveUsed[1]]["c"],battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
          time.sleep(0.2)
          damageDone = damageCalculation(moveUsed,currentPk,oppCurrentPk)
          pokemon.damageDealt(oppCurrentPk,damageDone,currentPk,oppPkAlive,trainerPkAlive,"trainer",battleStatsDisplay)
      else:
        print(bold + currentPk.name + " has fainted!" + reset)
        time.sleep(1)
        os.system('cls')
        trainerPkAlive -= 1
        if trainerPkAlive > 0:
          if oppType == "wild":
              animations.wildTrainerWithdraw(typeTable[currentPk.type1]["c"],typeTable[oppCurrentPk.type1]["c"],battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
          else:
              animations.trainerWithdraw(typeTable[currentPk.type1]["c"],typeTable[oppCurrentPk.type1]["c"],battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
          currentPk = battleFakemon(pkList,oppCurrentPk,statusMovesUsed,currentPk,attemptedEscape,oppName,oppPartyList,trainerPkAlive,oppPkAlive)
        else:
          return ["loss"]

  if currentPk.currentHp <= 0:
    print(bold+"You:"+reset)
    battleStatsDisplay(currentPk, trainerPkAlive)
    print()
    print(bold+"Opponent:"+reset)
    battleStatsDisplay(oppCurrentPk, oppPkAlive)
    animations.battleTurnGraphic(balls,trainer,oppType,None,typeTable[currentPk.type1]["c"], typeTable[oppCurrentPk.type1]["c"],None,None,typeTable)
    print()
    print(bold + currentPk.name + " has fainted!" + reset)
    time.sleep(2)
    os.system('cls')
    trainerPkAlive -= 1
    if trainerPkAlive > 0:
      currentPk = battleFakemon(pkList,oppCurrentPk,statusMovesUsed,currentPk,attemptedEscape,oppName,oppPartyList,trainerPkAlive,oppPkAlive)
    else:
      if oppType == "wild":
        animations.wildTrainerWithdraw(typeTable[currentPk.type1]["c"],typeTable[oppCurrentPk.type1]["c"],battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
      else:
        animations.trainerWithdraw(typeTable[currentPk.type1]["c"],typeTable[oppCurrentPk.type1]["c"],battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
      return ["loss"]

  if oppCurrentPk.currentHp <= 0:
    print(bold+"You:"+reset)
    battleStatsDisplay(currentPk, trainerPkAlive)
    print()
    print(bold+"Opponent:"+reset)
    battleStatsDisplay(oppCurrentPk, oppPkAlive)
    animations.battleTurnGraphic(balls,trainer,oppType,None,typeTable[currentPk.type1]["c"], typeTable[oppCurrentPk.type1]["c"],None,None,typeTable)
    print()
    print(bold + red + oppCurrentPk.name + " has fainted!" + reset)
    time.sleep(2)
    os.system('cls')
    oppPkAlive -= 1
    if oppPkAlive > 0:
      oppCurrentPk = cpuSwitch(currentPk,oppCurrentPk,oppName,oppPartyList)
    else:
      animations.oppTrainerWithdraw(typeTable[currentPk.type1]["c"],typeTable[oppCurrentPk.type1]["c"],battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
      return ["win"]

  os.system('cls')
  if trainerPkAlive == 0:
    return ["loss"]
  elif oppPkAlive == 0:
    return ["win"]
  elif battleChoice != 5:
    pokemon.statusEffect(currentPk,oppCurrentPk,"opp")
    pokemon.statusEffect(oppCurrentPk,currentPk,"trainer")
    return [currentPk,oppCurrentPk]
  
  if currentPk.currentHp < 0:
    print(bold+"You:"+reset)
    battleStatsDisplay(currentPk, trainerPkAlive)
    print()
    print(bold+"Opponent:"+reset)
    battleStatsDisplay(oppCurrentPk, oppPkAlive)
    animations.battleTurnGraphic(balls,trainer,oppType,None,typeTable[currentPk.type1]["c"], typeTable[oppCurrentPk.type1]["c"],None,None,typeTable)
    print()
    print(bold + currentPk.name + " has fainted!" + reset)
    time.sleep(2)
    os.system('cls')
    trainerPkAlive -= 1
    if trainerPkAlive > 0:
      currentPk = battleFakemon(pkList,oppCurrentPk,statusMovesUsed,currentPk,attemptedEscape,oppName,oppPartyList,trainerPkAlive,oppPkAlive)
    else:
      if oppType == "wild":
        animations.wildTrainerWithdraw(typeTable[currentPk.type1]["c"],typeTable[oppCurrentPk.type1]["c"],battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
      else:
        animations.trainerWithdraw(typeTable[currentPk.type1]["c"],typeTable[oppCurrentPk.type1]["c"],battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
      return ["loss"]

  if oppCurrentPk.currentHp < 0:
    print(bold+"You:"+reset)
    battleStatsDisplay(currentPk, trainerPkAlive)
    print()
    print(bold+"Opponent:"+reset)
    battleStatsDisplay(oppCurrentPk, oppPkAlive)
    animations.battleTurnGraphic(balls,trainer,oppType,None,typeTable[currentPk.type1]["c"], typeTable[oppCurrentPk.type1]["c"],None,None,typeTable)
    print()
    print(bold + red + oppCurrentPk.name + " has fainted!" + reset)
    time.sleep(2)
    os.system('cls')
    oppPkAlive -= 1
    if oppPkAlive > 0:
      oppCurrentPk = cpuSwitch(currentPk,oppCurrentPk,oppName,oppPartyList)
    else:
      animations.oppTrainerWithdraw(typeTable[currentPk.type1]["c"],typeTable[oppCurrentPk.type1]["c"],battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
      return ["win"]

def battleAttack(currentPk,oppCurrentPk): #the 2 objects and who is doing the attack (trainer or opp)
  os.system('cls') 
  print("You:")
  battleStatsDisplay(currentPk,trainerPkAlive)
  print("\nOpponent:")
  battleStatsDisplay(oppCurrentPk,oppPkAlive)
  animations.battleTurnGraphic(balls,trainer,oppType,"attack",typeTable[currentPk.type1]["c"], typeTable[oppCurrentPk.type1]["c"],currentPk,oppCurrentPk,typeTable)

  carryOn = False
  moveChoice = 5
  moveUsed = [None,None,None,None,None]
  while carryOn is False:
    moveChoice2 = input("\nNumber >> ")
    try:
      if "i" in moveChoice2:
        moveChoice = int(moveChoice2[0])
        list = [
          [currentPk.move1n,currentPk.move1t,currentPk.move1p,currentPk.move1s],
          [currentPk.move2n,currentPk.move2t,currentPk.move2p,currentPk.move2s],
          [currentPk.move3n,currentPk.move3t,currentPk.move3p,currentPk.move3s], 
          [currentPk.move4n,currentPk.move4t,currentPk.move4p,currentPk.move4s]
              ]
        os.system('cls')
        print("You:")
        battleStatsDisplay(currentPk,trainerPkAlive)
        print("\nOpponent:")
        battleStatsDisplay(oppCurrentPk,oppPkAlive)
        animations.battleTurnGraphic(balls,trainer,oppType,None,typeTable[currentPk.type1]["c"], typeTable[oppCurrentPk.type1]["c"],currentPk,oppCurrentPk,typeTable)
        print(list[moveChoice-1][0])
        print("Power "+list[moveChoice-1][2])
        print(typeTable[list[moveChoice-1][1]]["hc"]+" "+ list[moveChoice-1][1]+" "+reset)
        moveEffectiveness = 1
        moveEffectiveness2 = 1
        if list[moveChoice-1][3] != "st":
          if oppCurrentPk.type1 in typeTable[list[moveChoice-1][1]][2]:
            moveEffectiveness = 2
          elif oppCurrentPk.type1 in typeTable[list[moveChoice-1][1]][1]:
            moveEffectiveness = 1
          elif oppCurrentPk.type1 in typeTable[list[moveChoice-1][1]][0.5]:
            moveEffectiveness = 0.5
          elif oppCurrentPk.type1 in typeTable[list[moveChoice-1][1]][0]:
            moveEffectiveness = 0
                
          if oppCurrentPk.type2 != "Null":
            if oppCurrentPk.type2 in typeTable[list[moveChoice-1][1]][2]:
              moveEffectiveness2 = 2
            elif oppCurrentPk.type2 in typeTable[list[moveChoice-1][1]][1]:
              moveEffectiveness2 = 1
            elif oppCurrentPk.type2 in typeTable[list[moveChoice-1][1]][0.5]:
              moveEffectiveness2 = 0.5
            elif oppCurrentPk.type2 in typeTable[list[moveChoice-1][1]][0]:
              moveEffectiveness2 = 0

          overallMoveEffectiveness = float(moveEffectiveness) * float(moveEffectiveness2) #IS FLOAT
                  
          match overallMoveEffectiveness:
            case 0:
              print("No effect!")
            case 0.5:
              print("Not very effective!")
            case 2:
              print("Super effective!")
        else:
          print("\nStatus move")

        if list[moveChoice-1][3] == "s":
          print("Special move")
        elif list[moveChoice-1][3] == "p":
          print("Physical move")
        confirm = int(input("\n1. Use move\n2.Back <--\n\n>> "))
        if confirm == 1:
          carryOn = True
        else:
          os.system('cls')
          print("You:")
          battleStatsDisplay(currentPk,trainerPkAlive)
          print("\nOpponent:")
          battleStatsDisplay(oppCurrentPk,oppPkAlive)
          animations.battleTurnGraphic(balls,trainer,oppType,"attack",typeTable[currentPk.type1]["c"], typeTable[oppCurrentPk.type1]["c"],currentPk,oppCurrentPk,typeTable)

      elif int(moveChoice2) <= 5 and int(moveChoice2) > 0:
        carryOn = True
        moveChoice = int(moveChoice2)
      elif int(moveChoice2) > 5:
        print(red+"Your input is greater than 5"+reset)
      elif int(moveChoice2) < 1:
        print(red+"Your input is less than 1"+reset)
    except ValueError:
      print(red+"Only the letter i can be used"+reset)

  moveUsed = [" "," ",0," "," "]
  match moveChoice:
    case 1:
      textLine = currentPk.name + " used " + currentPk.move1n
      moveUsed = [currentPk.move1n,currentPk.move1t,currentPk.move1p,currentPk.move1s,textLine]
    case 2:
      textLine = currentPk.name + " used " + currentPk.move2n
      moveUsed = [currentPk.move2n,currentPk.move2t,currentPk.move2p,currentPk.move2s,textLine]
    case 3:
      textLine = currentPk.name + " used " + currentPk.move3n
      moveUsed = [currentPk.move3n,currentPk.move3t,currentPk.move3p,currentPk.move3s,textLine]
    case 4:
      textLine = currentPk.name + " used " + currentPk.move4n
      moveUsed = [currentPk.move4n,currentPk.move4t,currentPk.move4p,currentPk.move4s,textLine]
    case 5:
      moveUsed = []

  return moveUsed

def damageCalculation(moveUsed,currentPk,oppPk):
  moveEff = 1
  moveEff2 = 1
  if oppPk.type1 in typeTable[moveUsed[1]][2]:
    moveEff = 2
  elif oppPk.type1 in typeTable[moveUsed[1]][1]:
    moveEff = 1
  elif oppPk.type1 in typeTable[moveUsed[1]][0.5]:
    moveEff = 0.5
  elif oppPk.type1 in typeTable[moveUsed[1]][0]:
    moveEff = 0

  if oppPk.type2 != "Null":
    if oppPk.type2 in typeTable[moveUsed[1]][2]:
      moveEff2 = 2
    elif oppPk.type2 in typeTable[moveUsed[1]][1]:
      moveEff2 = 1
    elif oppPk.type2 in typeTable[moveUsed[1]][0.5]:
      moveEff2 = 0.5
    elif oppPk.type2 in typeTable[moveUsed[1]][0]:
      moveEff2 = 0

  global overallMoveEff
  overallMoveEff = float(moveEff) * float(moveEff2)
  critical = float(2) if random.randint(1, 96) < 6 else float(1)
  if moveUsed[3] == "s":
    attack = float(currentPk.currentSpAtt)
    defence = float(oppPk.currentSpDef)
  else:
    attack = float(currentPk.currentAtt)
    defence = float(oppPk.currentDef)

  STAB = 1.5 if moveUsed[1] == currentPk.type1 or moveUsed[1] == currentPk.type2 else float(1)

  damageDone = ((((((2*100*critical)/5)+2)*float(moveUsed[2])*(attack/defence))/50)+2)*STAB*overallMoveEff
  ranN = random.randint(75,170) / 235
  if damageDone * ranN == 1:
    damageDone *= 1
  else:
    damageDone *= ranN
  return damageDone

def battleBag(trainer,pkList,currentPk,oppCurrentPk,trainerPkAlive):
  print("You:")
  battleStatsDisplay(currentPk, trainerPkAlive)
  print("\nOpponent:")
  battleStatsDisplay(oppCurrentPk,oppPkAlive)
  animations.battleTurnGraphic(balls,trainer,oppType,"bag",typeTable[currentPk.type1]["c"], typeTable[oppCurrentPk.type1]["c"],None,None,typeTable)

  carryOn = False
  while carryOn is False:
    try:
      battleChoice = int(input("Number >> "))
      if battleChoice > 9:
        print(red+"Input greater than 9"+reset)
      elif battleChoice <= 0:
        print(red+"Input is less than 1"+reset)
      else:
        carryOn = True
    except ValueError:
      print(red + "That is not a number" + reset)
      
  os.system('cls')
  match battleChoice:
    case 1:
      trainerPkAlive = bag.useRevive(trainer,pkList,trainerPkAlive)
      trainer.revive[0] -= 1
    case 2:
      bag.usePotion(trainer,currentPk,"potion",pkList,oppCurrentPk)
      trainer.potion[0] -= 1
    case 3:
      bag.usePotion(trainer,currentPk,"super",pkList,oppCurrentPk)
      trainer.superPotion[0] -= 1
    case 4:
      bag.usePotion(trainer,currentPk,"hyper",pkList,oppCurrentPk)
      trainer.hyperPotion[0] -= 1
    case 5:
      bag.useFullRestore(trainer,currentPk,pkList,oppCurrentPk)
      trainer.fullRestore[0] -= 1
    case 6:
      bag.useStatusHeal(trainer,pkList)#burn
      trainer.burnHeal[0] -= 1
    case 7:
      bag.useStatusHeal(trainer,pkList)#antidote
      trainer.antidote[0] -= 1
    case 8:
      bag.useStatusHeal(trainer,pkList)#paralyse
      trainer.paralyseHeal[0] -= 1
    case 9:
      bag.usePotion(trainer,currentPk,"potion",pkList,oppCurrentPk)
      trainer.oranBerry[0] -= 1
      
  time.sleep(2)
  os.system('cls')
  return trainerPkAlive

def battleFakemon(pkList,oppCurrentPk,statusMovesUsed,currentPk,attemptedEscape,oppName,oppPartyList,trainerPkAlive,oppPkAlive):
  os.system('cls')
  partyPrint(pkList,True,"full",False)
  print("\n"+bold+"7. Back <--")
  switchChoice = 0
  carryOn2 = False
  while carryOn2 is False:
    carryOn = False
    while carryOn is False:
      try:
        switchChoice = int(input("Pick the pokemon you want to switch to (or back) >> "))
        if 0 < switchChoice < 7:
          if pkList[switchChoice-1].name == currentPk.name:
            print(bold + red + "You already have " + currentPk.name + " out!" + reset)
            time.sleep(1)
          else: 
            carryOn = True
        elif switchChoice == 7:
          carryOn = True
          carryOn2 = True
      except ValueError:
        print(red + "Please select a number" + reset)
    if switchChoice == 7:
      os.system('cls')
      battleTurn(currentPk,oppCurrentPk,attemptedEscape,statusMovesUsed,pkList,oppName,trainerPkAlive,oppPkAlive,trainer,oppPartyList)
      return
    os.system('cls')
    if pkList[switchChoice-1].currentHp > 0:
      print("-----------------------------------------------------------------------")
      print(pkList[switchChoice-1].name + " " + typeTable[pkList[switchChoice-1].type1]["hc"] +" "+pkList[switchChoice-1].type1+" "+reset,end=" ",flush=True)
      if pkList[switchChoice-1].type2 != "Null":
        print(" " + typeTable[pkList[switchChoice-1].type2]["hc"] +" "+pkList[switchChoice-1].type2+" "+reset)
      match pkList[switchChoice-1].status:
        case "burned":
          print(" " + red + "Burned")
        case "poisoned":
          print(" " + magenta + "Poisoned")
        case "paralysed":
          print(" " + yellow + "Paralysed")
      print()
      HPPrint(pkList[switchChoice-1],True)
      print("\n")
      list = [
        [pkList[switchChoice-1].move1n,pkList[switchChoice-1].move1t,pkList[switchChoice-1].move1s],
        [pkList[switchChoice-1].move2n,pkList[switchChoice-1].move2t,pkList[switchChoice-1].move2s],
        [pkList[switchChoice-1].move3n,pkList[switchChoice-1].move3t,pkList[switchChoice-1].move3s],
        [pkList[switchChoice-1].move4n,pkList[switchChoice-1].move4t,pkList[switchChoice-1].move4s]]
      print()
      
      longestNameLen = 0
      for j in range(0,len(list)):
        if len(list[j][0]) > longestNameLen:
          longestNameLen = len(list[j][0])

      for i in range(0,4):
        typeSpace = (longestNameLen+2) - len(list[i][0])+2
        moveEffectiveness = 1
        moveEffectiveness2 = 1
        print(list[i][0] + (typeSpace*" ") +typeTable[list[i][1]]["hc"]+" "+list[i][1]+" "+ reset,end="",flush=True)
        if list[i][2] != "st":
          if oppCurrentPk.type1 in typeTable[list[i][1]][2]:
            moveEffectiveness = 2
          elif oppCurrentPk.type1 in typeTable[list[i][1]][1]:
            moveEffectiveness = 1
          elif oppCurrentPk.type1 in typeTable[list[i][1]][0.5]:
            moveEffectiveness = 0.5
          elif oppCurrentPk.type1 in typeTable[list[i][1]][0]:
            moveEffectiveness = 0
  
          if oppCurrentPk.type2 != "Null":
            if oppCurrentPk.type2 in typeTable[list[i][1]][2]:
              moveEffectiveness2 = 2
            elif oppCurrentPk.type2 in typeTable[list[i][1]][1]:
              moveEffectiveness2 = 1
            elif oppCurrentPk.type2 in typeTable[list[i][1]][0.5]:
              moveEffectiveness2 = 0.5
            elif oppCurrentPk.type2 in typeTable[list[i][1]][0]:
              moveEffectiveness2 = 0
  
          overallMoveEffectiveness = float(moveEffectiveness) * float(moveEffectiveness2) #IS FLOAT
  
          match overallMoveEffectiveness:
            case 0:
              print(" (No effect!)",end="",flush=True)
            case 0.5:
              print(" (Not very effective!)",end="",flush=True)
            case 2:
              print(" (Super effective!)",end="",flush=True)
          print(" ")
        else:
          print("(Status move)")
      print("-----------------------------------------------------------------------")

      carryOn3 = False
      while carryOn3 is False:
        try:
          choice = int(input("\033[48;2;89;169;80m"+"1. Confirm "+reset+"\n"+"\033[48;2;235;68;34m"+"2. Back    "+reset+"\n>> "))
          if choice == 2:
            battleFakemon(pkList,oppCurrentPk,statusMovesUsed,currentPk,attemptedEscape,oppName,oppPartyList,trainerPkAlive,oppPkAlive)
            carryOn3 = True
            carryOn2 = True
          else:
            os.system('cls')
            print(bold + "You withdrew " + currentPk.name)
            time.sleep(2)
            os.system('cls')
            if oppType == "wild":
              animations.wildTrainerWithdraw(typeTable[currentPk.type1]["c"],typeTable[oppCurrentPk.type1]["c"],battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
            else:
              animations.trainerWithdraw(typeTable[currentPk.type1]["c"],typeTable[oppCurrentPk.type1]["c"],battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
            if oppCurrentPk.currentHp > 0.75 * oppCurrentPk.currentHp:
              print(pkList[switchChoice-1].name + "...I choose you!" + reset)
            elif oppCurrentPk.currentHp > 0.50 * oppCurrentPk.currentHp:
              print("You sent out " + pkList[switchChoice-1] + reset)
            elif oppCurrentPk.currentHp > 0.25 * oppCurrentPk.currentHp:
              print("Not too much longer, " + pkList[switchChoice-1] + reset)
            else:
              print(pkList[switchChoice-1].name + "...FINISH THEM!"+reset)
            time.sleep(2)
            os.system('cls')
            if oppType == "wild":
              animations.wildBattleInitialGraphic(typeTable[pkList[switchChoice-1].type1]["c"],typeTable[oppCurrentPk.type1]["c"],battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]],True)
            else:
              animations.trainerSendOut(typeTable[pkList[switchChoice-1].type1]["c"],typeTable[oppCurrentPk.type1]["c"],battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
            if choice == 1:
              currentPk = pkList[switchChoice-1]
              carryOn3 = True
              carryOn2 = True
        except ValueError:
          print(red + "Please enter a number" + reset)
  return currentPk

def cpuBattle(oppCurrentPk,currentPk,statusMovesUsed,trainerPkAlive,oppPkAlive):
  cpuMoveList = [
    [oppCurrentPk.move1n,oppCurrentPk.move1t,oppCurrentPk.move1p,oppCurrentPk.move1s,""],
    [oppCurrentPk.move2n,oppCurrentPk.move2t,oppCurrentPk.move2p,oppCurrentPk.move2s,""],
    [oppCurrentPk.move3n,oppCurrentPk.move3t,oppCurrentPk.move3p,oppCurrentPk.move3s,""],
    [oppCurrentPk.move4n,oppCurrentPk.move4t,oppCurrentPk.move4p,oppCurrentPk.move4s,""]]

  num = random.randint(1,10)
  for i in range(3,-1,-1):
    if "st" in cpuMoveList:
      if num < 3 - statusMovesUsed and cpuMoveList[i][3] != "st":
        cpuMoveList.pop(i)
        statusMovesUsed += 1
      elif num > 3 - statusMovesUsed and cpuMoveList[i][3] == "st":
        cpuMoveList.pop(i)
  cpuMoveUsed = random.sample(cpuMoveList,1)
  cpuMoveUsed[0][4] = oppCurrentPk.name + " used " + cpuMoveUsed[0][0]

  pkCol1 = typeTable[currentPk.type1]["c"]
  pkCol2 = typeTable[oppCurrentPk.type1]["c"]
  os.system('cls')
  print(bold+"You:"+reset)
  battleStatsDisplay(currentPk, trainerPkAlive)
  print()
  print(bold+"Opponent:"+reset)
  battleStatsDisplay(oppCurrentPk, oppPkAlive)
  animations.battleTurnGraphic(balls,trainer,oppType,None,typeTable[currentPk.type1]["c"], typeTable[oppCurrentPk.type1]["c"],None,None,typeTable)
  print()
  print(bold + cpuMoveUsed[0][4] + reset)
  time.sleep(1.5)
  os.system('cls')

  if cpuMoveUsed[0][3] == "st": #status move or not
    if int(cpuMoveUsed[0][2]) < -5 and int(cpuMoveUsed[0][2]) > 0: #self or not
      if oppType == "wild":
        animations.wildStatus("self",pkCol1,pkCol2,battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
      else:
        animations.status("self",pkCol1,pkCol2,battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
    else:
      if oppType == "wild":
        animations.wildStatus("self",pkCol1,pkCol2,battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
      else:
        animations.status("opp",pkCol1,pkCol2,battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
    print(bold+"You:"+reset)
    battleStatsDisplay(currentPk, trainerPkAlive)
    print()
    print(bold+"Opponent:"+reset)
    battleStatsDisplay(oppCurrentPk, oppPkAlive)
    animations.battleTurnGraphic(balls,trainer,oppType,None,typeTable[currentPk.type1]["c"], typeTable[oppCurrentPk.type1]["c"],None,None,typeTable)
    pokemon.assignStatus(oppCurrentPk,cpuMoveUsed[0][2],currentPk)
    print(reset)
  else:
    if oppType == "wild":
      animations.wildOppAttack(pkCol1,pkCol2,typeTable[cpuMoveUsed[0][1]]["c"],battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
    else:
      animations.oppAttack(pkCol1,pkCol2,typeTable[cpuMoveUsed[0][1]]["c"],battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
    time.sleep(0.2)
    damageDone = damageCalculation(cpuMoveUsed[0],oppCurrentPk,currentPk)
    pokemon.damageDealt(currentPk,damageDone,oppCurrentPk,trainerPkAlive,oppPkAlive,"opp",battleStatsDisplay)

def cpuSwitch(currentPk,oppCurrentPk,oppName,oppPartyList):
  time.sleep(0.3)
  print(bold + oppName + " withdrew " + oppCurrentPk.name + reset)
  time.sleep(2)
  os.system('cls')
  animations.oppTrainerWithdraw(typeTable[currentPk.type1]["c"],typeTable[oppCurrentPk.type1]["c"],battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
  valid = False
  while valid is False:
    num = random.randint(1,len(oppPartyList))
    if oppPartyList[num-1].name == oppCurrentPk.name and oppPartyList[num-1].currentHp > 0:
      oppCurrentPk = oppPartyList[num-1]
      valid = True
      animations.oppTrainerSendOut(typeTable[currentPk.type1]["c"],typeTable[oppCurrentPk.type1]["c"],battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]])
  return oppCurrentPk

def battleCatch(currentPk,oppCurrentPk,trainer,pkList,numTurns):
  os.system('cls')
  ballList = [trainer.pokeball,trainer.greatball,trainer.ultraball,
            trainer.quickball,trainer.masterball,trainer.netball,
            trainer.diveball,trainer.timerball,trainer.fastball]
  
  print("You:")
  battleStatsDisplay(currentPk, trainerPkAlive)
  print("\nOpponent:")
  battleStatsDisplay(oppCurrentPk,oppPkAlive)
  animations.battleTurnGraphic(balls,trainer,oppType,"catch",typeTable[currentPk.type1]["c"], typeTable[oppCurrentPk.type1]["c"],None,None,typeTable)
  
  carryOn = False
  while carryOn is False:
    ballChoice = input("\nNumber >> ")
    try:
      if "i" in ballChoice:
        ballChoice = int(ballChoice[0])
        ballInformation(ballList[ballChoice-1][1])
      elif int(ballChoice) <= 5 and int(ballChoice) > 0:
        carryOn = True
        ballChoice = int(ballChoice)
      elif int(ballChoice) > 9:
        print(red+"Your input is greater than 9"+reset)
      elif int(ballChoice) < 1:
        print(red+"Your input is less than 1"+reset)
    except ValueError:
      print(red+"Only the letter i can be used"+reset)

  ballList[ballChoice-1][0] -= 1
  os.system('cls')
  ballMultiplier = balls[ballList[ballChoice-1][1]][0]
  if ballList[ballChoice-1][1] == "quick ball":
    match numTurns:
      case 1:
        ballMultiplier = 5
      case 2:
        ballMultiplier = 4
      case 3:
        ballMultiplier = 3
  elif ballList[ballChoice-1][1] == "net ball" and (oppCurrentPk.type1 == "Bug" or oppCurrentPk.type2 == "Bug"):
    ballMultiplier = 3.5
  elif ballList[ballChoice-1][1] == "dive ball" and (oppCurrentPk.type1 == "Water" or oppCurrentPk.type2 == "Water"):
    ballMultiplier = 3.5
  elif ballList[ballChoice-1][1] == "timer ball": #if turns 5 x1.5,7 = x2,10 = x3
    if 5 <= numTurns < 7:
      ballMultiplier = 1.5
    elif 7 <= numTurns < 10:
      ballMultiplier = 2
    elif 10 <= numTurns < 20:
      ballMultiplier = 3
    elif 20 <= numTurns:
      ballMultiplier = 5
  elif ballList[ballChoice-1][1] == "fast ball" and oppCurrentPk.speed > 100:
    ballMultiplier = 4
  
  rolls = battleCatchEquation(pokemon.getHP(currentPk),currentPk.currentHp,ballMultiplier,currentPk.status)
  animations.pokemonCatch(typeTable[currentPk.type1]["c"],typeTable[oppCurrentPk.type1]["c"],rolls,battleStatsDisplay,[[currentPk,trainerPkAlive],[oppCurrentPk,oppPkAlive]],balls[ballList[ballChoice-1][1]][1])
  time.sleep(0.75)

  if rolls == 2:
    print("Aww! It was so close")
    os.system('cls')
    return False

  elif rolls == 1:
    print("The fakémon broke free!")
    os.system('cls')
    return False
  
  elif rolls == 0:
    print("The fakémon broke free!")
    os.system('cls')
    return False

  elif rolls == 3:    
    print("One...",end="",flush=True)
    time.sleep(0.5)
    print("Two...",end="",flush=True)
    time.sleep(0.5)
    print("And TA DA!")
    time.sleep(1)
    print("You caught "+oppCurrentPk.name+"!")
    time.sleep(3)
  
    pokemon.resetHP(oppCurrentPk)
    pokemon.resetStats(oppCurrentPk)

    carryOn3 = False
    while carryOn3 is False:
      os.system('cls')
      printingList = [oppCurrentPk]
      print("-----------------------------------------------------------------------")
      partyPrint(printingList,False,"full",False)
    
      carryOn = False
      while carryOn is False:
        try:
          swapCheck = int(input("\n1. Swap with existing fakémon in party\n2. Release into the wild\n>> "))
          if swapCheck == 2: #release pokemon
            carryOn = True
            carryOn3 = True
            os.system('cls')
            time.sleep(1)
            os.system('cls')
          elif swapCheck == 1: #swap pokemon
            carryOn = True
            carryOn3 = True
            os.system('cls')
          else: #neither
            print(red+"\nNumber is not 1 or 2"+reset)

        except ValueError:
          print(red+"\nPlease enter a number"+reset)

      if swapCheck == 1:
        print("-----------------------------------------------------------------------")
        partyPrint(pkList,False,"full",False)
        carryOn = False
        while carryOn is False:
          try:
            swapChoice = int(input("\nEnter the number of the pokemon you would like to swap out >> "))
            if swapChoice > 6:
              print(red+"Your input is greater than 6"+reset)
            elif swapChoice < 1:
              print(red+"Your input is less than 1"+reset)
            else:
              carryOn = True
              carryOn3 = True
          except ValueError:
            print(red+"\nPlease enter a number"+reset)
        pkList[swapChoice-1] = oppCurrentPk
        os.system('cls')
        print("You changed your team")
        time.sleep(3)
    
      else:
        print(bold+"You released "+oppCurrentPk.name+reset)
        carryOn3 = True

      os.system('cls')
      return True

def battleCatchEquation(maxHp,currentHp,ballMultiplier,status):
  statusMultiplier = 1.5 if status is None else 1
  captureRate = (( 1 + ( maxHp * 3 - currentHp * 2 ) * 50 * ballMultiplier * statusMultiplier ) / ( maxHp * 3 )) / 256
  breakOutChance = random.randint(0,100)/100
  breakOutThreshold = 1 - captureRate
  if captureRate > breakOutChance:
    rolls = 3
  elif breakOutChance > captureRate + 0.33*breakOutThreshold:
    rolls = 2
  elif breakOutChance > captureRate + 0.66*breakOutThreshold:
    rolls = 1
  else:
    rolls = 0

  return rolls

def ballInformation(ballType):
  print(balls[ballType][1]+ballType.upper()+reset+": ",end="",flush=True)
  match ballType:
    case "pokeball":
      print("A device for catching wild pokémon, the most standard type")
    case "great ball":
      print("A good, high perforamance pokeball that provides a higher success rate for catching pokémon than a standard pokeball")
    case "ultra ball":
      print("An ultra high performance pokeball that provides a higher success rate for catching pokémon than a great ball")
    case "quick ball":
      print("A somewhat different poke ball that is more effective at catching pokémon when used first thing in battle")
    case "master ball":
      print("The very best poke ball with the ultimate level of performance. With it, you will catch any pokémon without fail")
    case "net ball":
      print("A somewhat different poke ball that is more effective when catching bug-type pokémon")
    case "dive ball":
      print("A somewhat different pokéball that is more effective when catching water-type pokémon")
    case "timer ball":
      print("A somewhat different poke ball that becomes more effective at catching pokémon the more turns that are taken in battle")
    case "fast ball":
      print("A somewhat different poke ball that is more effective when catching pokémon that have a high speed stat")

if __name__ == '__main__':
  main(False)