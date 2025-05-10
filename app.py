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
Le Plan Matériel est le centre du multivers, le monde "réel" où vivent les mortels. Il comprend de nombreux mondes : Faerûn, Eberron, Krynn…

**Traits :** lois naturelles, magie équilibrée.  
**Connexion :** il est lié au Feywild (plan féerique) et au Shadowfell (plan d’ombre) comme des reflets déformés.
""")

with st.expander("🔮 Plans Parallèles"):
    st.markdown("### ✨ Feywild (Plan Féérique)")
    st.markdown("""
Reflet vibrant et magique du Plan Matériel. Lieu de nature luxuriante, de saisons imprévisibles et de puissants êtres féeriques (archifées, dryades...).

**Effets :** magie amplifiée, émotion exacerbée.  
**Habitants :** elfes féeriques, pixies, licornes.
""")

    st.markdown("### 🌑 Shadowfell (Plan de l’Ombre)")
    st.markdown("""
Reflet sombre et morne du monde matériel. Énergie nécrotique, désespoir ambiant. Les morts-vivants y sont puissants.

**Effets :** fatigue mentale, lieu de nécromancie.  
**Habitants :** âmes perdues, ombres, nécromanciens.
""")

with st.expander("🔁 Plans Transitifs"):
    st.markdown("### 🌫️ Plan Éthéré")
    st.markdown("""
Superposé au Plan Matériel, permet de voir sans être vu. Fréquenté par fantômes et voyageurs planaires.

**Effet :** invisibilité partielle, mouvement lent.  
**Usage :** utilisé par les sorts de voyage ou de dissimulation.
""")

    st.markdown("### 🌀 Plan Astral")
    st.markdown("""
Vaste mer argentée reliant les autres plans. Suspendu dans le temps, il sert de voie de passage.

**Effet :** corps physique reste derrière, pas de vieillissement.  
**Habitants :** githyankis, entités cosmiques, astral dreadnoughts.
""")

with st.expander("🔥 Plans Élémentaires"):
    st.markdown("### 🌬️ Plan de l’Air")
    st.markdown("""
Un royaume infini de cieux, de vents violents et d’îles flottantes. Djinns et créatures volantes y vivent.

**Dangers :** chute infinie, orages planaires.  
**Effets :** flottement naturel, difficulté à se stabiliser.
""")

    st.markdown("### 🌊 Plan de l’Eau")
    st.markdown("""
Un océan infini. Pas de surface ni de fond. Les marids règnent sur d’immenses cités sous-marines.

**Effets :** pression aquatique, absence de feu.  
**Habitants :** sirènes, krakens, poissons géants.
""")

    st.markdown("### 🔥 Plan du Feu")
    st.markdown("""
Un brasier sans fin, avec des terres de cendres et des cités de lave. Éfrits, salamandres, élémentaires y prospèrent.

**Température :** insoutenable sans magie.  
**Effets :** inflammation immédiate, rareté de l’eau.
""")

    st.markdown("### 🪨 Plan de la Terre")
    st.markdown("""
Domaine souterrain de tunnels et cavernes immenses. Parfois traversé de cristaux lumineux.

**Effets :** densité extrême, instabilité tectonique.  
**Habitants :** dao, xorn, golems.
""")

with st.expander("🌟 Plans Extérieurs"):
    st.markdown("### ⚖️ Mont Céleste (Loyal Bon)")
    st.markdown("""
Montagne infinie d’élévation morale et spirituelle. Ordre, bonté, justice.

**Habitants :** anges, archons.  
**Lieu sacré :** serments, pèlerinages, rédemption.
""")

    st.markdown("### 🌿 Arvandor (Chaotique Bon)")
    st.markdown("""
Domaine des dieux elfes, forêt éternelle et sauvage. Liberté, art et beauté.

**Habitants :** dieux elfes, esprits sylvestres.
""")

    st.markdown("### 🔥 Abysses (Chaotique Mauvais)")
    st.markdown("""
Plans en spirale de chaos pur. Chaque couche est différente. Demeure des démons.

**Effets :** mutation, anarchie totale.  
**Habitants :** Démogorgon, Orcus, Juiblex…
""")

    st.markdown("### 🧊 Baator / Neuf Enfers (Loyal Mauvais)")
    st.markdown("""
Neuf niveaux de tyrannie infernale. Bureaucratie démoniaque. Pactes, trahisons, domination.

**Habitants :** Asmodéus, diables majeurs.
""")

    st.markdown("### ⚙️ Mécanus (Loyal Neutre)")
    st.markdown("""
Rouages géants qui régissent la loi universelle. Tout y est calculé, logique absolue.

**Habitants :** Modrons, constructeurs divins.
""")

    st.markdown("### 🌪️ Limbe (Chaotique Neutre)")
    st.markdown("""
Champ de pure entropie. Seules les volontés fortes y façonnent la réalité.

**Habitants :** slaads, githzerai.
""")

    st.markdown("### ⚫ Outreterre (Neutre Pur)")
    st.markdown("""
Ville infinie au centre de tous les plans : Sigil. Gouvernée par la Dame des Douleurs.

**Particularité :** portails vers tous les autres plans.
""")
