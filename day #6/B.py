number = int(input())
message = ""
messages = []

while number > 0:
	message = input().upper().replace(" ", "")
	messages.append([number, message])
	number = int(input())

for m in messages:
    nextLetter = 0
    nextPlace = 0
    count = 0
    encrypted = []
    number = m[0]
    message = m[1]
    
    encrypted = [""] * len(message)
    if len(message) > number:
        while count < number:
            encrypted[nextPlace] = message[nextLetter]
            nextLetter += 1
            nextPlace += number
            if nextPlace >= len(message) or nextLetter >= len(message):
                count += 1
                nextPlace = count
    
    else:
            encrypted.append(message)
    print(''.join(encrypted))
