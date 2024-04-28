calendar_options = {
    "editable": "true",
    "selectable": "true",
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
    },
    "slotMinTime": "07:00:00",
    "slotMaxTime": "22:00:00",
    "initialView": "resourceTimelineDay",
    "resourceGroupField": "building",
    "resources": [
        {"id": "a", "building": "Building A", "title": "Building A"},
        {"id": "b", "building": "Stryker Center", "title": "Building B"},
        {"id": "c", "building": "Building B", "title": "Building C"},
        {"id": "d", "building": "Building B", "title": "Building D"},
        {"id": "e", "building": "Building C", "title": "Building E"},
        {"id": "f", "building": "Building C", "title": "Building F"},
    ],
}
calendar_events = [
    {
        "title": "Noah",
        "start": "2024-04-28T15:00:00",
        "end": "2024-04-28T20:00:00",
        "resourceId": "a",
    },
    {
        "title": "Zack",
        "start": "2024-04-28T15:00:00",
        "end": "2024-04-28T20:00:00",
        "resourceId": "a",
    },
    {
        "title": "Event 2",
        "start": "2024-04-28T07:30:00",
        "end": "2024-04-28T10:30:00",
        "resourceId": "b",
    },
    {
        "title": "Jayla",
        "start": "2024-04-28T09:44:00",
        "end": "2024-04-28T15:00:00",
        "resourceId": "a",
    },
    {
        "title": "Kelli",
        "start": "2024-04-28T09:44:00",
        "end": "2024-04-28T15:00:00",
        "resourceId": "a",
    },
]
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
calendar = calendar(
    events=calendar_events, options=calendar_options, custom_css=custom_css
)
st.write(calendar)
