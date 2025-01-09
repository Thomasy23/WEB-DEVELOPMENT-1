textFile = open("hello.txt", "r")

"""
Handle -> r, w, rw, rw+, w+

            r -> read only
            w -> write
            rw -> read & write
            rw+ -> read & write & add
            w+ -> write & add

"""

contents = textFile.read()
print(contents)

textFile.close()
