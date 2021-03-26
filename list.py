import os
import subprocess
#vs 
os.system("code")

#lampp

#terminal
os.system("gnome-terminal")

#google-chrome

# os.system("google-chrome")
# os.system("pwd")
# print("Done!")
#os.system("google-chrome")
import webbrowser
new =2
url = [
    'https://app.slack.com/',
    'http://webmail.leometric.com/',
    'http://leometric.com/employee_portal/'
    ]
for i in url:
    webbrowser.get(using='google-chrome').open(i)

print("Done!")


os.chdir("/opt/lampp")

#os.system("sudo ./manager-linux-x64.run")
subprocess.run(['sudo','./manager-linux-x64.run'], 
                      stdin=subprocess.PIPE, stdout=subprocess.PIPE)

