import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Data
ontological = ["God", "Animal", "Man", "Enterprise", "Systems"]
epistemological = ["Roots", "Trunk", "Branching", "Canopy", "Fruit"]
agentic = ["Fixed / Immobile", "Mobility", "Contemplation", "Scaling", "Recursive"]

# Create figure
fig, ax = plt.subplots(figsize=(10, 7))

# Table coordinates
x_positions = [0, 1, 2]  # columns
y_positions = list(range(5))[::-1]  # rows (top to bottom)

# Colors
colors = {
    "ontological": "#d4e6f1",
    "epistemological": "#d5f5e3",
    "agentic": "#f9e79f"
}

# Draw cells
for row in range(5):
    ax.add_patch(Rectangle((0, row), 1, 1, edgecolor="black", facecolor=colors["ontological"]))
    ax.add_patch(Rectangle((1, row), 1, 1, edgecolor="black", facecolor=colors["epistemological"]))
    ax.add_patch(Rectangle((2, row), 1, 1, edgecolor="black", facecolor=colors["agentic"]))
    
    # Add text
    ax.text(0.5, row + 0.5, ontological[4 - row], ha="center", va="center", fontsize=10, wrap=True)
    ax.text(1.5, row + 0.5, epistemological[4 - row], ha="center", va="center", fontsize=10, wrap=True)
    ax.text(2.5, row + 0.5, agentic[4 - row], ha="center", va="center", fontsize=10, wrap=True)

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
