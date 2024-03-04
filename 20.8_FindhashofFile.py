# Python Program to find the Hash of File.
# In this article, we'll learn to find the hash of a file and display it.

# There are many Hashing Functions like MD5, SHA-1, etc.

# First we will import the hashlib module
'''import hashlib
def hash_file(filename):
    # This function return the SHA-1 hash:
    # Now we will make a hash object.
    h = hashlib.sha1()

    # Open file for reading in binary mode.
    with open(filename, 'rb') as file:
        # Here now we will loop the file till the end of the file.
        chunk = 0
        while chunk != b'':
            # then read only 1024 bytes at a time.
            chunk = file.read(1024)
            h.update(chunk)
    # Here now we will return the hex representation of the digest
    return h.hexdigest()


message = hash_file("Saurabh.jpg")
print(message)'''