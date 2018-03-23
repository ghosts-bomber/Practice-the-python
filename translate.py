import urllib.request
import urllib.parse
import json

def main():
    while True:
        content = input('请输入需要翻译的内容（退出输入q）：')
        if content in ('q','Q','quit'):
            break
        
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        data = {}

        data['action'] = 'FY_BY_CLICKBUTTION'
        data['client'] = 'fanyideskweb'
        data['doctype'] = 'json'
        data['from'] = 'AUTO'
        data['i'] = content
        data['keyfrom'] = 'fanyi.web'
        data['salt'] = '1521714166492'
        data['sign'] = 'fe2f8d70e3f026dd2512e7b591907d10'
        data['smartresult'] = 'dict'
        data['to'] = 'AUTO'
        data['typoResult'] = 'false'
        data['version'] = '2.1'
       
        data = urllib.parse.urlencode(data).encode("utf-8")
            
        headers={}
        headers["User-Agent"]="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
        req = urllib.request.Request(url,data,method='POST')
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        target = json.loads(html)
        print('翻译结果为：%s'%(target['translateResult'][0][0]['tgt']))
        #print(html)
if __name__=="__main__":
    main()
