from datetime import date
from datetime import datetime

def create_12_tables(pool_tables, PoolTable):
    number = 0
    while len(pool_tables) < 12:
        number += 1
        pool_tables.append(PoolTable(number))


def display_all_pool_tables(pool_tables):
    print("________________________________________\n\n")
    for pool_table in pool_tables:
        if pool_table.is_occupied == False:
            print(f"Pool Table {pool_table.table_number} - NOT OCCUPIED\n")
        else:
            print(f"Pool Table {pool_table.table_number} - OCCUPIED - {pool_table.start_time}\n")
    print("________________________________________")


def check_in_write_to_txt(pool_table):
    date_input = str(date.today())
    date_time_format = datetime.strptime(date_input, '%Y-%m-%d')
    new_format = str(date_time_format.strftime('%m-%d-%Y'))
    with open(f"{new_format}.txt", "a") as file:                    # Taking current date, injecting as a string 
        # If time exceeds 60 mins, will write to text HOURS instead of minutes
        if  pool_table.total_time_minutes >= 60:
            file.write(f"Pool Table: {pool_table.table_number}\nStart Time: {pool_table.start_time}\nEnd Time: {pool_table.end_time}\nTime Played: {pool_table.formatted_hours} hour(s)\nBill: ${pool_table.formatted_cost}")
            file.write("\n")
        else:
            file.write(f"Pool Table: {pool_table.table_number}\nStart Time: {pool_table.start_time}\nEnd Time: {pool_table.end_time}\nTime Played: {pool_table.formatted_minutes} minutes\nBill: ${pool_table.formatted_cost}")
            file.write("\n")


