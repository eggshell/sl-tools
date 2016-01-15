#Use this script to take copy and pasted server information from SoftLayer's
#portal and format it into an ssh config file. User will default to root. If
#a different user is needed it will need to be changed manually.

while True:
    try:
        user_input = raw_input("Enter the name of the copy-pasted SL file: ")
        in_file = open(user_input, 'r')
    except IOError:
        print "Invalid file name, please try again"
    else:
        break

out_file = open('config', 'w')

for line in in_file:
    outline = ""
    if line.strip():
        if "100-node" in line:
            name = line[9:-24]
            if 'kvm' in name:
                name = name[3:]
                name = "compute" + name

            outline = outline + "Host " + name + '\n'

        if "10." in line and '100-node' not in line:
            outline = outline + '  HostName ' + line + '  User root\n  IdentityFile ~/.ssh/id_rsa\n\n'

    out_file.write(outline)

print 'Config file saved'
in_file.close()
out_file.close()
