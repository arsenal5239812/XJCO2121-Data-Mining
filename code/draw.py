import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set up the figure
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)
ax.axis('off')

# Step data: (x, y, text, tool)
positions = [
    (5, 11, "Raw Dataset\n(Amazon_Unlocked_Mobile.csv)", "Kaggle"),
    (5, 9, "Random Sampling\n→ Amazon_10k_Sample.csv", "Python (pandas)"),
    (5, 7, "Text Cleaning & Labelling\n→ full_10000_cleaned.csv", "Python (nltk, pandas)"),
    (5, 5, "TF-IDF Vectorisation\n→ numeric matrix", "Python (sklearn)"),
    (5, 3, "Convert to ARFF\n→ full_10000_vectorized.arff", "Python"),
    (5, 1, "Model Training & Evaluation\n(NB, SMO, RF)", "Weka")
]

# Helper: draw box
def draw_box(x, y, text):
    width, height = 3, 1.2
    rect = patches.Rectangle((x - width/2, y - height/2), width, height,
                             linewidth=1, edgecolor='black', facecolor='lightgray')
    ax.add_patch(rect)
    ax.text(x, y, text, ha='center', va='center', fontsize=9)

# Draw all steps and arrows
for i in range(len(positions)):
    x, y, text, tool = positions[i]
    draw_box(x, y, text)

    if i > 0:
        prev_x, prev_y, _, _ = positions[i - 1]
        # Draw arrow from previous box to current
        ax.annotate("", xy=(x, y + 0.6), xytext=(prev_x, prev_y - 0.6),
                    arrowprops=dict(arrowstyle="->", lw=1.5))
        # Add tool label near the arrow
        mid_y = (y + prev_y) / 2
        ax.text(x + 0.8, mid_y, tool, fontsize=8, style='italic', color='blue')

plt.tight_layout()
plt.savefig("pilot_study_flowchart.png", dpi=300, bbox_inches='tight')
plt.show()