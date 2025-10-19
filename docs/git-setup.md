# githubに学習用リポジトリ作成したときの手順記録
## 1.githubにリポジトリを作成する
TILという名前で新規リポジトリを作る
## 2.ローカルPCに1で作成したリポジトリ用のディレクトリを作成する
```bash
# ディレクトリを作成
$ mkdir -p github/TIL
# git管理開始
$ git init
# デフォルトブランチ名をmainにかえる
$ git branch -m master main
# リポジトリ説明のためのREADMEだけとりあえず作成 
$ echo "TIL is repository for learning" > README.md
# コミット
$ git add .
$ git commit -m "Initial Commit"
# リモートリポジトリに名前をつける
$ git remote add origin git@github.com:mrtx4r0/TIL
$ git remote -v
origin	git@github.com:mrtx4r0/TIL (fetch)
origin	git@github.com:mrtx4r0/TIL (push)
```
## 3.githubのリポジトリ（リモート）にPUSHする
