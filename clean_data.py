import pandas as pd


def read_csv() -> list[pd.DataFrame]:
    month = []
    month.append(pd.read_csv("Sales_January_2019.csv"))
    month.append(pd.read_csv("Sales_February_2019.csv"))
    month.append(pd.read_csv("Sales_March_2019.csv"))
    month.append(pd.read_csv("Sales_April_2019.csv"))
    month.append(pd.read_csv("Sales_May_2019.csv"))
    month.append(pd.read_csv("Sales_June_2019.csv"))
    month.append(pd.read_csv("Sales_July_2019.csv"))
    month.append(pd.read_csv("Sales_August_2019.csv"))
    month.append(pd.read_csv("Sales_September_2019.csv"))
    month.append(pd.read_csv("Sales_October_2019.csv"))
    month.append(pd.read_csv("Sales_November_2019.csv"))
    month.append(pd.read_csv("Sales_December_2019.csv"))
    return month


def clean_csv() -> list[pd.DataFrame]:
    clean = []
    dirty = read_csv()
    for each in dirty:
        each.dropna(inplace=True)
        filter = each["Quantity Ordered"] != "Quantity Ordered"
        each = each[filter]
        each["Quantity Ordered"] = pd.to_numeric(each["Quantity Ordered"])
        each["month"] = each["Order Date"].str[0:2]
        each["time"] = each["Order Date"].str[-6:-3]
        each["Price Each"] = pd.to_numeric(each["Price Each"])
        each["Order Date"] = pd.to_datetime(each["Order Date"])
        each["Cost"] = each["Price Each"] * each["Quantity Ordered"]
        each["Cost"] = each["Cost"].round(2)
        each["month"] = pd.to_numeric(each["month"])
        each["time"] = pd.to_numeric(each["time"])
        clean.append(each)
    return clean
