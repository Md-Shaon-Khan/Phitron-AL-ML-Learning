n = int(input("Enter number of processes: "))

p = []
at = []
bt = []

for i in range(n):
    p.append(input("Process Name: "))
    at.append(int(input("Arrival Time: ")))
    bt.append(int(input("Burst Time: ")))

wt = [0] * n
tat = [0] * n
done = [False] * n

time = 0
completed = 0

print("\nProcess\tAT\tBT\tWT\tTAT")

while completed < n:

    idx = -1
    min_bt = 9999

    for i in range(n):
        if at[i] <= time and done[i] == False:
            if bt[i] < min_bt:
                min_bt = bt[i]
                idx = i

    if idx == -1:
        time += 1
        continue

    wt[idx] = time - at[idx]
    tat[idx] = wt[idx] + bt[idx]

    time += bt[idx]
    done[idx] = True
    completed += 1

for i in range(n):
    print(p[i], "\t", at[i], "\t", bt[i], "\t", wt[i], "\t", tat[i])

print("\nAverage Waiting Time =", sum(wt) / n)
print("Average Turnaround Time =", sum(tat) / n)