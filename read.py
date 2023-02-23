import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value = 1000000)
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		bar.update(count)
bar.finish()
print('總留言筆數:', len(data))

#留言統計
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
"""
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good),' 筆留言提到good')
print('第一筆:', good[0])
"""
good = [d for d in data if 'good' in d] #快寫法
print('一共有', len(good),' 筆留言提到good')
print('第一筆:', good[0])
bad = ['bad' in d for d in data]

# 用字計數
start_time = time.time()
wc = {}
for d in data :
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] +=1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
end_time = time.time()
print('花了', end_time-start_time, 'seconds')
print(len(wc))

while True:
	word = input('請問你要查什麼字: ')
	if word == 'qqq':
		break
	elif word not in wc:
		print('抱歉，沒有出現這個字')
	else:
		print(word, ':', wc[word])
print('感謝你使用本查詢功能!!')
