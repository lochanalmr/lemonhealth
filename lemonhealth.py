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
        h = input("Insert height in meters: ")
        return float(h)
    elif unit == 'i':
        h = input("Insert height in inches: ")
        return float(h) / 39.37
    else:
        print("Invalid input")

def weightengine(unit):
    if unit == 'm':
        w = input("Insert weight in kg: ")
        return float(w)
    elif unit == 'i':
        w = input("Insert weight in lbs: ")
        return float(w) / 2.205
    else:
        print("Invalid input")
    
def bmi():
    print("Let's calculate your BMI")
    unit = unitselection()
    h = heightengine(unit)
    w = weightengine(unit)
    region = regioninput()
    bmi = w / (h**2)
    print(bmi)
    BMIclass(region, bmi)
    return float(bmi)

def BMIclass(region, bmi):
    if region=='g':
        if bmi<=18.5:
            print("You are classified as 'Underweight'")
        elif 18.5<=bmi<25:
            print("You are classified as 'Normal'")
        elif 25<=bmi<30:
            print("You are classified as 'Overweight'")
        elif bmi>=30:
            print("You are classified as 'Obese'")

    elif region=='a':
        if bmi<=18.5:
            print("You are classified as 'Underweight'")
        elif 18.5<=bmi<23:
            print("You are classified as 'Normal'")
        elif 23<=bmi<27:
            print("You are classified as 'Overweight'")
        elif bmi>=27:
            print("You are classified as 'Obese'")

def hipengine(unit):
    if unit == 'm':
        h = input("Insert hip circumference in cm: ")
        return float(h)
    elif unit == 'i':
        h = input("Insert hip circumference in inches: ")
        return (float(h) / 39.37) * 100
    else:
        print("Invalid input")

def bai():
    print("Let's calculate your BAI")
    unit = unitselection()
    h = heightengine(unit)
    hc = hipengine(unit)
    gender = genderselection()
    age = basic_data()
    bai = hc / (h**(1.5))
    print(bai)
    BAIclass(gender, age, bai)
    return bai

def BAIclass(gender, age, bai):
    if gender=='w':
        if age<20:
            print("We are unable to categorize BAI for people under 20")
        elif 20<=age<40:
            if bai<21:
                print("You are classified as 'Underweight'")
            elif 21<=bai<33:
                print("You are classified as 'Healthy'")
            elif 33<=bai<39:
                print("You are classified as 'Overweight'")
            elif bai>=39:
                print("You are classified as 'Obese'")
        elif 40<=age<60:
            if bai<23:
                print("You are classified as 'Underweight'")
            elif 23<=bai<35:
                print("You are classified as 'Healthy'")
            elif 35<=bai<41:
                print("You are classified as 'Overweight'")
            elif bai>=41:
                print("You are classified as 'Obese'")
        elif 60<age:
            if bai<25:
                print("You are classified as 'Underweight'")
            elif 25<=bai<38:
                print("You are classified as 'Healthy'")
            elif 38<=bai<43:
                print("You are classified as 'Overweight'")
            elif bai>=43:
                print("You are classified as 'Obese'")

    elif gender=='m':
        if age<20:
            print("We are unable to categorize BAI for people under 20")
        elif 20<=age<40:
            if bai<8:
                print("You are classified as 'Underweight'")
            elif 8<=bai<21:
                print("You are classified as 'Healthy'")
            elif 21<=bai<26:
                print("You are classified as 'Overweight'")
            elif bai>=26:
                print("You are classified as 'Obese'")
        elif 40<=age<60:
            if bai<11:
                print("You are classified as 'Underweight'")
            elif 11<=bai<23:
                print("You are classified as 'Healthy'")
            elif 23<=bai<29:
                print("You are classified as 'Overweight'")
            elif bai>=29:
                print("You are classified as 'Obese'")
        elif 60<age:
            if bai<13:
                print("You are classified as 'Underweight'")
            elif 13<=bai<25:
                print("You are classified as 'Healthy'")
            elif 25<=bai<31:
                print("You are classified as 'Overweight'")
            elif bai>=31:
                print("You are classified as 'Obese'")

def waistengine(unit):
    if unit == 'm':
        wc = input("Insert waist in cm: ")
        return float(wc)
    elif unit == 'i':
        wc = input("Insert waist in inches: ")
        return float(wc) * 2.54
    else:
        print("input error")

def whr():
    print("Let's calculate your WHR")
    unit = unitselection()
    wc = waistengine(unit)
    hc = hipengine(unit)
    gender = genderselection()
    whr = wc / hc
    print(whr)
    WHRclass(gender, whr)
    return whr

def WHRclass(gender, whr):
    if gender=='m':
        if whr<=0.95:
            print("You are classified as having a 'low health risk'")
            print("Health risk is commonly defined as increased risk of 'Cardiovascular diseases', 'Type-2 diabetes' in men")
            print("'Low health risk' predicts that you have a lower chance to develop above conditions")
        elif 0.95<whr<=1.0:
            print("You are classified as having a 'moderate health risk'")
            print("Health risk is commonly defined as increased risk of 'Cardiovascular diseases', 'Type-2 diabetes' in men")
            print("'Moderate health risk' predicts that you have a moderate chance to develop above conditions")
        elif whr>1.0:
            print("You are classified as having a 'high health risk'")
            print("Health risk is commonly defined as increased risk of 'Cardiovascular diseases', 'Type-2 diabetes' in men")
            print("'High health risk' predicts that you have a higher chance to develop above conditions")

    elif gender=='w':
        if whr<=0.80:
            print("You are classified as having a 'low health risk'")
            print("Health risk is commonly defined as increased risk of 'Cardiovascular diseases', 'Type-2 diabetes', 'Lower fertility' in women")
            print("'Low health risk' predicts that you have a lower chance to develop above conditions")
        elif 0.80<whr<=0.85:
            print("You are classified as having a 'moderate health risk'")
            print("Health risk is commonly defined as increased risk of 'Cardiovascular diseases', 'Type-2 diabetes', 'Lower fertility' in women")
            print("'Moderate health risk' predicts that you have a moderate chance to develop above conditions")
        elif whr>0.85:
            print("You are classified as having a 'high health risk'")
            print("Health risk is commonly defined as increased risk of 'Cardiovascular diseases', 'Type-2 diabetes', 'Lower fertility' in women")
            print("'High health risk' predicts that you have a higher chance to develop above conditions")

def MultiMeasure():
    print("\nLet's proceed with MultiMeasure")
    print("MultiMeasure function will calculate all health functions available in the program")
    print("All required data will be collected once, then all calculations will be presented together.\n")
    
    # Collect all data once
    unit = unitselection()
    height = heightengine(unit)
    weight = weightengine(unit)
    waist = waistengine(unit)
    hip = hipengine(unit)
    gender = genderselection()
    age = basic_data()
    region = regioninput()
    
    # Calculate all metrics
    bmi_result = weight / (height**2)
    bai_result = hip / (height**(1.5))
    whr_result = waist / hip
    
    # Display all results
    print("\n" + "="*50)
    print("MULTIMEASURE RESULTS")
    print("="*50)
    
    print(f"\nBody Mass Index (BMI): {bmi_result:.2f}")
    BMIclass(region, bmi_result)
    
    print(f"\nBody Adiposity Index (BAI): {bai_result:.2f}")
    BAIclass(gender, age, bai_result)
    
    print(f"\nWaist-to-Hip Ratio (WHR): {whr_result:.2f}")
    WHRclass(gender, whr_result)
    
    print("\n" + "="*50)

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
