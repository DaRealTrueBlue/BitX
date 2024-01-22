import requests
import subprocess

def updater(url):
    try:
        response = requests.get(url)
        code = response.text
        with open("main.py", "w") as file:
            file.write(code)
        subprocess.check_call(["python", "main.py"])
    except Exception as e:
        print("Error: %s" % e)
if __name__ == "__main__":
    print("Updating latest version...")
    website_url = "https://raw.githubusercontent.com/DaRealTrueBlue/BitX/master/main.py"
    updater(website_url)