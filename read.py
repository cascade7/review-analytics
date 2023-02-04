data = []
sum_len = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
for d in data:
	sum_len = sum_len + len(d)
print('總留言長度:', sum_len)
print('總留言筆數:', len(data))
print('平均留言長度:', sum_len/len(data))