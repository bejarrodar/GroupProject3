import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

from clean_data import clean_csv

df_list = clean_csv()

st.title("Sales 2019")
st.write(
    """
    Interactive Site
    """
)
months = st.sidebar.multiselect(
    "Select Months",
    [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ],
    [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ],
)


@st.cache
def get_dataset(months) -> pd.DataFrame | list:
    cat = []
    month_num = []
    if "January" in months:
        cat.append(df_list[0])
        month_num.append(1)
    if "February" in months:
        cat.append(df_list[1])
        month_num.append(2)
    if "March" in months:
        cat.append(df_list[2])
        month_num.append(3)
    if "April" in months:
        cat.append(df_list[3])
        month_num.append(4)
    if "May" in months:
        cat.append(df_list[4])
        month_num.append(5)
    if "June" in months:
        cat.append(df_list[5])
        month_num.append(6)
    if "July" in months:
        cat.append(df_list[6])
        month_num.append(7)
    if "August" in months:
        cat.append(df_list[7])
        month_num.append(8)
    if "September" in months:
        cat.append(df_list[8])
        month_num.append(9)
    if "October" in months:
        cat.append(df_list[9])
        month_num.append(10)
    if "November" in months:
        cat.append(df_list[10])
        month_num.append(11)
    if "December" in months:
        cat.append(df_list[11])
        month_num.append(12)

    return pd.concat(cat, axis=0), month_num


data, month_nums = get_dataset(months)
st.write("# For the selected months")
st.write("Number of transactions: ", len(data))
st.write("Average cost per transaction: ", data["Cost"].mean().round(2))
st.write(
    "Most made in a single month: ",
    max(data.reset_index().groupby("month").sum()["Cost"]),
)
col1, col2 = st.columns(2)
with col1:
    results_per_page = st.number_input("Number of results per page:", 1, len(data), 20)
    pages = len(data) / 20
    page = st.number_input("Page:", 1, int(pages))
with col2:
    st.dataframe(
        data.iloc[
            (page - 1) * results_per_page : ((page - 1) * results_per_page)
            + results_per_page
        ].style.format(precision=2)
    )


st.write("# Graph Comparing Number of Products Sold")
st.bar_chart(
    data=data.groupby("Product").count().reset_index(),
    x="Product",
    y="Quantity Ordered",
)

st.write("# Amount of Money Made each month")
st.line_chart(
    data=data[data["month"].isin(month_nums)].groupby("month").sum().reset_index(),
    x="month",
    y="Cost",
)

st.write("# Percent of Each Product Sold")
pie_data = data.groupby("Product").count()["Order ID"]
explode = []
for i in range(len(pie_data)):
    if pie_data.iloc[i] / sum(pie_data) < 0.05:
        explode.append(0.5)
    else:
        explode.append(0)
fig1, ax1 = plt.subplots()
ax1.pie(x=pie_data, labels=pie_data.index, explode=explode, autopct="%1.1f%%")
st.pyplot(fig1)

st.write("# Sales of Each Product by City")
fig2 = plt.figure(figsize=(20, 10))
sns.countplot(data=data, x="city", hue="Product")
st.pyplot(fig2)
