def calculate_bmi(weight, height):
    if height <= 0:
        raise ValueError("Height must be greater than 0")
    bmi = weight / (height ** 2)
    return round(bmi, 2)
