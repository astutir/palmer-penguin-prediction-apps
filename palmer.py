import streamlit as st

home = st.Page(r"Home\Dataset_Overview.py", title="Home", icon=":material/dashboard:", default=True)
data = st.Page(r"Projects\Data_Info.py", title="Data Info", icon=":material/bug_report:")
prediction = st.Page(r"Projects\Prediction.py", title="Prediction", icon=":material/notification_important:")

pg = st.navigation({
    "Home": [home],
    "Projects": [data, prediction],
})

pg.run()
