class Authenticate():
    def sign_in(self, credential_dict) -> bool:
        username = input("Enter your username : ")

        if (username not in credential_dict):
            print("\nUser not present.\n")
            return self.sign_in()

        password = input("Enter your password : ")

        value = credential_dict[username]

        retrieved_password = ""
        stripped_password = value.strip()
        unicode_array = stripped_password.split(" ")

        for _ in unicode_array:
            unicode = int(_)
            real_value = chr(unicode - 1)
            retrieved_password += real_value

        return True if (password == retrieved_password) else False

    def sign_up(self, credential_dict) -> dict:
        credentials = credential_dict
        username = input("Enter username : ")

        if (username not in credentials):
            password = input("Enter password: ")

            cipher_password = ""
            for _ in password:
                unicode = ord(_) + 1
                cipher_password += str(unicode) + " "

            credentials[username.lower()] = cipher_password

        else:
            print("\nUsername is taken.\n")
            self.sign_up()

        return credentials
