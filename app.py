import streamlit as st

st.set_page_config(page_title="Plans d'existence D&D", page_icon="🌌", layout="centered")

st.title("🌌 Plans d'existence - Donjons & Dragons")

st.image(
    "plans.jpg",
    caption="Illustration de la cosmologie des plans - Source : aidedd.org",
    use_container_width=True
)

with st.expander("🟢 Plan Matériel"):
    st.markdown("""
**Description** : Le monde physique où vivent la plupart des créatures. On y trouve Faerûn, Eberron, etc.  
**Usage** : Base des aventures, monde tangible.  
**Connexions** : Vers le Feywild et le Shadowfell.
""")

with st.expander("🔮 Plans Parallèles"):
    st.markdown("""
**Féerie (Feywild)** : Reflet magique, sauvage et capricieux du monde matériel.  
**Gisombre (Shadowfell)** : Monde d'ombre, de mort et de désespoir.
""")

with st.expander("🔁 Plans Transitis"):
    st.markdown("""
**Plan Éthéré** : Superposé au monde physique, utilisé pour l’invisibilité ou le voyage dimensionnel.  
**Plan Astral** : Vide intemporel entre les mondes, souvent emprunté par les puissants lanceurs de sorts.
""")

with st.expander("🔥 Plans Élémentaires"):
    st.markdown("""
**Air, Feu, Terre, Eau** : Royaumes d’éléments purs.  
**Para-élémentaires** : Magma, Glace, etc.  
**Quasi-élémentaires** : Cendre, Radiance, etc.
""")

with st.expander("🌟 Plans Extérieurs"):
    st.markdown("""
**Alignés sur l’alignement moral** :  
- Bien : Mont Céleste, Champs Élysées…  
- Mal : Abysses, Baator…  
- Neutre : Mécanus, Outreterre…
""")
