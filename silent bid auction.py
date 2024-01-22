"Silent Bid Auction using python and os module"
import os 
def find_winner(bidder_info):
    highest_bid = 0
    winner = ""
    for bidders in bidder_info:
        bidding_price = bidder_info[bidders]
        if bidding_price > highest_bid:
            highest_bid = bidding_price
            winner = bidders
    print(f"Here is the details of all the bidders:")
    for i in bidder_info.items():
        print(f"\n\t\t {i}")
    print(f"\nThe winner is {winner} with the bit price of {highest_bid}")
        
bidder_data = {}
bidding = True
while bidding:
    name = input("Enter your name: ")
    price = int(input("What is your bid?: "))
    bidder_data[name]=price
    more_bidders = input("Are there any more bidders? Type 'yes' or 'no': ").lower()
    if more_bidders == 'no':
        bidding = False
        find_winner(bidder_data)
    elif more_bidders == 'yes':
        os.system('cls')