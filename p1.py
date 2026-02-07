address = input()
good = True

if "http://" == address[:7]:
    address = address[7:]
elif "https://" == address[:8]:
    address = address[8:]
else:
    good = False

if not address[0].isalpha():
    good = False

if " " in address:
    good = False

if not((address[-4:] in [".com", ".edu", ".org"]) or (address[-3:] == ".io")):
    good = False

if good:
    print("valid")
else:
    print("invalid")