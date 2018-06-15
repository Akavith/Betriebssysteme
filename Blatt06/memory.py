import mmap

str = b"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"

with open("memory.txt", "wb") as f:
    f.seek(1073741824-1)
    f.write(b"\0")

with open("memory.txt", "r+b") as f:

    mm = mmap.mmap(f.fileno(), 0)

    while True:
        try:
            mm.write(str)
        except ValueError:
            break
    print("End")


    while True:
        4+4
    mm.close()
