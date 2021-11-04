# yucalc-gpa v1.1

[**GPA Calculator for Yamagata University**](https://yucalc-gpa.herokuapp.com/) のコードを置いています。Heroku上にアップロードしているディレクトリと同じものです。


＜ファイル構成＞<br>
* [コード](calcGPA_app.py) &dash; 公開しているプログラム本体のコードです。Streamlitを用いて実装しているため、HTMLコードはなく、このPythonファイルのみでできています。<br>
* [設定ファイル](Procfile) &dash; プログラムとプラットフォームを繋ぐ役割のファイルで、コマンドを記述してあります。要は指示書のようなものです。<br>
* [パッケージリスト](requirements.txt) &dash; プログラムを動作させるためにインストールしなければならないライブラリを記述しています。<br>

このリポジトリについての質問がありましたら、[Twitter](https://www.twitter.com/4voltex/)までご連絡ください。

## License
The source code is licensed MIT. The website content is licensed CC BY 4.0, see [LICENSE](LICENSE.txt).<br>
ソースコードはMITライセンスに、使用方法や本文書等はCC BY 4.0ライセンスに基づいて公開しています。詳しくは[ライセンス](LICENSE.txt)をお読みください。

### 更新履歴
* 2021-10-25 v1.0から1.1に更新。コードを修正、PEP8準拠に。
* 2021-11-05 Python3.10対応。

Last updated：2021-11-05 (JST)