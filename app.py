# import streamlit as st


# st.title("shank 123")

# st.header("Header 1")
# st.header("SubHeader 1")
# st.header("SubHeader2")

# st.header("Header 2")
# st.header("SubHeader 1")
# st.header("SubHeader2")


# st.write("hello 123")

# name = st.text_input("Enter your name")
# st.write(name)

# age = st.text_input("Enter your age")
# st.write(age)

# # Multiple Columns
# first,last = st.columns(2)
# firstName = first.text_input("Enter your first name")
# st.write(firstName)
# lastName = last.text_input("Enter your last name")
# st.write(lastName)

import streamlit as st
import pandas as pd
import numpy as np

# title 
st.title("we will learn")

# header
st.header('Header')

# subheader
st.subheader("subheader")

# text
st.text("text")


# input 
# text_input
# number_input
# WRITE SWISS 

name = st.text_input("enter your name ")
st.write(name)

number = st.number_input('Enter your age ')
st.write(number)


# for multiple columns
first, last = st.columns(2)
firstName =first.text_input("Enter your first name")
lastName = last.text_input("Enter your last name ")
st.write(firstName)
st.write(lastName)


# area 
# area = st.text_area('Enter your words')

# df=np.random.randn(20, 3)
# magic
# df1 = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['A', 'B', 'C']
# )
# # df
# st.table(df)
# # special 
# df = pd.DataFrame(df)
# st.dataframe(df1.style.highlight_max(axis=0))

df =   pd.DataFrame(
      np.random.rand(20,3),
      columns = ["A","B","C"]
)

st.table(df)

st.dataframe(df.style.highlight_max(axis=1))

# line_chart
st.line_chart(df)


# bar_chart
st.bar_chart(df)



# map
st.map()

# img = st.file_uploader('upload your file', type=["png", "jpg", "jpeg"])
# st.image(img)

# if file is not None:
#     image = Image.open(file)

#     st.image(
#         image,
#         caption=f"You amazing image has shape",
#         use_column_width=True,
#     )







import pandas as pd
import numpy as np 
import streamlit as st 
import matplotlib.pyplot as plt



number = st.number_input('enter your number', min_value=0, max_value=6, value=5)
st.write(number)

# slelectbox 
number = st.selectbox("Select your lucky nunmber", [1, 2, 3, 4, 5, 6])
st.write(number)


df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)


if st.checkbox('Please tick the checkbox'):
  st.write("Thank you for Click the checkbox")
  # st.balloons()
else:
  st.write("No checkbox clicked")

# checkbox
if st.checkbox('checkbox'):
  st.table(df)
  


# multiselect
fist = st.multiselect('selcts your options', [x for x in range(10, 20)])
st.write(type(fist))
st.table({
  "Selected Numbers":fist
})

# st.balloons()



# sidebar
val = st.sidebar.selectbox('How would like to connect ', ['Home', 'Email', 'Mobile Number'])
if val == 'Email':
  # st.balloons()
  st.sidebar.write("Welcome to the Email")

df1 = pd.DataFrame({
    "Number": [x for x in range(1, 10)],
    "Square" :[x*x for x in range(1, 10)],
    "cube":[x*x*x for x in range(1, 10)],
    "add10":[x+10 for x in range(1, 10)]
})
# df1

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

st.set_option("deprecation.showPyplotGlobalUse",False)

# st.balloons()
plt.style.use('ggplot')
col = st.sidebar.selectbox("choose your columns", df1.columns)
plt.plot(df1['Number'], df1[col])
st.pyplot()



# import streamlit as st
option = st.radio('Select three known variables:', ['initial velocity (u)', 'final velocity (v)', 'acceleration (a)', 'time (t)'])  




st.slider('Pick a Value', 5, 20, 7)
st.slider('Pick a Range', 5, 20, (7, 10))

import time

status = st.empty()
bar =  st.progress(0)
for i in range(1):
    status.text('Current Iteration {}'.format(i+1))
    bar.progress(i+1)
    time.sleep(0.2)

st.error('Error')
st.success('Success')
st.info('Info')
st.exception(RuntimeError('This is custom error'))
st.warning('Warning')















