# Brad Pappan, Student ID - 002656581
import datetime

import Hash
import distances
import packages


class Main:
    global time_conversion
    print("Parcel Service")
    print("Total miles for all three truck delivery routes is: " + packages.first_truck.mileage +
          packages.second_truck.mileage + packages.third_truck.mileage)

    program_start = input("Type 'begin' to start the program, or type 'exit' to quit.")


    if program_start == "begin":
        try:
            print("\n Please select one of the options to search for a package")
            print("1) Check where a package is")
            print("2) Look up a single package\n")
            print("3) Check the status of all packages\n")

            selection = input("Enter the number for the choice: ")

            if selection == '1':
                location_lookup = input("Enter a time to check where a package is using HH:MM:SS format.")
                (hh, mm, ss) = location_lookup.split(":")
                time_conversion = datetime.timedelta(hours=int(hh), minutes=int(mm), seconds=int(ss))

            if selection == '2':
                package_id_input = input("Enter the package ID")
                package_needed = Hash.my_hash.search(int(package_id_input))
                packages.current_status(time_conversion)

            if selection == '3':


