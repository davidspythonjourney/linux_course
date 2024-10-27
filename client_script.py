
from SshToServer import SshToServer
import pandas as pd
import os
import json
from dotenv import load_dotenv
load_dotenv()
#run server script from local script
def runServerScript():
    my_ssh = SshToServer("/Users/davidmarks/Desktop/linux_course/my-first-key-pair.pem", os.getenv("KEY_PAIR"), "ubuntu")
    stdout, stderr = my_ssh.runRemoteCommand("python3 server_script.py")
    if stdout:
        return json.loads(stdout)
    else:
        print(f"No valid Linux command executed. Error: {stderr}")

def createCsv(csv_info):
    csv_file_name = "linux.csv"
    if csv_info:
        insert_to_csv = pd.DataFrame([csv_info])
        write_option = 'a' if os.path.exists(csv_file_name) else 'w'
        header_bool = False if os.path.exists(csv_file_name) and os.path.getsize(csv_file_name) > 0 else True
        insert_to_csv.to_csv(csv_file_name, mode=write_option, index=False, header=header_bool)
        return True
    return False

def runScripts():
    get_word_counts = runServerScript()
    csv_success  = createCsv(get_word_counts)
    if csv_success:
        print("All Done it worked hazah! but will Nadav approve? we shall see!")
    else:
        print("Something went wrong check your code bro or review your python course!!")
    
if __name__ == "__main__":
    runScripts()



         
    
