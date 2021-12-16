# Creating a Pool Table Management App
from pool_table import PoolTable
from util import display_all_pool_tables
from util import create_12_tables
from util import check_in_write_to_txt


pool_tables = []

# Create 12 PoolTable Objects and append into pool_tables array
create_12_tables(pool_tables, PoolTable)

# Admin Main Menu
try:
    while True:
        print("________________________________________\n")
        print("Enter 1 to check out table")
        print("Enter 2 to check in table")
        print("Enter 3 to display all tables")
        print("Enter q to quit")
        print("________________________________________")
        choice = input("Enter Choice: ")

        # Checking in a table
        if choice == "1":
            display_all_pool_tables(pool_tables)
            table_choice = int(input("Enter table number to check-out: "))
            pool_table = pool_tables[table_choice - 1]

            # If table is already occupied, prompts user to choose different table
            if pool_table.is_occupied == True:
                print(f"\n~.*.~ Table {pool_table.table_number} is Occupied! ~.*.~\n")
                table_choice = int(input("Please choose another table: "))
                pool_table = pool_tables[table_choice - 1]
                pool_table.check_out()
            else:
                pool_table.check_out()

        # Checking out a table
        elif choice == "2":
            display_all_pool_tables(pool_tables)
            table_choice = int(input("Enter table number to check-in: "))
            pool_table = pool_tables[table_choice - 1]

            # If table is already unoccupied, prompts user to choose different table
            if pool_table.is_occupied == False:
                print(f"\n~.*.~ Table {pool_table.table_number} is already checked in! ~.*.~\n")
                table_choice = int(input("Please choose another table: "))
                pool_table = pool_tables[table_choice - 1]
                pool_table.check_in()
            else:    
                pool_table.check_in()
                check_in_write_to_txt(pool_table)
            
        # Display tables
        elif choice == "3":
            display_all_pool_tables(pool_tables)

        elif choice == "q":
            break

        else:
            print("\n")
            print("==============")
            print("Invalid Choice")
            print("==============")

        print("\n")
    
except IndexError:
    print("Please enter a number between 1-12 (inclusive)")

except TypeError:
    print("All pool tables are already checked out!")

except:
    print("Oops! Something bad happened!")