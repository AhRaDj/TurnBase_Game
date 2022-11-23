import os
import random

char = [{"Name" : "Knight", "Weapon Type" : "Sword", "Weapon" : "Wooden Sword", "ATK" : 70, "HP" : 1000, "Skill" : "Stun","Mana" : 100},
        {"Name" : "Mage", "Weapon Type" : "Staff", "Weapon" : "Bares Staff", "ATK" : 20, "HP" : 500, "Skill" : "Heal","Mana" : 100},
        {"Name" : "Monk", "Weapon Type" : "Gauntlet", "Weapon" : "Hard Knuckle", "ATK" : 60, "HP" : 800, "Skill" : "Rage","Mana" : 100},
        {"Name" : "Archer", "Weapon Type" : "Bow", "Weapon" : "Yuria Bow", "ATK" : 40, "HP" : 600, "Skill" : "Aim Focus","Mana" : 100}]

sword = [{"Name" : "Excalibur", "ATK" : 600},
         {"Name" : "Caladbolg", "ATK" : 400},
         {"Name" : "Echo Saber", "ATK" : 170},
         {"Name" : "Wooden Sword", "ATK" : 70}]

staff = [{"Name" : "Aghanim Staff", "ATK" : 300},
         {"Name" : "Power Staff", "ATK" : 200},
         {"Name" : "Wizard Staff", "ATK" : 150},
         {"Name" : "Bares Staff", "ATK" : 20}]

gauntlet = [{"Name" : "Kaiser Knuckles", "ATK" : 550},
            {"Name" : "Tiger Fangs", "ATK" : 450},
            {"Name" : "Cat Claws", "ATK" : 100},
            {"Name" : "Hard Knuckle", "ATK" : 60}]

bow = [{"Name" : "Perseus Bow", "ATK" : 500},
       {"Name" : "Artemis Bow", "ATK" : 450},
       {"Name" : "Crescent Bow", "ATK" : 200},
       {"Name" : "Yuria Bow", "ATK" : 40}]

def Back():
    back = input("Press any to continue")

def change(selectedchar,id ,senjata): #Pure Function
  for i in range(len(senjata)):
    print("ID : {} || Name : {} || ATK : {}".format(i, senjata[i]["Name"], senjata[i]["ATK"]))
  pilih = int(input("Choose Weapon : "))
  selectedchar[id]["Weapon"] = senjata[int(pilih)]["Name"]
  selectedchar[id]["ATK"] = senjata[int(pilih)]["ATK"]

def changeWeapon(char):
  selectchar = char
  for i in range(len(selectchar)): # Range
    print("ID : {} || Name : {} || Weapon : {} || ATK : {}".format(i, selectchar[i]["Name"], selectchar[i]["Weapon"], selectchar[i]["ATK"]))
  inputs = int(input("Choose Character by ID: "))
  try:
    if selectchar[inputs]["Weapon Type"] == "Sword":
      change(selectchar,inputs ,sword)
    elif selectchar[inputs]["Weapon Type"] == "Staff":
      change(selectchar,inputs ,staff)
    elif selectchar[inputs]["Weapon Type"] == "Gauntlet":
      change(selectchar,inputs ,gauntlet)
    elif selectchar[inputs]["Weapon Type"] == "Bow":
      change(selectchar,inputs ,bow)
    print("\nUpdated!!!")
    for i in range(len(selectchar)):
      print("ID : {} || Name : {} || Weapon : {} || ATK : {}".format(i, selectchar[i]["Name"], selectchar[i]["Weapon"], selectchar[i]["ATK"]))  
    pilihganti = input("Want to Change Again? (y/n)")
    if pilihganti == "y":
      os.system('cls')
      changeWeapon(selectchar)
      return selectchar
    else:
      return selectchar
  except ValueError:
    print("Error, Please enter numbers.")
    changeWeapon(selectchar)

def skill(operation, selectedchar, requirement_mana, pilihan): #High Order Order Function
  return operation(selectedchar, requirement_mana, pilihan)

def skillPhysical(selectedchar, requirement_mana, pilihan):
  selectedchar[pilihan]["Mana"] -= requirement_mana
  print("MP Remaining : {}".format(selectedchar[pilihan]["Mana"]))
  if selectedchar[pilihan]["Name"] == "Knight":
    print("Vacant Colossus got Stunned")
  elif selectedchar[pilihan]["Name"] == "Monk":
    print("Rage Skill Used, Attack = ",format((selectedchar[pilihan]["ATK"] * 2)))
  elif selectedchar[pilihan]["Name"] == "Archer":
    print("Aim Focus Used, Attack = ",format((selectedchar[pilihan]["ATK"] + 50)))

def skillHeal(selectedchar, requirement_mana, pilihan):
  selectedchar[pilihan]["Mana"] -= requirement_mana
  print("MP Remaining : {}".format(selectedchar[pilihan]["Mana"]))
  print("\nHealing For Everyone")
  for j in range(len(selectedchar)):
    selectedchar[j]["HP"] += 50
    print("HP : {} || {}".format(selectedchar[j]["HP"], selectedchar[j]["Name"]))

def fightBos(fightchar):
  vacantColossus = 5000
  newchar = fightchar
  while vacantColossus > 0:
    vacantColossusATK = random.randint(170,300)
    for i in range(len(newchar)):
      if vacantColossus <= 0 and vacantColossus > -500:
        vacantColossus = 0
        print("Vacant Colossus - HP: {}\n".format(vacantColossus))
        print("Challange Success\n")
        break
      os.system('cls')
      print("Vacant Colossus - HP: {}\n".format(vacantColossus))
      print("HP : {} - MP : {} || {} - {} - ATK {}".format(newchar[i]["HP"], newchar[i]["Mana"], newchar[i]["Name"], newchar[i]["Weapon"], newchar[i]["ATK"]))
      print("1. Attack")
      print("2. {}".format(newchar[i]["Skill"]))
      print("3. Run")
      fight = input("Select Action : ")
      if fight == "1":
        vacantColossus -= newchar[i]["ATK"]
        Back()
      elif fight == "2":
        print("{} - {}".format(newchar[i]["Name"], newchar[i]["Skill"]))
        if i == 0:
          if newchar[i]["Mana"] < 50:
            print("MP not enough, You pass the turn")
          else:
            skill(skillPhysical, newchar, 50, i)
            vacantColossusATK = 0
        elif i == 1:
          if newchar[i]["Mana"] < 30:
            print("MP not enough, You pass the turn")
          else:
            skill(skillHeal, newchar, 30, i)
        elif i == 2:
          if newchar[i]["Mana"] < 60:
            print("MP not enough, You pass the turn")
          else:
            vacantColossus -= (newchar[i]["ATK"] * 2)
            skill(skillPhysical, newchar, 60, i)
        elif i == 3:
          if newchar[i]["Mana"] < 40:
            print("MP not enough, You pass the turn")
          else:
            vacantColossus -= (newchar[i]["ATK"] + 50)
            skill(skillPhysical, newchar, 40, i)
        Back()
      elif fight == "3":
        vacantColossus = -501
        break
    if vacantColossus > 0:
      os.system('cls')
      if len(newchar) == 0:
        print("Game Over")
        print("Try Again Later")
        Back()
        start()
      else:
        attacked = random.randint(0,len(newchar)-1)
        newchar[attacked]["HP"] -= vacantColossusATK
        for i in range(len(newchar)):
          if newchar[i]["Mana"] < 100:
            newchar[i]["Mana"] += 10
        if vacantColossusATK == 0:
          print("Vacant Colossus miss Attack")
          vacantColossusATK = random.randint(170,300)
        else:
          print("{} got Attacked = {} Damage".format(newchar[attacked]["Name"], vacantColossusATK))
          if vacantColossusATK > 240:
            print("Critical Hit")
          else:
            print("Normal Hit")
          if newchar[attacked]["HP"] <= 0:
            print("{} has been Defeat".format(newchar[attacked]["Name"]))
            del newchar[attacked]
          else:
            print("HP : {} || {}".format(newchar[attacked]["HP"], newchar[attacked]["Name"]))
        Back()

    elif vacantColossus == -501:
      print("Run away safely\n")

def reset(resetchar):
  resetchar[0]["HP"] = 1000
  resetchar[1]["HP"] = 500
  resetchar[2]["HP"] = 800
  resetchar[3]["HP"] = 600
  for i in range(len(resetchar)):
    resetchar[i]["Mana"] = 100

def start():
  selectchar = char
  flag = True
  while flag:
    reset(selectchar)
    os.system('cls')
    print("Welcome New Challenger!!!\n")
    print("Select the activity you want to do:")
    print("1. Check Party")
    print("2. Change Weapon")
    print("3. Fight Vacant Colossus")
    print("4. Exit")
    inputs = input("Choose the number : ")
    if inputs == "1":
      os.system('cls')
      print("Party Status: \n")
      for i in range(len(selectchar)):
        print("{}\nWeapon : {}\nHP : {}\nMP : {}\nATK : {}\nSkill : {}\n".format(selectchar[i]["Name"], selectchar[i]["Weapon"],selectchar[i]["HP"], selectchar[i]["Mana"], selectchar[i]["ATK"], selectchar[i]["Skill"]))
      Back()
    elif inputs == "2":
      os.system('cls')
      selectchar = changeWeapon(selectchar)
      Back()
    elif inputs == "3":
      os.system('cls')
      newchar = selectchar.copy()
      fightBos(newchar)
      Back()  
    elif inputs == "4":
      flag = False
      return 'Thank you for playing this game'
    else:
      print("Wrong Input")
      Back()

start()