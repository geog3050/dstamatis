def determine_leaf_status(climate, temperatures):
    threshold_temperatures = {
        "Tropical": 30,
        "Continental": 25
    }
    threshold = threshold_temperatures.get(climate, 18)

    for temp in temperatures:
        if temp <= threshold:
            print("F")  # Leaf folded
        else:
            print("U")  # Leaf unfolded


if __name__ == "__main__":
    climate = input("Enter climate (Tropical, Continental, or other): ")
    temperatures = eval(input("Enter temperatures as a list of floats: "))

    determine_leaf_status(climate, temperatures)




