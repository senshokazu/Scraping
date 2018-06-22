import sys
import urllib.request

###Content-typeヘッダで取得する方法
req = urllib.request.Request('https://gihyo.jp/dp', headers={'User-Agent': 'Mozilla/5.0'})
reo = urllib.request.urlopen(req)
encoding=reo.info().get_content_charset(failobj="utf-8")
print('encoding', encoding, file=sys.stderr)
text=reo.read().decode(encoding)


#withブロックを抜けると、自動でclose()を呼び出してくれます。
#したがってwith構文を使うと、close()の呼び出しが不要になる。
#withでencodingを指定しないと、実行環境のOSの文字コードが選択されてしまうので、明示的に書く
with open('dp.html','w', encoding='utf-8') as f:
	print(text, file=f)
