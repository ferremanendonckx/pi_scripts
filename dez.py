import random
import time


def get_random_temperature(min_temp, max_temp):
    # Generate a random temperature within the specified range
    return random.uniform(min_temp, max_temp)


def get_random_lux(min_lux, max_lux):
    # Generate a random lux value within the specified range
    return random.uniform(min_lux, max_lux)


def main():
    min_temp = 20  # Minimum temperature in Celsius
    max_temp = 22  # Maximum temperature in Celsius
    min_lux = 100  # Minimum lux value
    max_lux = 130  # Maximum lux value

    while True:
        # Generate random temperature and lux values
        temperature = get_random_temperature(min_temp, max_temp)
        lux = get_random_lux(min_lux, max_lux)

        # Print the temperature and lux values in the terminal
        print("Room Temperature: {:.2f}°C".format(temperature))
        print("Lux Value: {:.2f}".format(lux))

        # Wait for a short duration before generating the next temperature and lux values
        time.sleep(2)


if __name__ == "__main__":
    main()
