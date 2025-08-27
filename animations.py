import os
import time
import math

black = "\033[0;30m"
red = "\033[38;2;241;54;35m"
green = "\033[0;32m"
yellow = "\033[38;2;217;177;56m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m" #text colours
white = "\033[0;37m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[38;2;175;143;233m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"

bold = "\u001b[1m"
reset = "\u001b[0m"

def battleTurnGraphic(balls,trainer,graphicType,textType,pk1Col,pk2Col,currentPk,oppCurrentPk,typeTable):
  if graphicType == "trainer":
    print(reset + r"""




             o                                                    o
            /|\                                                  /|\
            / \   """ + pk1Col + """   ██                                """ + pk2Col + """  ██  """ + reset + """    / \\
  --------------------------------------------------------------------------
    """)
  else:
    print(reset + r"""




            o
           /|\
           / \   """ + pk1Col + """   ██                                """ + pk2Col + """  ██  """ + reset + """
  --------------------------------------------------------------------------
    """)

  if textType == "selection":
    print(r"""          """+"\033[48;2;241;54;35m"+""" 1. Battle """+reset+"""  """+"\033[48;2;217;177;56m"+""" 2. Bag """+reset+"""  """+"\033[48;2;89;169;80m"+""" 3. Fakémon """+reset+"""  """+"\033[48;2;100;136;234m"+""" 4. Run """+reset+"""  """+"\033[48;2;174;55;255m"+""" 5. Catch """+reset+"""
  """)

  elif textType == "attack":
    list = [[currentPk.move1n,currentPk.move1t,currentPk.move1s],
            [currentPk.move2n,currentPk.move2t,currentPk.move2s],
            [currentPk.move3n,currentPk.move3t,currentPk.move3s],
            [currentPk.move4n,currentPk.move4t,currentPk.move4s]
          ]
    print()

    longestNameLen = 0
    for j in range(0,len(list)):
      if len(list[j][0]) > longestNameLen:
        longestNameLen = len(list[j][0])

    for i in range(0,4):
      typeSpace = (longestNameLen+2) - len(list[i][0])+2
      moveEffectiveness = 1
      moveEffectiveness2 = 1
      print(reset + 4*" " + str(i+1) + ". " + list[i][0]+(typeSpace*" ")+typeTable[list[i][1]]["hc"]+" "+list[i][1]+" "+ reset + " ",end="",flush=True)
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
            print("(No effect!)",end="",flush=True)
          case 0.5:
            print("(Not very effective!)",end="",flush=True)
          case 2:
            print("(Super effective!)",end="",flush=True)
        print(" ")
      else:
        print("(Status move)")
    print("    5. Back <--")
    print("\n<Type 'i' followed by the number (no spaces) for information about the move>")
    del list

  elif textType == "catch":
    list = [trainer.pokeball,trainer.greatball,trainer.ultraball,
            trainer.quickball,trainer.masterball,trainer.netball,
            trainer.diveball,trainer.timerball,trainer.fastball]

    for k in range(0,len(list)):
      print(str(k+1)+". "+balls[list[k][1]][1]+"●"+reset+" "+list[k][1]+" ("+str(list[k][0])+")")
    print("<-- back")
    print("\n<Type 'i' followed by the number (no spaces) for information about the pokeball>")
    
  elif textType == "bag":
    itemList = [trainer.revive,trainer.potion,trainer.superPotion,
              trainer.hyperPotion,trainer.fullRestore,trainer.burnHeal,
              trainer.antidote,trainer.paralyseHeal,trainer.oranBerry]
    
    #if oran berry, circle; if potion, rectangle; if revive, diamond ⧫ ● ▮
    for l in range(0,len(itemList)):
      print(str(l+1)+". ",end="",flush=True)
      if itemList[l][1] == "oran berry":
        print(blue+"●"+reset+" Oran Berry <"+green+"+30hp"+reset+"> (",end="",flush=True)
      elif itemList[l][1] == "revive":
        print(yellow+"⧫"+reset+" Revive (",end="",flush=True)
      elif itemList[l][1] == "potion":
        print("\033[38;2;216;70;236m"+"▮"+reset+" Potion <"+green+"+60hp"+reset+"> (",end="",flush=True)
      elif itemList[l][1] == "super potion":
        print("\033[38;2;255;126;63m"+"▮"+reset+" Super potion <"+green+"+120hp"+reset+"> (",end="",flush=True)
      elif itemList[l][1] == "hyper potion":
        print("\033[38;2;245;200;208m"+"▮"+reset+" Hyper potion <"+green+"+200hp"+reset+"> (",end="",flush=True)
      elif itemList[l][1] == "full restore":
        print("\033[38;2;128;218;99m"+"▮"+reset+" Full restore <"+green+"Full hp + status reset"+reset+"> (",end="",flush=True)
      elif itemList[l][1] == "burn heal":
        print("\033[38;2;108;188;103m"+"▮"+reset+" Burn heal (",end="",flush=True)
      elif itemList[l][1] == "antidote":
        print("\033[38;2;233;186;65m"+"▮"+reset+" Antidote (",end="",flush=True)
      elif itemList[l][1] == "paralyse heal":
        print("\033[38;2;216;212;86m"+"▮"+reset+" Paralyse heal (",end="",flush=True)
       
      print(str(itemList[l][0])+")")
######################################################################
def longGrass(points):
  spaces = "\n\n\n\n\n\n\n\n\n\n\n\n"
  if points > 1:
    print("You are on " + str(points) + " points")
  elif points == 1:
    print("You are on 1 point")
  print(spaces)
  print(green + r"""
                               @@@@                                       @@
                              @@@@~@                                     @@@
                             @@@~@@@@                                   @@@~
                              @@@@@@@                                    @@@"""+reset+"""
     o                         """+green+"""@@_@                                       @@"""+reset+"""
    /|\                         ||                         """+green+"""@@              """+reset+"""|
    / \                        _||_                       """+green+"""@@@@            """+reset+"""_|"""+reset+"""
  --------------------------------------------------------------------------
  """)
  time.sleep(0.7)
  os.system('cls') #23, 13
  if points > 1:
    print("You are on " + str(points) + " points")
  elif points == 1:
    print("You are on 1 point")
  print(spaces)
  print(green + r"""
                      @@@@                                        @@@@
                     @@@@~@                                      @@@@~@
                    @@@~@@@@                                    @@@~@@@@
                     @@@@@@@                                     @@@@@@@"""+reset+"""
             o        """+green+"""@@_@                                        @@_@"""+reset+"""
            /|\        ||                         """+green+"""@@               """+reset+"""||
            / \       _||_                       """+green+"""@@@@             """+reset+"""_||_"""+reset+"""
  --------------------------------------------------------------------------
  """)
  time.sleep(0.7)
  os.system('cls')
  if points > 1:
    print("You are on " + str(points) + " points")
  elif points == 1:
    print("You are on 1 point")
  print(spaces)
  print(green + r"""
             @@@@                                        @@@@
            @@@@~@                                      @@@@~@
           @@@~@@@@                                    @@@~@@@@
            @@@@@@@                                     @@@@@@@
             @@_@         """+reset+"""o                              """+green+"""@@_@"""+reset+"""
              ||         /|\             """+green+"""@@               """+reset+"""||           """+green+"""@@@ @"""+reset+"""
             _||_        / \            """+green+"""@@@@             """+reset+"""_||_         """+green+"""@@@@@@"""+reset+"""
  --------------------------------------------------------------------------
  """)
  time.sleep(0.7)
  os.system('cls')
  if points > 1:
    print("You are on " + str(points) + " points")
  elif points == 1:
    print("You are on 1 point")
  print(spaces)
  print(green + r"""
    @@@@                                        @@@@
   @@@@~@                                      @@@@~@
  @@@~@@@@                                    @@@~@@@@
   @@@@@@@                                     @@@@@@@
    @@_@                          """+reset+"""o             """+green+"""@@_@            @@"""+reset+"""
     ||                         """+green+"""@@"""+reset+"""|\             ||      """+green+"""@@@  @@@@@@"""+reset+"""
    _||_                       """+green+"""@@@@"""+reset+"""\            """+reset+"""_||_    """+green+"""@@@@@@@@@@@@@@@"""+reset+"""
  --------------------------------------------------------------------------
  """)
  time.sleep(1.2)
  os.system('cls')
  if points > 1:
    print("You are on " + str(points) + " points")
  elif points == 1:
    print("You are on 1 point")
  print(spaces)
  print(green + r"""
    @@@@                                        @@@@
   @@@@~@                                      @@@@~@
  @@@~@@@@                                    @@@~@@@@
   @@@@@@@                       """+red+"""!!!           """+green+"""@@@@@@@
    @@_@                         """+reset+"""\o/            """+green+"""@@_@            @@"""+reset+"""
     ||                         """+green+"""@@"""+reset+"""|              ||      """+green+"""@@@  @@@@@@"""+reset+"""
    _||_                       """+green+"""@@@@"""+reset+"""\            """+reset+"""_||_    """+green+"""@@@@@@@@@@@@@@@"""+reset+"""
  --------------------------------------------------------------------------
  """ + reset)
  time.sleep(0.7)
  os.system('cls')
######################################################################
def youAttack(pk1Col,pk2Col,moveTypeCol,BSD,parameters): #16 spaces
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




            o                                                    o
           /|7                                                  /|\
           / \   """ + pk1Col + """   ██                              """ + pk2Col + """    ██   """ + reset + """   / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.05)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




            o__                                                  o
           /|                                                   /|\
           / \    """ + pk1Col + """  ██                              """ + pk2Col + """    ██   """ + reset + """   / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.35)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




            o__                                                  o
           /|                                                   /|\
           / \    """ + pk1Col + """  ██""" + moveTypeCol + """-●                        """ + pk2Col + """        ██   """ + reset + """   / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




            o__                                                  o
           /|                                                   /|\
           / \     """ + pk1Col + """ ██""" + moveTypeCol + """       --●               """ + pk2Col + """         ██   """ + reset + """   / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




            o__                                                  o
           /|                                                   /|\
           / \   """ + pk1Col + """   ██""" + moveTypeCol + """               --●        """ + pk2Col + """        ██   """ + reset + """   / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




            o__                                                  o
           /|                                                   /|\
           / \   """ + pk1Col + """   ██""" + moveTypeCol + """                       --●     """ + pk2Col + """   ██   """ + reset + """   / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




            o__                                                  o
           /|                                                   /|\
           / \   """ + pk1Col + """   ██""" + moveTypeCol + """                                 -""" + pk2Col + """██   """ + reset + """   / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




            o__                                                  o
           /|                                                   /|\
           / \   """ + pk1Col + """   ██                          """ + red + """        ██   """ + reset + """   / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




            o__                                                  o
           /|                                                   /|\
           / \   """ + pk1Col + """   ██                           """ + pk2Col + """       ██   """ + reset + """   / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




            o                                                    o
           /|\                                                  /|\
           / \   """ + pk1Col + """   ██                           """ + pk2Col + """       ██   """ + reset + """   / \\
  --------------------------------------------------------------------------
  """)
######################################################################
def oppAttack(pk1Col, pk2Col, moveTypeCol,BSD,parameters): #""" + reset + """, """ + pk1Col + """, """ + pk2Col + """, """ + moveTypeCol + """
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




            o                                                    o
           /|\                                                  <|\
           / \   """ + pk1Col + """   ██                               """ + pk2Col + """   ██   """ + reset + """   / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




            o                                                  __o
           /|\                                                   |\
           / \   """ + pk1Col + """   ██                               """ + pk2Col + """   ██   """ + reset + """   / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




            o                                                  __o
           /|\                                                   |\
           / \   """ + pk1Col + """   ██                             """ + moveTypeCol + """   ●-""" + pk2Col + """██   """ + reset + """   / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.35)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




            o                                                  __o
           /|\                                                   |\
           / \   """ + pk1Col + """   ██                    """ + moveTypeCol + """   ●--     """ + pk2Col + """   ██   """ + reset + """   / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




            o                                                  __o
           /|\                                                   |\
           / \   """ + pk1Col + """   ██            """ + moveTypeCol + """   ●--             """ + pk2Col + """   ██   """ + reset + """   / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




            o                                                  __o
           /|\                                                   |\
           / \   """ + pk1Col + """   ██    """ + moveTypeCol + """   ●--                     """ + pk2Col + """   ██   """ + reset + """   / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




            o                                                  __o
           /|\                                                   |\
           / \   """ + pk1Col + """   ██""" + moveTypeCol + """-                              """ + pk2Col + """   ██   """ + reset + """   / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




            o                                                  __o
           /|\                                                   |\
           / \   """ + red + """   ██                               """ + pk2Col + """   ██   """ + reset + """   / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




            o                                                  __o
           /|\                                                   |\
           / \   """ + pk1Col + """   ██                               """ + pk2Col + """   ██   """ + reset + """   / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




            o                                                    o
           /|\                                                  /|\
           / \   """ + pk1Col + """   ██                               """ + pk2Col + """   ██   """ + reset + """   / \\
  --------------------------------------------------------------------------
  """)
######################################################################
def status(affected,pk1Col, pk2Col,BSD,parameters):
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""



  
            o                                                    o
           /|\                                                  /|\
           / \   """ + pk1Col + """   ██                                """ + pk2Col + """  ██  """ + reset + """    / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.5)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  if affected == "self":
    if pk1Col != blue:
      print(reset + r"""



      
             o                                                    o
            /|\                                                  /|\
            / \   """ + blue + """    ██                                """ + pk2Col + """  ██  """ + reset + """    / \\
  --------------------------------------------------------------------------
    """)
    else:
      print(reset + r"""



      
             o                                                    o
            /|\                                                  /|\
            / \   """ + yellow + """    ██                                """ + pk2Col + """  ██  """ + reset + """    / \\
  --------------------------------------------------------------------------
      """)
  else:
    if pk2Col != blue:
      print(reset + r"""



      
             o                                                    o
            /|\                                                  /|\
            / \   """ + pk1Col + """    ██                                """ + blue + """  ██  """ + reset + """    / \\
  --------------------------------------------------------------------------
    """)
    else:
      print(reset + r"""



      
             o                                                    o
            /|\                                                  /|\
            / \   """ + pk1Col + """    ██                                """ + yellow + """  ██  """ + reset + """    / \\
  --------------------------------------------------------------------------
      """)
  time.sleep(0.5)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""



  
            o                                                    o
           /|\                                                  /|\
           / \   """ + pk1Col + """   ██                                """ + pk2Col + """  ██  """ + reset + """    / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.5)
  os.system('cls')
######################################################################
def battleInitialGraphic(pk1Col,pk2Col):
  spaces = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
  spacesmo = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
  print(spaces)
  print(r"""

            o                                                    o
           /|\                                                  /|\
           / \                                                  / \
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  print(spaces)
  print(r"""

            o__"""+red+"""●                                              ●"""+reset+"""__o
           /|                                                    |\\
           / \\                                                  / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.5)
  os.system('cls')
  print(spaces)
  print(r"""

            o                                                    o
           /|\ """+red+"""●                                              ● """+reset+"""/|\\
           / \\                                                  / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  print(spaces)
  print(r"""
                """+red+"""●                                             ●"""+reset+"""
            o/                                                  \o
           /|                                                    |\\
           / \\                                                  / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  print(spacesmo)
  print(r"""
                    """+bright_blue+"""●                                     ●"""+reset+"""

            o/                                                  \o
           /|                                                    |\\
           / \\                                                  / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  print(spacesmo)
  print(r"""
                    """+bright_blue+"""*                                     *"""+reset+"""

            o/                                                  \o
           /|                                                    |\\
           / \\                                                  / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  print(spacesmo)
  print(r"""
                    """+bright_blue+"""*                                    *
                    **                                  **"""+reset+"""
            o__     """+bright_blue+"""**                                  **"""+reset+"""     __o
           /|                                                    |\\
           / \\                                                  / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  print(spaces)
  print(r"""
                    """+bright_blue+"""*                                    *"""+reset+"""
            o__     """+bright_blue+"""**                                  **"""+reset+"""     __o
           /|       """+bright_blue+"""**                                  **"""+reset+"""       |\\
           / \\      """+bright_blue+"""**                                  **"""+reset+"""      / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  print(spaces)
  print(r"""

            o                                                    o
           /|\      """+bright_blue+"""**                                  **"""+reset+"""      /|\\
           / \\      """+bright_blue+"""**                                  **"""+reset+"""      / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  print(spaces)
  print(r"""

            o                                                    o
           /|\                                                  /|\
           / \      """+bright_blue+"""██                                  ██"""+reset+"""      / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.06)
  os.system('cls')
  print(spaces)
  print(r"""

            o                                                    o
           /|\                                                  /|\
           / \\      """+pk1Col+"""██                                  """+pk2Col+"""██"""+reset+"""      / \\
  --------------------------------------------------------------------------
  """)
######################################################################
def wildOppAttack(pk1Col, pk2Col, moveTypeCol,BSD,parameters):
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




            o
           /|\
           / \   """ + pk1Col + """   ██                               """ + pk2Col + """   ██   """ + reset + """
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




            o
           /|\
           / \   """ + pk1Col + """   ██                             """ + moveTypeCol + """   ●-""" + pk2Col + """██   """ + reset + """
  --------------------------------------------------------------------------
  """)
  time.sleep(0.35)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




            o
           /|\
           / \   """ + pk1Col + """   ██                    """ + moveTypeCol + """   ●--     """ + pk2Col + """   ██   """ + reset + """
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




            o
           /|\
           / \   """ + pk1Col + """   ██            """ + moveTypeCol + """   ●--             """ + pk2Col + """   ██   """ + reset + """
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




            o
           /|\
           / \   """ + pk1Col + """   ██    """ + moveTypeCol + """   ●--                     """ + pk2Col + """   ██   """ + reset + """
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




            o
           /|\
           / \   """ + pk1Col + """   ██""" + moveTypeCol + """-                              """ + pk2Col + """   ██   """ + reset + """
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




            o
           /|\
           / \   """ + red + """   ██                               """ + pk2Col + """   ██   """ + reset + """
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




            o
           /|\
           / \   """ + pk1Col + """   ██                               """ + pk2Col + """   ██   """ + reset + """
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




            o
           /|\
           / \   """ + pk1Col + """   ██                               """ + pk2Col + """   ██   """ + reset + """
  --------------------------------------------------------------------------
  """)
######################################################################
def wildYouAttack(pk1Col, pk2Col, moveTypeCol,BSD,parameters):
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




            o
           /|7
           / \   """ + pk1Col + """   ██                              """ + pk2Col + """    ██   """ + reset + """
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




            o__
           /|
           / \    """ + pk1Col + """  ██                              """ + pk2Col + """    ██   """ + reset + """
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




            o__
           /|
           / \    """ + pk1Col + """  ██""" + moveTypeCol + """-●                        """ + pk2Col + """        ██   """ + reset + """
  --------------------------------------------------------------------------
  """)
  time.sleep(0.35)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




            o__
           /|
           / \     """ + pk1Col + """ ██""" + moveTypeCol + """       --●               """ + pk2Col + """         ██   """ + reset + """
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




            o__
           /|
           / \   """ + pk1Col + """   ██""" + moveTypeCol + """               --●        """ + pk2Col + """        ██   """ + reset + """
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




            o__
           /|
           / \   """ + pk1Col + """   ██""" + moveTypeCol + """                       --●     """ + pk2Col + """   ██   """ + reset + """
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




            o__
           /|
           / \   """ + pk1Col + """   ██""" + moveTypeCol + """                                 -""" + pk2Col + """██   """ + reset + """
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




            o__
           /|
           / \   """ + pk1Col + """   ██                          """ + red + """        ██   """ + reset + """
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




            o__
           /|
           / \   """ + pk1Col + """   ██                           """ + pk2Col + """       ██   """ + reset + """
  --------------------------------------------------------------------------
  """)
  time.sleep(0.2)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




            o
           /|\
           / \   """ + pk1Col + """   ██                           """ + pk2Col + """       ██   """ + reset + """
  --------------------------------------------------------------------------
  """)
######################################################################
def wildStatus(affected,pk1Col,pk2Col,BSD,parameters):
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""



  
            o
           /|\
           / \   """ + pk1Col + """   ██                                """ + pk2Col + """  ██  """ + reset + """
  --------------------------------------------------------------------------
  """)
  time.sleep(0.5)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  if affected == "self":
    if pk1Col != blue:
      print(reset + r"""



      
             o
            /|\
            / \   """ + blue + """    ██                                """ + pk2Col + """  ██  """ + reset + """
  --------------------------------------------------------------------------
    """)
    else:
      print(reset + r"""



      
             o
            /|\
            / \   """ + yellow + """    ██                                """ + pk2Col + """  ██  """ + reset + """
  --------------------------------------------------------------------------
      """)
  else:
    if pk2Col != blue:
      print(reset + r"""



      
             o
            /|\
            / \   """ + pk1Col + """    ██                                """ + blue + """  ██  """ + reset + """
  --------------------------------------------------------------------------
    """)
    else:
      print(reset + r"""



      
             o
            /|\
            / \   """ + pk1Col + """    ██                                """ + yellow + """  ██  """ + reset + """
  --------------------------------------------------------------------------
      """)
  time.sleep(0.5)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""



  
            o
           /|\
           / \   """ + pk1Col + """   ██                                """ + pk2Col + """  ██  """ + reset + """
  --------------------------------------------------------------------------
  """)
  time.sleep(0.5)
  os.system('cls')
######################################################################
def wildBattleInitialGraphic(pk1Col,pk2Col,BSD,parameters,check):
  spaces = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
  spacesmo = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
  if check is True:
    BSD(parameters[0][0],parameters[0][1])
    print()
    BSD(parameters[1][0],parameters[1][1])
  else:
    print(spaces)
  print(r"""

            o
           /|\
           / \\"""+pk2Col+"""                                          ██"""+reset+"""
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  if check is True:
    BSD(parameters[0][0],parameters[0][1])
    print()
    BSD(parameters[1][0],parameters[1][1])
  else:
    print(spaces)
  print(r"""

            o__"""+red+"""●"""+reset+"""
           /|
           / \\"""+pk2Col+"""                                          ██"""+reset+"""
  --------------------------------------------------------------------------
  """)
  time.sleep(0.5)
  os.system('cls')
  if check is True:
    BSD(parameters[0][0],parameters[0][1])
    print()
    BSD(parameters[1][0],parameters[1][1])
  else:
    print(spaces)
  print(r"""

            o
           /|\ """+red+"""●"""+reset+"""
           / \\"""+pk2Col+"""                                          ██"""+reset+"""
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  if check is True:
    BSD(parameters[0][0],parameters[0][1])
    print()
    BSD(parameters[1][0],parameters[1][1])
  else:
    print(spaces)
  print(r"""
                """+red+"""●"""+reset+"""
            o/
           /|
           / \\"""+pk2Col+"""                                          ██"""+reset+"""
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  if check is True:
    BSD(parameters[0][0],parameters[0][1])
    print()
    BSD(parameters[1][0],parameters[1][1])
  else:
    print(spacesmo)
  print(r"""
                    """+bright_blue+"""●"""+reset+"""

            o/
           /|
           / \\"""+pk2Col+"""                                          ██"""+reset+"""
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  if check is True:
    BSD(parameters[0][0],parameters[0][1])
    print()
    BSD(parameters[1][0],parameters[1][1])
  else:
    print(spacesmo)
  print(r"""
                    """+bright_blue+"""*"""+reset+"""

            o/
           /|
           / \\"""+pk2Col+"""                                          ██"""+reset+"""
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  if check is True:
    BSD(parameters[0][0],parameters[0][1])
    print()
    BSD(parameters[1][0],parameters[1][1])
  else:
    print(spacesmo)
  print(r"""
                    """+bright_blue+"""*
                    **"""+reset+"""
            o__     """+bright_blue+"""**"""+reset+"""
           /|
           / \\"""+pk2Col+"""                                          ██"""+reset+"""
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  if check is True:
    BSD(parameters[0][0],parameters[0][1])
    print()
    BSD(parameters[1][0],parameters[1][1])
  else:
    print(spaces)
  print(r"""
                    """+bright_blue+"""*"""+reset+"""
            o__     """+bright_blue+"""**"""+reset+"""
           /|       """+bright_blue+"""**"""+reset+"""
           / \\      """+bright_blue+"""**"""+pk2Col+"""                                  ██"""+reset+"""
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  if check is True:
    BSD(parameters[0][0],parameters[0][1])
    print()
    BSD(parameters[1][0],parameters[1][1])
  else:
    print(spaces)
  print(r"""

            o
           /|\      """+bright_blue+"""**"""+reset+"""
           / \\      """+bright_blue+"""**"""+pk2Col+"""                                  ██"""+reset+"""
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  if check is True:
    BSD(parameters[0][0],parameters[0][1])
    print()
    BSD(parameters[1][0],parameters[1][1])
  else:
    print(spaces)
  print(r"""

            o
           /|\
           / \      """+bright_blue+"""██                                  """+pk2Col+"""██"""+reset+"""
  --------------------------------------------------------------------------
  """)
  time.sleep(0.25)
  os.system('cls')
  if check is True:
    BSD(parameters[0][0],parameters[0][1])
    print()
    BSD(parameters[1][0],parameters[1][1])
  else:
    print(spaces)
  print(r"""

            o
           /|\
           / \\      """+pk1Col+"""██                                  """+pk2Col+"""██"""+reset+"""
  --------------------------------------------------------------------------
  """)
######################################################################
def health(currentPk,trainerPkAlive,currentHp,maxHp,damageDone,BSD,oppCurrentPk,oppPkAlive,typeTable,type,oppType,colourFlash,reduce):
  if damageDone > 0:
    greenbars = math.ceil((currentHp / maxHp) * 20)
    redbars = 20 - greenbars
    reductionBars = math.ceil((damageDone / maxHp)*20)
    oneBarHp = math.ceil(damageDone / reductionBars)
    hp = currentHp

    for i in range(0,reductionBars):

      colour = colourFlash if i == 0 else reset
      hpColour = colourFlash if i == 0 else green
      alivePkCol = colourFlash if i == 0 else red
      deadPkCol = colourFlash if i == 0 else bright_black

      if type == "trainer":
        print(reset+bold+"You:"+colour)
        BSD(oppCurrentPk,oppPkAlive)
        print()
        print(colour+bold+"Opponent:"+colour)
      else:
        print(colour+bold+"You:"+colour)
      print(colour + "|--------------------------|")
      print("| " + currentPk.name + " ", end="", flush=True)
      if currentPk.status == "paralysed":
        print("\033[48;2;254;203;51m" + " Paralysed " + colour + (13-len(currentPk.name))*" " + "|")
      elif currentPk.status == "poisoned":
        print("\033[48;2;163;62;161m" + " Poisoned " + colour + (14-len(currentPk.name))*" " + "|")
      elif currentPk.status == "burned":
        print("\033[48;2;235;68;34m" + " Burned " + colour + (16-len(currentPk.name))*" " + "|")
      else:
        print((24-len(currentPk.name))*" " +colour+ "|")
      print("| ", end = "", flush = True)

      if currentHp <= 0:
        print(bright_black + 20*"█"+colour)
      else:
        print(hpColour+"█"*greenbars+bright_black+"█"*redbars+colour,end="",flush=True)

      if math.floor(hp) >= 100:
        spaces = 0
      elif 100 > math.floor(hp) >= 10:
        spaces = 1
      else:
        spaces = 2

      print(colour+" " + str(math.floor(hp)) + (spaces*" "), end="", flush=True)
      if reduce is True:
        hp = hp-math.ceil(oneBarHp) if hp > 0 else 0
        greenbars -= 1
        redbars += 1
      else:
        hp = hp+math.ceil(oneBarHp) if hp > 0 else 0
        greenbars += 1
        redbars -= 1
      print(colour+" |")

      greyCircles = 6 - trainerPkAlive
      redCircles = 6 - greyCircles
      print("| ", end="",flush=True)
      while redCircles > 0:
        print(alivePkCol+"●", end='', flush=True)
        redCircles -= 1
      while greyCircles > 0:
        print(deadPkCol+"●", end='', flush=True)
        greyCircles -= 1
      print(colour + 19*" "+"|")

      print("|--------------------------|"+reset)

      if type == "opp":
        print()
        print(bold+"Opponent:"+reset)
        BSD(oppCurrentPk,oppPkAlive)
      battleTurnGraphic(None,None,oppType,None,typeTable[currentPk.type1]["c"],typeTable[oppCurrentPk.type1]["c"],currentPk,oppCurrentPk,typeTable)
      time.sleep(0.5)
      if i != reductionBars-1:
        os.system('cls')
######################################################################
def trainerLongGrass(points):
  spaces = "\n\n\n\n\n\n\n\n\n\n\n\n"
  if points > 1:
    print("You are on " + str(points) + " points")
  elif points == 1:
    print("You are on 1 point")
  print(spaces)
  print(green + r"""
                               @@@@                                       @@
                              @@@@~@                                     @@@
                             @@@~@@@@                                   @@@~
                              @@@@@@@                                    @@@"""+reset+"""
     o"""+green+"""                         @@_@"""+reset+"""                                  o"""+green+"""    @@"""+reset+"""
    /|\                         ||                                  /|\   ||
    / \                        _||_                                 / \  _||
  --------------------------------------------------------------------------
  """)
  time.sleep(0.7)
  os.system('cls') #23, 13
  if points > 1:
    print("You are on " + str(points) + " points")
  elif points == 1:
    print("You are on 1 point")
  print(spaces)
  print(green + r"""
                      @@@@                                        @@@@
                     @@@@~@                                      @@@@~@
                    @@@~@@@@                                    @@@~@@@@
                     @@@@@@@                                     @@@@@@@"""+reset+"""
             o"""+green+"""        @@_@"""+reset+"""                                    o"""+green+"""   @@_@"""+reset+"""
            /|\        ||                                    /|\   ||
            / \       _||_                                   / \  _||_
  --------------------------------------------------------------------------
  """)
  time.sleep(0.7)
  os.system('cls')
  if points > 1:
    print("You are on " + str(points) + " points")
  elif points == 1:
    print("You are on 1 point")
  print(spaces)
  print(green + r"""
             @@@@                                        @@@@
            @@@@~@                                      @@@@~@
           @@@~@@@@                                    @@@~@@@@
            @@@@@@@                                     @@@@@@@
             @@_@"""+reset+"""         o                          o"""+green+"""   @@_@"""+reset+""" 
              ||         /|\                        /|\   ||"""+green+"""            @@@ @"""+reset+""" 
             _||_        / \                        / \  _||_"""+green+"""          @@@@@@"""+reset+"""
  --------------------------------------------------------------------------
  """)
  time.sleep(0.7)
  os.system('cls')
  if points > 1:
    print("You are on " + str(points) + " points")
  elif points == 1:
    print("You are on 1 point")
  print(spaces)
  print(green + r"""
             @@@@                                        @@@@
            @@@@~@                                      @@@@~@
           @@@~@@@@                                    @@@~@@@@
            @@@@@@@                                 """+red+"""!!!"""+green+""" @@@@@@@
             @@_@"""+reset+"""         o                        __o"""+green+"""   @@_@"""+reset+""" 
              ||         /|\                         |\   ||"""+green+"""            @@@ @"""+reset+""" 
             _||_        / \                        / \  _||_"""+green+"""          @@@@@@"""+reset+"""
  --------------------------------------------------------------------------
  """)
  time.sleep(1)
  os.system('cls')
######################################################################
def trainerSendOut(pk1Col,pk2Col,BSD,parameters):
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""



  
            o                                                      o
           /|\                                                    /|\
           / \ """+pk2Col+"""                                          ██"""+reset+"""       / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.5)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""


  
  
            o__"""+red+"""●"""+reset+"""                                                   o
           /|                                                     /|\\
           / \ """+pk2Col+"""                                          ██"""+reset+"""       / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.35)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""



  
            o                                                      o
           /|\ """+red+"""●"""+reset+"""                                                  /|\\
           / \ """+pk2Col+"""                                          ██"""+reset+"""       / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.09)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""


  
                """+red+"""●"""+reset+"""
            o/                                                     o
           /|                                                     /|\\
           / \ """+pk2Col+"""                                          ██"""+reset+"""       / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.09)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""

  
                    """+bright_blue+"""●"""+reset+"""
  
            o/                                                     o
           /|                                                     /|\\
           / \ """+pk2Col+"""                                          ██"""+reset+"""       / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.09)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""

  
                    """+bright_blue+"""*"""+reset+"""
  
            o/                                                     o
           /|                                                     /|\\
           / \ """+pk2Col+"""                                          ██"""+reset+"""       / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.09)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""

  
                    """+bright_blue+"""*
                    **"""+reset+"""
            o__     """+bright_blue+"""**"""+reset+"""                                             o
           /|                                                     /|\\
           / \ """+pk2Col+"""                                          ██"""+reset+"""       / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.09)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""

  
                    """+bright_blue+"""*"""+reset+"""
            o__     """+bright_blue+"""**"""+reset+"""                                             o
           /|       """+bright_blue+"""**"""+reset+"""                                            /|\\
           / \       """+bright_blue+"""**"""+pk2Col+"""                                  ██"""+reset+"""       / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.09)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""


  
  
            o                                                      o
           /|\      """+bright_blue+"""**"""+reset+"""                                            /|\\
           / \       """+bright_blue+"""**"""+pk2Col+"""                                  ██"""+reset+"""       / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.09)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""


  
  
            o                                                      o
           /|\                                                    /|\
           / \      """+bright_blue+"""██                                   """+pk2Col+"""██"""+reset+"""       / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.09)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""


  
  
            o                                                      o
           /|\                                                    /|\
           / \       """+pk1Col+"""██                                  """+pk2Col+"""██"""+reset+"""       / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(1)
  os.system('cls')
######################################################################
def oppTrainerSendOut(pk1Col,pk2Col,BSD,parameters):
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""


  

            o                                                    o
           /|\                                                  /|\
           / \       """+pk1Col+"""██                                         / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




            o  """+red+"""                                               ●"""+reset+"""__o
           /|\\                                                   |\\
           / \\       """+pk1Col+"""██                                         / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.5)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




            o                                                    o
           /|\ """+red+"""                                               ● """+reset+"""/|\\
           / \\       """+pk1Col+"""██                                         / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""


  
                """+red+"""                                              ●"""+reset+"""
            o                                                   \o
           /|\\                                                   |\\
           / \\       """+pk1Col+"""██                                         / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""

  
                    """+bright_blue+"""                                      ●"""+reset+"""

            o                                                   \o
           /|\\                                                   |\\
           / \\       """+pk1Col+"""██                                         / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""

  
                    """+bright_blue+"""                                      *"""+reset+"""

            o                                                   \o
           /|\\                                                   |\\
           / \\       """+pk1Col+"""██                                         / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""

  
                    """+bright_blue+"""                                     *
                                                        **"""+reset+"""
            o       """+bright_blue+"""                                    **"""+reset+"""     __o
           /|\\                                                   |\\
           / \\       """+pk1Col+"""██                                         / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""


  
                    """+bright_blue+"""                                     *"""+reset+"""
            o       """+bright_blue+"""                                    **"""+reset+"""     __o
           /|\\     """+bright_blue+"""                                     **"""+reset+"""       |\\
           / \\       """+pk1Col+"""██"""+bright_blue+"""                                 **"""+reset+"""      / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""
  

  

            o                                                    o
           /|\      """+bright_blue+"""                                    **"""+reset+"""      /|\\
           / \\       """+pk1Col+"""██"""+bright_blue+"""                                 **"""+reset+"""      / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""


  

            o                                                    o
           /|\                                                  /|\
           / \\      """+pk1Col+"""██"""+bright_blue+"""                                 ██"""+reset+"""      / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""


  

            o                                                    o
           /|\                                                  /|\
           / \\      """+pk1Col+"""██                                 """+pk2Col+"""██"""+reset+"""      / \\
  --------------------------------------------------------------------------
  """)
  time.sleep(1)
  os.system('cls')
######################################################################
def trainerWithdraw(pk1Col,pk2Col,BSD,parameters):
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o                                                    o
            /|\                                                  /|\
            / \   """ + pk1Col + """   ██                                """ + pk2Col + """  ██  """ + reset + """    / \\
  --------------------------------------------------------------------------
    """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o__"""+red+"""●"""+reset+"""                                                 o
            /|                                                   /|\\
            / \      """+pk1Col+"""██                                  """+pk2Col+"""██"""+reset+"""      / \\
  --------------------------------------------------------------------------
    """)
  time.sleep(0.5)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o__"""+red+"""●"""+reset+"""                                                 o
            /|                                                   /|\\
            / \      """+bright_blue+"""██                                  """+pk2Col+"""██"""+reset+"""      / \\
  --------------------------------------------------------------------------
    """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o__"""+red+"""●"""+reset+"""                                                 o
            /|       """+blue+"""*"""+reset+"""                                           /|\\
            / \      """+blue+"""**                                  """+pk2Col+"""██"""+reset+"""      / \\
  --------------------------------------------------------------------------
    """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o__"""+red+"""●"""+reset+"""                                                 o
            /|      """+blue+"""**"""+reset+"""                                           /|\\
            / \      """+blue+"""*                                   """+pk2Col+"""██"""+reset+"""      / \\
  --------------------------------------------------------------------------
    """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o__"""+red+"""●  """+blue+"""*"""+reset+"""                                              o
            /|     """+blue+"""**"""+reset+"""                                            /|\\
            / \                                          """+pk2Col+"""██"""+reset+"""      / \\
  --------------------------------------------------------------------------
    """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o__"""+red+"""●"""+blue+"""**"""+reset+"""                                               o
            /|     """+blue+"""*"""+reset+"""                                             /|\\
            / \                                          """+pk2Col+"""██"""+reset+"""      / \\
  --------------------------------------------------------------------------
    """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o__"""+red+"""●"""+blue+"""*"""+reset+"""                                                o
            /|                                                   /|\\
            / \                                          """+pk2Col+"""██"""+reset+"""      / \\
  --------------------------------------------------------------------------
    """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o__"""+red+"""●"""+reset+"""                                                 o
            /|                                                   /|\\
            / \                                          """+pk2Col+"""██"""+reset+"""      / \\
  --------------------------------------------------------------------------
    """)
  time.sleep(0.5)
  os.system('cls')
######################################################################
def oppTrainerWithdraw(pk1Col,pk2Col,BSD,parameters):
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o                                                    o
            /|\                                                  /|\\
            / \      """+pk1Col+"""██                                  """+pk2Col+"""██"""+reset+"""      / \\
  --------------------------------------------------------------------------
    """)
  time.sleep(0.5)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o                                                 """+red+"""●"""+reset+"""__o
            /|\                                                   |\\
            / \      """+pk1Col+"""██                                  """+pk2Col+"""██"""+reset+"""      / \\
  --------------------------------------------------------------------------
    """)
  time.sleep(0.35)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o                                                 """+red+"""●"""+reset+"""__o
            /|\                                           """+blue+"""*"""+reset+"""       |\\
            / \      """+pk1Col+"""██                                  """+blue+"""**"""+reset+"""      / \\
  --------------------------------------------------------------------------
    """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o                                                 """+red+"""●"""+reset+"""__o
            /|\                                           """+blue+"""**"""+reset+"""      |\\
            / \      """+pk1Col+"""██                                   """+blue+"""*"""+reset+"""      / \\
  --------------------------------------------------------------------------
    """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o                                              """+blue+"""*  """+red+"""●"""+reset+"""__o
            /|\                                            """+blue+"""**"""+reset+"""     |\\
            / \      """+pk1Col+"""██"""+reset+"""                                          / \\
  --------------------------------------------------------------------------
    """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o                                              """+blue+"""** """+red+"""●"""+reset+"""__o
            /|\                                             """+blue+"""*"""+reset+"""     |\\
            / \      """+pk1Col+"""██"""+reset+"""                                          / \\
  --------------------------------------------------------------------------
    """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o                                                """+blue+"""*"""+red+"""●"""+reset+"""__o
            /|\                                                   |\\
            / \      """+pk1Col+"""██"""+reset+"""                                          / \\
  --------------------------------------------------------------------------
    """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o                                                 """+red+"""●"""+reset+"""__o
            /|\                                                   |\\
            / \      """+pk1Col+"""██"""+reset+"""                                          / \\
  --------------------------------------------------------------------------
    """)
  time.sleep(0.35)
  os.system('cls')
######################################################################
def wildTrainerWithdraw(pk1Col,pk2Col,BSD,parameters):
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o                                                    
            /|\                                                     
            / \   """ + pk1Col + """   ██                                """ + pk2Col + """  ██  """ + reset + """
  --------------------------------------------------------------------------
    """)
  time.sleep(0.5)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o__"""+red+"""●"""+reset+"""                                                 
            /|                                                  
            / \      """+pk1Col+"""██                                  """+pk2Col+"""██"""+reset+"""
  --------------------------------------------------------------------------
    """)
  time.sleep(0.35)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o__"""+red+"""●"""+reset+"""                                                 
            /|                                                   
            / \      """+pk1Col+"""██                                  """+pk2Col+"""██"""+reset+""" 
  --------------------------------------------------------------------------
    """)

  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o__"""+red+"""●"""+reset+"""                                                 
            /|       """+blue+"""*"""+reset+"""                                          
            / \      """+blue+"""**                                  """+pk2Col+"""██"""+reset+"""     
  --------------------------------------------------------------------------
    """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o__"""+red+"""●"""+reset+"""                                                 
            /|      """+blue+"""**"""+reset+"""                                           
            / \      """+blue+"""*                                   """+pk2Col+"""██"""+reset+"""      
  --------------------------------------------------------------------------
    """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o__"""+red+"""●  """+blue+"""*"""+reset+"""                                              
            /|     """+blue+"""**"""+reset+"""                                           
            / \                                          """+pk2Col+"""██"""+reset+"""    
  --------------------------------------------------------------------------
    """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o__"""+red+"""●"""+blue+"""**"""+reset+"""                                               
            /|     """+blue+"""*"""+reset+"""                                            
            / \                                          """+pk2Col+"""██"""+reset+"""   
  --------------------------------------------------------------------------
    """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o__"""+red+"""●"""+blue+"""*"""+reset+"""                                                
            /|                                                  
            / \                                          """+pk2Col+"""██"""+reset+"""  
  --------------------------------------------------------------------------
    """)
  time.sleep(0.13)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o__"""+red+"""●"""+reset+"""                                                 
            /|                                                  
            / \                                          """+pk2Col+"""██"""+reset+"""     
  --------------------------------------------------------------------------
    """)
  time.sleep(0.5)
  os.system('cls')
######################################################################
def pokemonCatch(pk1Col,pk2Col,noRolls,BSD,parameters,ballCol):
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




             o
            /|\
            / \      """+pk1Col+"""██                                  """+pk2Col+"""██"""+reset+"""
  --------------------------------------------------------------------------
    """)
  time.sleep(0.35)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




             o
           """+ballCol+"""●"""+reset+"""/|\\
            / \      """+pk1Col+"""██                                  """+pk2Col+"""██"""+reset+"""
  --------------------------------------------------------------------------
    """)
  time.sleep(0.23)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




          """+ballCol+"""●"""+reset+"""__o
             |\\
            / \      """+pk1Col+"""██                                  """+pk2Col+"""██"""+reset+"""
  --------------------------------------------------------------------------
    """)
  time.sleep(0.15)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""



           """+ballCol+"""●"""+reset+"""
            \o
             |\\
            / \      """+pk1Col+"""██                                  """+pk2Col+"""██"""+reset+"""
  --------------------------------------------------------------------------
    """)
  time.sleep(0.15)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""


                 """+ballCol+"""●"""+reset+"""
           
             o/
            /|
            / \      """+pk1Col+"""██                                  """+pk2Col+"""██"""+reset+"""
  --------------------------------------------------------------------------
    """)
  time.sleep(0.15)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""

                      """+ballCol+"""●"""+reset+"""
                 

           __o
             |\\
            / \      """+pk1Col+"""██                                  """+pk2Col+"""██"""+reset+"""
  --------------------------------------------------------------------------
    """)
  time.sleep(0.15)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""
                            """+ballCol+"""●"""+reset+"""
                         
                 

             o
            /|\\
            / \      """+pk1Col+"""██                                  """+pk2Col+"""██"""+reset+"""
  --------------------------------------------------------------------------
    """)
  time.sleep(0.15)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""
                                  """+ballCol+"""●"""+reset+"""



             o
            /|\\
            / \      """+pk1Col+"""██                                  """+pk2Col+"""██"""+reset+"""
  --------------------------------------------------------------------------
    """)
  time.sleep(0.15)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""
                                            
                                        """+ballCol+"""●"""+reset+"""


             o
            /|\\
            / \      """+pk1Col+"""██                                  """+pk2Col+"""██"""+reset+"""
  --------------------------------------------------------------------------
    """)
  time.sleep(0.15)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""

                                            
                                            """+ballCol+"""●"""+reset+"""

             o
            /|\\
            / \      """+pk1Col+"""██                                  """+pk2Col+"""██"""+reset+"""
  --------------------------------------------------------------------------
    """)
  time.sleep(0.15)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""


                                                
                                                  """+ballCol+"""●"""+reset+"""
             o
            /|\\
            / \      """+pk1Col+"""██                                  """+pk2Col+"""██"""+reset+"""
  --------------------------------------------------------------------------
    """)
  time.sleep(0.15)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""



                                                    
             o                                        """+ballCol+"""●"""+reset+"""
            /|\\
            / \      """+pk1Col+"""██                                  """+pk2Col+"""██"""+reset+"""
  --------------------------------------------------------------------------
    """)
  time.sleep(0.15)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




             o                                        
            /|\                                         """+ballCol+"""●"""+reset+"""
            / \      """+pk1Col+"""██                                  """+pk2Col+"""██"""+reset+"""
  --------------------------------------------------------------------------
    """)
  time.sleep(0.15)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




             o                                        """+ballCol+"""●"""+reset+"""
            /|\\                                         
            / \      """+pk1Col+"""██                                  """+pk2Col+"""██"""+reset+"""
  --------------------------------------------------------------------------
    """)
  time.sleep(0.15)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""



                                                  """+blue+"""●"""+reset+"""
             o
            /|\\
            / \      """+pk1Col+"""██                                  """+blue+"""██"""+reset+"""
  --------------------------------------------------------------------------
    """) #BLUE
  time.sleep(0.15)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""



                                                  """+blue+"""●"""+reset+"""
             o
            /|\                                          """+blue+"""**"""+reset+"""
            / \      """+pk1Col+"""██                                  """+blue+"""**"""+reset+"""
  --------------------------------------------------------------------------
    """)
  time.sleep(0.15)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""



                                                  """+blue+"""●"""+reset+"""
             o                                          """+blue+"""**"""+reset+"""
            /|\                                          """+blue+"""**"""+reset+"""
            / \      """+pk1Col+"""██"""+reset+"""                                  
  --------------------------------------------------------------------------
    """)
  time.sleep(0.15)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""



                                                  """+blue+"""●   **"""+reset+""" 
             o                                         """+blue+"""**"""+reset+"""
            /|\                                          
            / \      """+pk1Col+"""██"""+reset+"""                                  
  --------------------------------------------------------------------------
    """)
  time.sleep(0.15)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""



                                                  """+blue+"""●  **"""+reset+""" 
             o                                         """+blue+"""*"""+reset+"""
            /|\                                          
            / \      """+pk1Col+"""██"""+reset+"""                                  
  --------------------------------------------------------------------------
    """)
  time.sleep(0.15)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""



                                                  """+blue+"""●**"""+reset+""" 
             o                                         
            /|\                                          
            / \      """+pk1Col+"""██"""+reset+"""                                  
  --------------------------------------------------------------------------
    """)
  time.sleep(0.15)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""



                                                  """+blue+"""●"""+reset+""" 
             o                                         
            /|\                                          
            / \      """+pk1Col+"""██"""+reset+"""                                  
  --------------------------------------------------------------------------
    """)
  time.sleep(0.15)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""



                                                  """+ballCol+"""●"""+reset+"""
             o                                         
            /|\                                          
            / \      """+pk1Col+"""██"""+reset+"""                                  
  --------------------------------------------------------------------------
    """)
  time.sleep(0.15)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""



                                                   
             o                                    """+ballCol+"""●"""+reset+"""   
            /|\                                          
            / \      """+pk1Col+"""██"""+reset+"""                                  
  --------------------------------------------------------------------------
    """)
  time.sleep(0.15)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




             o                                       
            /|\                                   """+ballCol+"""●"""+reset+"""      
            / \      """+pk1Col+"""██"""+reset+"""                                  
  --------------------------------------------------------------------------
    """)
  time.sleep(0.15)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(r"""




             o                                       
            /|\                                 
            / \      """+pk1Col+"""██                           """+ballCol+"""●"""+reset+"""
  --------------------------------------------------------------------------
    """)
  time.sleep(0.33)
  os.system('cls')
  
  for i in range(0,noRolls):
    print(bold+"You:"+reset)
    BSD(parameters[0][0],parameters[0][1])
    print()
    print(bold+"Opponent:"+reset)
    BSD(parameters[1][0],parameters[1][1])
    print(r"""
  
  
  
  
             o                                       
            /|\                                 
            / \      """+pk1Col+"""██                           """+bright_yellow+"""●"""+reset+"""
  --------------------------------------------------------------------------
      """)
    time.sleep(0.53)
    os.system('cls')
    print(bold+"You:"+reset)
    BSD(parameters[0][0],parameters[0][1])
    print()
    print(bold+"Opponent:"+reset)
    BSD(parameters[1][0],parameters[1][1])
    print(r"""
  
  
  
  
             o                                       
            /|\                                 
            / \      """+pk1Col+"""██                           """+ballCol+"""●"""+reset+"""
  --------------------------------------------------------------------------
      """)
    time.sleep(0.33)
    os.system('cls')
  if noRolls == 3:
    print(bold+"You:"+reset)
    BSD(parameters[0][0],parameters[0][1])
    print()
    print(bold+"Opponent:"+reset)
    BSD(parameters[1][0],parameters[1][1])
    print(r"""




             o                                       
            /|\                                   """+bright_yellow+"""*"""+reset+"""
            / \      """+pk1Col+"""██                           """+ballCol+"""●"""+reset+"""
  --------------------------------------------------------------------------
      """)
    time.sleep(0.23)
    os.system('cls')
    print(bold+"You:"+reset)
    BSD(parameters[0][0],parameters[0][1])
    print()
    print(bold+"Opponent:"+reset)
    BSD(parameters[1][0],parameters[1][1])
    print(r"""




             o                                       
            /|\                                  """+bright_yellow+"""* *"""+reset+"""
            / \      """+pk1Col+"""██                           """+ballCol+"""●"""+reset+"""
  --------------------------------------------------------------------------
      """)
    time.sleep(0.23)
    os.system('cls')
    print(bold+"You:"+reset)
    BSD(parameters[0][0],parameters[0][1])
    print()
    print(bold+"Opponent:"+reset)
    BSD(parameters[1][0],parameters[1][1])
    print(r"""




             o                                       
            /|\                                 
            / \      """+pk1Col+"""██                           """+ballCol+"""●"""+reset+"""
  --------------------------------------------------------------------------
        """)
  else:
    print(bold+"You:"+reset)
    BSD(parameters[0][0],parameters[0][1])
    print()
    print(bold+"Opponent:"+reset)
    BSD(parameters[1][0],parameters[1][1])
    print(r"""




             o                                       
            /|\                                 
            / \      """+pk1Col+"""██                           """+blue+"""●"""+reset+"""
  --------------------------------------------------------------------------
      """)
    time.sleep(0.15)
    os.system('cls')
    print(bold+"You:"+reset)
    BSD(parameters[0][0],parameters[0][1])
    print()
    print(bold+"Opponent:"+reset)
    BSD(parameters[1][0],parameters[1][1]) #18
    print(r"""




             o                                       
            /|\                                 
            / \      """+pk1Col+"""██                           """+blue+"""*"""+reset+"""
  --------------------------------------------------------------------------
      """)
    time.sleep(0.15)
    os.system('cls')
    print(bold+"You:"+reset)
    BSD(parameters[0][0],parameters[0][1])
    print()
    print(bold+"Opponent:"+reset)
    BSD(parameters[1][0],parameters[1][1]) #18
    print(r"""




             o                                       
            /|\                                    """+blue+"""**"""+reset+"""
            / \      """+pk1Col+"""██                            """+blue+"""*"""+reset+"""                       
  --------------------------------------------------------------------------
      """)
    time.sleep(0.15)
    os.system('cls')
    print(bold+"You:"+reset)
    BSD(parameters[0][0],parameters[0][1])
    print()
    print(bold+"Opponent:"+reset)
    BSD(parameters[1][0],parameters[1][1]) #18
    print(r"""




             o                                       
            /|\                                     """+blue+"""***"""+reset+"""
            / \      """+pk1Col+"""██"""+reset+"""                                                    
  --------------------------------------------------------------------------
      """)
    time.sleep(0.15)
    os.system('cls')
    print(bold+"You:"+reset)
    BSD(parameters[0][0],parameters[0][1])
    print()
    print(bold+"Opponent:"+reset)
    BSD(parameters[1][0],parameters[1][1]) #18
    print(r"""




             o                                       
            /|\                                       """+blue+"""**"""+reset+"""
            / \      """+pk1Col+"""██                                 """+blue+"""*"""+reset+"""                  
  --------------------------------------------------------------------------
      """)
    time.sleep(0.15)
    os.system('cls')
    print(bold+"You:"+reset)
    BSD(parameters[0][0],parameters[0][1])
    print()
    print(bold+"Opponent:"+reset)
    BSD(parameters[1][0],parameters[1][1]) #18
    print(r"""




             o                                       
            /|\                                       
            / \      """+pk1Col+"""██                                  """+blue+"""**"""+reset+"""                  
  --------------------------------------------------------------------------
      """)
    time.sleep(0.15)
    os.system('cls')
    print(bold+"You:"+reset)
    BSD(parameters[0][0],parameters[0][1])
    print()
    print(bold+"Opponent:"+reset)
    BSD(parameters[1][0],parameters[1][1]) #18
    print(r"""




             o                                       
            /|\                                       
            / \      """+pk1Col+"""██                                  """+blue+"""██"""+reset+"""                  
  --------------------------------------------------------------------------
      """)
    time.sleep(0.15)
    os.system('cls')
    time.sleep(0.15)
    os.system('cls')
    print(bold+"You:"+reset)
    BSD(parameters[0][0],parameters[0][1])
    print()
    print(bold+"Opponent:"+reset)
    BSD(parameters[1][0],parameters[1][1]) #18
    print(r"""




             o                                       
            /|\                                       
            / \      """+pk1Col+"""██                                  """+pk2Col+"""██"""+reset+"""                  
  --------------------------------------------------------------------------
        """)
######################################################################    #4
def wildDefeat(pk1Col,pk2Col,BSD,parameters):
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o                                                    
            /|\                                                     
            / \   """ + pk1Col + """   ██                                """ + pk2Col + """  ██  """ + reset + """
  --------------------------------------------------------------------------
    """)
  time.sleep(0.5)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o                                                    
            /|\                                                     
            / \   """ + pk1Col + """   ██                                """ + pk2Col + """   ██  """ + reset + """
  --------------------------------------------------------------------------
    """)
  time.sleep(0.5)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o                                                    
            /|\                                                     
            / \   """ + pk1Col + """   ██                                """ + pk2Col + """      ██  """ + reset + """
  --------------------------------------------------------------------------
    """)
  time.sleep(0.5)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o                                                    
            /|\                                                     
            / \   """ + pk1Col + """   ██                                """ + pk2Col + """         ██  """ + reset + """
  --------------------------------------------------------------------------
    """)
  time.sleep(0.5)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o                                                    
            /|\                                                     
            / \   """ + pk1Col + """   ██                                """ + pk2Col + """            ██  """ + reset + """
  --------------------------------------------------------------------------
    """)
  time.sleep(0.5)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o                                                    
            /|\                                                     
            / \   """ + pk1Col + """   ██                                """ + pk2Col + """               ██  """ + reset + """
  --------------------------------------------------------------------------
    """)
  time.sleep(0.5)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o                                                    
            /|\                                                     
            / \   """ + pk1Col + """   ██                                """ + pk2Col + """                  █  """ + reset + """
  --------------------------------------------------------------------------
    """)
  time.sleep(0.5)
  os.system('cls')
  print(bold+"You:"+reset)
  BSD(parameters[0][0],parameters[0][1])
  print()
  print(bold+"Opponent:"+reset)
  BSD(parameters[1][0],parameters[1][1])
  print(reset + r"""




             o                                                    
            /|\                                                     
            / \   """ + pk1Col + """   ██""" + reset + """
  --------------------------------------------------------------------------
    """)
  time.sleep(0.5)
  os.system('cls')
