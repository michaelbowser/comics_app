from repositories.publisher import (
    add_publisher,
    get_all_publishers,
)
from repositories.series import (
     add_series,
     get_all_series,
) 

def display_menu():
    print("\nComic Database")
    print("_" * 30)
    print("1. List publishers")
    print("2. Add publisher")
    print("3. List series ")
    print("4. Add series ")
    print("5. Exit")

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

def list_series():

    print("\nSeries\n")

    for series_id, publisher, title, volume, start_year in get_all_series():

        print(
             f"{series_id}:"
             f"{publisher} | "
             f"{title} | "
             f"Vol. {volume} | "
             f"{start_year}"

        )

def create_series():
     print("\nAvailable Publishers\n")

     for publisher_id, name in get_all_publishers():
         print(f"{publisher_id}: {name}")

         publisher_id = int(input("\nPublisher ID: "))

         title = input("Series Title: ").strip()

         volume = int(input("Volume: "))

         start_year = int(input("Start Year:"))

         series_id = add_series(
             publisher_id,
             title,
             volume,
             start_year,
         )

         print(f"\nSeries created with ID {series_id}")

def main():

        while True:
            display_menu()
            
            choice = input("\nChoice: ").strip()


            match choice:

                case "1":
                    list_publishers()

                case "2":
                    create_publisher()

                case "3":
                    list_series()

                case "4":
                    create_series()

                case "5":
                    print("\nGoodbye!")
                    break

                case _:
                    print("\nInvalid choice")




if __name__ == "__main__":
    main()






