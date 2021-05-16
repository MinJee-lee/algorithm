n,m = map(int,input().split()) # split()로 구분 후 입력받음

result = 0

for i in range(n): # 한 줄씩 입럭받기 
    data = list(map(int,input().split())) # 리스트로 받기
    zui_min = min(data) # 현재 줄에서 가장 작은 수 찾기 
    result = max(result,zui_min) # 가장 작은 수들 중에서 큰수 찾기

    print(result)

    