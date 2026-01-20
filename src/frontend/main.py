import streamlit as st
import httpx
from datetime import date


API_URL = "http://127.0.0.1:8000"


def InputInformationPage():
    # ⚙️ Configuration de la page (à appeler UNE SEULE FOIS dans l'app)
    st.set_page_config(
        page_title="Formulaire utilisateur",
        layout="wide",
    )

    st.title("Création d'un utilisateur")
    st.markdown("Veuillez renseigner les informations ci-dessous.")

    # === FORMULAIRE ===
    with st.form("create_user_form"):
        name = st.text_input("Nom", placeholder="Ex : Dupont")
        email = st.text_input("Email", placeholder="exemple@mail.com")
        age = st.number_input(
            "Âge",
            min_value=0,
            max_value=120,
            step=1,
        )
        date_ctrl = st.date_input(
            "Date dernier contrôle",
            value=date.today(),
        )

        submitted = st.form_submit_button("Créer utilisateur")

    # === ACTION APRÈS SOUMISSION ===
    if submitted:
        # 🔍 Validation minimale côté frontend
        if not name or not email:
            st.warning("Le nom et l'email sont obligatoires.")
            return

        payload = {
            "name": name,
            "email": email,
            "age": int(age),
            "DateDaernierControlTech": date_ctrl.isoformat(),
        }

        try:
            # 📡 Appel à l'API FastAPI
            response = httpx.post(
                f"{API_URL}/users/",
                json=payload,
                timeout=1.0,
            )

            if response.status_code == 200:
                st.success("Utilisateur créé avec succès ✅")

            elif response.status_code == 409:
                st.error("Un utilisateur avec cet email existe déjà.")

            else:
                st.error(
                    f"Erreur serveur ({response.status_code}) : {response.text}"
                )

        except httpx.RequestError:
            st.error("Impossible de contacter l'API. Vérifiez que le backend est lancé.")
    
if __name__ =="__main__":
    InputInformationPage()