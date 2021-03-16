def sliding_average(values, window):
    averages = []

    for i in range(len(values) - window + 1):
        averages.append(sum(values[i:i+window]) / window)
        
    return averages

def better_sliding_average(values, window):
    previous = sum(values[0:window])
    averages = [previous / window]

    for i in range(1, len(values) - window+1):
        previous = previous - values[i-1] + values[i+window-1]
        averages.append(previous / window)
    
    return averages

# try sliding_max : complexity n + w at best
# avec une autre structure n * log(w) 

if __name__ == "__main__":
    win = 3
    my_array = [2,4,6,1,3,4,7,10,12]
    edge = [0,1,2]

    print(sliding_average(my_array, win))
    print(better_sliding_average(my_array, win))