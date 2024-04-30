import streamlit as st
from streamlit_gsheets import GSheetsConnection


def get_sheet():
    conn = st.connection("gsheets", type=GSheetsConnection)
    data = conn.read(worksheet="Sheet1")
    time_cols = ["Name", "Location", "Start-Time-Str", "End-Time-Str"]
    data = data[time_cols].dropna(subset=time_cols)
    data_list = []
    for index, row in data.iterrows():

        entry = {
            "title": row["Name"],
            "start": row["Start-Time-Str"],
            "end": row["End-Time-Str"],
            "resourceId": row["Location"],
        }
        data_list.append(entry)
    return data_list
