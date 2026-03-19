print("\nLemonHealth v1")

def get_choice(prompt, valid_choices, error_text="Invalid selection. Please try again."):
    valid_choices = {choice.lower().strip() for choice in valid_choices}
    while True:
        value = input(prompt).lower().strip()
        if value in valid_choices:
            return value
        print(error_text)


def get_positive_float(prompt):
    while True:
        value = input(prompt).strip()
        try:
            number = float(value)
            if number <= 0:
                print("Please enter a number greater than zero.")
                continue
            return number
        except ValueError:
            print("Invalid number. Please enter numeric digits only.")


def get_positive_int(prompt):
    while True:
        value = input(prompt).strip()
        try:
            number = int(value)
            if number <= 0:
                print("Please enter an integer greater than zero.")
                continue
            return number
        except ValueError:
            print("Invalid integer. Please enter numeric digits only.")


def basic_data():
    return get_positive_int("Age: ")


def genderselection():
    print("Gender related data will only be used for classification of BAI")
    return get_choice("Insert M for men, or W for women: ", ["m", "w"], "Invalid gender. Please insert M or W.")


def unitselection():
    print("We recommend using metric units for calculations, but using imperial units is also available as an option")
    unit = get_choice(
        "Insert I to calculate using imperial units,\nM to calculate using metric units: ",
        ["m", "i"],
        "Invalid unit. Please type M or I."
    )
    if unit == 'm':
        print("Metric unit based calculation was chosen, so enter lengths in meters, and weight in kg")
    else:
        print("Imperial unit based calculation was chosen, so enter lengths in inches, and weight in lbs")
    return unit


def regioninput():
    return get_choice("Insert G for non-asian users, A for asian users: ", ["g", "a"], "Invalid region. Please insert G or A.")


def heightengine(unit):
    if unit == 'm':
        return get_positive_float("Insert height in meters: ")
    return get_positive_float("Insert height in inches: ") / 39.37


def weightengine(unit):
    if unit == 'm':
        return get_positive_float("Insert weight in kg: ")
    return get_positive_float("Insert weight in lbs: ") / 2.205


def bmi():
    print("Let's calculate your BMI")
    unit = unitselection()
    h = heightengine(unit)
    w = weightengine(unit)
    region = regioninput()
    bmi_value = w / (h**2)
    print(f"BMI: {bmi_value:.2f}")
    BMIclass(region, bmi_value)
    return bmi_value


def BMIclass(region, bmi):
    if region == 'g':
        if bmi <= 18.5:
            print("You are classified as 'Underweight'")
        elif bmi < 25:
            print("You are classified as 'Normal'")
        elif bmi < 30:
            print("You are classified as 'Overweight'")
        else:
            print("You are classified as 'Obese'")
    else:
        if bmi <= 18.5:
            print("You are classified as 'Underweight'")
        elif bmi < 23:
            print("You are classified as 'Normal'")
        elif bmi < 27:
            print("You are classified as 'Overweight'")
        else:
            print("You are classified as 'Obese'")


def hipengine(unit):
    if unit == 'm':
        return get_positive_float("Insert hip circumference in cm: ")
    return get_positive_float("Insert hip circumference in inches: ") * 2.54


def bai():
    print("Let's calculate your BAI")
    unit = unitselection()
    h = heightengine(unit)
    hc = hipengine(unit)
    gender = genderselection()
    age = basic_data()
    bai_value = hc / (h**1.5)
    print(f"BAI: {bai_value:.2f}")
    BAIclass(gender, age, bai_value)
    return bai_value


def BAIclass(gender, age, bai):
    if age < 20:
        print("We are unable to categorize BAI for people under 20")
        return

    if gender == 'w':
        if age < 40:
            thresholds = [(21, "Underweight"), (33, "Healthy"), (39, "Overweight")]
        elif age < 60:
            thresholds = [(23, "Underweight"), (35, "Healthy"), (41, "Overweight")]
        else:
            thresholds = [(25, "Underweight"), (38, "Healthy"), (43, "Overweight")]
    else:
        if age < 40:
            thresholds = [(8, "Underweight"), (21, "Healthy"), (26, "Overweight")]
        elif age < 60:
            thresholds = [(11, "Underweight"), (23, "Healthy"), (29, "Overweight")]
        else:
            thresholds = [(13, "Underweight"), (25, "Healthy"), (31, "Overweight")]

    for threshold, label in thresholds:
        if bai < threshold:
            print(f"You are classified as '{label}'")
            return
    print("You are classified as 'Obese'")


def waistengine(unit):
    if unit == 'm':
        return get_positive_float("Insert waist in cm: ")
    return get_positive_float("Insert waist in inches: ") * 2.54


def whr():
    print("Let's calculate your WHR")
    unit = unitselection()
    wc = waistengine(unit)
    hc = hipengine(unit)
    gender = genderselection()
    whr_value = wc / hc
    print(f"WHR: {whr_value:.2f}")
    WHRclass(gender, whr_value)
    return whr_value


def WHRclass(gender, whr):
    if gender == 'm':
        if whr <= 0.95:
            label = "low health risk"
        elif whr <= 1.0:
            label = "moderate health risk"
        else:
            label = "high health risk"
        print(f"You are classified as having a '{label}'")
    else:
        if whr <= 0.80:
            label = "low health risk"
        elif whr <= 0.85:
            label = "moderate health risk"
        else:
            label = "high health risk"
        print(f"You are classified as having a '{label}'")


def MultiMeasure():
    print("\nLet's proceed with MultiMeasure")
    print("MultiMeasure function will calculate all health functions available in the program")
    print("All required data will be collected once, then all calculations will be presented together.\n")

    unit = unitselection()
    height = heightengine(unit)
    weight = weightengine(unit)
    waist = waistengine(unit)
    hip = hipengine(unit)
    gender = genderselection()
    age = basic_data()
    region = regioninput()

    bmi_result = weight / (height**2)
    bai_result = hip / (height**1.5)
    whr_result = waist / hip

    print("\n" + "-" * 50)
    print("LEMONHEALTH MULTIMEASURE RESULTS")
    print("-" * 50)

    print(f"\nBody Mass Index (BMI): {bmi_result:.2f}")
    BMIclass(region, bmi_result)

    print(f"\nBody Adiposity Index (BAI): {bai_result:.2f}")
    BAIclass(gender, age, bai_result)

    print(f"\nWaist-to-Hip Ratio (WHR): {whr_result:.2f}")
    WHRclass(gender, whr_result)

    print("\n" + "=" * 50)


def modeSelection():
    print("\nWhat do you want to calculate?")
    print("BMI- Body Mass Index \nBAI- Body Adiposity Index \nWHR- Waist to Hip Ratio\nMM- MultiMeasure")
    print("MultiMeasure function will run all supported functions methodically")
    while True:
        opt = get_choice("\nBMI/BAI/WHR/MM: ", ["bmi", "bai", "whr", "mm"], "Input error. Choose BMI, BAI, WHR or MM.")
        if opt == 'bmi':
            bmi()
            break
        elif opt == 'bai':
            bai()
            break
        elif opt == 'whr':
            whr()
            break
        elif opt == 'mm':
            MultiMeasure()
            break


if __name__ == "__main__":
    modeSelection()
    print("\nLemonHealth v1")
    input("Press enter to close the program")
