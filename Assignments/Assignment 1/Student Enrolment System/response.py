class Response():
    def greetings(self) -> None:
        """Prints greeting message on the screen"""
        print("\n\
|----------------------------------------------|\n\
|                 -> WELCOME <-                |\n\
|                      TO                      |\n\
|            STUDENT ENROLMENT SYSTEM          |\n\
|----------------------------------------------|\n")

    def farewell(self) -> None:
        """Prints farewell message on the screen"""
        print("\n\
|----------------------------------------------|\n\
|                -> Thank You <-               |\n\
|                      For                     |\n\
|                Using The System              |\n\
|----------------------------------------------|\n")

    def not_valid_response(self) -> None:
        """Prints an error message on the screen"""
        print("\n\
|----------------------------------------------|\n\
|            Enter a valid Response.           |\n\
|----------------------------------------------|\n")

    def sign_in_label(self) -> None:
        """Prints title of the screen"""
        print("\n\
|----------------------------------------------|\n\
|                    Sign In                   |\n\
|----------------------------------------------|\n")

    def sign_up_label(self) -> None:
        """Prints title of the screen"""
        print("\n\
|----------------------------------------------|\n\
|                    Sign Up                   |\n\
|----------------------------------------------|\n")

    def enrolment_form(self)->None:
        """Prints title of the screen"""
        print("\n\
|----------------------------------------------|\n\
|                Enrolment Form                |\n\
|----------------------------------------------|\n")