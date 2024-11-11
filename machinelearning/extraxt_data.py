

ITERATIONS = 1000
with open('./data/Pet_Supplies.json','r') as in_file:
    with open (f'./data/Pet_Supplies_{ITERATIONS}.json','w') as out_file:
        for _ in range(ITERATIONS):
            line = in_file.readline()
            out_file.write(line)

