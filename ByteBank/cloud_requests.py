import scratchattach as sa
import traceback
import main
import notifications_transactions
import leaderboard
import my_secrets  # This imports USERNAME and PASSWORD

session = sa.login(my_secrets.USERNAME, my_secrets.PASSWORD)
cloud = session.connect_cloud("1026899140") #replace with your project id


client = cloud.requests()


@client.request
def ping(): #called when client receives request
    print("pong")
    return "pong" #sends back 'pong' to the Scratch project

@client.request
def get_balance():
    print(client.get_requester().lower())

    try:
        balance = main.get_value(client.get_requester().lower())
        formatted_message = f"You have {balance} dollar(s)"
        return balance
    except Exception as e:
        print(f"Error retrieving balance for {client.get_requester()}: {e}")
        return "Error retrieving balance. Check the Python console for details."

    

@client.request
def pay(to, amount, message):
    
    try:
        user = sa.get_user(to)
        from_user = session.connect_user(client.get_requester()) # Returns a sa.User object
    except:
        return("user non existent")


    if from_user.is_new_scratcher() == False:
        
        try:
            print(client.get_requester())
            print(to)
            print(int(amount))
            username = str(client.get_requester()).lower()

            return_value = main.pay_user(client.get_requester().lower(), str(to).lower(), amount, message)
                
            if return_value == "failed":
                return("error")
            else:
                return main.get_value(username)  # Simply return the value from main.pay_user()
        except Exception as e:
            print(e)
            traceback.print_exc()

            return("error")
    else:
        return("error")


@client.request
def get_notifications():
    return main.view_notifications(str(client.get_requester()).lower())

@client.request
def get_all_info():
    username = str(client.get_requester()).lower()
    
    bytes = str(main.get_value(username))
    
    notif = main.view_notifications(str(client.get_requester()).lower())
    
    return bytes + "^" + notif
    
    
    

@client.request
def clear_notifications():
    notifications_transactions.clear_notifications(str(client.get_requester()).lower())
    return()



@client.request
def get_leaderboard():
    return leaderboard.get()

@client.request
def get_transactions(keyword):
    return notifications_transactions.find_transactions(keyword)


@client.event
def on_ready():
    print("Request handler is running")

client.start() #make sure this is ALWAYS at the bottom of your Python file
