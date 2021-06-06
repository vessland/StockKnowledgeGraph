import requests
import json
import jsonpath
import pandas as pd
from openpyxl import load_workbook

def create_params(page):
    params = {
        'pz': '50^',
        'po': '1^',
        'np': '1^',
        'ut': 'b2884a393a59ad64002292a3e90d46a5^',
        'fltt': '2^',
        'invt': '2^',
        'fid0': 'f4001^',
        'fid': 'f62^',
        'fs': 'm:0 t:6 f:^!2,m:0 t:13 f:^!2,m:0 t:80 f:^!2,m:1 t:2 f:^!2,m:1 t:23 f:^!2,m:0 t:7 f:^!2,m:1 t:3 f:^!2^',
        'stat': '1^',
        'fields': 'f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124^',
        'rt': '53407822^',
        # ('cb', 'jQuery18307739865615069035_1602234656657^'),
        '_': '1602234665664',
    }
    value = str(page) + '^'
    params['pn'] = value
    # print(params)
    return params

def get_response(params):
    cookies = {
        'waptgshowtime': '20210509',
        'st_si': '62033869304648',
        'st_asi': 'delete',
        'cowCookie': 'true',
        'qgqp_b_id': 'b6a504ec0746ecec06a8c9db5dde3bec',
        'intellpositionL': '249px',
        'intellpositionT': '755px',
        'st_pvi': '93530241304569',
        'st_sp': '2021-05-09^%^2021^%^3A34^%^3A43',
        'st_inirUrl': 'https^%^3A^%^2F^%^2Fwww.eastmoney.com^%^2F',
        'st_sn': '28',
        'st_psi': '20210509171102245-113300300813-9103840696',
    }
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'Accept': '*/*',
        'Referer': 'http://data.eastmoney.com/',
        'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
    }
    response = requests.get('http://push2.eastmoney.com/api/qt/clist/get', headers=headers, params=params,
                            cookies=cookies, verify=False)
    return response

def get_data(response):
    content = response.text
    data = json.loads(content)
    return data

def data_cleaning(data, page):
    stock_code_list = jsonpath.jsonpath(data, '$..f12')
    name_list = jsonpath.jsonpath(data, '$..f14')
    latest_price_list = jsonpath.jsonpath(data, '$..f2')
    price_limit_list = jsonpath.jsonpath(data, '$..f3')
    # 主力净流入
    net_amount_list1 = jsonpath.jsonpath(data, '$..f62')
    net_proportion_list1 = jsonpath.jsonpath(data, '$..f184')
    # 超大单净流入
    net_amount_list2 = jsonpath.jsonpath(data, '$..f66')
    net_proportion_list2 = jsonpath.jsonpath(data, '$..f69')
    # 大单净流入
    net_amount_list3 = jsonpath.jsonpath(data, '$..f72')
    net_proportion_list3 = jsonpath.jsonpath(data, '$..f75')
    # 中单净流入
    net_amount_list4 = jsonpath.jsonpath(data, '$..f78')
    net_proportion_list4 = jsonpath.jsonpath(data, '$..f81')
    # 小单净流入
    net_amount_list5 = jsonpath.jsonpath(data, '$..f84')
    net_proportion_list5 = jsonpath.jsonpath(data, '$..f87')
    df = pd.DataFrame(stock_code_list, columns=['代码'])
    df['名称'] = name_list
    df['最新价'] = latest_price_list
    df['涨跌幅(%)'] = price_limit_list
    df['主力净流入-净额'] = net_amount_list1
    df['主力净流入-净占比(%)'] = net_proportion_list1
    df['超大单净流入-净额'] = net_amount_list2
    df['超大单净流入-净占比(%)'] = net_proportion_list2
    df['大单净流入-净额'] = net_amount_list3
    df['大单净流入-净占比(%)'] = net_proportion_list3
    df['中单净流入-净额'] = net_amount_list4
    df['中单净流入-净占比(%)'] = net_proportion_list4
    df['小单净流入-净额'] = net_amount_list5
    df['小单净流入-净占比(%)'] = net_proportion_list5

if __name__ == '__main__':
    for page in range(1, 83):
        params = create_params(page)
        response = get_response(params)
        data = get_data(response)
        data_cleaning(data, page=page)