import streamlit as st
import numpy as np
import pandas as pd
from  PIL import Image 
import time

st.title('steamlit 超入門')
st.write('Interactive wedget')

'start!!!'
latest_iterlation = st.empty()
bar= st.progress(0)

for i in  range(100):
    latest_iterlation.text(f'Iterration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done !!!!!!!!!'    




left_column, right_column = st.beta_columns(2)
button = left_column.button('Right column is showen')
if button:
    right_column.write('Yes')


# expander = st.beta_expander('Ask')
# expander.write('Questionary')
# expander.write('Questionary')
# expander.write('Questionary')
# expander.write('Questionary')



# option= st.sidebar.text_input('Tell me your hobby?')
# condition= st.sidebar.slider('your condition now?', 0,100,59)


# 'your hobby is ' , option 
# 'Your condition',  condition 



# condition= st.slider('your condition now?', 0,100,59)
# 'Your condition',  condition 

# option= st.text_input('Tell me your hobby?')
# 'your hobby is ' , option 


# option = st.selectbox(
#     'tell your number', 
#     list(range(1,11))
# )

# 'your number ', option , 'it it?'

# st.write('dispya Image')
# if st.checkbox('Show image'):
#     img= Image.open('bus.jpg')
#     st.image(img, caption='bus', use_column_width=True)

# st.write('DataFrame')

# df = pd.DataFrame({
#     '1列目': [1,2,3,4],
#     '2列目': [10,20,30,40]
# })

# # st.write(df)

# # st.dataframe(df.style.highlight_max(axis=1))

# st.table(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ### 項

# ```python 
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69, 139.70],
#     columns = ['lat','lon']
# )

# st.map(df)



