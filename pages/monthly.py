from streamlit_calendar import calendar
import streamlit as st
from database import get_sheet
from streamlit_gsheets import GSheetsConnection

st.set_page_config(layout="wide")
calendar_options = {
    "nowIndicator": "true",
    "editable": "false",
    "selectable": "true",
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
    },
    "slotMinTime": "07:00:00",
    "slotMaxTime": "22:00:00",
    "initialView": "dayGridMonth",
    "resourceGroupField": "building",
    "resources": [
        {"id": "rec_center", "building": "Rec Center", "title": "Rec Center"},
        {"id": "stryker", "building": "Stryker Center", "title": "Stryker Center"},
    ],
}
calendar_events = get_sheet()

custom_css = """
    .fc-event-past {
        opacity: 0.8;
    }
    .fc-event-time {
        font-style: italic;
    }
    .fc-event-title {
        font-weight: 700;
    }
    .fc-toolbar-title {
        font-size: 2rem;
    }
"""
calendar(events=calendar_events, options=calendar_options, custom_css=custom_css)
