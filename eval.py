import streamlit as st

st.title("📊 Évaluateur de Rentabilité Client")

st.header("Critères qualitatifs")

org = st.selectbox("Organisation client", [0, 1, 2])
presc = st.selectbox("Prescription client", [0, 1, 2])
missions = st.selectbox("Missions potentielles", [0, 1, 2])
complexite = st.selectbox("Complexité structure", [0, 1, 2])
finance = st.selectbox("Capacité de financement", [0, 1, 2])
taille = st.selectbox("Taille structure", [0, 1, 2])

st.header("Ancienneté")

anciennete = st.radio(
    "Ancienneté du client",
    ["< 5 ans", "Entre 5 et 10 ans", "> 10 ans"]
)

st.header("Données économiques")

honoraires = st.number_input("Honoraires annuels (€)", min_value=0)
temps = st.number_input("Temps annuel (heures)", min_value=0)

if st.button("Calculer la rentabilité"):

    score = 0

    # Pondérations
    score += org * 1
    score += presc * 3
    score += missions * 2
    score += complexite * 1
    score += finance * 2
    score += taille * 1

    # Ancienneté
    if anciennete == "> 10 ans":
        score += 4
    elif anciennete == "Entre 5 et 10 ans":
        score += 2

    # Rentabilité horaire
    if temps > 0:
        taux = honoraires / temps
    else:
        taux = 0

    # Bonus rentabilité
    if honoraires > 2500:
        if taux > 100:
            score += 10
        elif taux > 50:
            score += 5

    st.subheader("📈 Résultats")
    st.write(f"Rentabilité horaire : {round(taux,2)} € / h")
    st.write(f"Score final : {score}")

    # Classification
    if score >= 30:
        st.success("Client stratégique 🟢")
    elif score >= 20:
        st.warning("Client à développer 🟡")
    else:
        st.error("Client à surveiller 🔴")
