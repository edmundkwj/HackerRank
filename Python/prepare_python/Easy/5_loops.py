# https://www.hackerrank.com/challenges/python-loops/

if __name__ == '__main__':
    n = int(input())
    if 1 <= n <= 20: 
        for i in range(n):
            print(i * i)