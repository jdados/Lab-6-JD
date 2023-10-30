
# encoder function, author: Jeremiah Dados
def encoder(password):
    x = ""
    for i in password:
        x = x + str(int(i)+3)
    return x

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
            continue
        elif c == 3:
            break


