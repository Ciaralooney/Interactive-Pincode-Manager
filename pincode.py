# Name: Ciara Looney
def print_all(list_names, list_pincodes):
    print(f"Username\t Pincode\n"
          f"++++++++++++++++++")
    for i, element in enumerate(list_pincodes):
        print(f"{list_names[i]:1}\t\t{list_pincodes[i]}")


def change_pincode(name, list_names, list_pincodes):
    for i, element in enumerate(list_names):
        if name == list_names[i]:
            user_pin = int(input("Enter your old pin: "))
            if user_pin == list_pincodes[i]:
                while True:
                    try:
                        # updating the pin code
                        new_pin = int(input("Enter a new 6 digit pin: "))
                        # Validate the pincode which should be only a 6 digit number
                        if new_pin < 0 or new_pin > 6:
                            break
                        else:
                            print("Please enter a numeric 6 digit pin")
                    except ValueError:
                        print("Please enter a numeric value")

                # updating the pin code
                list_pincodes.append(new_pin)


def print_short_names(list_names):
    short_names = []
    for i, element in enumerate(list_names):
        # if the length of the word is less than 5
        if len(element) < 5:
            short_names.append(list_names[i])  # adding the short names ot the list
    else:
        pass

    return short_names


def main():
    list_names = ["Josephine", "Bran", "Charlie", "Gary", "Theta"]
    list_pincodes = [123456, 737564, 314325, 674982, 996633]
    name = input("Enter your name: ")
    change_pincode(name, list_names, list_pincodes)
    print_all(list_names, list_pincodes)
    print_short_names(list_names)
    short_names = print_short_names(list_names)
    print(f"Names less than 5 letters: {short_names}")


main()
