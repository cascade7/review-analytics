data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('總留言筆數:', len(data))

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('總留言長度:', sum_len)
print('平均留言長度:', sum_len/len(data))

new = []
for d in data :
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言小於100個字')
print('第一筆:', new[0])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good),' 筆留言提到good')
print('第一筆:', good[0])

good = [d for d in data if 'good' in d] #快寫法
print('一共有', len(good),' 筆留言提到good')
print('第一筆:', good[0])
bad = ['bad' in d for d in data]