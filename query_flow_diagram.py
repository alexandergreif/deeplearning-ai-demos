import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(16, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 14)
ax.axis('off')

# Color scheme
colors = {
    'frontend': '#FF6B6B',
    'api': '#4ECDC4',
    'rag': '#45B7D1',
    'ai': '#96CEB4',
    'tools': '#FFEAA7',
    'vector': '#DDA0DD',
    'arrow': '#2C3E50'
}

# Define box style
box_style = "round,pad=0.1"

# 1. Frontend Layer
frontend_box = FancyBboxPatch((0.5, 11.5), 2, 1.5,
                              boxstyle=box_style,
                              facecolor=colors['frontend'],
                              edgecolor='black', linewidth=2)
ax.add_patch(frontend_box)
ax.text(1.5, 12.25, 'FRONTEND\n(script.js)', ha='center', va='center', fontsize=11, fontweight='bold')

# 2. FastAPI Layer
api_box = FancyBboxPatch((4, 11.5), 2, 1.5,
                         boxstyle=box_style,
                         facecolor=colors['api'],
                         edgecolor='black', linewidth=2)
ax.add_patch(api_box)
ax.text(5, 12.25, 'FASTAPI\n(app.py)', ha='center', va='center', fontsize=11, fontweight='bold')

# 3. RAG System Layer
rag_box = FancyBboxPatch((7.5, 11.5), 2, 1.5,
                         boxstyle=box_style,
                         facecolor=colors['rag'],
                         edgecolor='black', linewidth=2)
ax.add_patch(rag_box)
ax.text(8.5, 12.25, 'RAG SYSTEM\n(rag_system.py)', ha='center', va='center', fontsize=11, fontweight='bold')

# 4. AI Generator
ai_box = FancyBboxPatch((7.5, 9), 2, 1.5,
                        boxstyle=box_style,
                        facecolor=colors['ai'],
                        edgecolor='black', linewidth=2)
ax.add_patch(ai_box)
ax.text(8.5, 9.75, 'AI GENERATOR\n(ai_generator.py)', ha='center', va='center', fontsize=11, fontweight='bold')

# 5. Tool Manager & Search Tool
tools_box = FancyBboxPatch((4, 6.5), 2, 1.5,
                           boxstyle=box_style,
                           facecolor=colors['tools'],
                           edgecolor='black', linewidth=2)
ax.add_patch(tools_box)
ax.text(5, 7.25, 'SEARCH TOOLS\n(search_tools.py)', ha='center', va='center', fontsize=11, fontweight='bold')

# 6. Vector Store
vector_box = FancyBboxPatch((1, 6.5), 2, 1.5,
                            boxstyle=box_style,
                            facecolor=colors['vector'],
                            edgecolor='black', linewidth=2)
ax.add_patch(vector_box)
ax.text(2, 7.25, 'VECTOR STORE\n(vector_store.py)', ha='center', va='center', fontsize=11, fontweight='bold')

# Add step numbers and descriptions
steps = [
    (1.5, 10.8, "1. User types query\n   POST /api/query"),
    (5, 10.8, "2. Validate request\n   Create session"),
    (8.5, 10.8, "3. Format prompt\n   Get history"),
    (8.5, 8.3, "4. Call Claude API\n   with tools"),
    (5, 5.8, "5. Execute search\n   Format results"),
    (2, 5.8, "6. Semantic search\n   ChromaDB query"),
]

for x, y, text in steps:
    ax.text(x, y, text, ha='center', va='center', fontsize=9,
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

# Draw arrows for request flow (downward)
arrows_request = [
    # Frontend to API
    ((2.5, 12.25), (4, 12.25)),
    # API to RAG
    ((6, 12.25), (7.5, 12.25)),
    # RAG to AI
    ((8.5, 11.5), (8.5, 10.5)),
    # AI to Tools (when tool_use needed)
    ((7.5, 9.75), (6, 7.25)),
    # Tools to Vector Store
    ((4, 7.25), (3, 7.25)),
]

for start, end in arrows_request:
    arrow = ConnectionPatch(start, end, "data", "data",
                          arrowstyle="->", shrinkA=5, shrinkB=5,
                          mutation_scale=20, fc=colors['arrow'], ec=colors['arrow'],
                          linewidth=2)
    ax.add_patch(arrow)

# Draw arrows for response flow (upward, offset slightly)
arrows_response = [
    # Vector Store back to Tools
    ((3, 6.8), (4, 6.8)),
    # Tools back to AI
    ((6, 7.5), (7.5, 9.5)),
    # AI back to RAG
    ((8.2, 10.5), (8.2, 11.5)),
    # RAG back to API
    ((7.5, 12.5), (6, 12.5)),
    # API back to Frontend
    ((4, 12.5), (2.5, 12.5)),
]

for start, end in arrows_response:
    arrow = ConnectionPatch(start, end, "data", "data",
                          arrowstyle="->", shrinkA=5, shrinkB=5,
                          mutation_scale=20, fc='green', ec='green',
                          linewidth=2, linestyle='--')
    ax.add_patch(arrow)

# Add data flow annotations
ax.text(3.25, 12.6, 'Query +\nSession ID', ha='center', va='center', fontsize=8,
        bbox=dict(boxstyle="round,pad=0.2", facecolor='lightblue', alpha=0.7))

ax.text(6.75, 12.6, 'Prompt +\nHistory', ha='center', va='center', fontsize=8,
        bbox=dict(boxstyle="round,pad=0.2", facecolor='lightblue', alpha=0.7))

ax.text(6.75, 8.5, 'Tool\nCall', ha='center', va='center', fontsize=8,
        bbox=dict(boxstyle="round,pad=0.2", facecolor='lightyellow', alpha=0.7))

ax.text(3.5, 6.8, 'Search\nResults', ha='center', va='center', fontsize=8,
        bbox=dict(boxstyle="round,pad=0.2", facecolor='lightgreen', alpha=0.7))

ax.text(3.25, 12.0, 'Answer +\nSources', ha='center', va='center', fontsize=8,
        bbox=dict(boxstyle="round,pad=0.2", facecolor='lightgreen', alpha=0.7))

# Add title and legend
ax.text(5, 13.5, 'RAG Chatbot - User Query Flow', ha='center', va='center',
        fontsize=18, fontweight='bold')

# Legend
legend_elements = [
    patches.Patch(color=colors['frontend'], label='Frontend Layer'),
    patches.Patch(color=colors['api'], label='API Layer'),
    patches.Patch(color=colors['rag'], label='RAG Orchestration'),
    patches.Patch(color=colors['ai'], label='AI Generation'),
    patches.Patch(color=colors['tools'], label='Search Tools'),
    patches.Patch(color=colors['vector'], label='Vector Storage'),
]

ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(0, 1))

# Add flow direction legend
ax.text(9, 3, 'Flow Direction:', fontsize=12, fontweight='bold')
ax.text(9, 2.5, '→ Request Flow', fontsize=10, color=colors['arrow'])
ax.text(9, 2.1, '→ Response Flow', fontsize=10, color='green')

# Add key technical details
details_text = """Key Technical Details:
• FastAPI validates QueryRequest model
• RAG system manages session state
• AI uses Claude API with tool calling
• Search tool performs semantic search
• ChromaDB stores vector embeddings
• Sources tracked for transparency"""

ax.text(0.5, 4.5, details_text, fontsize=9, va='top',
        bbox=dict(boxstyle="round,pad=0.5", facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig('/Users/alexandergreif/PycharmProjects/CodingChallanges/Claude_Code_workshop/rag_query_flow_diagram.png',
            dpi=300, bbox_inches='tight')
plt.show()