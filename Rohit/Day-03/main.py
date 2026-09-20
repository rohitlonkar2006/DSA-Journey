def multiply(a,b):
    return a*b

def calculate_area(length,width):
    area = multiply(length,width)
    return area


def main():
    room_length = 5
    room_width = 3
    room_area = calculate_area(room_length, room_width)
    return room_area
    
main()