capacity = int(input("Enter the bucket size"))
outrate = int(input("Enter the outflow rate"))

buffer = 0
n = 0
while n < 5:
    inflow = int(input("Enter the momentary inflow"))
    buffer += inflow
    if buffer >= capacity:
        print("Bucket full")
        break
    buffer -= outrate
    if buffer < 0:
        buffer = 0
    print(buffer)
    n+=1

    
    
