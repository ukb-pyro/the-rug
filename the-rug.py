import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Data
ontological = ["God", "Animal", "Man", "Enterprise", "Systems"]
epistemological = ["Roots", "Trunk", "Branching", "Canopy", "Fruit"]
agentic = ["Fixed / Immobile", "Mobility", "Contemplation", "Scaling", "Recursive"]

# Status mapping for colors
status_colors = {
    "God": "#c6efce",  # green
    "Roots": "#c6efce",
    "Fixed / Immobile": "#c6efce",
    "Animal": "#ffeb9c",  # amber
    "Trunk": "#ffeb9c",
    "Mobility": "#ffeb9c",
    "Man": "#ffeb9c",
    "Branching": "#ffeb9c",
    "Contemplation": "#ffeb9c",
    "Enterprise": "#ffeb9c",
    "Canopy": "#ffeb9c",
    "Scaling": "#ffeb9c",
    "Systems": "#f4cccc",  # red
    "Fruit": "#f4cccc",
    "Recursive": "#f4cccc",
}

# Annotations (repair levers)
annotations = {
    "God": "Values Charter",
    "Roots": "Tie to Origin/Earth",
    "Fixed / Immobile": "Boundaries & Substrate",
    "Animal": "Reduce Reactivity",
    "Trunk": "Logistics & Support",
    "Mobility": "From Serf to Free",
    "Man": "Branching Ritual",
    "Branching": "Weekly 3 Forks",
    "Contemplation": "Deep Work",
    "Enterprise": "Governed Scaling",
    "Canopy": "Energy & Rights",
    "Scaling": "Coop/Steward Growth",
    "Systems": "Return the Loop",
    "Fruit": "Seeds & Dividends",
    "Recursive": "Human-in-the-Loop",
}

fig, ax = plt.subplots(figsize=(10, 7))

# Draw cells
for row in range(5):
    for col_idx, col_key in enumerate(["ontological", "epistemological", "agentic"]):
        label = [ontological, epistemological, agentic][col_idx][4 - row]
        ax.add_patch(Rectangle((col_idx, row), 1, 1, edgecolor="black",
                               facecolor=status_colors[label]))
        ax.text(col_idx + 0.5, row + 0.7, label, ha="center", va="center", fontsize=10, fontweight="bold", wrap=True)
        ax.text(col_idx + 0.5, row + 0.3, annotations[label], ha="center", va="center", fontsize=8, wrap=True)

# Labels
ax.text(0.5, 5.4, "Ontological\n(GAMES)", ha="center", va="center", fontsize=12, fontweight="bold")
ax.text(1.5, 5.4, "Epistemological\n(Plants)", ha="center", va="center", fontsize=12, fontweight="bold")
ax.text(2.5, 5.4, "Agentic / Causal\n(Modes of Being)", ha="center", va="center", fontsize=12, fontweight="bold")

# Grounding layer
ax.add_patch(Rectangle((-0.2, -1), 3.4, 0.7, edgecolor="black", facecolor="#f5b7b1"))
ax.text(1.5, -0.65, "Grounding: L’Origin/Earth, Minerals, Water, Fixers, Network",
        ha="center", va="center", fontsize=11, wrap=True)

# Cosmos layer
ax.add_patch(Rectangle((-0.2, 6), 3.4, 0.7, edgecolor="black", facecolor="#aed6f1"))
ax.text(1.5, 6.35, "Cosmos: Sun, Radiation",
        ha="center", va="center", fontsize=11, wrap=True)

# Arrows from Cosmos to columns
for col in [0.5, 1.5, 2.5]:
    ax.annotate("", xy=(col, 6), xytext=(col, 5.7),
                arrowprops=dict(arrowstyle="->", lw=1.5))

# Arrows from columns to Grounding
for col in [0.5, 1.5, 2.5]:
    ax.annotate("", xy=(col, 0), xytext=(col, -0.3),
                arrowprops=dict(arrowstyle="->", lw=1.5))

# Formatting
ax.set_xlim(-0.2, 3.2)
ax.set_ylim(-1.2, 6.8)
ax.axis("off")

plt.show()
