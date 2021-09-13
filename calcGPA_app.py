import streamlit as st
import streamlit.components.v1 as stc
import math,re

def main():
    stc.html("""
        <html>
        <head>
        <style>
        body {
            background-color: white;
        }
        </style>
        </head>
        <body>
        <h1>GPA Calculator for Yamagata University</h1>
        <h3>学務情報システムに表示された成績から、GPA・GPS・総(修得/履修)単位数を計算するプログラムです。</h3>
        <h4>はじめに<a href="./statics/Readme.html" target="_blank" rel="noreferrer noopener">使い方</a>をお読みください</h4>
        </body>
        </html>
    """, height=250)
    #stc.html("<h1>GPA Calculator for Yamagata University</h1>")
    #st.subheader("学務情報システムに表示された成績から、GPA・GPS・総(修得/履修)単位数を計算するプログラムです。")
    text = st.text_area(label="ここに成績を貼り付けてください。",value="")
    text = re.sub("\t",",",text)
    lines = re.split("合|否|認",text)
    GPSum, dNum, FNum = 0, 0, 0

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
    # GP計算
                GP = out * degree
                GPSum += GP
                dNum += degree
                if out == 0:
                    FNum += degree

    try:
        GPA = math.floor(GPSum / dNum * 10 ** 2) / (10 ** 2)
    except ZeroDivisionError:
        pass
    try:
        st.write("GPS：", GPSum, "\n履修単位数：", dNum, "\n修得単位数：", dNum - FNum, "\nGPA：", GPA)
    except UnboundLocalError:
        pass

if __name__ == "__main__":
    main()