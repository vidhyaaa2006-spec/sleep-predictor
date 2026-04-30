import streamlit as st
import matplotlib.pyplot as plt

st.title("🌙 Sleep Quality Predictor")

# -----------------------------
# LAYOUT
# -----------------------------
col1, col2 = st.columns(2)

# INPUT (LEFT)
with col1:
    st.subheader("Input")
    sleep = st.slider("Sleep Hours", 0.0, 10.0, 7.0)
    screen = st.slider("Screen Time", 0, 180, 60)
    exercise = st.slider("Exercise", 0, 60, 20)
    stress = st.slider("Stress", 0, 10, 5)

    predict = st.button("Predict")

# OUTPUT (RIGHT)
with col2:
    st.subheader("Result")

    if predict:
        score = 100
        score -= abs(7 - sleep) * 10
        score -= screen * 0.2
        score += exercise * 0.5
        score -= stress * 5
        score = max(0, min(100, score))

        if score >= 75:
            quality = "Good 😃"
        elif score >= 50:
            quality = "Average 🙂"
        else:
            quality = "Poor 😴"

        st.metric("Score", f"{round(score,2)}")
        st.write("Quality:", quality)

        # -----------------------------
        # GRAPH
        # -----------------------------
        st.subheader("Graph")
        factors = ["Sleep", "Screen", "Exercise", "Stress"]
        values = [sleep, screen/10, exercise/10, stress]

        fig, ax = plt.subplots()
        ax.bar(factors, values)
        st.pyplot(fig)

        # Suggestions
        if screen > 60:
            st.write("👉 Reduce screen time")
        if exercise < 20:
            st.write("👉 Do exercise")
        if stress > 6:
            st.write("👉 Reduce stress")
        if sleep < 6:
            st.write("👉 Sleep more")