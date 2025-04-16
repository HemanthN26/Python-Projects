def highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    max(bidding_dictionary)

    for bidder in bidding_dictionary:
        bid_amount = int(bidding_dictionary[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the highest bit of ${highest_bid}")

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = input("What is your bid: $")
    bids[name] = price
    to_continue = input("Are there any bidders? Type 'Yes' or 'No'").lower()
    if to_continue == "no":
        continue_bidding = False
        highest_bidder(bids)
    elif to_continue == 'yes':
        print("\n" * 20)

