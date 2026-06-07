import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="ICT for Cybersecurity - Industrial IoT",
    page_icon="🛡️",
    layout="wide"
)

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "Home",
        "Industrial IoT",
        "Cyber Threats",
        "Risk Assessment",
        "Monitoring Dashboard",
        "Security Controls"
    ]
)

# -------------------------------
# HOME
# -------------------------------
if page == "Home":

    st.title("🛡 ICT for Cybersecurity: Industrial IoT")

    st.markdown("""
    ### Group Project

    This project focuses on Industrial Internet of Things (IIoT)
    cybersecurity challenges, risks, monitoring, and protection strategies.
    """)

    st.subheader("Project Team")

    team = pd.DataFrame(
        {
            "Member": [
                "Muhammad Sameer",
                "Zain Abbas",
                "Shabaz"
            ]
        }
    )

    st.table(team)

    col1, col2, col3 = st.columns(3)

    col1.metric("Connected Devices", "250")
    col2.metric("Threat Alerts", "12")
    col3.metric("Security Score", "88%")

# -------------------------------
# INDUSTRIAL IOT
# -------------------------------
elif page == "Industrial IoT":

    st.title("🏭 Industrial IoT")

    st.write("""
    Industrial Internet of Things (IIoT) refers to interconnected
    industrial devices, sensors, machines, and control systems.

    Applications include:

    - Smart Manufacturing
    - Smart Energy Systems
    - Oil and Gas Monitoring
    - Industrial Robotics
    - Smart Water Systems
    """)

# -------------------------------
# CYBER THREATS
# -------------------------------
elif page == "Cyber Threats":

    st.title("⚠ Cybersecurity Threats")

    threats = pd.DataFrame(
        {
            "Threat": [
                "Ransomware",
                "DDoS Attack",
                "Malware",
                "Unauthorized Access",
                "Data Breach",
                "Insider Threat"
            ],
            "Risk Level": [
                "High",
                "High",
                "High",
                "Medium",
                "Medium",
                "Medium"
            ]
        }
    )

    st.dataframe(threats, use_container_width=True)

# -------------------------------
# RISK ASSESSMENT
# -------------------------------
elif page == "Risk Assessment":

    st.title("📊 Risk Assessment")

    devices = st.slider(
        "Connected Devices",
        1,
        1000,
        100
    )

    vulnerabilities = st.slider(
        "Known Vulnerabilities",
        0,
        100,
        20
    )

    exposure = st.slider(
        "Network Exposure (%)",
        0,
        100,
        50
    )

    risk_score = (
        devices * 0.2
        + vulnerabilities * 2
        + exposure
    )

    st.metric(
        "Calculated Risk Score",
        round(risk_score, 2)
    )

    if risk_score < 100:
        st.success("Low Risk")
    elif risk_score < 250:
        st.warning("Medium Risk")
    else:
        st.error("High Risk")

# -------------------------------
# DASHBOARD
# -------------------------------
elif page == "Monitoring Dashboard":

    st.title("📈 Device Monitoring Dashboard")

    data = pd.DataFrame(
        {
            "Device": [
                "PLC-01",
                "PLC-02",
                "Sensor-01",
                "Sensor-02",
                "Gateway-01"
            ],
            "CPU Usage": np.random.randint(20, 90, 5),
            "Status": [
                "Online",
                "Online",
                "Offline",
                "Online",
                "Online"
            ]
        }
    )

    st.dataframe(data, use_container_width=True)

    st.subheader("CPU Usage")

    st.bar_chart(
        data.set_index("Device")["CPU Usage"]
    )

# -------------------------------
# SECURITY CONTROLS
# -------------------------------
elif page == "Security Controls":

    st.title("🔐 Security Controls")

    controls = [
        "Multi-Factor Authentication (MFA)",
        "Network Segmentation",
        "Encryption",
        "Zero Trust Security",
        "Intrusion Detection System (IDS)",
        "Regular Firmware Updates",
        "Vulnerability Assessment",
        "SIEM Monitoring"
    ]

    for control in controls:
        st.success(control)

st.divider()

st.caption(
    "ICT for Cybersecurity : Industrial IoT | Group Project"
)
