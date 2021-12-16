from datetime import datetime



class PoolTable:
    def __init__(self, pool_table_number):
        self.table_number = pool_table_number
        self.is_occupied = False
        self.start_time = None
        self.end_time = None
        self.time_played = None
        self.cost = None
                         

    def check_in(self):
            self.is_occupied = False
            self.end_time = datetime.now()
            self.time_played = self.end_time - self.start_time
            self.total_time_minutes = float(self.time_played.total_seconds() / 60)      # calculating elaspe time from when table was checked out in minutes
            self.total_time_hours = float(self.total_time_minutes / 60)
            self.formatted_minutes = "{:.2f}".format(self.total_time_minutes)           # formatting float to only have 2 decimal places
            self.formatted_hours = "{:.2f}".format(self.total_time_hours)
            if self.total_time_minutes >= 60:
                print(f"\n~.*.~ You've checked in Table: {self.table_number} || Time Played : {self.formatted_hours} hour(s) ~.*.~")
            else:
                self.total_time_minutes = float(self.time_played.total_seconds() / 60)
                print(f"\n~.*.~ You've checked in Table: {self.table_number} || Time Played : {self.formatted_minutes} minutes ~.*.~")
            
            self.cost = self.total_time_minutes * .5                                    # calculating cost, $30 per hour
            self.formatted_cost = "{:.2f}".format(self.cost)                            # formatting cost
            print(f"\nBill: ${self.formatted_cost}")
            


    def check_out(self):
            self.is_occupied = True
            self.start_time = datetime.now()
            print(f"\n~.*.~ You've checked out Table {self.table_number} ~.*.~")


    

    
