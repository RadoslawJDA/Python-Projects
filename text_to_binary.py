
def binary(text):
    binary_text = " ".join(format(ord(letter), "b") for letter in text)
    print(binary_text)


def decimal(binary_text):
    decimal_text = "".join(chr(int(digit, 2)) for digit in binary_text.split(" "))
    print(decimal_text)


should_continue = True
while should_continue:
    inp_text = input("Type the text to convert\n")
    choice = input("Decide to Convert Text To Binary('bin') or Decimal('dec')")
    if choice == "bin":
        binary(text=inp_text)
    elif choice == "dec":
        decimal(binary_text=inp_text)
    else:
        print("Type 'bin' or 'dec' to convert the text")

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if result == "no":
        should_continue = False
        print("Goodbye")
