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
    traceback.print_stack()

def validate_order(order_id):
    print(f">> Validating Order #{order_id}")
    process_order(order_id)
    print(f">> Validation Completed #{order_id}")

def recieve_order(order_id):
    print(f"Recieving order #{order_id}")
    validate_order(order_id)
    print(f">> Order Recieved #{order_id}")

recieve_order(67)
print("Finished")