TICKET_PRICE = 10

service_charge = 2

tickets_remaining = 100  

def calculate_price( number_of_tickets):
  return (number_of_tickets * TICKET_PRICE) + service_charge

while tickets_remaining != 0:

  name = input("What is your name please  ")
  
  print(f" Hello {name}, there are {tickets_remaining} tickets remaing.")
  
  
  number_of_tickets = int(input(f"Alright {name}, how many tickets would you like to purchase today?   "))
  
  if number_of_tickets > tickets_remaining:
    print(f"sorry {name} we only have {tickets_remaining} left")
    
    continue
  
  price_of_purchased_tickets = calculate_price( number_of_tickets)
  
  total_due = (f" Hey {name}, the price of the tickets would be {price_of_purchased_tickets}.")
  
  print(total_due)
  
  confirm_purchase = input("Would you like to purchase these tickets YES/NO ? ")
  
  if confirm_purchase.lower() == "yes":
     # run credit card to purchase tickets 
    print( f" tickets SOLD thank you {name} for your purchase")
    tickets_remaining -= number_of_tickets
    
    
  else:
    print(f" Thanks Anyways {name}")
    
  print( f" there are {tickets_remaining} tickets remaing")
  
  
print( f" sorry {name} we are all sold out")
  
    