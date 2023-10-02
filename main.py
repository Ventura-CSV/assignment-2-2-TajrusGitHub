def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    # Ask the user to enter a temperature in Celsius
    celsius = float(input("Enter temperature in Celsius: 42"))

    # Convert Celsius to Fahrenheit
    fahrenheit = celsius_to_fahrenheit(celsius)

    # Display the temperature in Fahrenheit with two decimal places
    print(f"Fahrenheit: {fahrenheit:.2f}")

    # Return the values (optional, as not specified in the instructions)
    return celsius, fahrenheit

if __name__ == '__main__':
    main()
