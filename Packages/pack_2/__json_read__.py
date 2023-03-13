import json


class json_read():
    def __init__(self) -> None:
        pass

    def read(self, path) -> None:
        """
        Print a string of contents in file
        Requires path of file as a parameter
        """
        try:
            if path == None or path == "":
                raise FileNotFoundError
            else:
                with open(path, "r+") as file:
                    print(file.read())

        except FileNotFoundError:
            print("File Path Not Valid")

    def write(self, path, data) -> None:
        """
        Writes the data on the path file
        Requires path of file and data as a parameter
        """
        try:
            if path == None or path == "":
                raise FileNotFoundError
            else:
                with open(path, "w+") as file:
                    file.write(json.dumps(data, indent=2))

        except FileNotFoundError:
            print("File Path Not Valid")


# test = json_read()
# path1 = "Packages/data/sample.json"
# test.read(path1)

# path2 = "Packages/data/test.json"
# data = {
#     "name": "Ayush",
#     "url": "https://www.ayush.org",
#     "welcome_text": "Hello! How are you?"
# }
# test.write(path2, data)
# test.read(path2)
