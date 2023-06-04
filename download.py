import subprocess
import requests
import re

def down(bypass):
    if isinstance(bypass, str):
        try:
            down = bypass['list'][0]['dlink']
            title = bypass['list'][0]['server_filename']

            subprocess.run(['aria2c', '--console-log-level=warn', '-x', '16', '--max-connection-per-server=16', '-s', '64', '-k', '2M', '--file-allocation=none', '-o', title, down], check=True)
    
            return title
        except Exception as e:
            print(f"Download Error - {str(e)}")
            return
    else:
        try:
            title = "hello.txt"
            subprocess.run(['aria2c', '--console-log-level=warn', '-x', '16', '--max-connection-per-server=16', '-s', '64', '-k', '2M', '--file-allocation=none', '-o', title, down], check=True)
            return title
        except Exception as e:
            print(f"Download Error - {str(e)}")
            return
    

