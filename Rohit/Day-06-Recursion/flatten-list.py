# def flatten_list(data):
#     output = []
#     for item in data:
#         if isinstance(item,list):
#                 output = output + flatten_list(item)
#         else:
#             output.append(item)
#     return output

# print(flatten_list([1,[2,[3,[4,5]],[8,9]],6]))

# Reducing The Complexity
def flatten_list(data, output):
    for item in data:
        if isinstance(item,list):
                flatten_list(item,output)
        else:
            output.append(item)
    return output

print(flatten_list([1,[2,[3,[4,5]]],6],[]))