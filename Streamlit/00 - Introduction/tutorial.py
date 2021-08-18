import streamlit as st

st.title("A Beginner's Guide to Streamlit")

st.header("Introduction")

st.subheader("Installation")

st.text("To install Streamlit, use the following command:")

st.markdown("## `pip install streamlit`")

st.code("import streamlit as st", language = "python")

with st.echo():
    st.markdown("# Streamlit Rocks!")
    
st.latex(r"\psi \left ( r_{1} \right ) = \dfrac{1}{4 \pi \epsilon_{0}}\int_{}^{} d^3 r_{2} \dfrac{\rho \left ( r_{2} \right )}{|r_{1}-r_{2}|}")

st.caption("Example Equation")

sample_data = {"A": [1,2,3,4,5],
               "B": [5,4,3,2,1]}

import pandas as pd

df = pd.DataFrame(sample_data)

st.dataframe(df)

st.table(df)

st.json(sample_data)

import numpy as np

df = np.random.randn(5,5)

st.line_chart(df)

st.area_chart(df)

st.bar_chart(df)

import matplotlib.pyplot as plt
arr1, arr2 = np.random.randn(100), np.random.rand(100)
arr3 = np.random.randint(1,1001,100)

fig, ax = plt.subplots()

ax.set_title("Matplotlib Scatter Plot")

ax.scatter(arr1, arr2, s = arr3, c = arr3, alpha = 0.6)
st.pyplot(fig)

import seaborn as sns
insects = [np.random.choice(["Lacewing", "Locust", "Ladybird", "Leafhopper"]) for i in range(32)]
df = pd.DataFrame({"Insect":insects,
                   "Count": np.random.randint(1,501,32)})
fig, ax = plt.subplots()
ax.set_title("Seaborn Box Plot")
ax = sns.boxplot(df["Insect"], df["Count"])
st.pyplot(fig)

import plotly.express as px
df["Pest"] = df["Insect"].apply(lambda x: "Yes" if x == "Locust" or x == "Leafhopper" else "No")
fig = px.bar(df, x="Insect", y="Count", color = "Pest", title = "Plotly Bar Plot")
st.plotly_chart(fig, use_container_width = True)

if st.checkbox("Click to show table"):
    st.table(df.sample(5))

if st.button("Click to show more information"):
    st.write("Lacewings and ladybirds are beneficial insects.")

radio_selection = st.radio("Which of these insects is not a pest?",
                           ["Locust", "Lacewing", "Leafhopper"])
if st.button("Submit your answer", key = "Radio"):
    if radio_selection == "Lacewing":
        st.write("You are correct!")
    else:
        st.write("You are wrong. Try again.")

selectbox_selection = st.selectbox("Which of these insects is a beetle?",
                                   ["Leafhopper", "Ladybird",
                                    "Locust", "Lacewing"])
if st.button("Submit your answer", key = "Selectbox"):
    if selectbox_selection == "Ladybird":
        st.write("You are correct!")
    else:
        st.write,("You are wrong. Try again.")

select_slider_selection = st.select_slider("Which of these insects is nocturnal?",
                                          ["Leafhopper", "Ladybird", "Locust", "Lacewing"])
if st.button("Submit your answer", key = "Select Slider"):
    if select_slider_selection == "Lacewing":
        st.write("You are correct!")
    else:
        st.write("You are wrong. Try again.")
        
multiselect_selection = st.multiselect("Which of these are pests?",
                                       ["Lacewing", "Locust",
                                        "Leafhopper", "Ladybird"])
if st.button("Submit your answer", key = "Multiselect"):
    if "Lacewing" in multiselect_selection or "Ladybird" in multiselect_selection:
        st.write("You are wrong. Try again.")
    else:
        st.write("You are correct!")

slider_integer_selection = st.slider("Select a number", key = "Slider Integer",
                                     min_value = 0, max_value = 100, value = 25)
st.write(slider_integer_selection, type(slider_integer_selection))
slider_float_selection = st.slider("Select a number", key = "Slider Float",
                                   min_value = 0.0, max_value = 100.0, value = 25.0)
st.write(slider_float_selection, type(slider_float_selection))

number_input_selection = st.number_input("Enter a number", min_value = -10, max_value = 10, value = 0, key = " Number Input Integer")
st.write(number_input_selection, type(number_input_selection))
number_input_selection = st.number_input("Enter a number", min_value = -1.0, max_value = 1.0, value = 0.0, key = "Number Input Float")
st.write(number_input_selection, type(number_input_selection))

text_input_selection = st.text_input("From what you have learnt today, give an example of a pest")
st.write(text_input_selection)
text_area_selection = st.text_area("Give a summary of what you have learnt about insects today")
st.write(text_area_selection)

if st.sidebar.checkbox("Click to show table", key = "Sidebar Checkbox"):
    st.table(df.sample(5))
    
with st.form("Sample Form"):
    st.write("Gathering insect information inside the form")
    select_slider_value = st.select_slider("Select an insect", ["Lacewing", "Ladybird", "Leafhopper", "Locust"])
    number_input_value = st.number_input("How many insects have we studied?", min_value = 0)

    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write("You selected the {}. We studied {} insects. This information is within the form.".format(select_slider_value, number_input_value))

checkbox_value = st.checkbox("Click. Or not. The choice is yours!")
st.write("You clicked the checkbox:", checkbox_value, "This information is outside the form.")
st.write("These values, {} and {}, that were set inside the form are accessible outside the form".format(select_slider_value, number_input_value))

col1, col2, col3 = st.columns([2.6,5,3.8])

col1.subheader("Line Chart")
col1.line_chart(sample_data)

col2.subheader("Area Chart")
col2.area_chart(sample_data)

col3.subheader("Bar Chart")
col3.bar_chart(sample_data)

x = 200
y = 3000000
    
def non_cached_function(x, y):
    return x ** y

start = time()
non_cached_function(x,y)
duration = round((time() - start),3)

st.write("Non-Cached Function took {} seconds to run".format(duration))

@st.cache
def cached_function(x, y):
    return x ** y

start = time()
cached_function(x,y)
duration = round((time() - start),3)

st.write("Cached Function took {} seconds to run".format(duration))

file = st.file_uploader("Select a file to upload", type = ["csv", "txt"])

if file is not None:
    bytes_data = file.getvalue()
    st.write(bytes_data)