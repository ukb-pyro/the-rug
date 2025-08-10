import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Data
ontological = ["God", "Animal", "Man", "Enterprise", "Systems"]
epistemological = ["Roots", "Trunk", "Branching", "Canopy", "Fruit"]
agentic = ["Fixed / Immobile", "Mobility", "Contemplation", "Scaling", "Recursive"]

# Status colors
status_colors = {
    "God": "#c6efce",
    "Roots": "#c6efce",
    "Fixed / Immobile": "#c6efce",
    "Animal": "#ffeb9c",
    "Trunk": "#ffeb9c",
    "Mobility": "#ffeb9c",
    "Man": "#ffeb9c",
    "Branching": "#ffeb9c",
    "Contemplation": "#ffeb9c",
    "Enterprise": "#ffeb9c",
    "Canopy": "#ffeb9c",
    "Scaling": "#ffeb9c",
    "Systems": "#f4cccc",
    "Fruit": "#f4cccc",
    "Recursive": "#f4cccc",
}

# Captions for narrative
captions = {
    "God": "Values Charter — anchor principles we won't trade away.",
    "Roots": "Tie to Origin/Earth — energy, materials, watersheds as constraints.",
    "Fixed / Immobile": "Boundaries & Substrate — stability as defense against capture.",
    "Animal": "Reduce Reactivity — shift from over-stimulated to purposeful motion.",
    "Trunk": "Logistics & Support — scaffolding that enables higher thinking.",
    "Mobility": "From Serf to Free — self-directed movement, not constant demand.",
    "Man": "Branching Ritual — intentional decision cadence.",
    "Branching": "Weekly 3 Forks — limit options, name reversal conditions.",
    "Contemplation": "Deep Work — protect bandwidth for focus.",
    "Enterprise": "Governed Scaling — growth with charter intact.",
    "Canopy": "Energy & Rights — expansion without overreach.",
    "Scaling": "Coop/Steward Growth — align ownership with contributors.",
    "Systems": "Return the Loop — value feeds back to people.",
    "Fruit": "Seeds & Dividends — portability, replanting, no extraction-only.",
    "Recursive": "Human-in-the-Loop — pause automation for consent/review.",
}

fig, ax = plt.subplots(figsize=(14, 10))

# Draw cells with captions
for row in range(5):
    for col_idx, col_key in enumerate(["ontological", "epistemological", "agentic"]):
        label = [ontological, epistemological, agentic][col_idx][4 - row]
        ax.add_patch(Rectangle((col_idx, row), 1, 1, edgecolor="black",
                               facecolor=status_colors[label]))
        ax.text(col_idx + 0.5, row + 0.75, label, ha="center", va="center",
                fontsize=10, fontweight="bold", wrap=True)
        ax.text(col_idx + 0.5, row + 0.35, captions[label], ha="center", va="top",
                fontsize=7, wrap=True)

# Labels
ax.text(0.5, 5.4, "Ontological\n(GAMES)", ha="center", va="center", fontsize=12, fontweight="bold")
ax.text(1.5, 5.4, "Epistemological\n(Plants)", ha="center", va="center", fontsize=12, fontweight="bold")
ax.text(2.5, 5.4, "Agentic / Causal\n(Modes of Being)", ha="center", va="center", fontsize=12, fontweight="bold")

# Grounding
ax.add_patch(Rectangle((-0.2, -1), 3.4, 0.7, edgecolor="black", facecolor="#f5b7b1"))
ax.text(1.5, -0.65, "Grounding: L’Origin/Earth, Minerals, Water, Fixers, Network",
        ha="center", va="center", fontsize=11, wrap=True)

# Cosmos
ax.add_patch(Rectangle((-0.2, 6), 3.4, 0.7, edgecolor="black", facecolor="#aed6f1"))
ax.text(1.5, 6.35, "Cosmos: Sun, Radiation",
        ha="center", va="center", fontsize=11, wrap=True)

# Arrows
for col in [0.5, 1.5, 2.5]:
    ax.annotate("", xy=(col, 6), xytext=(col, 5.7),
                arrowprops=dict(arrowstyle="->", lw=1.5))
    ax.annotate("", xy=(col, 0), xytext=(col, -0.3),
                arrowprops=dict(arrowstyle="->", lw=1.5))

# Formatting
ax.set_xlim(-0.2, 3.2)
ax.set_ylim(-1.2, 6.8)
ax.axis("off")

plt.show()
