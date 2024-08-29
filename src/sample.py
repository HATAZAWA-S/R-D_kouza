import os
import sys

import numpy as np
import pandas as pd


def sample_function():
    # 100行3列のデータフレームを作成する
    df = pd.DataFrame(np.random.rand(100, 3))
    # カラム名を設定する
    df.columns = ["col1", "col2", "col3"]
    # "A"が20個あるlistを作成
    list_a = ["A"] * 20
    # "B"が30個あるlistを作成
    list_b = ["B"] * 30
    # "C"が50個あるlistを作成
    list_c = ["C"] * 50
    # list_a, list_b, list_cを結合する
    list_all = list_a + list_b + list_c
    # データフレームにカラム"col4"として追加する
    df["col4"] = list_all
    # データフレームを返す
    return df


def main():
    df = sample_function()
    print(df)


if __name__ == "__main__":
    main()
