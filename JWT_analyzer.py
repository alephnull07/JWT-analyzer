import base64
import binascii

print("Welcome to the JSON Web Token Analyzer!")

def JWT():
    JWT = input("Enter your JSON Web Token here: ") + "."

    split_arr = []
    last_period = 0
    for x in range(len(JWT)):
        if JWT[x] == ".":
            split_arr.append(JWT[last_period:x])
            last_period = x + 1

    header = base64.b64decode(split_arr[0] + '==').decode('utf-8')
    payload = base64.b64decode(split_arr[1] + '==').decode('utf-8')
    signature = split_arr[2]

    print("Header: \n" + str(header))
    print("Payload: \n" + str(payload))
    print("Signature: \n" + str(signature))
    
JWT()
