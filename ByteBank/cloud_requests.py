import scratchattach as scratch3
import main
import notifications_transactions
import leaderboard

session = scratch3.login("1", "2")
conn = session.connect_cloud("3") #replace with your project id


client = scratch3.CloudRequests(conn)

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
def pay(to, amount):
	try:
		user = scratch3.get_user(to)

	except:
		return("user non existent")
	try:	
		print(client.get_requester())
		print(to)
		print(int(amount))
		username = str(client.get_requester()).lower()

		return_value = main.pay_user(client.get_requester().lower(), str(to).lower(), amount)
			
		if return_value == "failed":
			return("error")
		else:
			return main.get_value(username)  # Simply return the value from main.pay_user()
	except:
		return("error")



@client.request
def get_notifications():
    return notifications_transactions.view_notifications(str(client.get_requester()).lower())

@client.request
def get_all_info():
    username = str(client.get_requester()).lower()
    
    bytes = str(main.get_value(username))
    
    notif = notifications_transactions.view_notifications(str(client.get_requester()).lower())
    
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

client.run(no_packet_loss=True) #make sure this is ALWAYS at the bottom of your Python file
