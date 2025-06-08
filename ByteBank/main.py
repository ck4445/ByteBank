import json
import numpy as np
import leaderboard
import notifications_transactions

startmoney = 1000

data = {
}


def read_file():
    f = open("/home/pi/Python_Projects/ByteBank/data.txt", "r")
    file_contents = f.read()
    f.close()
    return(file_contents)

def write_file(content):
    f = open("/home/pi/Python_Projects/ByteBank/data.txt", "w")
    f.write(json.dumps(content))
    f.close()
    

def add_save(key, value):
    data = json.loads(read_file())
    data[key] = value
    write_file(data)
    print(f"Added user: {key} with balance: {value}")  # Print confirmation message
    return "done"

def get_value(username):
    data = dict(json.loads(read_file()))
      # Print the loaded data dictionary

    if not username in data:
        add_save(username, startmoney)
    else:
        print(f"Found user: {username}")  # Print if user exists

    return data.get(username)

def pay_user(from_user, to_user, amount):

    data = json.loads(read_file())


    if not to_user in data:
        data[to_user] = startmoney 
        write_file(data)

    if not int(data.get(from_user)) >= int(amount) or int(amount) <= 0:
            print("failed")
            return("failed")
    else:
        data[from_user] = int(data.get(from_user)) - int(amount)
        data[to_user] = int(data.get(to_user)) + int(amount)
        write_file(data)
        notifications_transactions.new_notification(to_user, from_user, amount)
       
        return("successful")
        
def sort():
    output = leaderboard.sort(json.loads(read_file()))
    return()
        
        



    

    


