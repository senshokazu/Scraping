#ファイル名はDockerfile

#FROMイメージ名 で対象イメージを元に新たなイメージファイルを作成できる。 
FROM python

#update sources list
#このコマンドはよくわからないが、キャッシュの問題を解消するためらしい。
RUn apt-get clean
RUN apt-get update

#Install vim_packege
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]

#エイリアス設定を記載してある。Dokcerfileと同じ配下に置く。
#改行コードの問題を解消するため、vimで.bashrcを作成するか、sublimeで改行コードの変更(表示→改行コード→unixを選択)を必ず行う。
ADD .bashrc /root/.bashrc