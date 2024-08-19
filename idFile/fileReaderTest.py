#Just a test to see how to read files in python 
ids=[]
with open('ids.txt','r') as f:
    for i, line in enumerate(f):
        if i % 2 == 0:
            if(i != 0):
                id= line.strip()
                ids.append(id)
        elif i % 2 == 1:
            id2= line.strip()
            print(id2)

    print(ids)
