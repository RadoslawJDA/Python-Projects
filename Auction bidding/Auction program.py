a = 0


def max_bidder():
    max_bid = 0

    for bid in bids:
        if bids[bid] > max_bid:
            max_bid = bids[bid]
            winner = bid
            print(f"Winner of an auction is {winner} with {max_bid}$ bid")


while a == 0:
    name = input("Type in your name: ")
    price = int(input("Type in your bid: "))

    bids = {name: price}

    choice = input("Is there another person who wants to bid? Y or N: ")
    if choice == "N":
        a = 1
        max_bidder()
