# This is a simple password cracking script

import crypt

# Actual cracking function
def testPass(cryptPass):
    salt = cryptPass[0:2]  # Turns word into crypt for comparison
    dictFile = open('dictionary.txt','r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word,salt) # Compares salt value to password hash
        if (cryptWord == cryptPass):
            print "[+] Found Password: "+word+"\n"
            return
    print "[-] Password not found.\n"
    return  # Displays text for if the password was found using common dictionary terms

# Text manipulation and operation function
def main():
    passFile = open('passwords.txt') # Selects the user to be cracked
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print "[*] Cracking Password for: "+user
            testPass(cryptPass)
if __name__ == "__main__":
    main()
