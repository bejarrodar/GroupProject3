import matplotlib.pyplot as plt
import pandas as pd
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


@st.experimental_memo
def get_dataset(months) -> pd.DataFrame:
    cat = []
    if "January" in months:
        cat.append(df_list[0])
    if "February" in months:
        cat.append(df_list[1])
    if "March" in months:
        cat.append(df_list[2])
    if "April" in months:
        cat.append(df_list[3])
    if "May" in months:
        cat.append(df_list[4])
    if "June" in months:
        cat.append(df_list[5])
    if "July" in months:
        cat.append(df_list[6])
    if "August" in months:
        cat.append(df_list[7])
    if "September" in months:
        cat.append(df_list[8])
    if "October" in months:
        cat.append(df_list[9])
    if "November" in months:
        cat.append(df_list[10])
    if "December" in months:
        cat.append(df_list[11])

    return pd.concat(cat, axis=0)


data = get_dataset(months)
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
st.bar_chart(data[["Product", "Quantity Ordered"]].groupby("Product").count())
