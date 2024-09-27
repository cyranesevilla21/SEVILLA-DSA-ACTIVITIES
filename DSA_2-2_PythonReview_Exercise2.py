def calculate_voltage(current, resistance):
    #Calculates Voltage using Ohm's Law: V = I * R
    return current * resistance

def calculate_current(voltage, resistance):
    #Calculates Current using Ohm's Law: I = V / R
    if resistance == 0:
        return None  
    return voltage / resistance

def calculate_resistance(voltage, current):
    #Calculates Resistance using Ohm's Law: R = V / I
    if current == 0:
        return None  
    return voltage / current

def main():
    # Ask the user what they want to calculate
    print("Ohm's Law Calculator")
    print("1. Calculate Voltage (V)")
    print("2. Calculate Current (I)")
    print("3. Calculate Resistance (R)")
    
    try:
        choice = int(input("Enter your choice (1, 2, or 3): "))
    except ValueError:
        print("Invalid input! Please enter 1, 2, or 3.")
        return

    if choice == 1:
        # Calculate Voltage
        try:
            current = float(input("Enter the current (I) in amperes: "))
            resistance = float(input("Enter the resistance (R) in ohms: "))
        except ValueError:
            print("Invalid input! Please enter numerical values.")
            return
        
        voltage = calculate_voltage(current, resistance)
        print(f"The voltage (V) is: {voltage:.2f} volts")

    elif choice == 2:
        # Calculate Current
        try:
            voltage = float(input("Enter the voltage (V) in volts: "))
            resistance = float(input("Enter the resistance (R) in ohms: "))
        except ValueError:
            print("Invalid input! Please enter numerical values.")
            return

        current = calculate_current(voltage, resistance)
        if current is None:
            print("Error: Resistance cannot be zero when calculating current.")
        else:
            print(f"The current (I) is: {current:.2f} amperes")

    elif choice == 3:
        # Calculate Resistance
        try:
            voltage = float(input("Enter the voltage (V) in volts: "))
            current = float(input("Enter the current (I) in amperes: "))
        except ValueError:
            print("Invalid input! Please enter numerical values.")
            return

        resistance = calculate_resistance(voltage, current)
        if resistance is None:
            print("Error: Current cannot be zero when calculating resistance.")
        else:
            print(f"The resistance (R) is: {resistance:.2f} ohms")

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
