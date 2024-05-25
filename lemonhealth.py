print("\nLemonHealth v1")

def basic_data():
    age=input("Age: ")
    return int(age)

def genderselection():
    print("Gender related data will only be used for classification of BAI")
    gender=str(input("Insert M for men, or W for women "))
    return gender

def unitselection():
    print("We recommend using metric units for calculations, but using imperial units is also available as an option")
    unit=str(input("Insert I to calculate using imperial units,\nM to calculate using metric units ")).lower().strip()
    if unit == 'm':
        print("Metric unit based calculation was chosen, so enter lengths in meters, and weight in kg")
    elif unit == 'i':
        print("Imperial unit based calculation was chosen, so enter lengths in inches, and weight in lbs")
    else:
        print("Invalid input")
    return unit

def regioninput():
    region=str(input("Insert G for non-asian users, A for asian users ")).lower().strip()
    return region

def heightengine(unit):
    if unit == 'm':
        h = heightinput("Insert height in meters: ")
        return h
    elif unit == 'i':
        h = heightinput("Insert height in inches: ")
        return (h/39.37)
    else:
        print("Invalid input")

def weightengine(unit):
    if unit == 'm':
        w = weightinput("Insert weight in kg: ")
        return w
    elif unit == 'i':
        w = heightinput("Insert weight in lbs: ")
        return (w/2.205)
    else:
        print("Invalid input")
    
def bmi():
    print("Let's calculate your BMI")
    unit = unitselection()
    h = heightengine(unit)
    w = weightengine(unit)
    region = regioninput()
    bmi = w/ (h**2)
    bmi = bmi()
    print(bmi)
    BMIclass(region)
    return bmi

def BMIclass(region):
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

def hipengine(unit):
    if unit == 'm':
        h = input("Insert hip circumference in cm: ")
        return h
    elif unit == 'i':
        h = heightinput("Insert hip circumference in inches: ")
        return ((h/39.37)*(100))
    else:
        print("Invalid input")

def bai():
    print("Let's calculate your BMI")
    unit = unitselection()
    h = heightengine(unit)
    hc = hipengine(unit)
    gender = genderselection()
    age = basic_data()
    bai = hc / (h**(1.5))
    bai = bai()
    print(bai)
    BAIclass(gender, age)
    return bai

def BAIclass(gender, age):
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

def waistengine(unit):
    if unit == 'm':
        wc = input("Insert waist in cm: ")
        return wc
    elif unit == 'i':
        wc = input("Insert waist in inches: ")
        return wc
    else:
        print("input error")

def whr():
    print("Let's calculate your WHR")
    unit = unitselection()
    wc = waistengine(unit)
    hc = hipengine(unit)
    gender = genderselection()
    whr = wc / hc
    whr = whr()
    print(whr)
    WHRclass(gender)
    return whr

def WHRclass(gender):
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

    bmi = bmi()
    bai = bai()
    whr = whr()

def modeSelection():
    print("\nWhat do you want to calculate?")
    print("BMI- Body Mass Index \nBAI- Body Adiposity Index \nWHR- Waist to Hip Ratio\nMM- MultiMeasure")
    print("MultiMeasure function will run all supported functions methodically")
    opt = input("\nBMI/BAI/WHR/MM: ").lower().strip()
    
    if opt == 'bmi':
        bmi()
    elif opt == 'mm':
        MultiMeasure()
    elif opt == 'bai':
        bai()
    elif opt == 'whr':
        whr()
    else:
        print("input error")

modeSelection()

print("\nLemonHealth v1")
exitp = input("Press enter to close the program")
