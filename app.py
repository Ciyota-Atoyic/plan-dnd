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
    st.markdown("### 🔥 Baator – Les Neuf Enfers (Loyal Mauvais)")
    st.markdown("""
Un plan infernal structuré en **neuf strates**, chacune dirigée par un archidiable. Baator est un royaume de lois cruelles, où les contrats sont plus tranchants que les lames.

- **Gouverné par :** Asmodéus, Seigneur des Neuf Enfers
- **Strates célèbres :** Avernus (champ de bataille), Dis (forteresse de fer), Nessus (trône d’Asmodéus)
- **Habitants :** Diables, erinyes, légions infernales
- **Particularité :** Les pactes occultes y prennent forme

**Lore :** C’est ici que de nombreux Tieffelins trouvent leurs origines infernales.
""")

    st.markdown("### ⚖️ Mont Céleste – Celestia (Loyal Bon)")
    st.markdown("""
Un plan en forme de montagne gigantesque aux **sept cieux superposés**. Refuge des âmes justes, des anges et des champions de la justice.

- **Aspect :** Pureté, lumière, harmonie hiérarchisée
- **Habitants :** Archons, anges, âmes élevées
- **Lieux sacrés :** Empyrée, fontaines de guérison, portails de pénitence

**Usage en jeu :** Terre d’épreuves pour les paladins et clercs cherchant la rédemption.
""")

    st.markdown("### 🌿 Arvandor – Plan des Elfes (Chaotique Bon)")
    st.markdown("""
Forêt infinie où l’art, la liberté et la beauté dominent. Domaine de **Corellon Larethian**, dieu des elfes.

- **Paysage :** Nature luxuriante, magie sauvage, féerie constante
- **Habitants :** Elfes divins, dryades, esprits sylvestres
- **Effets :** Favorise la créativité et la spontanéité

**Lien :** Accessible via le Feywild ou les rituels elfiques anciens.
""")

    st.markdown("### ⚙️ Mécanus – Plan de la Loi Parfaite (Loyal Neutre)")
    st.markdown("""
Rouages titanesques qui tournent sans fin dans le vide. Chaque engrenage est un monde, où tout est prédéfini par l’ordre universel.

- **Habitants :** Modrons, légions juridiques, entités logiques
- **Rythme :** Aucun hasard, tout est prévu
- **Dieux présents :** Helm, Saint Cuthbert

**Effets magiques :** Les sorts chaotiques sont affaiblis ici.
""")

    st.markdown("### 🌪️ Limbe – Le Chaos Primordial (Chaotique Neutre)")
    st.markdown("""
Un océan de matière brute et informe, façonné uniquement par l’esprit de ceux qui y voyagent. C’est le plan de la pensée créatrice... ou destructrice.

- **Habitants :** Slaads, githzerai, élémentaires fous
- **Danger :** Forme instable, mutation spontanée
- **Utilité :** Terrain d'entraînement mental des moines githzerai

**Note :** Certaines citadelles sont figées grâce à la force de volonté collective.
""")

    st.markdown("### ⚫ Outreterre – Sigil et ses Portes (Neutre Pur)")
    st.markdown("""
Au centre de la Grande Roue se trouve **Sigil**, la Cité des Portes, suspendue dans une coquille en forme d’anneau. Gouvernée par la mystérieuse Dame des Douleurs.

- **Accès :** Portails vers tous les autres plans
- **Population :** Cosmopolite : diables, anges, mortels…
- **Particularité :** Neutralité forcée – pas de dieux autorisés

**Usage :** Base parfaite pour une campagne planaire.
""")

    st.markdown("### 🌊 Champs Élysées – Plan de Paix Absolue (Neutre Bon)")
    st.markdown("""
Royaume de nature parfaite, où repos et harmonie sont éternels. C’est le plan de l’oubli heureux.

- **Ambiance :** Douce, lente, paisible
- **Habitants :** Esprits en paix, licornes, bêtes mythiques
- **Danger :** Rester trop longtemps mène à l’apathie éternelle

**Utilisation :** Refuge ultime pour les âmes blessées ou repentantes.
""")

    st.markdown("### 🔥 Abysses – Le Chaos Démoniaque (Chaotique Mauvais)")
    st.markdown("""
Un gouffre infini aux strates illimitées. Chaque couche est une horreur unique. Le domaine incontesté des démons.

- **Strates notables :** 88e (Zuggtmoy), 113e (Orcus), 222e (Demogorgon)
- **Habitants :** Balors, succubes, larves
- **Règle :** Aucun. Survie, domination, destruction

**Danger ultime :** Aucune logique, aucune limite.
""")

    st.markdown("### ⚫ Gehenne – Plan de l’Équilibre Incliné (Neutre Mauvais)")
    st.markdown("""
Plan de volcans en équilibre sur des pentes impossibles. Lieu de souffrance silencieuse et de secret.

- **Population :** Yugoloths, âmes punies, monstres neutres
- **Climat :** Souffre, pénombre, vents coupants
- **Objectif :** Échange, espionnage, torture philosophique

**Particularité :** Chaque action a un prix mesuré.
""")
