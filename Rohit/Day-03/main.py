import traceback
import inspect
# EXAMPLE 1

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

# EXAMPLE 02
# def process_order(order_id):
#     print(f">> Processing Order #{order_id}")
#     traceback.print_stack()

# def validate_order(order_id):
#     print(f">> Validating Order #{order_id}")
#     process_order(order_id)
#     print(f">> Validation Completed #{order_id}")

# def recieve_order(order_id):
#     print(f"Recieving order #{order_id}")
#     validate_order(order_id)
#     print(f">> Order Recieved #{order_id}")

# recieve_order(67)
# print("Finished")

#EXAMPLE 3

def calculate_tax(price, tax_rate):
    tax_amount = price * tax_rate
    
    print("=== Stack Frames With Variable ===\n")
    frame = inspect.currentframe()
    depth = 0
    
    while frame:
        name = frame.f_code.co_name
        local_vars = frame.f_locals.copy()
        
        for var in ['frame', 'depth','name', 'local_vars', '__builtins__']:
            local_vars.pop(var, None)
        
        indent = "  " * depth
        print(f"{indent} Frame: {name}")
        if local_vars:
            print(f"{indent}  Variables: {local_vars}")
        else:
            print(f"{indent}  (no relevant variables)")
        print()
        frame = frame.f_back
        depth += 1

def create_invoice(item_name, item_price):
    tax_rate = 0.18
    total = item_price + (item_price * tax_rate)
    calculate_tax(item_price, tax_rate)
    return total

def handle_purchase(customer_name):
    item = "laptop"
    price = 5000
    invoice_total = create_invoice(item, price)
    return invoice_total

handle_purchase("Rahul")