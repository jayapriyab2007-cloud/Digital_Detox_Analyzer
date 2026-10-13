import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Digital Detox Score Analyzer",
    page_icon="📱",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>

.main-title{
    text-align:center;
    color:#2E8B57;
    font-size:42px;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    font-size:20px;
    color:gray;
}

.report-box{
    background-color:#F8F9FA;
    padding:20px;
    border-radius:15px;
    border:2px solid #E0E0E0;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.title("📖 Instructions")

st.sidebar.info("""
1. Enter your details.

2. Fill in your daily habits.

3. Click **Analyze Lifestyle**.

4. View your Digital Detox Score.

5. Follow the personalized suggestions.
""")

st.sidebar.success("Healthy Digital Habits = Healthy Mind 🌿")

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.markdown('<p class="main-title">📱 Digital Detox Score Analyzer</p>', unsafe_allow_html=True)

st.markdown(
    '<p class="sub-title">Analyze your digital habits and improve your lifestyle.</p>',
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# USER DETAILS
# --------------------------------------------------
st.header("👤 User Information")

name = st.text_input("Enter Your Name")

col1, col2 = st.columns(2)

with col1:
    screen_time = st.number_input(
        "💻 Daily Screen Time (Hours)",
        0.0,24.0,0.0,0.5
    )

    sleep = st.number_input(
        "😴 Sleep Duration (Hours)",
        0.0,24.0,0.0,0.5
    )

with col2:
    social_media = st.number_input(
        "📱 Social Media Usage (Hours)",
        0.0,24.0,0.0,0.5
    )

    exercise = st.number_input(
        "🏃 Exercise (Minutes)",
        0,300,0
    )

water = st.slider(
    "💧 Daily Water Intake (Litres)",
    0.0,5.0,2.0,0.5
)

st.divider()

# --------------------------------------------------
# BUTTON
# --------------------------------------------------
if st.button("🔍 Analyze Lifestyle", use_container_width=True):

    if name.strip() == "":
        st.error("⚠ Please enter your name.")

    else:

        score = 100
        suggestions = []

        # Screen Time
        if screen_time > 8:
            score -= 30
            suggestions.append("Reduce your daily screen time to below 6 hours.")

        elif screen_time >= 6:
            score -= 15
            suggestions.append("Try reducing your screen time slightly.")

        # Social Media

        if social_media > 4:
            score -= 20
            suggestions.append("Limit social media usage.")

        elif social_media >= 2:
            score -= 10
            suggestions.append("Reduce unnecessary scrolling.")

        # Sleep

        if sleep < 6:
            score -= 20
            suggestions.append("Sleep at least 7-8 hours every night.")

        elif sleep < 7:
            score -= 10
            suggestions.append("Increase your sleep duration.")

        # Exercise

        if exercise < 30:
            score -= 15
            suggestions.append("Exercise for at least 30 minutes daily.")

        # Water

        if water < 2:
            score -= 10
            suggestions.append("Drink more water (2-3 litres daily).")

        score = max(score,0)

        # Rating

        if score >= 90:
            rating = "🌟 Excellent"
            color = "success"

        elif score >= 75:
            rating = "😊 Good"
            color = "info"

        elif score >= 60:
            rating = "🙂 Average"
            color = "warning"

        elif score >= 40:
            rating = "😐 Poor"
            color = "warning"

        else:
            rating = "⚠ Needs Improvement"
            color = "error"

        st.divider()

        st.header("📊 Digital Detox Report")

        c1,c2,c3 = st.columns(3)

        c1.metric("Digital Detox Score", f"{score}/100")
        c2.metric("Lifestyle Rating", rating)
        c3.metric("Water Intake", f"{water} L")

        st.progress(score/100)

        if color=="success":
            st.success(rating)

        elif color=="info":
            st.info(rating)

        elif color=="warning":
            st.warning(rating)

        else:
            st.error(rating)

        st.divider()

        st.subheader("💡 Personalized Suggestions")

        if len(suggestions)==0:

            st.success("🎉 Congratulations! Your digital lifestyle is excellent.")

            st.balloons()

        else:

            for tip in suggestions:
                st.write("✔",tip)

        st.divider()

        st.subheader("🌿 Healthy Habit Tips")

        tips = [
            "📖 Read a book for at least 30 minutes.",
            "🚶 Take a short walk without your phone.",
            "👨‍👩‍👧 Spend quality time with your family.",
            "🧘 Practice meditation for 10 minutes.",
            "😴 Avoid using mobile phones before bedtime."
        ]

        for t in tips:
            st.write(t)

        st.divider()

        st.subheader("📌 Summary")

        st.markdown(f"""
### Hello, **{name}** 👋

Your Digital Detox Score is **{score}/100**.

**Lifestyle Rating:** **{rating}**

Following the above suggestions can help improve your digital well-being and maintain a healthier lifestyle.
""")
