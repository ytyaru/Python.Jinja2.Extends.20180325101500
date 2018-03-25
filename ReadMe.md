# このソフトウェアについて

Jinja2でテンプレファイルをextendsしてみる。

extendsはテンプレの引数値を定義すること。

* [extendsのわかりにくい点](memo/difficult.md)

## 前回まで

リポジトリ|概要
----------|----
[Python.Jinja2.20180325075747](https://github.com/ytyaru/Python.Jinja2.20180325075747)|Hello Jinja2, ファイルの読込
[Python.Jinja2.Include.20180325100000](https://github.com/ytyaru/Python.Jinja2.Include.20180325100000)|テンプレをinclude

# 開発環境

* [Raspberry Pi](https://ja.wikipedia.org/wiki/Raspberry_Pi) 3 Model B
    * [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) GNU/Linux 8.0 (jessie)
        * [pyenv](http://ytyaru.hatenablog.com/entry/2019/01/06/000000)
            * Python 3.6.4
                * Jinja2 2.1.0
                    * [install](http://ytyaru.hatenablog.com/entry/2019/02/25/000000)

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

利用ライブラリは以下。

Library|License|Copyright
-------|-------|---------
[jinja2](https://github.com/pallets/jinja)|[BSD](https://github.com/pallets/jinja/blob/master/LICENSE)|[Copyright (c) 2009 by the Jinja Team, see AUTHORS for more details.](https://github.com/pallets/jinja/blob/master/LICENSE)
