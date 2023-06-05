import subprocess
import csv
import dotenv
import os

def get_cred():
  file = "cred.env"
  dotenv.load(file)
  username = os.getenv("USER")
  password = os.getenv("PASSWORD")

  return (username, password)
  
def get_server_list(file):
  servers = []
  with open(file, 'r') as f:
    reader = csv.reader(f)

    next(reader)
    for row in reader:
      servers.append(row[1])
  return servers

def sshing_to_server(server):
  username, password = get_cred()
  command = 'sshpass -p {} ssh {}@{}'.format(password, username, server)
  subprocess.Popen('xfce4-terminal --hold -e "{}"'.format(command),
                   shell=True,)

if __name__ == "__main__":
  file = 'servers.csv'
  servers = get_server_list(file)
  for server in servers:
    sshing_to_server(server)
