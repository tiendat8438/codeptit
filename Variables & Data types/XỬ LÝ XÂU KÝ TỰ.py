s1, s2 = input().lower(), input().lower()
A = set(s1.split())
B = set(s2.split())
hop = sorted(A | B)
giao = sorted(A & B) 
print(*hop)
print(*giao)
