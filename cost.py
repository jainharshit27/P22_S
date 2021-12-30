dict1={"Bread":1, "Cheese":2, "Tomato":2, "Onion":1, "Pickle":2, "Cottage Cheese":5, "Bread":1}
sum = 0
for cost in dict1.values():
    sum += cost
    
print(sum)
