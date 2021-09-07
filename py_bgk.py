'''
cron: 25 8 * * *
new Env('不挂科签到')
'''

import requests
import re
import os

def run(budss):

    url = 'https://appwk.baidu.com/naapi/stsign/activity?fr=3&ssid=Imhhb25wcGQ3MDMi&screen=1440_810&baiduid=&a=3140176867&Bdi_bear=WIFI&zid=stdGghFsZGvv5K3ctqv1SvSxT1imvFhxFtD8i3W8KCNB6kgFXor08vSz_-9NSO5Hlg1eqxyiIQNXz1uSOdSDJyQ&api_level=25&reso=1440_810&csr=1&nettype=wifi&sys_ver=7.1.2&sc=marketing_activity&channel=1024254c&android_id=290a1a8ff258f2c4&pid=1&bssid=NTg6MDA6REQ6ODM6Qjk6Qjc=&sign=c60858ab617a81198533979ea6778a24&wk_cs_app=1&channelType=&app_ver=2.1.3&mf=LENOVO&mac=58:00:DD:83:B9:B7&signCuid=459d32e6afcf24976cc0c48e79389538&ev=sign&appid=38&wk_New_Behavior=1&bid=1&from=3_1024254c&app=android&density=270&c3_aid=A00-N5YSZ7MVXQG3FBKWZBMQRGDFLSAZACJZ-Y74ZIW5T&opid=wk_na&cuid=1AAB14EDD36216C5CB77CBA5233D78A9%7CVYAP75YUK&app_ua=LENOVOL79031&phone_model=LENOVO%20L79031&brand=LENOVO&ua=bd_810_1440_LENOVOL79031_2.1.3_7.1.2&ip=10.0.2.15&uid=wkst_abd_000000000000000&aid=740000&vendor=LENOVO&ver=2.1.3&model=LENOVO%20L79031'
    headers = {
        'Cookie': 'BDUSS='+budss,
        'User-Agent': 'okhttp/3.11.0',
    }
    res = requests.get(url, headers=headers).json()
    # with open('log.json', 'r') as f:
    #     res = f.read()
    # res = json.loads(res)
    # print(res)
    if res['data']['signResult']['windowInfo'] == []:
        print('今天已经签到了')
    else:
        title = res['data']['signResult']['windowInfo']['title']
        # subTitle = res['data']['signResult']['windowInfo']['subTitle']
        qd_pattern = re.findall(
            '<span style="color:#F7603E">(\d)</span>天可得<span style="color:#F7603E">(.*?)</span></span>', str(res))[0]
        # print(qd_pattern)
        longs = f'{title}\n还需要{qd_pattern[0]}天可获得{qd_pattern[1]}'
        print(longs)


if __name__ == '__main__':
    budss_all = os.environ.get('BUDSS')
    if '#' in budss_all:
        budss = budss_all.split('#')
        print(f'当前有{len(budss)}个账号')
        for i in range(0, len(budss)):
            run(budss[i])
    else:
        run(budss_all)
