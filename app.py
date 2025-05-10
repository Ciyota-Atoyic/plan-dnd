

import streamlit as st

st.set_page_config(page_title="Plans d'existence D&D", page_icon="🌌", layout="centered")
st.title("🌌 Plans d'existence - Donjons & Dragons")

st.image(
    "plans.jpg",
    caption="Illustration de la cosmologie des plans - Source : aidedd.org",
    use_container_width=True
)

choix = st.radio(
    "Choisissez une catégorie de plans :",
    [
        "Plan Matériel",
        "Plans Parallèles",
        "Plans Transitifs",
        "Plans Élémentaires",
        "Plans Extérieurs"
    ]
)



if choix == "Plan Matériel": aidedd.org",
    use_container_width=True
)

with st.expander("🟢 Plan Matériel"):
    st.markdown("""
Le Plan Matériel est le centre du multivers, le monde "réel" où vivent les mortels. Il comprend de nombreux mondes : Faerûn, Eberron, Krynn…

**Traits :** lois naturelles, magie équilibrée.  
**Connexion :** il est lié au Feywild (plan féerique) et au Shadowfell (plan d’ombre) comme des reflets déformés.
""")



elif choix == "Plans Parallèles"::
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



elif choix == "Plans Transitifs"::
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



elif choix == "Plans Élémentaires"::
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



elif choix == "Plans Extérieurs":
 (Détaillés)"):

    st.markdown("## 🔥 Baator – Les Neuf Enfers (Loyal Mauvais)")
    st.markdown("""
Baator est un plan rigide et impitoyable divisé en **neuf couches**, chacune dirigée par un archidiable et régie par des lois tyranniques.

### 1. Avernus
Champ de bataille éternel contre les démons. Cieux rouges, pluies de sang, rivières de feu. Gouvernée par Zariel.
- **Usage :** Front de la Guerre Sanglante
- **Effets :** Brouillage magique, hostilité permanente

### 2. Dis
Cité-labyrinthe de fer ardent. Dominée par Dispater. Pièges, illusions et bureaucratie infernale.
- **Usage :** Prison mentale et politique
- **Danger :** Perte d’identité par paperasse

### 3. Minauros
Marais fétide et puant. Gouverné par Mammon. Boue acide et infrastructures instables.
- **Effets :** Affaiblissement, maladies, pourriture

### 4. Phlégethos
Océan de lave flamboyante, domaine de Belial et Fierna. Lieu de plaisir cruel et d’excès flamboyant.
- **Habitat :** Palaces de feu et douleur

### 5. Stygia
Océan glacé avec épaves et ruines figées dans la glace. Dirigé par Levistus (emprisonné sous la glace).
- **Effets :** Tempêtes magiques, isolement psychique

### 6. Malbolge
Montagne effondrée en éternelle reconstruction. Gouvernée par Glasya. Tortures architecturales.
- **Dynamique :** Ruines, tunnels, instabilité physique et politique

### 7. Maladomini
Ruines de villes abandonnées, constructions jamais terminées. Gouvernée par Baalzebul.
- **Thème :** Déchéance, vanité, orgueil sans fin

### 8. Cania
Froid extrême, murs de glace noire. Contrôlée par Mephistopheles. Laboratoire de magie noire et de manipulation planaires.
- **Effets :** Congélation instantanée sans magie de protection

### 9. Nessus
Abysses infernaux où trône Asmodéus. Forteresse impénétrable. Pouvoir absolu.
- **Lieux :** Malsheem (capitale), archives infernales
""")

    st.markdown("## ⚖️ Mont Céleste – Celestia (Loyal Bon)")
    st.markdown("""
Un plan en forme de montagne aux **sept strates célestes**. Chaque couche représente une montée vers la pureté divine.

### 1. Lunia – Mer d'Argent
Côte argentée, où les âmes arrivent. Protégée par des anges et archons.
- **Portails :** Connexion au Plan Astral

### 2. Mercuria – Champ des Héros
Plaine dorée et temples glorieux. Lieu de justice, où reposent les champions du Bien.
- **Habitants :** Héros ressuscités, clercs honorés

### 3. Venya – Vallée de Compassion
Collines paisibles, terres fertiles. Harmonie entre la bonté et l’ordre.
- **Divinités :** Chauntea, Yondalla

### 4. Solania – Montagnes de Révélation
Sommets argentés, monastères célestes. Recherche de sagesse divine.
- **Habitants :** Moines célestes, esprits contemplatifs

### 5. Mertion – Ville de la Rédemption
Cité brillante, salles de guérison, confession céleste.
- **Usage :** Pèlerinage d’âmes blessées

### 6. Jovar – Royaume des Anges
Cité d’or, justice parfaite. Tribunal divin, légions de lumière.
- **Lieu de :** Jugement des plans

### 7. Chronias – L’Illumination Pure
Noyau sacré. Inaccessible aux mortels. L’âme y est absorbée dans la perfection.
- **Effet :** Dissolution dans le divin
""")

    st.markdown("## 🌿 Arvandor – Royaume Elfique (Chaotique Bon)")
    st.markdown("""
Arvandor est le domaine de **Corellon Larethian** et des divinités elfiques. Ce plan forestier et éternel évolue selon la nature et les mythes.

### Domaines majeurs :

#### • Forêt Céleste
Une canopée d’arbres millénaires, maisons suspendues dans les cieux.
- **Effets :** Régénération magique, communion avec la nature

#### • Clairières Étoilées
Cercles de danse féerique où les fées et dryades festoient.
- **Événement :** Transes prophétiques

#### • Palais de Corellon
Cité sculptée dans la lumière, siège du dieu des elfes.
- **Habitants :** Divinités : Sehanine, Labelas Enoreth, Erevan Ilesere

#### • Torrent d'Arborescence
Cascade de magie pure qui nourrit le plan.
- **Usage :** Rituels ancestraux, créations artistiques divines
""")
st.markdown("## ⚙️ Mécanus – Rouages de la Loi Parfaite (Loyal Neutre)")
    st.markdown("""
Mécanus est un plan constitué de **rouages mécaniques géants**, chacun abritant une civilisation ou un royaume. Chaque rouage tourne lentement et en harmonie avec les autres.

### 12 Royaumes Notables :

- **Regulus** : Capitale des modrons, siège de Primus, l'entité suprême de la Loi.
- **Nemausus** : Ancien domaine elfique, aujourd’hui stabilisé par la Loi.
- **The Clockwork City** : Citadelle humaine de philosophes et d’horlogers.
- **Metron** : Haut lieu des décisions interplanaires neutres.
- **Colyphyr** : Marché juridico-magique.
- **Dural** : Forteresse des juristes extraplanaires.
- **Xeraph** : Monastère dédié au temps cyclique.
- **Cognis** : Centre de calculs divins.
- **Axis Terminus** : Point zéro du mouvement planaire.
- **Volach** : Rouage scellé aux lois inconnues.
- **Verity** : Refuge pour les entités véridiques.
- **Zenith** : Sommet logique absolu (lieu théorique)

**Spécificité :** Le temps y est strictement mesuré, et l’erreur y est punie par l’exil.

""")

    st.markdown("## ⚫ Outreterre – Sigil et les 3 Couronnes (Neutre Pur)")
    st.markdown("""
Au centre de la Grande Roue se trouve **Sigil**, la Cité des Portes, suspendue en hauteur, régie par la Dame des Douleurs.

### Les 3 Niveaux symboliques de l’Outreterre :

- **La Couronne Inférieure** : Quartiers pauvres, temples déchus, portails instables. Refuge des fuyards planaires.
- **La Couronne Médiane** : Zone commerciale, cosmopolite, foire aux portails, auberges extraplanaires.
- **La Couronne Supérieure** : Sphères philosophiques, demeures extraplanaires, refuges des factions.

**Note :** Chaque couronne influence la stabilité magique des portails qu’elle contient.

""")

    st.markdown("## 🌊 Champs Élysées – Demeure de l’Harmonie Parfaite (Neutre Bon)")
    st.markdown("""
Un plan d’équilibre paisible, divisé en **quatre strates** toutes baignées d’une lumière dorée.

### 1. Amoria
Champs ouverts, cieux dégagés, lieux de chasse divine et de sérénité communautaire.

### 2. Eronia
Montagnes paisibles et vallées florissantes. Guérison naturelle, inspiration poétique.

### 3. Belierin
Forêts épaisses et lacs sacrés. Silence, méditation, communion avec la nature.

### 4. Thalasia
Océan cristallin, barques d’âmes flottantes. Repos éternel. Cité engloutie d’Erathaol.

**Spécial :** Plus on s’enfonce dans les strates, plus l’âme se libère des souffrances mortelles.

""")

    st.markdown("## 🌳 Abysses – L'Arbre Monde, la Sève du Chaos")
    st.markdown("""
Les Abysses sont un gouffre infini en spirale, traversé par **l'Arbre Monde (Yggdrasil démoniaque)**. Ses racines percent les strates et ses branches propagent la corruption.

- **Origine :** Née du premier meurtre céleste, l’Arbre Monde porte la sève noire du chaos.
- **Strates traversées :**
  - 88e : **Fungus Infernal** de Zuggtmoy, champignon géant fusionné à l’arbre
  - 113e : **Nécropole d’Orcus**, branches mortes et moelles des morts
  - 222e : **Forêt Fractale** de Demogorgon, feuillage psychotique
  - Autres : Vortex larvaire, Gouleplan, Marais de sang

**Danger :** Suivre une branche trop loin peut vous faire chuter dans une strate plus profonde sans retour possible.

""")

    st.markdown("## ⚫ Géhenne – Les 4 Strates de la Balance Pentée (Neutre Mauvais)")
    st.markdown("""
La Géhenne est un plan volcanique, chaque strate étant une montagne suspendue dans le vide et inclinée à un angle extrême.

### 1. Khalas
Rivières de soufre, torrents ardents, temples corrompus des yugoloths. Lieu d’invocations et de négociations sombres.

### 2. Chamada
Flammes explosives, failles déchirantes, grands marchés noirs extraplanaires.

### 3. Mungoth
Terres de cendres, vent empoisonné, refuge de pactes oubliés. Demeures des traîtres et renégats planaires.

### 4. Krangath
Strate morte, sans feu ni chaleur, dominée par le silence et les ruines. Sanctuaire des yugoloths anciens.

**Spécificité :** Chacune des strates exige un effort constant pour ne pas glisser vers la damnation.

""")
