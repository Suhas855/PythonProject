firstName = "Suhas"  # input("whats your name? ")
lastName = "Kotha"

fullName = firstName + " " + lastName
score1 = int(input("score1"))
score2 = int(input("score2"))
scoreTest = score1/score2
finalScore = score2 - score1
print(f"Score1: {scoreTest}")
print(f"Score1: {scoreTest:5.2f}")
print(f"score1: {score1:10d}")
print(f"score1: {score1:10d}")
# sep = "___"
# print(f"{sep18s}")
# print("My name is: " + fullName + ", not done yet,....")
# print("Result: " + str(score2 - score1) + ", end of program....")

# print("My name: %s, my score: %i" % (fullName, finalScore))
# print("My Name: {}, my score: {}" .format(finalScore, fullName))
# print("My name: {first}, my score: {second}".format(second=finalScore, first=fullName))
# print(f"My Name: {fullName}, my score: {finalScore}")  # This is the best way so use it like this


school = "maridiANS" #"Linda"

# print(school[0]) 0 = the first letter of the string
# Length = len(school) length will write all the letters in the string

# print(school[8]) will print the eighth letter
# print(school[1, (Length - 1)])
# print(school[?:?]) this means that it will print any letter all the way to a higher letter but can only go up and down
# print(school[<start - 0>:<increment: 1 or -1>])
print(school[1:6:-1])
print(school[1:6:2])
print(school[2:6:2])
# 1 + (-1): 0
# 0 + (-1): -1


# input: "maridiAN"
# output: 1st letter in UPPER. all other in LOWER : Meridian


# 1. plain format, passing multiple values
# 2. string concatenate : string join
# 3. using % format
# 4. using format()
# 5. using format() with kay-value
# 6. using f-string
# 7. using %s means it's a string  %s = string
# 8. using %i means it's an integer
