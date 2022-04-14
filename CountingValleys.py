def countingValleys(steps, path):
    
    counter = 0
    valleys = 0
    
    for i in range(steps):
        if path[i] == 'D':
            counter -= 1  
        elif path[i] == 'U':
            counter +=1
            if (counter == 0 ):
                valleys +=1
    return valleys