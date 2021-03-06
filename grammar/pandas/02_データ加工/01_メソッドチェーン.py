# ******************************************************************************
# Category  : Grammar of Pandas
# Chapter   : 02 データ加工
# Title     : 01 メソッドチェーン
# Created by: Owner
# Created on: 2020/12/20
# ******************************************************************************


# ＜目標＞
# - Pandasがどのような構造のライブラリかを把握する


# ＜目次＞
# 0 準備
# 1 バージョン確認


# 0 準備 -----------------------------------------------------------------------------------

# ライブラリ
import os
import pandas as pd


# パス取得
cwd = os.getcwd()
path = os.path.join(cwd, 'grammar', 'pandas', 'csv', 'iris.csv')
iris = pd.read_csv(path)


# 1 バージョン確認 ----------------------------------------------------------------------------

df = (iris
        .head(10)
        .tail(5))


