from imports import *


class Main():
    enroled_students = {
        "maths": {
            "m1": {
                "age": 21,
                "disable": "n",
                "phone_number": "9816048093"
            },
        },
        "biology": {
            "b1": {
                "age": 21,
                "disable": "y",
                "phone_number": "9816045793"

            }
        },
        "commerce": {
            "c1": {
                "age": 21,
                "disable": "n",
                "phone_number": "9816047593"

            }
        }
    }
    credentials = {
        "bhupender": "98 ",
        "aman": "98 ",
    }

    def print_enroled_students():
        print("--------------------------------------")
        for k, v in Main.enroled_students.items():
            print(f"{k} : {v}")
        print("--------------------------------------")

    def print_credentials():
        print("--------------------------------------")
        for k, v in Main.credentials.items():
            print(f"{k} : {v}")
        print("--------------------------------------")


def main() -> None:
    say = Response()
    auth = Authenticate()
    enrol = EnrolStudent()

    say.greetings()

    have_account = input("Do You Have An Account? (y / n) : ")
    os.system('clear')

    while (have_account != 'y') and (have_account != 'n'):
        say.not_valid_response()
        have_account = input("Do You Have An Account? (y / n) : ")
        os.system('clear')

    if (have_account.lower() == 'y'):
        say.sign_in_label()
        while (not auth.sign_in(Main.credentials)):
            print("\nWrong Password!\n")
        os.system('clear')
        print("\nWelcome!\n")

    elif (have_account.lower() == 'n'):
        say.sign_up_label()
        Main.credentials = auth.sign_up(Main.credentials)
        os.system('clear')
        print("\nWelcome!\n")

    AvailableSeats.total_seats()

    print("In Which Course Do You Want To Enroll:\n1 -> Maths\n2 -> Biology\n3 -> Commerce")

    selected_course = input("\nEnter Your Choice : ")
    os.system('clear')
    while (selected_course != '1') and (selected_course != '2') and (selected_course != '3'):
        say.not_valid_response()
        selected_course = input("\nEnter Your Choice (1 / 2 / 3): ")
        os.system('clear')

    if (selected_course == '1'):
        if (not AvailableSeats.seats_available_maths()):
            print("\nNo Seats Available In Maths Department.\n")
            AvailableSeats.total_seats()
            say.farewell()
            sys.exit()

    elif (selected_course == '2'):
        if (not AvailableSeats.seats_available_biology()):
            print("\nNo Seats Available In Biology Department.\n")
            AvailableSeats.total_seats()
            say.farewell()
            sys.exit()

    elif (selected_course == '3'):
        if (not AvailableSeats.seats_available_commerce()):
            print("\nNo Seats Available In Commerce Department.\n")
            AvailableSeats.total_seats()
            say.farewell()
            sys.exit()

    say.enrolment_form()
    age = int(input("Enter Your Age : "))
    while (age <= 0 or age >= 90):
        say.not_valid_response()
        age = int(input("Enter Your Age : "))

    disable = input("Do You Have Any Disability (y / n) : ")
    while (disable != 'y' and disable != 'n'):
        say.not_valid_response()
        disable = input("Do You Have Any Disability (y / n) : ")

    phone_number = input("Enter Your Phone Number : ")

    if (selected_course == '1'):
        if (disable == 'y'):
            AvailableSeats.rsv_maths -= 1

        AvailableSeats.maths -= 1
        Main.enroled_students = enrol.apply(
            "maths", age, disable, phone_number, Main.enroled_students)

    elif (selected_course == '2'):
        if (disable == 'y'):
            AvailableSeats.rsv_biology -= 1

        AvailableSeats.biology -= 1
        Main.enroled_students = enrol.apply(
            "biology", age, disable, phone_number, Main.enroled_students)

    elif (selected_course == '3'):
        if (disable == 'y'):
            AvailableSeats.rsv_commerce -= 1

        AvailableSeats.commerce -= 1
        Main.enroled_students = enrol.apply(
            "commerce", age, disable, phone_number, Main.enroled_students)
    
    AvailableSeats.total_seats()
    os.system('clear')

    exit_choice = input("Do You Want To Restart The System (y / n) : ")
    while (exit_choice != 'y') and (exit_choice != 'n'):
        say.not_valid_response()
        exit_choice = input("Do You Want To Restart The System (y / n) : ")
        os.system('clear')

    # Main.print_credentials()
    # Main.print_enroled_students()
    if (exit_choice != 'y'):
        sys.exit()
    elif (exit_choice != 'n'):
        main()


if __name__ == "__main__":
    main()
