#initialization
sum = 0
flag = False
n = 10
scores = []
scores_cpy  = []

#input n scores
#check if any score is over 100
#add to sum of scores to calculate average later
for i in range(n):
    score = float(input(f"Enter score {i+1}: "))
    if flag == False:
        if score > 100:
            flag = True
    sum+=score
    scores.append(score)

#If a score over 100 has been entered, print a message
if flag == True:
    print("A value over 100 has been entered\n")

#Sort the scores in ascending order
scores.sort()
scores_cpy = scores.copy() # copy the list to keep the original list

#Output the highest, lowest, and average scores
print(f"Highest score: {scores[n-1]}")
print(f"Lowest score: {scores[0]}")
print(f"Average score: {sum/n}")
print(f"Second highest score: {scores[n-2]}")

#Remove the two lowest scores and calculate the average
scores_cpy.pop(0)
scores_cpy.pop(0)

sum = 0 #reset sum
for i in range(n-2):#since two lowest scores have been removed, n-2 scores remain
    sum += scores_cpy[i]

#Output
sum = sum/(n-2)
print(f"Average score (excluding two lowest scores): {sum}")
