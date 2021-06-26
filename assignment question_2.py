order_Amount = float(input("What is the order amount?"))
state = str(input("What is the state?")).upper()
if state == "WI" :
    tax = order_Amount * 5.5/100
    total = order_Amount + tax
    print("The subtotal is ",order_Amount)
    print("The tax is ",tax)
    print("The total is ",total)
else:
    print("The total is ",order_Amount)
