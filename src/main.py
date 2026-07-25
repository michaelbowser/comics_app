
from repositories.publisher import (
    add_publisher,
    get_all_publishers,
)

def main():
    print("Current publishers:\n")

    for publisher_id, name in get_all_publishers():
        print(f"{publisher_id}: {name}")

    print("\nAdding Image Comics...\n")

    new_id = add_publisher("Image Comics")

    print(f"Created publisher #{new_id}")

    print("\nUpdated publisher list:\n")

    for publisher_id, name in get_all_publishers():
            print(f"{publisher_id}: {name}")

if __name__ == "__main__":
    main()
