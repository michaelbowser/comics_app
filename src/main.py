
from repositories.owned_comic import (
    add_owned_comic,
    get_all_owned_comics,
)

from repositories.issue import (
    add_issue,
    get_all_issues,
    get_issues_by_series,
)

from repositories.publisher import (
    add_publisher,
    get_all_publishers,
)
from repositories.series import (
     add_series,
     get_all_series,
)
def display_menu():
    print("\nComic Database\n")
    print("---\n")
    print("1. List publishers")
    print("2. Add publisher")
    print("3. List series")
    print("4. Add series")
    print("5. List issues")
    print("6. Add issue")
    print("7. List owned comics")
    print("8. Add owned comic")
    print("9. Exit")

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

def list_issues():
    issues = get_all_issues()

    print("\nIssues\n")

    for issue_id, series_id, issue_number, publication_year, is_key_issue, variant in issues:
        key_status = "Yes" if is_key_issue else "No"
        variant_status = variant if variant else "None"

        print(
            f"Issue #{issue_number} | "
            f"Published: {publication_year} | "
            f"Key Issue: {key_status} | "
            f"Variant: {variant_status}"
        )   


def create_issue():
    
    series_id = int(input("\nSeries_id : ").strip())

    issue_number =int(input("\nIssue_number: ").strip())
    
    publication_year = input("\npublication_year: ").strip()

    key_issue = input("\nKey Issue? (y or n): ").strip().lower()
    is_key_issue = key_issue == "y"
 
    variant = input("\nVariant (press enter if none): ").strip()

    if not variant:
        variant = None
    
    issue_id = add_issue(
        series_id,
        issue_number,
        publication_year,
        is_key_issue,
        variant,
    )

    print(f"\nIssue created with ID {issue_id}")

def list_owned_comics():
    owned_comics = get_all_owned_comics()

    print("\nOwned Comics\n")

    for (
        owned_id,
        issue_id,
        title,
        issue_number,
        publication_year,
        is_key_issue,
        variant,
        box_id,
        box_label,
        box_location,
        grade,
        purchase_price,
        purchase_date,
        estimated_value,
        signed,
        certification_company,
        certification_number,
        notes,
    ) in owned_comics:

        key_status = "Yes" if is_key_issue else "No"
        variant_status = variant if variant else "None"
        box_status = box_label if box_label else "Unassigned"
        signed_status = "Yes" if signed else "No"

        print(
            f"{title} #{issue_number}\n"
            f"  Published: {publication_year}\n"
            f"  Key Issue: {key_status}\n"
            f"  Variant: {variant_status}\n"
            f"  Grade: {grade}\n"
            f"  Purchase Price: ${purchase_price}\n"
            f"  Purchase Date: {purchase_date}\n"
            f"  Estimated Value: ${estimated_value}\n"
            f"  Signed: {signed_status}\n"
            f"  Box: {box_status}\n"
            f"  Notes: {notes if notes else 'None'}\n"
        )

def create_owned_comic():
    issues = get_all_issues()

    print("\nAvailable Issues\n")

    for issue_id, series_id, issue_number, publication_year, is_key_issue, variant in issues:
        print(f"{issue_id}: Issue #{issue_number} ({publication_year})")

    issue_id = int(input("\nIssue ID: "))
    box_input = input("\nBox ID (press Enter if unassigned): ").strip()
    box_id = int(box_input) if box_input else None

    grade_input = input("\nGrade: ").strip()
    grade = float(grade_input)

    purchase_input = input("\nPurchase price: (Enter none if not known ) ").strip()

    if purchase_input.lower() == 'none':
        purchase_price = None
    else:
        purchase_price = float(purchase_input)

    
    purchase_date = input("\nPurchase date (YYYY-MM-DD):(press 0 if none)  ").strip()

    estimated_value = float(input("\nEstimated value: ").strip())

    signed_input = input("\nSigned? (y or n): ").strip().lower()
    signed = signed_input == "y"

    certification_company = input(
        "\nCertification company (press Enter if none): "
    ).strip()

    if not certification_company:
        certification_company = None

    certification_number = input(
        "\nCertification number (press Enter if none): "
    ).strip()

    if not certification_number:
        certification_number = None

    notes = input(
        "\nNotes (press Enter if none): "
    ).strip()

    if not notes:
        notes = None 

    owned_id = add_owned_comic(
        issue_id,
        box_id,
        grade,
        purchase_price,
        purchase_date,
        estimated_value,
        signed,
        certification_company,
        certification_number,
        notes,
    )
    print(f"\nOwned comic created with ID {owned_id}")


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
                list_issues()

            case "6":
                create_issue()

            case "7":
                list_owned_comics()

            case "8":
                create_owned_comic()

            case "9":
                print("\nGoodbye!")
                break

            case _:
                print("\nInvalid choice")




if __name__ == "__main__":
    main()






