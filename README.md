# prj-template
プロジェクト用のテンプレートフォルダ構成です。

## Directory
テンプレートとして以下のような構成をとっています。プロジェクト・プロダクトに応じてフォルダ追加などを行っていただければと思います。
```
prj-template/
│
├── README.md                   # プロジェクトの説明や使い方を記述
├── pyproject.toml              # プロジェクトのビルド、パッケージ依存関係の管理
├── .gitignore                  # Gitで追跡しないファイルやフォルダを指定
├── .pre-commit-config.yaml     # pre-commitフックの設定
├── Makefile                    # ビルド操作やその他のスクリプトを自動化
├── poetry.lock                 # Poetryで管理される依存関係の具体的なバージョンを固定
│
├── inputs/                     # 入力データや設定ファイルを格納
├── notebook/                   # Jupyterノートブックなどの開発ドキュメントを格納
├── outputs/                    # 出力データや結果を格納
├── src/                        # ソースコードを格納
└── tests/                      # pytest用ソースコードを格納

```

## Environment
以下の環境で動作確認済み。
- Windows11
- Ubuntu 18.04, 20.04, 22.04, 24.04

環境構築の方法に関しては、以下のIssueを参考にしてください。
- https://github.com/kmdsd/technology-acquisition/issues/96
- https://github.com/kmdsd/technology-acquisition/issues/100

Windows環境で行う場合にはmake別途インストールが必要なので注意が必要です。

## How to Use
## create repository
1. 新規のrepositoryを作成してください
2. 作成時にテンプレートの使用有無があるので、その際に本repoを設定してください。
3. このテンプレートの状態で新規repoが作成できます。


## create environment
```shell
make install
```

> [!NOTE]
> `pyproject.toml`の `name`が仮想環境名になります。ご自身で変更していただければと思います。

## Run python
poetry を使用しているので、poetryでの実行方法に則って実行してください。

```shell
poetry run python src/sample.py
```

## pre-commit
このリポジトリでは、pushした際に各メンバーでコードスタイルを統一するためcommit時にisortとblackが実行されるようになっています。（pre-commit）
設定に関しては、`.pre-commit-config.yaml`に記載しており、環境構築時に自動的に構築されるようになっています。

> [!NOTE]
> pre-commit は `.git` がある前提になっています。ローカル検証などで、git のリポジトリを使用していない場合には、`Makefile`の `poetry run pre-commit install`を削除してから実行してください。

> [!NOTE]
> pre-commitとしているblackは、対象のフォルダに対してフォーマット処理を行います。なので`.pre-commit-config.yaml`に記載しているフォルダが存在しているのかを確かめてからcommit処理をしてください。（フォルダがないとエラーになります）
```
  # blackのチェック
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black
        args: [src] # 対象のフォルダがあるのかを確認すること
```


## VS Codeの拡張機能をインストール

pythonとjupyterの拡張機能を追加します。

- 拡張機能の検索コンソールで`@recommended`と入力すると`.vscode`の`extensions.json`に記載された拡張機能の一覧が表示されるため、それらをすべてインストールします。
- 必要な拡張機能は適宜追加してください。