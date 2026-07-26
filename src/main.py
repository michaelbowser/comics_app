
from repositories.publisher import (
    add_publisher,
    get_all_publishers,
)

def display_menu():
    print("\nComic Database")
    print("_" * 30)
    print("1. List publishers")
    print("2. Add publisher")
    print("3. Exit")

def list_publishers():
     publishers = get_all_publishers()

     print("\nPublishers\n")

     for publisher_id, name in publishers:
        print(f"{publisher_id}: {name}")

def create_publisher():
     name = input("\nPublisher name: ").strip()

     if not name:
        print("Publisher name cannot be empty.")
        return 

     publisher_id = add_publisher(name)

     print(f"\nPublisher created with ID {publisher_id}")

def main():

     while True:
        display_menu()

        choice = input("\nChoice: ").strip()

        if choice == "1":
            list_publishers()

        elif choice == "2":
            create_publisher()

        elif choice == "3":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice.")


if __name__ == "__main__":
    main()



