import re
from html import unescape

with open('dp.html','r', encoding='utf-8') as f:
	html=f.read()


# re.findall()を使って、書籍一冊に相当する部分のhtmlを取得する。
#*?は*と同じだが、なるべく短い文字列にマッチする(non-greedy)ことを表すメタ文字。
#\sは空白文字
for partial_html in re.findall(r'<a itemprop="url".*?</ul>\s*</a></li>', html,re.DOTALL):
	url=re.search(r'a itemprop="url" href="(.*?)">', partial_html).group(1)
	url='https://gihyo.jp' + url  # /で始まっているのでドメイン名追加する。

	title=re.search(r'<p itemprop="name".*?</p>', partial_html).group(0)
	title=title.replace('<br/>', ' ')
	title=re.sub(r'<.*?>', '', title)
	title=unescape(title) #文字参照をもとに戻す
	'''
	htmlでは「<」、「>」などはタグの記号なので、
	文字として表示する場合はそのまま使えない。「<」は「&lt;」、「>」は「&gt;」としなければならない。
	text = '&amp; &lt; &gt;'
	print(unescape(text)) >>> & < >
	'''

	print(url, title)