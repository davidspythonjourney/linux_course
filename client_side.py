from SshToServer import SshToServer

# my_ssh = SshToServer("/Users/davidmarks/Desktop/linux_course/my-first-key-pair.pem", "3.95.182.128", "ubuntu" )
# result, result_err = my_ssh.runRemoteCommand("dfdsfs")
# print(f"my results for ssh remote command: {result}")
# print(f"my results for ssh remote err command: {result_err}")

#run remote val cmd
def validCommand():
    my_ssh = SshToServer("/Users/davidmarks/Desktop/linux_course/my-first-key-pair.pem", "18.207.203.105", "ubuntu")
    stdout, stderr = my_ssh.runRemoteCommand("python3 server_side.py")
    if stdout:
        print("Congrats! You provided a valid Linux command.")
        print("Output:", stdout) 
    else:
        print(f"No valid Linux command executed. Error: {stderr}")
validCommand()

