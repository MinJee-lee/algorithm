# case 1
word = input().lower()    
word_list = list(set(word))
cnt = []

for i in word_list:     
    count = word.count(i)
    cnt.append(count)   

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))].upper())

# case 2

N = input().upper() # 단어를 입력받는다.
M = list(set(words))  # 입력받은 문자열에서 중복값을 제거

cnt_list = []  # count값을 담을 배열을 선언
for x in target : 중복값을 제거한 문자열을 반복문을 돌아서
    cnt = words.count(x) 각 원소(단어)의 개수를 구한다.
    cnt_list.append(cnt)  # cnt 숫자를 cnt_list 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :  # cnt 숫자 최대값이 중복되면 '?' 출력
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(target[max_index])