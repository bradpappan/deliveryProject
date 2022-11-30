# Brad Pappan, Student ID - 002656581
import datetime
import packages


print("Parcel Service")
print("Total miles for all three truck delivery routes is: " + packages.total_miles())

program_start = input("Type 'begin' to start the program and display where the packages are by time, or type "
                      "'exit' to quit.")

if program_start == "begin":
    try:
        location_lookup = input("Enter a time to check where a package is using HH:MM:SS format.")
        (hh, mm, ss) = location_lookup.split(":")
        time_conversion = datetime.timedelta(hours=int(hh), minutes=int(mm), seconds=int(ss))

    except ValueError:
        print("Invalid entry")
        exit()
