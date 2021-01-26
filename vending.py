

nike_items = {
    1: {'name': 'Air Max Plus', 'value': 125},
    2: {'name': 'Epic React Flynit', 'value': 150},
    3: {'name': 'Air VaporMax Flyknit 2', 'value': 190},
    4: {'name': 'Air Max', 'value': 150},
    5: {'name': 'Zoom Stefan Janoski', 'value': 85}
}

def refund_cal(refund):
    """
    rfund the amount in valid bill : 1, 5, 10, 25, 50, 100
    :param refund:
    :return:
    """
    print(f"*** the refund amount {refund}")
    while refund > 0:
        if refund // 50 > 0:
            n = refund // 50
            print(f"50 Bill * {n} = {n * 50}")
            refund -= (n * 50)
        elif refund // 25 > 0:
            n = refund // 25
            print(f"25 Bill * {n} = {n * 25}")
            refund -= (n * 25)
        elif refund // 5 > 0:
            n = refund // 5
            print(f" 5 Bill * {n} = {n * 5}")
            refund -= (n * 5)
        else:
            n = refund
            refund -= (n * 1)
            print(f" 1 Bill * {n} = {n * 1}")

def process_item(no):
    """
    print the purchased item details
    :param no: item number
    :return:
    """
    print("____________________________________________")
    print("Thank you for purchasing. Here is your item ")
    print(f"Item No   : {no}")
    print(f"Item Name : {nike_items[no]['name']}")
    print(f"Item No   : {nike_items[no]['value']}")
    print("____________________________________________")

def get_item_details():
    """
    display the nike items and its details from dictionary (database).
    request user to select the item number to purchase the item
    :return:
    """

    list_item()
    item_no = int(input("Select the Item No: "))
    if item_no in nike_items:
        return item_no
    else:
        for i in range(3):
            item_no = int(input("enter valid Item No: "))
            if item_no in nike_items:
                break
        else:
            print("sorry cannot process now : Max try reached!!")
            return None
    return item_no


def get_amount():
    """
    request user to enter the valid amount to puchase the item
    :return:
    """
    valid_bill = [1, 5, 10, 25, 50, 100]
    amount = int(input(f"Add the amount in {valid_bill}:"))
    while True:
        if amount in valid_bill:
            break
        else:
            amount = int(input(f"Add Valid amount in:{valid_bill}"))
    return amount


def list_item():
    """
    list the available item in dictionaries
    :return:
    """
    for key, value in nike_items.items():
        print(f"{key} : {value['name']} - ${value['value']}")


if __name__ == '__main__':
    print("Welcome to Nike Vending Machine")
    while True:
        item_no = get_item_details()
        if item_no:
            amount = get_amount()
            while amount < nike_items[item_no]['value']:
                amount += get_amount()

            process_item(item_no)
            if amount > nike_items[item_no]['value']:
                print("____________________________________________")
                print(f"total amount provided :{amount}")
                print("____________________________________________")
                refund = amount - nike_items[item_no]['value']
                refund_cal(refund)

        inp = input("Want to purchase another item (Y/n):")
        if inp == 'n':
            break

