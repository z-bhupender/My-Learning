class AvailableSeats():
    maths = 30
    biology = 30
    commerce = 0

    rsv_maths = (maths * 10) // 100
    rsv_biology = (biology * 10) // 100
    rsv_commerce = (commerce * 10) // 100

    def total_seats() -> None:
        print("|----------------------------------------------|\n\
|             Total Seats Available            |\n\
|----------------------------------------------|\n\
|   Subjects   |   General   |   Handicapped   |\n\
|----------------------------------------------|")
        print(
            f"|   Maths      |      {AvailableSeats.maths - AvailableSeats.rsv_maths}     |        {AvailableSeats.rsv_maths}        |")
        print("|----------------------------------------------|")
        print(
            f"|   Biology    |      {AvailableSeats.biology - AvailableSeats.rsv_biology}     |        {AvailableSeats.rsv_biology}        |")
        print("|----------------------------------------------|")
        print(
            f"|   Commerce   |      {AvailableSeats.commerce - AvailableSeats.rsv_commerce}      |        {AvailableSeats.rsv_commerce}        |")
        print("|----------------------------------------------|")

        print("")

    def seats_available_maths() -> bool:
        return False if (AvailableSeats.maths == 0) else True

    def seats_available_biology() -> bool:
        return False if (AvailableSeats.biology == 0) else True

    def seats_available_commerce() -> bool:
        return False if (AvailableSeats.commerce == 0) else True
