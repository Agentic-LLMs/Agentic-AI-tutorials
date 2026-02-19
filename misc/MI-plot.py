import matplotlib.pyplot as plt
import numpy as np

## Plotting function to generate an example of Polysemanticity

def draw_polysemantic_plot():
    # Set style parameters to match the clean, scholarly feel
    plt.rcParams.update({
        'font.family': 'sans-serif',
        'font.size': 10,
        'axes.linewidth': 1.5,
        'xtick.major.width': 1.5,
        'ytick.major.width': 1.5
    })

    fig, ax = plt.subplots(figsize=(7, 7), dpi=150)
    
    # Define abstract concepts: (x, y) coordinates for the vectors
    concepts = [
        {"name": "Concept 1", "coords": (0.85, 0.15), "color": "#1f77b4", "marker": "*"},
        {"name": "Concept 2", "coords": (0.10, 0.70), "color": "#ff7f0e", "marker": "^"},
        {"name": "Concept 3", "coords": (0.70, 0.75), "color": "#2ca02c", "marker": "s"},
        {"name": "Concept 4", "coords": (0.2, 0.40), "color": "#d62728", "marker": "p"},
        {"name": "Concept 5", "coords": (0.60, 0.30), "color": "#9467bd", "marker": "D"}
    ]

    # Plot origin point (representing 0 activation)
    ax.scatter(0, 0, color='black', s=50, zorder=5)

    # Plot vectors and labels
    for item in concepts:
        x, y = item["coords"]
        color = item["color"]
        marker = item["marker"]
        name = item["name"]
        
        # Draw the vector line from origin
        ax.annotate('', xy=(x, y), xytext=(0, 0),
                    arrowprops=dict(edgecolor=color, arrowstyle='->', lw=2.5, alpha=0.7, shrinkA=0, shrinkB=0))
        
        # Draw the symbol at the tip
        ax.scatter(x, y, s=250, color=color, marker=marker, 
                   edgecolor='black', linewidth=1, zorder=10)
        
        # Add text labels with a slight offset
        ax.text(x + 0.03, y + 0.02, name, fontsize=11, fontweight='bold', color='#333333')

    # Formatting the axes
    ax.set_xlim(-0.05, 1.0)
    ax.set_ylim(-0.05, 1.0)
    ax.set_xlabel("Neuron A Activation", fontsize=12, labelpad=10)
    ax.set_ylabel("Neuron B Activation", fontsize=12, labelpad=10)
    ax.set_title("Polysemanticity in Neuron Activation Space", fontsize=14, fontweight='bold', pad=25)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(True, linestyle='--', alpha=0.3, zorder=0)
    ax.set_aspect('equal')

    # Explanatory text box
    summary_text = (
        "$\mathbf{Polysemanticity}$:\n"
        "A single neuron (axis) participates in representing\n"
        "multiple distinct concepts. These concepts are\n"
        "distributed as 'directions' in the activation space\n"
        "rather than aligning perfectly with individual axes."
    )
    
    bbox_props = dict(boxstyle='round,pad=0.8', facecolor='#f9f9f9', alpha=0.9, edgecolor='#cccccc')
    ax.text(0.05, 0.95, summary_text, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=bbox_props, linespacing=1.5)

    plt.tight_layout()
    plt.savefig('polysemanticity_concept_plot.pdf')
    plt.show()

draw_polysemantic_plot()