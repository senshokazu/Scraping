import re
import sys
import urllib.request 

###metaタグで取得する方法

req = urllib.request.Request('https://gihyo.jp/dp', headers={'User-Agent': 'Mozilla/5.0'})
reo = urllib.request.urlopen(req)

bytes_content=reo.read() 

###errors 引数は、入力文字列に対しエンコーディングルールに従った変換ができなかったときの対応方法を指定します。
###この引数に使える値は 'strict' (UnicodeDecodeError を送出する)、 'replace' (REPLACEMENT CHARACTER である U+FFFD を使う)、 
###'ignore' (結果となる Unicode から単に文字を除く) 、'backslashreplace'(エスケープシーケンス \xNN を挿入する) です。次の例はこれらの違いを示しています:

###ちなみにU+FFFDについてはこちらのURLを参考(http://glyphwiki.org/wiki/ufffd)
scanned_text= bytes_content[:1024].decode('ascii', errors='replace')

#\w はアンダーバーを含む半角英数字 [_0-9a-zA-Z]を意味する
match=re.search(r'charset=["\']?([\w-]+)', scanned_text)

if match:
	#matchの引数に0を指定すると、正規表現全体にマッチした値を取得できる
	#
	encoding=match.group(1)
else:
	encoding='utf-8' 

text=bytes_content.decode(encoding)
print(text)

### file: 出力先。デフォルトは標準出力だが、ファイルオブジェクトなどを指定することもできる。
###sys.stderrは 標準エラー出力のファイルオブジェクトである 
print('encoding:', encoding , file=sys.stderr)





