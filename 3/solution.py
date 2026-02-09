def fruits(fruit_list):
    result = {}
    for item in fruit_list:
        if (
            item.get("shape") == "sphere"
            and item.get("mass") >= 300
            and item.get("mass") <= 600
            and item.get("volume") >= 100
            and item.get("volume") <= 500
        ):
            fruit_name = item.get("name")
            result[fruit_name] = result.get(fruit_name, 0) + 1

    return result


# result = fruits((
#     		{'name':'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
#     		{'name':'mango', 'shape': 'square', 'mass': 150, 'volume': 120}, 
#    			{'name':'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
#     		{'name':'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250}
# 		))

# print(result)
