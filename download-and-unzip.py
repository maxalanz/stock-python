import requests
import zipfile
import io
import os
from requests.auth import HTTPBasicAuth

# WebDAV URL 和认证信息
webdav_url = 'https://dav.jianguoyun.com/dav/python/code/stock-python.zip'
username = os.getenv('WEBDAV_ID')
password = os.getenv('WEBDAV_PASSWORD')

# 下载 ZIP 文件
response = requests.get(webdav_url, auth=HTTPBasicAuth(username, password))
response.raise_for_status()  # 确保请求成功

# 使用内存中的文件对象解压 ZIP 文件
with zipfile.ZipFile(io.BytesIO(response.content)) as z:
    # 获取 ZIP 文件中的所有文件名
    file_names = z.namelist()
    
    # 解压到当前目录
    for file_name in file_names:
        z.extract(file_name, path='.')
        print(f'Extracted: {file_name}')