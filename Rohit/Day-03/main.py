import traceback

# def multiply(a,b):
#     return a*b

# def calculate_area(length,width):
#     area = multiply(length,width)
#     return area


# def main():
#     room_length = 5
#     room_width = 3
#     room_area = calculate_area(room_length, room_width)
#     print(room_area)
    
# main()

def process_order(order_id):
    print(f">> Processing Order #{order_id}")
    traceback.print(order_id)

def validate_order(order_id):
    print(f">> Validating Order #{order_id}")
    recieve(order_id)

def recieve(order_id):
    print(f"Recieving order #{order_id}")
    validate_order(order_id)

recieve(67)
print("Finished")