# ******************************************************************************
# Category  : Grammar of Pandas
# Chapter   : 01 基本操作
# Title     : 01 情報確認
# Created by: Owner
# Created on: 2020/12/20
# ******************************************************************************


# ＜目標＞
# - Pandasがどのような構造のライブラリかを把握する


# ＜参考資料＞
# Pandasユーザーガイド
# - https://pandas.pydata.org/docs/user_guide/index.html#user-guide


# ＜目次＞
# 0 準備
# 1 バージョン確認


# 0 準備 -----------------------------------------------------------------------------------

# ライブラリ
import pandas as pd


# 1 バージョン確認 ----------------------------------------------------------------------------

# バージョン情報の取得
print(pd.__version__)


# 依存関係のあるパッケージ
# --- バージョン情報を含めて表示
pd.show_versions()


# 2 オプション設定 ----------------------------------------------------------------------------

# オプション一覧
dir(pd.options)

# オプションの詳細
# --- compute
dir(pd.options.compute)

# --- display
dir(pd.options.display)

# --- html
dir(pd.options.html)

# --- io
dir(pd.options.io)

# --- mode
dir(pd.options.mode)

# --- plotting
dir(pd.options.plotting)


# 3 ライブラリ構造 ----------------------------------------------------------------------------

dir(pd)
