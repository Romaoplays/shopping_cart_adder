import csv
import os


try:
    csv_file = open("shopping_cart.csv", encoding="utf-8-sig")
except FileNotFoundError:
    csv_file = open("shopping_cart.csv", "w", encoding="utf-8-sig")
    csv_file.close()


def get_total():
    csv_file = open("shopping_cart.csv", "r", encoding="utf-8-sig")
    csv_reader = csv.reader(csv_file)
    csv_list = list(csv_reader)
    total = 0
    for i in range(len(csv_list)):
        if csv_list[i] != []:
            total = total + (float(csv_list[i][1]) * float(csv_list[i][2]))
    csv_file.close()
    return round(total, 2)


def print_cart():
    csv_file = open("shopping_cart.csv", "r", encoding="utf-8-sig")
    i = 1
    csv_reader = csv.reader(csv_file)
    csv_list = list(csv_reader)
    if len(csv_list) != 0:
        print("\nCurrent Cart:")
        for j in range(len(csv_list)):
            if csv_list[j] != []:
                print(
                    f"{str(i)} - {csv_list[j][0]} || R$ {float(csv_list[j][1]):.2f} * {csv_list[j][2]}"
                )
                i = i + 1
        csv_file.close()
        print(f"\nTotal Cost: R$ {float(get_total()):.2f}")
    else:
        print("\nCart Empty!")


while True:
    print("\nWhat to do?\n1 - View Shopping Cart\n2 - Reset Shopping Cart")
    resposta = input()

    if resposta == "1":
        while True:

            print_cart()

            print("\nWhat to do?\n 1 - Add Item\n 2 - Remove Item\n 3 - Exit")
            resposta = input()
            if resposta == "1":
                lista_items = []
                print("\nItem Name:")
                lista_items.append(input())
                print("\nItem Price:")
                while True:
                    try:
                        lista_items.append(float(input()))
                        break
                    except ValueError:
                        print("--Please insert a valid number--")

                print("\nItem Quantity:")
                while True:
                    try:
                        lista_items.append(int(input()))
                        break
                    except ValueError:
                        print("--Please insert a valid number--")
                print(
                    f"\nItem: {lista_items[0]}\nPrice: R$ {lista_items[1]:.2f}\nQuantity: {lista_items[2]}"
                )
                while True:
                    print("\n\nConfirm? y/n")
                    resposta = input()
                    if resposta == "y":
                        csv_file = open("shopping_cart.csv", "a", encoding="utf-8-sig")
                        csv_writer = csv.writer(csv_file)
                        csv_writer.writerow(lista_items)
                        csv_file.close()

                        print("\n--Confirmed!--")

                        print(f"\nCurrent Total: R$ {get_total()}")

                        break

                    elif resposta == "n":
                        print("\n--Discarded!--")
                    else:
                        print("\n--Please select a valid input--")

            elif resposta == "2":
                print("Which line to remove?")

                csv_file = open("shopping_cart.csv", "r", encoding="utf-8-sig")
                csv_reader = csv.reader(csv_file)
                csv_list = list(csv_reader)
                csv_file.close()

                while True:
                    line_to_remove = input()
                    try:
                        line_to_remove = int(line_to_remove)
                    except ValueError:
                        print("\n--Please select a valid input--")
                        continue
                    j = 0
                    removal_list = []
                    for j in range(len(csv_list)):
                        if csv_list[j] != []:
                            removal_list.append(csv_list[j])

                    print(f"\nRow: {removal_list[line_to_remove-1]}")

                    while True:
                        print("\nConfirm? y/n")
                        resposta = input()
                        if resposta == "y":
                            removal_list.remove(removal_list[line_to_remove - 1])
                            os.remove("shopping_cart.csv")

                            csv_file = open(
                                "shopping_cart.csv", "w", encoding="utf-8-sig"
                            )
                            csv_writer = csv.writer(csv_file)
                            for i in range(len(removal_list)):
                                csv_writer.writerow(removal_list[i])

                            csv_file.close()

                            print("--Confirmed!--")
                            break

                        elif resposta == "n":
                            print("\n--Discarded!--")
                            break
                        else:
                            print("\n--Please select a valid input--")

                    break

            elif resposta == "3":
                break

    elif resposta == "2":
        csv_file.close()
        os.remove("shopping_cart.csv")
        csv_file = open("shopping_cart.csv", "w", encoding="utf-8-sig")
        csv_file.close()
        print("\n--File Cleared!--")

    else:
        print("\n--Please insert a valid number--")
