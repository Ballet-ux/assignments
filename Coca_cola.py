def coke_machine():
    total_due = 50
    accepted_coins = [25, 10, 5]
    
    while total_due > 0:
        print(f"Amount due: {total_due} cents")
        coin = int(input("Insert coin (25, 10, or 5 cents): "))
        
        if coin in accepted_coins:
            total_due -= coin
        else:
            print("Invalid coin. Please insert 25, 10, or 5 cents only.")
    
    change = abs(total_due)
    print(f"Change owed: {change} cents")

# Run the coke machine function
coke_machine()
