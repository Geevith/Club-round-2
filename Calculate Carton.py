def calculate_cartons(bottles):
    carton_sizes = {
        'xl': 48,
        'large': 24,
        'medium': 12,
        'small': 6
    }
    
    carton_breakup = {
        'xl': 0,
        'large': 0,
        'medium': 0,
        'small': 0
    }
    
    for carton, capacity in carton_sizes.items():
        carton_breakup[carton] = bottles // capacity
        bottles = bottles % capacity
    
    if bottles > 0:
        carton_breakup['small'] += 1
    
    result = []
    for carton, count in carton_breakup.items():
        if count > 0:
            result.append(f"{count} {carton}")
    
    print(", ".join(result))

calculate_cartons(140)
