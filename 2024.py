n = int(input())
scores = []

for i in range(n):
    scores.append(int(input()))

unique_scores = list(set(scores))
unique_scores.sort()

print(unique_scores[-3], scores.count(unique_scores[-3]))