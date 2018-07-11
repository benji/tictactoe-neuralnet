
stats = {}

with open("training.dat", "r") as file:
    for line in file:
        arr = line.strip().split('|')
        n_moves = 0
        for i in range(0, len(arr)-1):
            if int(arr[i]) != 0:
                n_moves = n_moves+1
        if not n_moves in stats:
            stats[n_moves] = 0
        stats[n_moves] = stats[n_moves]+1

print stats
