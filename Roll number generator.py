"""
Esayway in an online exam for new graduates of any discipline to find entry level jobs in their fields.
The website generates the roll number of its registered students with the help of the students application numbers. 
The process induce a key K for generating an individual roll number. To generate the roll number, each digit in the 
application number is replaced by the Kth digits that comes after it in the application number. the series of digits 
is considered in a cyclic fashion for the last k digits.
write an algorithm to generate the roll number from the given application number.

Input
The input consists of two space-separated positive integers - applicant number and key, representing the application number 
and key (K), respectively.

Output 
Print an integer representing the roll number.

Constraints 
0< applicant number <= 10^9.

Example input : 43251 3 Output : 25143 Explanation: replace 4 with 2;3 with 5;2 with 1; 5 with 4; and 1 with 3. So, the output is 25143

"""

data = str(input("Enter Application number and Key: "))

l = 0

#spliting given app no and k number
datasplit = data.split(" ")
roll = datasplit[0]
k = int(datasplit[1])

roll = list(map(int,str(roll)))
nofdigits = len(roll)
newroll = []

for iterator in range(nofdigits):

    if iterator + (k - 1) == nofdigits:
        l = 0
        newroll.append(roll[l])

    if iterator + (k - 1) > nofdigits:
        l = iterator + (k - 1) - nofdigits 
        newroll.append(roll[l])
    
    elif iterator + (k - 1) < nofdigits:
        newroll.append(roll[l + (k - 1)])

    l += 1

newroll = int("".join(list(map(str,newroll))))

print(newroll)