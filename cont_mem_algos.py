def best_fit(memory, request, index):
    if not memory:
        return None
    
    best_index = None
    best_fit_size = float('inf')
    
    for i in range(len(memory)):
        current_index = (index + i) % len(memory)
        base, size = memory[current_index]
        
        if size >= request and size < best_fit_size:
            best_fit_size = size
            best_index = current_index
    
    if best_index is None:
        return None
    
    base_allocated = memory[best_index][0]
    new_size = memory[best_index][1] - request
    
    if new_size == 0:
        del memory[best_index]
        index = best_index % len(memory) if memory else 0
    else:
        memory[best_index] = (base_allocated + request, new_size)
        index = best_index
    
    return memory, base_allocated, request, index
