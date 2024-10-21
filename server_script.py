import os
from collections import Counter
import subprocess
import json

def readFile(file_name: str):
    if os.path.exists(file_name):
        with open(file_name, "r") as log_file:
            return log_file.readlines()
           
def grepLogToCounter():
    key_words = ["INFO", "ERROR", "WARN"]
    grep_file = "/var/log/syslog"
    if os.path.exists(grep_file):
        try:
            join_search_words = "|".join(key_words)
            command = f'grep -E "{join_search_words}" {grep_file}'
            timestamp = int(subprocess.run(['date', '+%s'], capture_output=True, text=True).stdout.strip())
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            count_word = Counter(result.stdout.split())
            csv_info = {"time": timestamp, "info": count_word.get("INFO"), "error": count_word.get("ERROR"), "warn": count_word.get("WARN") }
            print(json.dumps(csv_info))
        except subprocess.CalledProcessError as e:
            print(f"Command '{command}' returned non-zero exit status {e.returncode}")
            print(f"Error output: {e.stderr}")
            
if __name__ == "__main__":
    grepLogToCounter()