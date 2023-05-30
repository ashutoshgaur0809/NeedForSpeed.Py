import math
for i in range(int(input())):
    u, v, a, s = map(int, input().split()) # Taking input
    print('No' if ((u**2) - (2 * a * s)) > v**2 else 'Yes')