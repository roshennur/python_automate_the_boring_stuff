import random

results = []
head_streaks = 0
tail_streaks = 0

head = ['H'] * 6
tail = ['T'] * 6

#First part of code: 100 times coin flips
for i in range(101):
    if random.randint(0,1) == 0:
        results.append('H')
    else:
        results.append('T')

#Second part of code that looks for streaks in list
for j in range(len(results)-5):
    if results[j:j + 6] == head:
        head_streaks += 1
    elif results[j:j+6] == tail:
        tail_streaks += 1

print('Head streaks: '+ str(head_streaks))
print('Tail streaks: '+ str(tail_streaks))

if head_streaks == 0 and tail_streaks == 0:
    print('No streaks found')
