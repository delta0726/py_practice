# ******************************************************************************
# Category  : Grammar of Pandas
# Chapter   : 01 基本操作
# Title     : 02 クイック操作
# Created by: Owner
# Created on: 2020/12/20
# ******************************************************************************


# ＜概要＞
# - 普段の操作でよく使うものをピックアップ


# ＜目次＞
# 0 準備
# 1 データフレームの概要
# 2 データ確認
# 3 欠損値の確認
# 4 シリーズの抽出
# 5 クイック分析
# 6 クリップボード操作


# 0 準備 ------------------------------------------------------------------------------------

# ライブラリ
import os
import pandas as pd

# データ読み込み
current_path = os.getcwd()
file = os.path.sep.join(['', 'grammar', 'pandas', 'csv', 'iris.csv'])
iris = pd.read_csv(current_path + file)

# データ確認
iris.head()


# 1 データフレームの概要-------------------------------------------------------------------------

# データフレームの構造
iris.info()

# 列名取得
iris.columns

# 列ごとのデータ型
iris.dtypes

# インデックス取得
iris.index

# 全要素数
iris.size

# 行数と列数
# --- 行列数
# --- 行数
# --- 列数
iris.shape
iris.shape[0]
iris.shape[1]


# 2 データ確認 ---------------------------------------------------------------------------------

# 先頭行の確認
iris.head(n=5)

# 末尾行の確認
iris.tail(n=5)

# データ部分の抽出
iris.values


# 3 欠損値の確認 -------------------------------------------------------------------------------

# 有効データ数のカウント
iris.count()

# 欠損値のカウント
iris.isnull().sum()

# 欠損値がないか判定
iris.isnull().any()


# 4 シリーズの抽出 -----------------------------------------------------------------------------

# シリーズの抽出
# ---- pandas.core.series.Series
iris.Species

# Numpy配列に変換
# --- numpy.ndarray
iris.Species.to_numpy()


# 5 クイック分析 -----------------------------------------------------------------------------

# 基本統計量
iris.describe()

# 相関分析
iris.corr()


# 6 クリップボード操作 -------------------------------------------------------------------------

# クリップボード出力
# --- エクセルやRで確認する際に便利
iris.to_clipboard()

# クリップボード入力
# --- 簡単に外部からデータ取得
iris2 = pd.read_clipboard()


