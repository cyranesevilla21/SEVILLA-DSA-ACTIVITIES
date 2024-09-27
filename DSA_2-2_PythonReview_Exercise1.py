def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    try:
        temperature = float(input("Enter the temperature you want to convert: "))
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return
    
    print("Select conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    try:
        conversion_type = int(input("Enter 1 or 2: "))
    except ValueError:
        print("Invalid input! Please enter 1 or 2.")
        return

    if conversion_type == 1:
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature}° Celsius is equal to {result:.2f}° Fahrenheit.")
    elif conversion_type == 2:
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature}° Fahrenheit is equal to {result:.2f}° Celsius.")
    else:
        print("Invalid option! Please enter 1 or 2.")

if __name__ == "__main__":
    main()
