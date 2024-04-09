print("\nLemonHealth v0.01")

def basicData():
    age=input("Age: ")
    return int(age)

def genderselection():
    print("Gender related data will only be used for classification of BAI")
    gender=str(input("Insert M for men, or W for women "))
    return gender

def unitselection():
    print("We recommend using metric units for calculations, but using imperial units is also available as an option")
    unit=str(input("Insert I to calculate using imperial units,\nM to calculate using metric units ")).lower().strip()
    return unit

def regioninput():
    region=str(input("Insert G for non-asian users, A for asian users ")).lower().strip()
    return region

def heightinput():
    h = float(input("Height: "))
    return h

def weightinput():
    w = float(input("Weight: "))
    return w

def heightengine(unit):
    if unit == 'm':
        print("Insert height in meters")
        h = heightinput()
        return h
    elif unit == 'i':
        print("Insert height in inches")
        h = heightinput()
        return (h/39.37)
    else:
        print("Invalid input")

def weightengine(unit):
    if unit == 'm':
        print("Insert weight in kg")
        w = weightinput()
        return w
    elif unit == 'i':
        print("Insert weight in lbs")
        w = heightinput()
        return (w/2.205)
    else:
        print("Invalid input")
    
def bmi():
    print("Let's calculate your BMI")
    unit = unitselection()
    h = heightengine(unit)
    w = weightengine(unit)
    bmi = w/ (h**2)
    return bmi

def BMIclass():
    bmi = bmi()
    print("Regional data will be used for BMI classification, according to your region")
    region = regioninput()
    print(bmi)

    if region=='g':
        if bmi<=18.5:
            print("You are classified as 'Underweight'")
        if 18.5<=bmi<25:
            print("You are classified as 'Normal'")
        if 25<=bmi<30:
            print("You are classified as 'Overweight'")
        if bmi>=30:
            print("You are classified as 'Obese'")

    if region=='a':
        if bmi<=18.5:
            print("You are classified as 'Underweight'")
        if 18.5<=bmi<23:
            print("You are classified as 'Normal'")
        if 23<=bmi<27:
            print("You are classified as 'Overweight'")
        if bmi>=27:
            print("You are classified as 'Obese'")

#need to insert bmi like function to calculate bai, and functions to retreive other needed data

def BAIclass():
    gender = genderselection()
    age = basicData()
    bai = bai()

    if gender=='w':
           if age<20:
               print("We are unable to categorize BAI for people under 20")
           if 20<=age<40:
               if bai<21:
                   print("You are classified as 'Underweight'")
               if 21<=bai<33:
                   print("You are classified as 'Healthy'")
               if 39>bai>=33:
                   print("You are classified as'Overweight'")
               if bai>=39:
                   print("You are classified as 'Obese'")
           if 40<=age<60:
               if bai<23:
                   print("You are classified as 'Underweight'")
               if 23<=bai<35:
                   print("You are classified as 'Healthy'")
               if 41>bai>=35:
                   print("You are classified as'Overweight'")
               if bai>=41:
                   print("You are classified as 'Obese'")
           if 60<age:
               if bai<25:
                   print("You are classified as 'Underweight'")
               if 25<=bai<38:
                   print("You are classified as 'Healthy'")
               if 43>bai>=38:
                   print("You are classified as'Overweight'")
               if bai>=43:
                   print("You are classified as 'Obese'")

    if gender=='m':
           if age<20:
               print("We are unable to categorize BAI for people under 20")
           if 20<=age<40:
               if bai<8:
                   print("You are classified as 'Underweight'")
               if 8<=bai<21:
                   print("You are classified as 'Healthy'")
               if 26>bai>=21:
                   print("You are classified as'Overweight'")
               if bai>=26:
                   print("You are classified as 'Obese'")
           if 40<=age<60:
               if bai<11:
                   print("You are classified as 'Underweight'")
               if 11<=bai<23:
                   print("You are classified as 'Healthy'")
               if 29>bai>=23:
                   print("You are classified as'Overweight'")
               if bai>=29:
                   print("You are classified as 'Obese'")
           if 60<age:
               if bai<13:
                   print("You are classified as 'Underweight'")
               if 13<=bai<25:
                   print("You are classified as 'Healthy'")
               if 31>bai>=25:
                   print("You are classified as'Overweight'")
               if bai>=31:
                   print("You are classified as 'Obese'")


def WHRcalcclass():
    print("Let's calculate your WHR")
    print("The units of the inputs don't matter here, but make sure to use the same units")
    wcm=float(input("Waist circumference: "))
    hcm=float(input("Hip circumference: "))
    print("Gender related data will only be used for classification of BAI")
    gender=str(input("Insert M for men, or W for women ")).lower()
    whr=wcm/hcm
    print("WHR=",whr)

    if gender=='m':
        if whr<=0.95:
            print("You are classified as having a 'low health risk'")
            print("Health risk is commonly defined as increased risk of 'Cardiovascular diseases', 'Type-2 diabetes' in men")
            print("'Low health risk' predicts that you have a lower chance to develop above conditions")
        if 0.95<whr<=1.0:
            print("You are classified as having a 'moderate health risk'")
            print("Health risk is commonly defined as increased risk of 'Cardiovascular diseases', 'Type-2 diabetes' in men")
            print("'Moderate health risk' predicts that you have a moderate chance to develop above conditions")
        if whr>1.0:
            print("You are classified as having a 'high health risk'")
            print("Health risk is commonly defined as increased risk of 'Cardiovascular diseases', 'Type-2 diabetes' in men")
            print("'High health risk' predicts that you have a higher chance to develop above conditions")

    if gender=='w':
        if whr<=0.80:
            print("You are classified as having a 'low health risk'")
            print("Health risk is commonly defined as increased risk of 'Cardiovascular diseases', 'Type-2 diabetes', 'Lower fertility' in women")
            print("'Low health risk' predicts that you have a lower chance to develop above conditions")
        if 0.80<whr<=0.85:
            print("You are classified as having a 'moderate health risk'")
            print("Health risk is commonly defined as increased risk of 'Cardiovascular diseases', 'Type-2 diabetes', 'Lower fertility' in women")
            print("'Moderate health risk' predicts that you have a moderate chance to develop above conditions")
        if whr>0.85:
            print("You are classified as having a 'high health risk'")
            print("Health risk is commonly defined as increased risk of 'Cardiovascular diseases', 'Type-2 diabetes', 'Lower fertility' in women")
            print("'High health risk' predicts that you have a higher chance to develop above conditions")

def MultiMeasure():
    print("\nLet's proceed with MultiMeasure")
    print("MultiMeasure function will calculate all health functions available in the program")
    print("\nUsing metric units is recommended, but imperial unit based calculation is also available.")
    unit1=input("Enter M to calculate using metric units or I to calculate using imperial units: ").strip().lower()

    if unit1=='m':
        weight1m=float(input("\nWeight (kg): "))
        height1m=float(input("Height (m): "))
        hc1m=float(input("Hip Circumference (cm): "))
        wc1m=float(input("Waist cicumference (cm): "))
        print("\nAlright, required basic data was collected")
        print("Now, let's get the required data to classify your data")
        gender1 = genderselection()
        age1 = basicData()
        region1 = regioninput()
        print("\nAll required data is now collected.")
        print("Your inputs are being processed ...")
        bmi=weight1m/(height1m**2)
        bai=height1m/(hc1m**1.5-18)
        whr=hc1m/wc1m

        import time
        time.sleep(5)

        print("Let's see the results: ")
        print("BMI:",bmi)
        print("BAI: ",bai)
        print("WHR: ",whr)
        print("\nData is now being classified according to your age, region and gender...")

        time.sleep(5)
        print("Classification complete")

        if gender1=='m':
            print("\nWHR classification details: ")
            if whr<=0.95:
                print("You are classified as having a 'low health risk'")
                print("Health risk is commonly defined as increased risk of 'Cardiovascular diseases', 'Type-2 diabetes' in men")
                print("'Low health risk' predicts that you have a lower chance to develop above conditions")
            if 0.95<whr<=1.0:
                print("You are classified as having a 'moderate health risk'")
                print("Health risk is commonly defined as increased risk of 'Cardiovascular diseases', 'Type-2 diabetes' in men")
                print("'Moderate health risk' predicts that you have a moderate chance to develop above conditions")
            if whr>1.0:
                print("You are classified as having a 'high health risk'")
                print("Health risk is commonly defined as increased risk of 'Cardiovascular diseases', 'Type-2 diabetes' in men")
                print("'High health risk' predicts that you have a higher chance to develop above conditions")

            print("\nBAI classification details: ")
            if age1<20:
                print("We are unable to categorize BAI for people under 20")
            if 20<=age1<40:
               if bai<8:
                   print("You are classified as 'Underweight'")
               if 8<=bai<21:
                   print("You are classified as 'Healthy'")
               if 26>bai>=21:
                   print("You are classified as'Overweight'")
               if bai>=26:
                   print("You are classified as 'Obese'")
            if 40<=age1<60:
               if bai<11:
                   print("You are classified as 'Underweight'")
               if 11<=bai<23:
                   print("You are classified as 'Healthy'")
               if 29>bai>=23:
                   print("You are classified as'Overweight'")
               if bai>=29:
                   print("You are classified as 'Obese'")
            if 60<age1:
               if bai<13:
                   print("You are classified as 'Underweight'")
               if 13<=bai<25:
                   print("You are classified as 'Healthy'")
               if 31>bai>=25:
                   print("You are classified as'Overweight'")
               if bai>=31:
                   print("You are classified as 'Obese'")

            print("\nBMI classification details: ")
            if region1=='o':
                if bmi<=18.5:
                    print("You are classified as 'Underweight'")
                if 18.5<=bmi<25:
                    print("You are classified as 'Normal'")
                if 25<=bmi<30:
                    print("You are classified as 'Overweight'")
                if bmi>=30:
                    print("You are classified as 'Obese'")
            elif region1=='a':
                if bmi<=18.5:
                    print("You are classified as 'Underweight'")
                if 18.5<=bmi<23:
                    print("You are classified as 'Normal'")
                if 23<=bmi<27:
                    print("You are classified as 'Overweight'")
                if bmi>=27:
                    print("You are classified as 'Obese'")

def modeSelection():
    print("\nWhat do you want to calculate?")
    print("BMI- Body Mass Index \nBAI- Body Adiposity Index \nWHR- Waist to Hip Ratio\nMM- MultiMeasure")
    print("MultiMeasure function will calculate all other mentioned functions")
    opt=input("\nBMI/BAI/WHR/MM: ").lower().strip()
    if opt == 'bmi':
        BMIclass()
    if opt == 'mm':
        MultiMeasure()
    if opt == 'bai':
        bai()
    if opt == 'whr':
        WHRcalcclass()

modeSelection()

print("\nLemonHealth v0.01")
exitp=input("Press enter to close the program")
print("Goodbye, if you have enough time to read this, which means you need to check your PC right now :)")
print("Otherwise, you are trying to steal the code by opening this inside an ide :)")
