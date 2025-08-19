import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt

st.set_page_config(page_title="نمونه نمودارها در Streamlit", layout="wide")
st.title("نمونه نمودارها در Streamlit")

# ----------------------
# داده نمونه
# ----------------------
np.random.seed(42)
data = pd.DataFrame({
    "x": np.arange(1, 11),
    "y": np.random.randint(1, 20, 10),
    "z": np.random.randint(1, 50, 10),
    "category": list("ABCDEFGHIJ")
})

# ----------------------
# نمودارهای داخلی Streamlit
# ----------------------
st.header("نمودارهای داخلی Streamlit")
st.subheader("Line Chart")
st.line_chart(data[["x","y"]].set_index("x"))

st.subheader("Area Chart")
st.area_chart(data[["x","y"]].set_index("x"))

st.subheader("Bar Chart")
st.bar_chart(data[["x","y"]].set_index("x"))

# ----------------------
# نمودارهای Matplotlib
# ----------------------
st.header("نمودارهای Matplotlib")

fig, ax = plt.subplots()
ax.plot(data["x"], data["y"], marker='o')
ax.set_title("نمودار خطی Matplotlib")
st.pyplot(fig)

fig, ax = plt.subplots()
ax.bar(data["x"], data["y"], color='orange')
ax.set_title("نمودار میله‌ای Matplotlib")
st.pyplot(fig)

fig, ax = plt.subplots()
ax.scatter(data["x"], data["y"], color='green')
ax.set_title("نمودار پراکندگی Matplotlib")
st.pyplot(fig)

fig, ax = plt.subplots()
ax.hist(data["y"], bins=5, color='purple')
ax.set_title("هیستوگرام Matplotlib")
st.pyplot(fig)

fig, ax = plt.subplots()
ax.pie(data["y"], labels=data["category"], autopct='%1.1f%%')
ax.set_title("نمودار دایره‌ای Matplotlib")
st.pyplot(fig)

fig, ax = plt.subplots()
ax.boxplot(data["y"])
ax.set_title("نمودار جعبه‌ای Matplotlib")
st.pyplot(fig)

# ----------------------
# نمودارهای Plotly
# ----------------------
st.header("نمودارهای Plotly")

fig = px.line(data, x="x", y="y", title="نمودار خطی Plotly")
st.plotly_chart(fig)

fig = px.bar(data, x="x", y="y", title="نمودار میله‌ای Plotly")
st.plotly_chart(fig)

fig = px.scatter(data, x="x", y="y", size="z", color="y", title="نمودار پراکندگی Plotly")
st.plotly_chart(fig)

fig = px.pie(data, names="category", values="y", title="نمودار دایره‌ای Plotly")
st.plotly_chart(fig)

fig = px.histogram(data, x="y", nbins=5, title="هیستوگرام Plotly")
st.plotly_chart(fig)

fig = px.imshow(np.random.rand(5,5), title="نمودار حرارتی (Heatmap) Plotly")
st.plotly_chart(fig)

fig = px.scatter_3d(data, x="x", y="y", z="z", color="y", size="z", title="نمودار 3D Plotly")
st.plotly_chart(fig)

# ----------------------
# نمودارهای Altair
# ----------------------
st.header("نمودارهای Altair")

chart = alt.Chart(data).mark_line().encode(x='x', y='y').properties(title="نمودار خطی Altair")
st.altair_chart(chart, use_container_width=True)

chart = alt.Chart(data).mark_bar().encode(x='x', y='y').properties(title="نمودار میله‌ای Altair")
st.altair_chart(chart, use_container_width=True)

chart = alt.Chart(data).mark_point().encode(x='x', y='y', size='z', color='y').properties(title="نمودار پراکندگی Altair")
st.altair_chart(chart, use_container_width=True)

chart = alt.Chart(data).mark_area().encode(x='x', y='y').properties(title="نمودار مساحتی Altair")
st.altair_chart(chart, use_container_width=True)

chart = alt.Chart(data).mark_bar().encode(x='y', y='count()').properties(title="هیستوگرام Altair")
st.altair_chart(chart, use_container_width=True)

# ----------------------
# نمودارهای Seaborn
# ----------------------
st.header("نمودارهای Seaborn")

fig, ax = plt.subplots()
sns.boxplot(y=data["y"], ax=ax)
ax.set_title("نمودار جعبه‌ای Seaborn")
st.pyplot(fig)

fig, ax = plt.subplots()
sns.violinplot(y=data["y"], ax=ax)
ax.set_title("نمودار Violin Seaborn")
st.pyplot(fig)

fig, ax = plt.subplots()
sns.histplot(data["y"], bins=5, kde=True, ax=ax)
ax.set_title("هیستوگرام Seaborn")
st.pyplot(fig)

fig, ax = plt.subplots()
sns.heatmap(data[["x","y"]].corr(), annot=True, cmap="coolwarm", ax=ax)
ax.set_title("Heatmap Seaborn")
st.pyplot(fig)
