
import streamlit as st

st.title("Diablo Immortal Damage Calculator")

# Inputs
base_dmg = st.number_input("Total Base DMG", min_value=0.0, value=10000.0)
resonance = st.number_input("Resonance", min_value=0.0, value=1000.0)
tourmaline = st.number_input("Tourmaline DMG", min_value=0.0, value=1500.0)
intelligence = st.number_input("INT / STR", min_value=0.0, value=2000.0)
paragon = st.number_input("Paragon DMG", min_value=0.0, value=300.0)
horadrim = st.number_input("Horadrim DMG", min_value=0.0, value=200.0)

b1 = st.slider("B1 Modifier (%)", 0.0, 100.0, 6.0) / 100
b2 = st.slider("B2 Modifier (%)", 0.0, 100.0, 10.0) / 100
b3 = st.slider("B3 Modifier (%)", 0.0, 100.0, 5.0) / 100
crit_chance = st.slider("Crit Chance (%)", 0.0, 100.0, 22.0) / 100
crit_dmg = st.slider("Crit DMG Multiplier", 0.0, 3.0, 1.5)
attack_speed = st.slider("Attack Speed (%)", 0.0, 100.0, 50.0) / 100

# Calculation
resonance_bonus = resonance * 0.0005 * base_dmg
int_bonus = intelligence * 0.3

base_total = base_dmg + resonance_bonus + tourmaline + int_bonus + paragon + horadrim
normal_dmg = base_total * (1 + b1) * (1 + b2) * (1 + b3) * 1.113
crit_dmg_total = normal_dmg * (1 + crit_dmg)
avg_dmg = base_total * (1 + attack_speed)
build_score = (1 + b1) * (1 + b2) * (1 + b3) * 1.113 * (1 + crit_chance * crit_dmg) * (1 + attack_speed)

# Output
st.markdown("### Results")
st.write(f"**Base DMG:** {base_total:.2f}")
st.write(f"**Normal DMG:** {normal_dmg:.2f}")
st.write(f"**Crit DMG:** {crit_dmg_total:.2f}")
st.write(f"**Avg. DMG (AS scaled):** {avg_dmg:.2f}")
st.write(f"**Build Score:** {build_score:.2f}")
