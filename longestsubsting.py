char = 256
def longsubstring(string):
    n = len(string)
    c = 1
    m = 1
    prev = 0
    i = 0
    visit = [-1] * char
    visit[ord(string[0])] = 0
    for i in xrange(1,n):
        prev = visit[ord(string[i])]
        if prev == -1 or (i - c> prev):
            c+=1
        else:
            if c > m:
                m = c
            c = i - prev
        visit[ord(string[i])] = i
    if c > m:
        m = c
    return m
string = input("Enter the string")
print "The input string is " + string
length = longsubstring(string)
print ("The length of the longest substring without repeating characters" +
       " substring is " + str(length))
