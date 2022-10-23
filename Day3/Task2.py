# Print Table of 5, 6, 7, 8, 9, 10
def table(N):
    print("Table of",N)
    for i in range(1,N+1):
        print(N, "x", i, "=", N*i)
    print("Table of", N, "has been printed\n")
    

table(5)
table(6)
table(7)
table(8)
table(9)
table(10)
