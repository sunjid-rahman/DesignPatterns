class CelsiusTemperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def get_temperature_celsius(self):
        return self.temperature


class FahrenheitTemperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def get_temperature_fahrenheit(self):
        return self.temperature


class TemperatureAdapter:
    def get_temperature(self):
        pass


class CelsiusToFahrenheitAdapter(TemperatureAdapter):
    def __init__(self, celsius_temperature):
        self.celsius_temperature = celsius_temperature

    def get_temperature(self):
        celsius_temp = self.celsius_temperature.get_temperature_celsius()
        fahrenheit_temp = (celsius_temp * 9 / 5) + 32
        return fahrenheit_temp


class FahrenheitToCelsiusAdapter(TemperatureAdapter):
    def __init__(self, fahrenheit_temperature):
        self.fahrenheit_temperature = fahrenheit_temperature

    def get_temperature(self):
        fahrenheit_temp = self.fahrenheit_temperature.get_temperature_fahrenheit()
        celsius_temp = (fahrenheit_temp - 32) * 5 / 9
        return celsius_temp


if __name__ == "__main__":
    celsius_temp = CelsiusTemperature(20.0)
    fahrenheit_temp = CelsiusToFahrenheitAdapter(celsius_temp)
    print(f"The temperature in Fahrenheit is {fahrenheit_temp.get_temperature()} degrees.")

    fahrenheit_temp = FahrenheitTemperature(68.0)
    celsius_temp = FahrenheitToCelsiusAdapter(fahrenheit_temp)
    print(f"The temperature in Celsius is {celsius_temp.get_temperature()} degrees.")
