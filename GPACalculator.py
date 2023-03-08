""" Copyright (c) 2021-2023 Minori Hagino (twitter.com/4voltex)
    This software is released under the MIT License, see LICENSE."""
import streamlit as st
import streamlit.components.v1 as stc
import math
import re

def main():
    stc.iframe("https://page.remh.dev/analytics.html",scrolling=False)
    stc.html("""
        <html>
        <head>
        <meta name="twitter:card" content="summary">
        <style>
        body {
            background-color: white;
        }
        strong {
            color: red;
        }
        </style>
        </head>
        <body>
        <h3>学務情報システムに表示された成績から、GPA・GPS・総(修得/履修)単位数を計算するプログラムです。</h3>
        <h4>はじめに<a href="https://page.remh.dev/documents/readme/" target="_blank" rel="noreferrer noopener">使い方</a>をお読みください。</h4>
        <p><strong>※現在、学務情報システムがたいへん混み合っています。成績をコピーしたら、このプログラムに貼り付ける前にログアウトすることを推奨します。</strong></p>
        </body>
        </html>
    """,height=220)
    text = st.text_area(label="ここに成績を貼り付けてください。",value="")
    text = re.sub("\t",",",text)
    lines = re.split("\n",text)
    grade_point_sum, degree_count, faulting_count = 0, 0, 0

    for line in lines:
        line = line.split(",")
        line = [i for i in line if i != ""]
        if 1 <= len(line) <= 4:
            pass
        elif len(line) < 1:
            break
        else:
            l = [line[-5],line[-1]]
            degree = int(float(l[0]))
    
    # 評定を数値化
            if "Ｓ" in l[1]:
                out = 4
            elif "Ａ" in l[1]:
                out = 3
            elif "Ｂ" in l[1]:
                out = 2
            elif "Ｃ" in l[1]:
                out = 1
            elif "Ｎ" in l[1]:
                out = -1
            else:
                out = 0
    
    # 単位認定科目であるか否かを判定
            if out < 0:
                pass
            else:
    # GP(grade_point)計算
                grade_point = out*degree
                grade_point_sum += grade_point
                degree_count += degree
                if out == 0:
                    faulting_count += degree

    try:
        grade_point_average = math.floor(grade_point_sum/degree_count*10**2)/(10**2)
    except ZeroDivisionError:
        pass
    try:
        st.write("GPS：", grade_point_sum, "\n履修単位数：", degree_count, "\n修得単位数：", degree_count-faulting_count, "\nGPA：", grade_point_average)
    except UnboundLocalError:
        pass

if __name__ == "__main__":
    main()