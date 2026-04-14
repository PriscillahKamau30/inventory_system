import requests

BASE_URL = "http://127.0.0.1:5555"


def menu():
    print("\n=== INVENTORY MENU ===")
    print("1. View All Products")
    print("2. Add Product")
    print("3. Get Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Exit")


# VIEW ALL
def view_products():
    res = requests.get(f"{BASE_URL}/inventory")
    print(res.json())


# ADD PRODUCT
def add_product():
    code = input("Enter barcode: ")

    res = requests.post(
        f"{BASE_URL}/inventory",
        json={"code": code}
    )

    print(res.json())


# GET ONE
def get_product():
    code = input("Enter barcode: ")

    res = requests.get(f"{BASE_URL}/inventory/{code}")
    print(res.json())


# UPDATE
def update_product():
    code = input("Enter barcode: ")
    name = input("Enter new name: ")

    res = requests.patch(
        f"{BASE_URL}/inventory/{code}",
        json={"name": name}
    )

    print(res.json())


# DELETE
def delete_product():
    code = input("Enter barcode: ")

    res = requests.delete(f"{BASE_URL}/inventory/{code}")
    print(res.json())


# MAIN LOOP
while True:
    menu()
    choice = input("Choose option: ")

    if choice == "1":
        view_products()
    elif choice == "2":
        add_product()
    elif choice == "3":
        get_product()
    elif choice == "4":
        update_product()
    elif choice == "5":
        delete_product()
    elif choice == "6":
        break
    else:
        print("Invalid choice")