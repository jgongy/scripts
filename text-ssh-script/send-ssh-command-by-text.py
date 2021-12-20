import json
import os
import subprocess
import getpass

EMAIL_BODY_FILENAME = "email-body.txt"
TARGET_EMAIL = "##########@tmomail.net"

def getTunnelString():
  tunnelJSONBytes = subprocess.run(["curl", "-s",
                                    "localhost:4040/api/tunnels"],
                                   stdout=subprocess.PIPE)
  tunnelJSONString = tunnelJSONBytes.stdout.decode("utf-8")
  return tunnelJSONString

def generateSSHCommandString():
  tunnelJSONString = getTunnelString()
  tunnelJSONDict = json.loads(tunnelJSONString)
  tunnels = tunnelJSONDict["tunnels"][0]
  public_url = tunnels["public_url"]
  parts = public_url.split(":")
  portString = parts[2];
  hostString = parts[1].strip("/")

  username = getpass.getuser()
  command = "ssh -p " + portString + " " + username + "@" + hostString
  return command

def main():
  tunnelJSONString = getTunnelString()
  command = generateSSHCommandString()
  email_body = open(EMAIL_BODY_FILENAME, "w")
  email_body.write(tunnelJSONString + "\n" + command)
  email_body.close()
  os.system("mutt -s \"SSH Command\" "
            + TARGET_EMAIL
            + " < "
            + EMAIL_BODY_FILENAME
            + " 2>/dev/null")
  os.remove(EMAIL_BODY_FILENAME)
  return 0

if __name__ == '__main__':
  main()
