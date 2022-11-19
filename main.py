# Brad Pappan, Student ID - 002656581
import distances
import packages


class Main:
    print("Parcel Service")
    print("Total miles for all three truck delivery routes is: " + packages.first_truck.mileage +
          packages.second_truck.mileage + packages.third_truck.mileage)

    program_start = input("Type 'begin' to start the program, or type 'exit' to quit.")


    if program_start == "begin":
        try:
            print("\n Please select one of the options to search package by ID")
            print("1) Look up a single package\n")
            print("2) Check the status of all packages\n")

            selection = input("Enter the the number for the choice: ")

