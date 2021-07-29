# lst = [1,2,3,4,5]
# print(lst)
# lst.reverse()
# print(lst)

lst2 = [1,2,3,4,5]
print("lst2 뒤집기 전 : ", lst2)

lst3 = reversed(lst2)
print("lst2 뒤집기 후 : ", lst2)
print("lst3 : ", list(lst3))


kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "banaana", "orange"]

# zip(kor, eng) # 리스트 두개를 세로로 합침
print(list(zip(kor, eng)))

mixed = [('사과', 'apple'), ('바나나', 'banaana'), ('오렌지', 'orange')]
print(list(zip(*mixed))) # 각 항목별 순서대로 분리

kor2 , eng2 = zip(*mixed)
print(kor2)
print(eng2)