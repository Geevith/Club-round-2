def calculate_cartons(num_bottles):
    carton_sizes = {
        "xl": 48,
        "large": 24,
        "medium": 12,
        "small": 6
    }

    
    cartons_used = {}

    
    for size, capacity in carton_sizes.items():
        if num_bottles >= capacity:
            count = num_bottles // capacity 
            cartons_used[size] = count  
            num_bottles %= capacity  

    
    output = []
    for size in cartons_used:
        output.append(f"{cartons_used[size]} {size}")

    print(', '.join(output))


i_bottles = 140
calculate_cartons(i_bottles)  