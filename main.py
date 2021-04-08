import datetime
import os
import csv
import json
import ast
import random
import matplotlib.pyplot as plt
import numpy as np

Name = ""
BMR = 0.0
activity_level_selector = {"1": 1.2, "2": 1.375, "3": 1.55, "4": 1.725, "5": 1.9}
print("Welcome to Mini Cooking Recipe Generator and Calorie Tracking System")
file = open ("userinformation.txt", 'r')
file.close()
fileSize = os.path.getsize("userinformation.txt")
if fileSize != 0 :
    with open("userInformation.txt", "r") as userFileR:
        allData = userFileR.read()
    allUsers = ast.literal_eval(allData)
    userFileR.close()
def editOrDelete(Name):
    print("please select your operation number")
    print("1. Edit profile")
    print("2. Delete profile")
    operation = input()
    if operation == "1":
        print("which value do you wish to edit")
        print("1. Name")
        print("2. date of birth")
        print("3. gender")
        print("4. height(m)")
        print("5. weight(kg)")
        print("6. activity level")
        print("7. allergies")
        opSelect = input()
        if opSelect == "1":
            print("enter New name")
            NameN = input()
            userProfile.update({"Name":NameN})
            userProfile.update({"Edit date":str(datetime.datetime.today())})
            allUsers[NameN]= allUsers.pop(Name)
            write = allUsers
            with open('userinformation.txt', 'w') as writeFile:
                writeFile.write(json.dumps(write))
                writeFile.close()
        elif opSelect == "2":
            print("enter New date of birth")
            BirthDateN = input()
            BirthDateN = datetime.datetime.strptime(BirthDateN, "%d/%m/%Y").date()
            currentDate = datetime.datetime.today().date()
            age = currentDate.year - BirthDateN.year
            if (currentDate.month - BirthDateN.month) < 0:
                age -= 1
            elif (currentDate.month - BirthDateN.month) == 0 and (currentDate.day - BirthDateN.day) < 0:
                age -= 1
            gender = userProfile.get("gender")
            weight = userProfile.get("weight")
            height = userProfile.get("height")
            activity_level = userProfile.get("activity")
            if gender == "f" or gender == "F":
                BMR = 655.1 + (9.563 * float(weight)) + (1.85 * float(height) * 100) - (4.676 * age)
            elif gender == "m" or gender == "M":
                BMR = 66.47 + (13.75 * float(weight)) + (5.003 * float(height) * 100) - (6.755 * age)
            TEE = BMR * activity_level
            BMR = format(BMR, '.2f')
            TEE = format(TEE, '.2f')
            userProfile.update({"date of birth": str(BirthDateN)})
            userProfile.update({"age": age})
            userProfile.update({"BMR": BMR})
            userProfile.update({"TEE": TEE})
            userProfile.update({"Edit date": str(datetime.datetime.today())})
            write = allUsers
            with open('userinformation.txt', 'w') as writeFile:
                writeFile.write(json.dumps(write))
                writeFile.close()
        elif opSelect == "3":
            print("enter New gender (M/F)")
            genderN = input()
            weight = userProfile.get("weight")
            height = userProfile.get("height")
            activity_level = userProfile.get("activity")
            age = userProfile.get("age")
            if genderN == "m" or genderN == "M" or genderN == "F" or genderN == "f":
                if genderN == "f" or genderN == "F":
                    BMR = 655.1 + (9.563 * float(weight)) + (1.85 * float(height) * 100) - (4.676 * age)
                elif genderN == "m" or genderN == "M":
                    BMR = 66.47 + (13.75 * float(weight)) + (5.003 * float(height) * 100) - (6.755 * age)
                TEE = BMR * activity_level
                BMR = format(BMR, '.2f')
                TEE = format(TEE, '.2f')
                userProfile.update({"gender": genderN})
                userProfile.update({"BMR": BMR})
                userProfile.update({"TEE": TEE})
                userProfile.update({"Edit date": str(datetime.datetime.today())})
                write = allUsers
                with open('userinformation.txt', 'w') as writeFile:
                    writeFile.write(json.dumps(write))
                    writeFile.close()
        elif opSelect == "4":
            print("enter New Height in meters")
            heightN = input()
            weight = userProfile.get("weight")
            activity_level = userProfile.get("activity")
            gender = userProfile.get("gender")
            age = userProfile.get("age")
            BMI = float(weight) / (float(heightN) ** 2)
            BMIrange = ""
            if BMI < 18.5:
                BMIrange = "underweight"
            elif 24.9 > BMI >= 18.5:
                BMIrange = "normal"
            elif 29.9 >= BMI >= 25:
                BMIrange = "overweight"
            elif BMI >= 30.0:
                BMIrange = "obese"
            if gender == "m" or gender == "M" or gender == "F" or gender == "f":
                if gender == "f" or gender == "F":
                    BMR = 655.1 + (9.563 * float(weight)) + (1.85 * float(heightN) * 100) - (4.676 * age)
                elif gender == "m" or gender == "M":
                    BMR = 66.47 + (13.75 * float(weight)) + (5.003 * float(heightN) * 100) - (6.755 * age)
            TEE = BMR * activity_level
            BMR = format(BMR, '.2f')
            BMI = format(BMI, '.2f')
            TEE = format(TEE, '.2f')
            userProfile.update({"BMI": BMI})
            userProfile.update({"BMI range": BMIrange})
            userProfile.update({"BMR": BMR})
            userProfile.update({"TEE": TEE})
            userProfile.update({"height": heightN})
            userProfile.update({"Edit date": str(datetime.datetime.today())})
            write = allUsers
            with open('userinformation.txt', 'w') as writeFile:
                writeFile.write(json.dumps(write))
                writeFile.close()
        elif opSelect == "5":
            print("enter New weight in KG")
            weightN = input()
            activity_level = userProfile.get("activity")
            gender = userProfile.get("gender")
            age = userProfile.get("age")
            height = userProfile.get("height")
            BMI = float(weightN) / (float(height) ** 2)
            BMIrange = ""
            if BMI < 18.5:
                BMIrange = "underweight"
            elif 24.9 > BMI >= 18.5:
                BMIrange = "normal"
            elif 29.9 >= BMI >= 25:
                BMIrange = "overweight"
            elif BMI >= 30.0:
                BMIrange = "obese"
            if gender == "m" or gender == "M" or gender == "F" or gender == "f":
                if gender == "f" or gender == "F":
                    BMR = 655.1 + (9.563 * float(weightN)) + (1.85 * float(height) * 100) - (4.676 * age)
                elif gender == "m" or gender == "M":
                    BMR = 66.47 + (13.75 * float(weightN)) + (5.003 * float(height) * 100) - (6.755 * age)
            TEE = BMR * activity_level
            BMR = format(BMR, '.2f')
            BMI = format(BMI, '.2f')
            TEE = format(TEE, '.2f')
            userProfile.update({"BMI": BMI})
            userProfile.update({"BMI range": BMIrange})
            userProfile.update({"BMR": BMR})
            userProfile.update({"TEE": TEE})
            userProfile.update({"weight": weightN})
            userProfile.update({"Edit date": str(datetime.datetime.today())})
            write = allUsers
            with open('userinformation.txt', 'w') as writeFile:
                writeFile.write(json.dumps(write))
                writeFile.close()
        elif opSelect == "6":
            print("enter you New desired activity level")
            activity_level = input()
            BMR = userProfile.get("BMR")
            TEE = BMR * activity_level
            userProfile.update({"activity": activity_level})
            userProfile.update({"TEE": TEE})
            userProfile.update({"Edit date": str(datetime.datetime.today())})
            write = allUsers
            with open('userinformation.txt', 'w') as writeFile:
                writeFile.write(json.dumps(write))
                writeFile.close()
        elif opSelect == "7":
            allergies = []
            with open('ingredients.csv') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=';')
                for row in spamreader:
                    i = 16
                    print(((i - int(len(row[0]))) * ' ').join(row))
            csvfile.close()
            allergyNo = input()
            if allergyNo != "-1":
                while True:
                    with open('ingredients.csv') as csvfile:
                        spamreader = csv.reader(csvfile, delimiter=';')
                        for row in spamreader:
                            for field in row:
                                if field == allergyNo:
                                    allergy = row[0]
                                    allergies.append(allergy)
                    csvfile.close()
                    print("enter the ingredient number")
                    allergyNo = input()
                    if allergyNo == "-1":
                        break
                userProfile.update({"allergies": allergies})
                userProfile.update({"Edit date": str(datetime.datetime.today())})
                write = allUsers
                with open('userinformation.txt', 'w') as writeFile:
                    writeFile.write(json.dumps(write))
                    writeFile.close()
    if operation == "2":
        del allUsers[Name]
        write = allUsers
        with open('userinformation.txt', 'w') as writeFile:
            writeFile.write(json.dumps(write))
            writeFile.close()



    pass


def validateUser(userProfile):
    if userProfile:
        Name = userProfile.get("Name")
        print("is this your user? (y/n)")
        print(allUsers.get(Name))
        valid = input()
        if valid == "y" or valid == "Y":
            userProfile = allUsers.get(Name)
            return userProfile, Name
            pass
    else:
        print("enter the name of your user")
        Name = input()
        if allUsers.get(Name) == None:
            print("user does not exist")
            validateUser(userProfile)
        print("is this your user? (y/n)")
        print(allUsers.get(Name))
        valid = input()
        if valid == "y" or valid == "Y":
            userProfile = allUsers.get(Name)
            return userProfile, Name
            pass
        elif valid == "n" or valid == "N":
            print("would you like to create a new user? (y/n)")
            creation = input().lower()
            if creation == "n":
               validateUser(userProfile)
            elif creation == "y":
                userProfile = createUser()
                Name = userProfile.get("Name")
                return userProfile, Name

    pass

def createUser():
    print("Enter your desired user name")
    Name = input()
    print("Enter your body weight in Kilograms")
    weight = input()
    print("Enter your height in meters")
    height = input()
    print("Enter your birth date (dd/mm/yyyy)")
    BirthDate = input()
    print("Enter you gender (M/F)")
    gender = input()
    BirthDate = datetime.datetime.strptime(BirthDate, "%d/%m/%Y").date()
    currentDate = datetime.datetime.today().date()
    age = currentDate.year - BirthDate.year
    if (currentDate.month - BirthDate.month) < 0:
        age -= 1
    elif (currentDate.month - BirthDate.month) == 0 and (currentDate.day - BirthDate.day) < 0:
        age -= 1
    BMI = float(weight) / (float(height) ** 2)
    BMIrange = ""
    if BMI < 18.5:
        BMIrange = "underweight"
    elif 24.9 > BMI >= 18.5:
        BMIrange = "normal"
    elif 29.9 >= BMI >= 25:
        BMIrange = "overweight"
    elif BMI >= 30.0:
        BMIrange = "obese"
    if gender == "f" or gender == "F":
        BMR = 655.1 + (9.563 * float(weight)) + (1.85 * float(height) * 100) - (4.676 * age)
    elif gender == "m" or gender == "M":
        BMR = 66.47 + (13.75 * float(weight)) + (5.003 * float(height) * 100) - (6.755 * age)
    print("Please choose your preferred activity level (Enter a Number)")
    print("1. Little/No exercise")
    print("2. Light exercise")
    print("3. Moderate exercise (2-3 days a week)")
    print("4. very active (6-7 days a week)")
    print("5. Extra active (very active and physical job)")
    activity_level = activity_level_selector.get(input())
    TEE = BMR * activity_level
    print("please select any of the following ingredients in case of allergies or enter -1 if you have none")
    allergies = []
    with open('ingredients.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            i = 16
            print(((i - int(len(row[0]))) * ' ').join(row))
    csvfile.close()
    allergyNo = input()
    if allergyNo != "-1":
        while True:
            with open('ingredients.csv') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=';')
                for row in spamreader:
                    for field in row:
                        if field == allergyNo:
                            allergy = row[0]
                            allergies.append(allergy)
            csvfile.close()
            print("enter the ingredient number")
            allergyNo = input()
            if allergyNo == "-1":
                break
    joinDate = currentDate
    with open("userInformation.txt", "r") as userFile:
        allData = userFile.read()
        userFile.close()
    BMR = format(BMR, '.2f')
    BMI = format(BMI, '.2f')
    TEE = format(TEE, '.2f')
    if fileSize != 0:
        userInfo = ast.literal_eval(allData)
        userInfo[Name] = {"join Date": str(joinDate), "Name": Name, "gender": gender, "height": height,
                          "weight": weight,
                          "date of birth": str(BirthDate), "age": age, "BMI": BMI, "BMI range": BMIrange,
                          "BMR": BMR,
                          "activity": activity_level, "TEE": TEE, "allergies": allergies}
    elif fileSize == 0:
        userInfo = {}
        userInfo[Name] = {"join Date": str(joinDate), "Name": Name, "gender": gender, "height": height,
                          "weight": weight,
                          "date of birth": str(BirthDate), "age": age, "BMI": BMI, "BMI range": BMIrange,
                          "BMR": BMR,
                          "activity": activity_level, "TEE": TEE, "allergies": allergies}
    write = userInfo
    with open('userinformation.txt', 'w') as appendF:
        appendF.write(json.dumps(write))
        appendF.close()
    return userInfo

    pass


def generateReciepe(userProfile, Name):
    RecipesNames = []
    RecipesCals= 0
    if Name:
        print(f"HI {Name}")
        RecipesFile = open(f"{Name}-recipes.txt", 'w')
        print("you can perform the following")
        print("1. Generate recipes randomly")
        print("2. Generate recipes randomly based on your caloric needs")
        print("3. Generate recipes randomly based on food allergies")
        print("4. Generate recipes randomly based on caloric needs and food allergies")
        reciepeOP = input()
        if reciepeOP == "1":
            print("you can generate 4-6 recipes, how many would you like to generate?")
            genNo = int(input())
            if genNo in range(4, 7):
                i = 0
                while i < genNo:
                    with open("recipes 2.csv") as csvFile:
                        reciepes = csv.reader(csvFile, delimiter=';')
                        row = random.choice(list(reciepes))
                        print(
                            f"Recipe Name : {row[1]} \n Calories : {row[9]}\n Servings : {row[10]}\n Prep Time : {row[4]}\n Cook Time : {row[5]}\n Total Time : {row[6]}\n Ingredients : {row[7]}\n Method : {row[8]}")
                        print(f"\n do you like this recipe? (y/n)")
                        answer = input()
                        if answer == "y" or answer == "Y":
                            i += 1
                            RcName = row[1]
                            RcCal = row[9]
                            RecipesNames.append(RcName)
                            RecipesCals += float(RcCal)

                        elif answer == "n" or answer == "N":
                            continue
                currentDate = datetime.datetime.today().date()
                currentTime = datetime.datetime.today().time()
                dicKey = int(currentTime.minute) + int(currentTime.hour)
                format(dicKey, '.2f')
                avgCals = RecipesCals / genNo
                format(avgCals, '.2f')
                fileSize = os.path.getsize(f"{Name}-recipes.txt")
                if fileSize == 0:
                    RecipeCsvWrite = {}
                    RecipeCsvWrite[str(dicKey)] = {"Names": RecipesNames, "Total Cals": RecipesCals, "average Caloris": avgCals,
                                      "Session Date": str(currentDate)}
                    RecipesFile.write(json.dumps(RecipeCsvWrite))
                    RecipesFile.close()
                else:
                    RecipeCsvWrite = ast.literal_eval(allData)
                    RecipeCsvWrite[str(dicKey)] = {"Names": RecipesNames, "Total Cals": RecipesCals,
                                                   "average Caloris": avgCals,
                                                   "Session Date": str(currentDate)}
                    RecipesFile.write(json.dumps(RecipeCsvWrite))
                    RecipesFile.close()
        elif reciepeOP == "2":
            print("you can generate 4-6 recipes, how many would you like to generate?")
            genNo = int(input())
            if genNo in range(4, 7):
                i = 0
                while i < genNo:
                    Tee = userProfile.get("TEE")
                    CaloricNeed = float(Tee)/genNo
                    with open("recipes 2.csv") as csvFile:
                        reciepes = csv.reader(csvFile, delimiter=';')
                        row = random.choice(list(reciepes))
                        CaloricLimit = float(row[9])/int(row[10])
                        if CaloricLimit <= CaloricNeed:
                            print(f"your Caloric Need is {CaloricNeed}")
                            print(f"Calories per serving in the Following reciepe is {CaloricLimit} ")
                            print(
                                f"Recipe Name : {row[1]} \n Calories : {row[9]}\n Servings : {row[10]}\n Prep Time : {row[4]}\n Cook Time : {row[5]}\n Total Time : {row[6]}\n Ingredients : {row[7]}\n Method : {row[8]}")
                            print(f"\n do you like this recipe? (y/n)")
                            answer = input()
                            if answer == "y" or answer == "Y":
                                i += 1
                                RcName = row[1]
                                RcCal = row[9]
                                RecipesNames.append(RcName)
                                RecipesCals += float(RcCal)

                            elif answer == "n" or answer == "N":
                                continue
                currentDate = datetime.datetime.today().date()
                currentTime = datetime.datetime.today().time()
                dicKey = int(currentTime.minute) + int(currentTime.hour)
                format(dicKey, '.2f')
                avgCals = RecipesCals / genNo
                format(avgCals, '.2f')
                fileSize = os.path.getsize(f"{Name}-recipes.txt")
                if fileSize == 0:
                    RecipeCsvWrite = {}
                    RecipeCsvWrite[str(dicKey)] = {"Names": RecipesNames, "Total Cals": RecipesCals,
                                                   "average Caloris": avgCals,
                                                   "Session Date": str(currentDate)}
                    RecipesFile.write(json.dumps(RecipeCsvWrite))
                    RecipesFile.close()
                else:
                    RecipeCsvWrite = ast.literal_eval(allData)
                    RecipeCsvWrite[str(dicKey)] = {"Names": RecipesNames, "Total Cals": RecipesCals,
                                                   "average Caloris": avgCals,
                                                   "Session Date": str(currentDate)}
                    RecipesFile.write(json.dumps(RecipeCsvWrite))
                    RecipesFile.close()
        elif reciepeOP == "3":
            print("you can generate 4-6 recipes, how many would you like to generate?")
            genNo = int(input())
            if genNo in range(4, 7):
                i = 0
                while i < genNo:
                    allergies = userProfile.get("allergies")
                    if allergies:
                        print(f"your allergies are:{allergies}")
                        with open("recipes 2.csv") as csvFile:
                            reciepes = csv.reader(csvFile, delimiter=';')
                            row = random.choice(list(reciepes))
                            allergicSet = set(allergies)
                            RcIng = list(row[7])
                            allergicIngs = allergicSet.intersection(RcIng)
                            if allergicIngs:
                                continue
                            else:
                                print(
                                    f"Recipe Name : {row[1]} \n Calories : {row[9]}\n Servings : {row[10]}\n Prep Time : {row[4]}\n Cook Time : {row[5]}\n Total Time : {row[6]}\n Ingredients : {row[7]}\n Method : {row[8]}")
                                print(f"\n do you like this recipe? (y/n)")
                                answer = input()
                                if answer == "y" or answer == "Y":
                                    i += 1
                                    RcName = row[1]
                                    RcCal = row[9]
                                    RecipesNames.append(RcName)
                                    RecipesCals += float(RcCal)

                                elif answer == "n" or answer == "N":
                                    continue
                    else:
                        print("you dont have any allergies")
                        break
                currentDate = datetime.datetime.today().date()
                currentTime = datetime.datetime.today().time()
                dicKey = int(currentTime.minute) + int(currentTime.hour)
                format(dicKey, '.2f')
                avgCals = RecipesCals / genNo
                format(avgCals, '.2f')
                fileSize = os.path.getsize(f"{Name}-recipes.txt")
                if fileSize == 0:
                    RecipeCsvWrite = {}
                    RecipeCsvWrite[str(dicKey)] = {"Names": RecipesNames, "Total Cals": RecipesCals,
                                                   "average Caloris": avgCals,
                                                   "Session Date": str(currentDate)}
                    RecipesFile.write(json.dumps(RecipeCsvWrite))
                    RecipesFile.close()
                else:
                    RecipeCsvWrite = ast.literal_eval(allData)
                    RecipeCsvWrite[str(dicKey)] = {"Names": RecipesNames, "Total Cals": RecipesCals,
                                                   "average Caloris": avgCals,
                                                   "Session Date": str(currentDate)}
                    RecipesFile.write(json.dumps(RecipeCsvWrite))
                    RecipesFile.close()
        elif reciepeOP == "4":
            print("you can generate 4-6 recipes, how many would you like to generate?")
            genNo = int(input())
            if genNo in range(4, 7):
                i = 0
                while i < genNo:
                    allergies = userProfile.get("allergies")
                    if allergies:
                        Tee = userProfile.get("TEE")
                        print(f"your allergies are:{allergies}")
                        with open("recipes 2.csv") as csvFile:
                            reciepes = csv.reader(csvFile, delimiter=';')
                            row = random.choice(list(reciepes))
                            allergicSet = set(allergies)
                            RcIng = list(row[7])
                            allergicIngs = allergicSet.intersection(RcIng)
                            CaloricNeed = float(Tee) / genNo
                            CaloricLimit = float(row[9]) / int(row[10])
                            if allergicIngs:
                                continue
                            elif CaloricLimit <= CaloricNeed:
                                print(f"your Caloric Need is {CaloricNeed}")
                                print(f"Calories per serving in the Following reciepe is {CaloricLimit} ")
                                print(
                                    f"Recipe Name : {row[1]} \n Calories : {row[9]}\n Servings : {row[10]}\n Prep Time : {row[4]}\n Cook Time : {row[5]}\n Total Time : {row[6]}\n Ingredients : {row[7]}\n Method : {row[8]}")
                                print(f"\n do you like this recipe? (y/n)")
                                answer = input()
                                if answer == "y" or answer == "Y":
                                    i += 1
                                    RcName = row[1]
                                    RcCal = row[9]
                                    RecipesNames.append(RcName)
                                    RecipesCals += float(RcCal)

                                elif answer == "n" or answer == "N":
                                    continue
                    else:
                        print("you dont have any allergies")
                        break
                currentDate = datetime.datetime.today().date()
                currentTime = datetime.datetime.today().time()
                dicKey = int(currentTime.minute) + int(currentTime.hour)
                format(dicKey, '.2f')
                avgCals = RecipesCals / genNo
                format(avgCals, '.2f')
                fileSize = os.path.getsize(f"{Name}-recipes.txt")
                if fileSize == 0:
                    RecipeCsvWrite = {}
                    RecipeCsvWrite[str(dicKey)] = {"Names": RecipesNames, "Total Cals": RecipesCals,
                                                   "average Caloris": avgCals,
                                                   "Session Date": str(currentDate)}
                    RecipesFile.write(json.dumps(RecipeCsvWrite))
                    RecipesFile.close()
                else:
                    RecipeCsvWrite = ast.literal_eval(allData)
                    RecipeCsvWrite[str(dicKey)] = {"Names": RecipesNames, "Total Cals": RecipesCals,
                                                   "average Caloris": avgCals,
                                                   "Session Date": str(currentDate)}
                    RecipesFile.write(json.dumps(RecipeCsvWrite))
                    RecipesFile.close()


    else : 
        print("No User Profile Loaded")
        userProfile, Name = validateUser(userProfile)
        generateReciepe(userProfile, Name)
    pass


def displayRecipe(name):
    with open("recipes 2.csv") as csvFile:
        reciepes = csv.reader(csvFile, delimiter=';')
        for row in reciepes:
            if name == row[1]:
                print(
                    f" Recipe Name : {row[1]} \n Calories : {row[9]}\n Servings : {row[10]}\n"
                    f" Prep Time : {row[4]}\n Cook Time : {row[5]}\n Total Time : {row[6]}\n"
                    f" Ingredients : {row[7]}\n Method : {row[8]}")
                print(f"\nhow many servings would you like to analyze thier health stats")
                servings = int(input())
                RcCal = row[9]
                RcServ = row[10]
                calPerServ = float(RcCal) / float(RcServ)
                userCals = servings * calPerServ
                return userCals, calPerServ, servings
    pass


def printRecipe(userProfile, item):
    reciepesNewCals = []
    totalCals = 0
    for name in item:
        userCals, calPerServ, servings = displayRecipe(name)
        totalCals += userCals
        userCals = format(userCals, '.2f')
        print(f"Your meal has {userCals} calories")
        tee = userProfile.get("TEE")
        if (float(tee) / servings) < calPerServ:
            print("You Have calorie surplus")
        else:
            print("you have Calorie deficit")
        reciepesNewCals.append(userCals)
    return totalCals, reciepesNewCals
    pass


def updatereciepes(key, totalCals, Name):
    with open(f"{Name}-recipes.txt") as reciepeCsv:
        userRecipes = reciepeCsv.read()
        recipeChoice = ast.literal_eval(userRecipes)
        sessionDict = recipeChoice.get(key)
        Names = sessionDict.get("Names")
        totalCals = format(totalCals, '.2f')
        sessionDict.update({"Total Cals" : totalCals})
        mealsNo = len(Names)
        avgCals = float(totalCals) / mealsNo
        avgCals = format(avgCals, '.2f')
        sessionDict.update({"average Caloris": avgCals})
        recipeChoice[key] = sessionDict
        write = recipeChoice
        with open(f"{Name}-recipes.txt", 'w') as writeFile:
            writeFile.write(json.dumps(write))
            writeFile.close()

        return totalCals, avgCals
    pass


def PlotPie(userCalories):
    plt.pie(userCalories )
    plt.show()
    pass


def generateHealthInfo(userProfile, Name):
    allCalLists = []
    if userProfile:
        File = open(f"{Name}-recipes.txt", 'a')
        File.close()
        fileSize = os.path.getsize(f"{Name}-recipes.txt")
        if fileSize != 0:
            with open(f"{Name}-recipes.txt") as reciepeCsv:
                userRecipes = reciepeCsv.read()
                recipeChoice = ast.literal_eval(userRecipes)
                for key, value in recipeChoice.items():
                    sessionDict = recipeChoice.get(key)
                    Names = sessionDict.get("Names")
                    totalCals, userCalories = printRecipe(userProfile, Names)
                    totalCaloriess, avgCals = updatereciepes(key, totalCals, Name)
                    print(f"Your New Total Calories = {totalCaloriess}")
                    print(f"Your New Average Calories = {avgCals}")
                    tee = userProfile.get("TEE")
                    if float(tee) < totalCals:
                        print("you are suffering from calorie surplus")
                    else:
                        print("your are experiencing calorie deficit")
                plotVar = userCalories
                PlotPie(plotVar)
        else:
            print("you Dont have any recipe sessions")
            print("please generate recipes")
            generateReciepe(userProfile, Name)
            generateHealthInfo(userProfile, Name)
    else:
        Profile, Name = validateUser(userProfile)
        generateHealthInfo(Profile, Name)
    pass

userProfile = {}
while True:
    print("Select the number of your desired task")
    print("1. create or load a new user profile")
    print("2. edit or delete existing user profile")
    print("3. view user profile")
    print("4. Generate recipe recommendations for the session")
    print("5. View user meals and generate health information")
    print("6. Exit the program")
    task_number = input()
    userName = ''
    if task_number == "1":
        print("do you have an existing user? (y/n)")
        user_existing = input()
        if user_existing == "y" or user_existing == "Y":
            userProfile, Name = validateUser(userProfile)
        elif user_existing == "n" or user_existing == "N":
            userProfile = createUser()
            with open("userInformation.txt", "r") as userFileR:
                allData = userFileR.read()
            allUsers = ast.literal_eval(allData)
            userFileR.close()

    if task_number == "2":
        if userProfile:
            editOrDelete(Name)
        else:
            userProfile, Name = validateUser(userProfile)
            editOrDelete(Name)
    if task_number == "3":
        userProfile, Name = validateUser(userProfile)
    if task_number == "4":
        generateReciepe(userProfile, Name)
    if task_number == "5":
        generateHealthInfo(userProfile, Name)
    if task_number == "6":
        break
