memory = [0]*256
store = {'A':0, 'B':0}
p_c=0
i_l = [
    ('LOAD', 'A', 20),
    ('LOAD', 'B', 20),
    ('ADD', 'A', 'B'),
    ('STORE', 'A',0),
    ('HALT',)
]
def run(i_l):
    global p_c
    while p_c < len(i_l):
        instruction = i_l[p_c]
        operation=instruction[0]
        if operation == 'LOAD':
            store[instruction[1]] = instruction[2]
        elif operation == 'ADD':
            store[instruction[1]] += store[instruction[2]]
        elif operation == 'STORE':
            memory[instruction[2]] = store[instruction[1]]
        elif operation == 'HALT':
            break
        p_c += 1
        
run(i_l)
print("memory[0] =", memory[0])