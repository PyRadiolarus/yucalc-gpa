# yucalc-gpa v1.1

[**GPA Calculator for Yamagata University**](https://calc.remh.dev/) のコードを置いています。Heroku上にアップロードしているディレクトリと同じものです。

＜ファイル構成＞

* [コード](GPACalculator.py) &dash; 公開しているプログラム本体のコードです。Streamlitを用いて実装しているため、HTMLコードはなく、このPythonファイルのみでできています。

* [Pythonバージョン指定ファイル](.python-version) &dash; Pythonのバージョンを指定するファイル。もともとは ```runtime.txt``` というファイルで管理していましたが、2025年2月にHerokuが ```runtime.txt``` をdeprecated（非推奨）にし、代替として ```.python-version``` を指定しました。

* [設定ファイル](Procfile) &dash; プログラムとプラットフォームを繋ぐ役割のファイルで、コマンドを記述してあります。要は指示書のようなものです。

* [パッケージリスト](requirements.txt) &dash; プログラムを動作させるためにインストールしなければならないライブラリを記述しています。

このリポジトリについての質問がありましたら、[Twitter](https://www.x.com/4voltex/)もしくは[メール](<mailto:postmaster@remh.dev>)までご連絡ください。

## License

The source code is licensed MIT. The website content is licensed CC BY 4.0, see [LICENSE](LICENSE.txt).

ソースコードはMITライセンスに、使用方法や本文書等はCC BY 4.0ライセンスに基づいて公開しています。詳しくは[ライセンス](LICENSE.txt)をお読みください。

### 更新履歴

* 2021-10-25 v1.0から1.1に更新。コードを修正、PEP8準拠に。
* 2021-11-05 Python 3.10対応。
* 2021-11-20 独自ドメイン適用。
* 2021-12-16 コード本体をリネーム。
* 2022-03-02 連絡先記載。
* 2022-03-17 ライブラリ更新。
* 2025-02-04 Python 3.13対応、OSイメージ更新。
* 2025-10-17 ライブラリおよびライセンス更新、連絡先変更。runtime.txtを廃止、.python-versionに。

Last updated：2025-10-17 (JST)
