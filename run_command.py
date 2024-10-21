from SshToServer import SshToServer

# my_ssh = SshToServer("/Users/davidmarks/Desktop/linux_course/my-first-key-pair.pem", "3.95.182.128", "ubuntu" )
# result, result_err = my_ssh.runRemoteCommand("dfdsfs")
# print(f"my results for ssh remote command: {result}")
# print(f"my results for ssh remote err command: {result_err}")

#run remote val cmd
def validCommand():
    cmd = input("Please enter a Linux command: ")
    my_ssh = SshToServer("/Users/davidmarks/Desktop/linux_course/my-first-key-pair.pem", "3.95.182.128", "ubuntu")
    stdout, stderr = my_ssh.runRemoteCommand(cmd)
    if stdout:
        print("Congrats! You provided a valid Linux command.")
        print("Output:", stdout) 
    else:
        print(f"No valid Linux command executed. Error: {stderr}")
# validCommand()

