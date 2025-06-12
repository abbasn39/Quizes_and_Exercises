#Create a health management system witht 3 clients Harry, Rohan and Hammad. This system will log their exercise
# and meals along with time stamps. Create 6 different files each client will have 2 food logs and exercise logs.
# Use the following functions for time stamps.

def getdate():
    import datetime
    return datetime.datetime.now()

Clients=["harry","rohan","hammad"]
LogType=["exercise","meal"]
while True:
    client_input = input(f"Please choose from the following\n"
                         f"\n-Enter existing client name to log record. "
                         f"\n-Enter 'add' to add a client."
                         f"\n-Enter 'remove' to remove a client."
                         f"\n-Type 'exit' to quit:"
                         f"\n{Clients}\n").lower().strip()
    if client_input.lower() == "exit":
        print("Exiting Log. Goodbye!")
        break


    if client_input.lower() == "add":
        Add_Client=input("Please enter client's name to add to client list.\n").lower().strip()
        Clients.append(Add_Client)
        continue
    if client_input.lower() == "remove":
        Remove_Client=input("Please enter client's name to remove from client list.\n").lower().strip()
        Clients.remove(Remove_Client)
        print("Client Removed Successfully")
        continue
    if client_input not in Clients:
        print("Invalid client name. Try again.")
        continue
    logtype_input = input(f"Please enter log type:\n{LogType}\n").lower().strip()
    if logtype_input not in LogType:
        print("Invalid log type. Try again.")
        continue

    filename = f"{client_input}_{logtype_input}.txt"

    with open(filename, "a") as f:
        if logtype_input == "meal":
            Q = input("Enter quantity of food consumed:\n")
            F = input("Enter name of food consumed:\n")
            f.write(f"{getdate()}\tQuantity: {Q}\tFood: {F}\n")
        elif logtype_input == "exercise":
            S = input("Enter number of sets:\n")
            R = input("Enter number of reps:\n")
            E = input("Enter name of exercise:\n")
            f.write(f"{getdate()}\tSets x Reps = {S} x {R}  of {E}\n")

    print("Log saved successfully.")


#Note: On each run this program will reset the list to the above three names(Harry, Rohan, Hammad) ie all
# the added or removed clients will reset.