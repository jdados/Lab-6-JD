
# encoder function, author: Jeremiah Dados
def encoder(password):
    x = ""
    for i in password:
        x = x + str(int(i)+3)
    return x

# decoder function, author: Cayden Keene
def decoder(encoded_password):
    password = ""
    for i in encoded_password:
        if int(i) == 0:
            password += "7"
        elif int(i) == 1:
            password += "8"
        elif int(i) == 2:
            password += "9"
        else:
            password += str(int(i) - 3)
    return password

# main function, author: Jeremiah Dados
if __name__ == '__main__':
    while True:
        print("Menu\n"
        "-------------\n"
        "1. Encode\n"
        "2. Decode\n"
        "3. Quit\n")
        c = int(input("Please enter an option: "))
        if c == 1:
            p = input("Please enter your password to encode: ")
            encoded_password = encoder(p)
            print("Your password has been encoded and stored!\n")
        elif c == 2:
            # decoder function call goes here
            # decoder call (added by Cayden Keene)
            p = decoder(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {p}.")
            continue
        elif c == 3:
            break


