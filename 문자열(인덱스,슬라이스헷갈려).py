# 문자열 출력방법
print("Hi Seok.")
# 문자열도 덧셈과 곱셈이 가능하다.
a="Hi "
b="Seok."
print(a+b)
print((a+b)*4)
# 큰따옴표("")를 출력하는 방법은 \"내용\"
print("\"Hi Seok.\"")
# \n : 줄바꿈기능, \t : 탭기능
print("안녕하세요.\n이것이 줄바꿈기능이고,\t 이것이 탭넣기 기능입니다.")

# 인덱스 : 객체명[숫자] (위치 값구하기)
a="Hellow_python"
#  0123456789101112
print(a[12])
# 역으로 셀 때는 -13 -12 ... -3 -2 -1
print(a[-13])
# 슬라이스 : 객체명[시작지점:끝지점:증가폭] * 끝지점값보다 1적은 위치까지 출력됨 *
print(a[2:9])
print(a[2:])
print(a[:-2])
print(a[:])
# 0부터시작해서 7까지의 인덱스를 불러오는데 그 뜀간격이 2라는 말
# H.l.o._
print(a[0:7:2])
# 문자열을 거꾸로 나타낼 때
print(a[::-1])
# 시작지점부터 거꾸로간다 ex) [1::-1] = eH
print(a[4::-1])
# 시작지점부터 끝지점까지 거꾸로간다. * 이건 방향이 반대로가는 (step=-1)니까 끝지점 +1까지 출력됨
print(a[5:2:-1])