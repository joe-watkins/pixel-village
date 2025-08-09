1. Overview
PixelTown AI is a real-time, multi-agent social simulation where AI-driven “citizens” live together in a charming pixel-art village. Each agent has a unique personality, backstory, and memory system, allowing them to interact naturally, form relationships, and engage in emergent events.

The simulation is viewable through a top-down pixel-art interface, where each AI appears as a cute animated sprite moving through a hand-crafted pixel town.

Runs locally on Windows or in the cloud with the same visual interface.

Success Criteria:

Achieve user engagement metrics of 80% retention after 1 week.

Adoption by at least 3 research institutions within the first year.

2. Goals & Non-Goals
Goals:

Blend Generative Agents–style AI behavior with a visually appealing pixel-art town.

Make it fun to watch while still research-friendly.

Give users clickable, interactive access to each AI’s thoughts, logs, and memories.

Non-Goals:

Realistic human models (pixel art only).

Complex 3D environments (2D sprites + tiles).

Exclusion Rationale:

Focus on simplicity and accessibility for broader user adoption.

3. Key Features
3.1 AI Agent Core
LLM-based reasoning & dialogue (cloud or local models).

Persistent memory system (vector DB) so AIs remember prior events.

Personality model (Big Five traits) + quirks & habits.

Backstory generator for unique starting contexts.

Integration Details:

Memory system will dynamically update based on interactions and events.

Personality traits will influence decision-making and dialogue generation.

3.2 Visual Simulation
Pixel-Art Town:

Buildings: homes, café, park, library, shop.

Animated environmental elements (trees swaying, day/night cycle).

Pixel Characters:

16×16 or 32×32 sprites, animated walking cycles.

Each agent has a custom color palette & outfit.

Icons over heads for current action (speech bubble, coffee cup, heart).

Movement & Pathfinding:

A* or simple grid-based pathfinding for smooth movement between locations.

3.3 UI Interactions
Click Agent → Detail Panel:

Name, age, job, personality, current thoughts.

Memory list with timestamps.

Relationships graph (friendships, rivalries).

Event Feed: Rolling log of town-wide events.

Speed Control: Pause, 1x, 2x, 5x simulation speed.

Graph Details:

Friendships will be represented with green lines, rivalries with red lines.

3.4 Time & Events
Simulated 24-hour clock.

AI plans change based on time, weather, or events.

Scheduled events (parties, elections, protests, birthdays).

4. Technical Requirements
4.1 Architecture
Frontend:

Phaser.js (for pixel-art rendering, browser/Electron support).

Electron wrapper for local Windows app.

Backend:

Python (FastAPI) for simulation logic.

SQLite for base data and vector DB (e.g., Chroma or Milvus) for memories.

Local Ollama instance for LLM-based reasoning and dialogue generation.

Testing Details:

Performance testing will focus on local execution using tools like Pytest and profiling libraries.

Stress testing for Ollama models to ensure they can handle multiple concurrent agent queries.

4.2 Deployment
Local: Electron build for Windows with packaged assets. The app will run entirely offline, bundling all necessary components (frontend, backend, and database) into a single executable.

LLM Integration:

Local Ollama instance for AI reasoning and dialogue generation.

Cached responses for fallback mechanisms to ensure smooth operation even during heavy processing.

4.3 Performance
Target: 25–50 active agents with smooth animation at 60 FPS. All processing will occur locally, ensuring minimal latency (< 500 ms) for AI decision → visual update.

5. Pixel Agent Template Example
yaml
Copy
Edit
name: "Hiro Tanaka"
sprite: "sprites/hiro.png"
age: 27
occupation: "Baker"
personality:
  openness: 0.77
  conscientiousness: 0.91
  extraversion: 0.55
  agreeableness: 0.80
  neuroticism: 0.32
quirks:
  - Always carries a baguette
  - Gives bread to stray cats
  - Obsessed with weather forecasts
backstory:
  - Moved to PixelTown to open his dream bakery
  - Secretly wants to start a jazz band
starting_location: "Bakery"
relationships: []
current_goal: "Host a neighborhood bread tasting"
6. Visual Design
Art Style: SNES-era pixel art (bright but slightly desaturated palette).

Characters: Chibi-style proportions, expressive face frames.

UI Panels: Minimal, semi-transparent overlay boxes.

Town Layout: Tile-based map, handcrafted for personality.

Weather & Day/Night: Ambient changes with soft pixel lighting.

Concept Details:

Visual design will include mockups for key screens (e.g., agent detail panel).

Weather effects will influence agent behavior (e.g., staying indoors during rain).

7. Future Enhancements
Seasonal festivals with custom sprites.

Players can drop “story seeds” into the town (rumors, objects).

AI photo album: snapshots of important moments.

Timeline:

Year 1: Seasonal festivals.

Year 2: Story seeds and photo album.

8. Development Phases

Phase 1: Core Foundations
- Set up the environment:
  - Install dependencies: Phaser.js, Electron, Python (FastAPI), SQLite, Ollama models.
  - Create a basic Electron app structure with Phaser.js integration.
- Build the Pixel-Art Town:
  - Create the tile-based map with basic buildings (homes, café, park, library, shop).
  - Add environmental animations (e.g., trees swaying).
- Agent Movement:
  - Implement A* or grid-based pathfinding for agent movement between locations.

Phase 2: AI Agent Core
- Integrate Ollama Models:
  - Set up local Ollama instance for reasoning and dialogue generation.
  - Test basic queries to ensure smooth operation.
- Memory System:
  - Use SQLite and vector DB (e.g., Chroma or Milvus) for persistent memory storage.
  - Implement basic memory updates based on interactions.
- Personality Model:
  - Add Big Five traits and quirks to agents.
  - Ensure traits influence decision-making and dialogue.

Phase 3: Visual Simulation
- Agent Sprites:
  - Design 16×16 or 32×32 animated sprites with walking cycles.
  - Add icons above agents for current actions (speech bubble, coffee cup, heart).
- UI Panels:
  - Create the agent detail panel (name, age, job, personality, thoughts, memory list).
  - Implement the relationships graph (friendships/rivalries).

Phase 4: Time & Events
- Simulated Clock:
  - Add a 24-hour clock system.
  - Ensure AI plans change based on time.
- Scheduled Events:
  - Implement basic events (e.g., parties, birthdays).
  - Add weather effects (e.g., rain influencing behavior).

Phase 5: Testing & Optimization
- Performance Testing:
  - Ensure smooth animation at 60 FPS with 25–50 active agents.
  - Test Ollama models for handling concurrent queries.
- Stress Testing:
  - Simulate heavy processing scenarios to ensure fallback mechanisms work.

Phase 6: Polish & Enhancements
- Visual Design Refinements:
  - Add weather effects and day/night ambient changes.
  - Ensure UI panels are responsive and visually appealing.
- Future Enhancements:
  - Plan for seasonal festivals and story seeds.