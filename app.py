import streamlit as st
import pandas as pd

# --- ZIP OFFICIAL BRANDING ---
st.set_page_config(page_title="Zip | Partnership OS", page_icon="💜", layout="wide")

# Official Zip Styles
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFA; } /* Zip 'Control' White */
    [data-testid="stSidebar"] { background-color: #1A0826; } /* Zip 'Confidence' Dark */
    .stMetric { background-color: #ffffff; border: 1px solid #AA8FFF; padding: 15px; border-radius: 10px; }
    h1, h2, h3 { color: #1A0826; font-family: 'Helvetica Neue', sans-serif; }
    .stButton>button { background-color: #AA8FFF; color: white; border-radius: 20px; font-weight: bold; border: none; }
    </style>
    """, unsafe_allow_stdio=True)

# --- SIDEBAR & NAV ---
st.sidebar.markdown("<h1 style='color: #AA8FFF;'>Zip</h1>", unsafe_allow_stdio=True)
st.sidebar.subheader("AD Partnership OS")
nav = st.sidebar.radio("Go to:", ["Relationship Dashboard", "Note Reformatter", "Prospect Pipeline"])

# --- PARTNER DATA ---
partners = [
    {"Name": "FEVO", "Status": "Live", "Type": "Channel", "Parent": None},
    {"Name": "Phillies", "Status": "Live", "Type": "Sub-Partner", "Parent": "FEVO"},
    {"Name": "Flyers", "Status": "Live", "Type": "Sub-Partner", "Parent": "FEVO"},
    {"Name": "MLB", "Status": "Live", "Type": "Direct", "Parent": None},
    {"Name": "SHEIN", "Status": "Live", "Type": "Direct", "Parent": None},
    {"Name": "Eagles", "Status": "Prospect", "Type": "Direct", "Parent": None},
    {"Name": "Sixers", "Status": "Prospect", "Type": "Direct", "Parent": None}
]
df = pd.DataFrame(partners)

# --- VIEW 1: DASHBOARD ---
if nav == "Relationship Dashboard":
    st.title("Partner Strategy & Health")
    
    # KPI Row
    c1, c2, c3 = st.columns(3)
    c1.metric("Managed Partners", "12")
    c2.metric("Active Prospects", "10")
    c3.metric("Channel Efficiency", "88%")

    st.markdown("### 🏟️ Sports & Entertainment Portfolio")
    selected = st.selectbox("Select Partner Insight", df['Name'].tolist())
    
    p_info = df[df['Name'] == selected].iloc[0]
    if p_info['Parent']:
        st.warning(f"Note: {selected} is a child account under **{p_info['Parent']}**")
    
    st.dataframe(df, use_container_width=True)

# --- VIEW 2: NOTE REFORMATTER ---
elif nav == "Note Reformatter":
    st.title("Personal CRM: Note Cleanup")
    st.write("Convert AI transcripts/Plain text into Salesforce-ready updates.")
    
    raw_text = st.text_area("Paste Raw Meeting Notes...", height=250)
    
    if st.button("Zip-ify Summary"):
        st.subheader("🚀 Refined Executive Update")
        st.code(f"STRATEGY: Partner scaling via Zip BNPL\nACTION: Confirm Q4 gameday volume targets with {df['Name'][0]} stakeholders.")

# --- VIEW 3: PROSPECTS ---
elif nav == "Prospect Pipeline":
    st.title("Future Partners")
    st.table(df[df['Status'] == 'Prospect'])
