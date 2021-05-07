import streamlit as st
import time


st.title('streamlit test')

st.write('プログレスバーの表示')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)
'Done!!'

left_col,right_col = st.beta_columns(2)
button = left_col.button('右カラムに文字を表示')
if button:
    right_col.write('ここは右カラム')

expander1 = st.beta_expander('問い合わせ')
expander1.write('問い合わせ内容')
expander2 = st.beta_expander('問い合わせ')
expander2.write('問い合わせ内容')
expander3 = st.beta_expander('問い合わせ')
expander3.write('問い合わせ内容')

# text = st.text_input('あなたの趣味を教えて下さい')
# condition =  st.slider('あなたの今の調子は？',0,100,50)

# 'あなたの趣味は、',text,'です。'
# 'コンディションは:',condition,
# if st.checkbox('show image'):
#     img = Image.open('PXL_20210213_112002749.jpg')
#     st.image(img,caption='cooky',use_column_width=True)
