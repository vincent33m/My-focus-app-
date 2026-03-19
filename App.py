import streamlit as st
import random

# App Config
st.set_page_config(page_title="FocusFlow: Goal & Fuel", page_icon="⚡")

st.title("⚡ FocusFlow")
st.subheader("ADHD-Friendly Goal Tracker")

# --- SIDEBAR: GOAL SETTING ---
with st.sidebar:
    st.header("🎯 Your North Star")
    goal = st.selectbox("What's the mission?", ["Build Muscle", "Burn Fat", "Mental Clarity/Endurance"])
    energy_level = st.slider("Current Energy Level (1-10)", 1, 10, 5)
    
# --- MAIN INTERFACE ---
tab1, tab2, tab3 = st.tabs(["Daily Workout", "Dopamine Meals", "Progress"])

with tab1:
    st.header("💪 Today's Movement")
    if st.button("Generate My Workout"):
        # Logic tailored to ADHD: Short, high-intensity or engaging movements
        workouts = {
            "Build Muscle": ["Pushups (3x10)", "Bulgarian Split Squats (3x8)", "Plank (45s)"],
            "Burn Fat": ["Mountain Climbers (30s)", "Burpees (10)", "Jump Rope (2 mins)"],
            "Mental Clarity/Endurance": ["Sun Salutations (5 mins)", "Fast Walk (15 mins)", "Shadow Boxing (3 mins)"]
        }
        
        selected = workouts[goal]
        st.success(f"**Focus on these 3 things only. Don't look at the rest!**")
        for exercise in selected:
            st.write(f"- {exercise}")
        st.balloons()

with tab2:
    st.header("🍽️ The 'Not-a-Diet' Menu")
    st.info("Focus: Quick, high-protein, and high-flavor to keep your brain happy.")
    
    if st.button("I'm Hungry - Give Me a Plan"):
        meals = [
            {"Name": "Air-Fryer Taco Bowl", "Why": "Crunchy, salty, and fast. Hits the dopamine button."},
            {"Name": "Protein Mug Cake", "Why": "Feels like a cheat, works like a fuel."},
            {"Name": "'Lazy' Greek Wrap", "Why": "No cooking required. Zero friction."}
        ]
        meal = random.choice(meals)
        st.markdown(f"### 🌮 {meal['Name']}")
        st.write(f"**The ADHD Hack:** {meal['Why']}")

with tab3:
    st.header("📈 Small Wins")
    st.checkbox("Drank 1 glass of water")
    st.checkbox("Moved for at least 5 minutes")
    st.checkbox("Ate one 'color' (veg/fruit)")
