import os
import urllib.request
import zipfile
from pathlib import Path

from secret import API_KEY

url = 'https://antcpt.com/anticaptcha-plugin.zip'
filehandle, _ = urllib.request.urlretrieve(url)

with zipfile.ZipFile(filehandle, "r") as f:
    f.extractall("plugin")

api_key = API_KEY
file = Path('./plugin/js/config_ac_api_key.js')
file.write_text(
    file.read_text().replace("antiCapthaPredefinedApiKey = ''", "antiCapthaPredefinedApiKey = '{}'".format(api_key)))

zip_file = zipfile.ZipFile('./plugin.zip', 'w', zipfile.ZIP_DEFLATED)
for root, dirs, files in os.walk("./plugin"):
    for file in files:
        path = os.path.join(root, file)
        zip_file.write(path, arcname=path.replace("./plugin/", ""))
zip_file.close()
