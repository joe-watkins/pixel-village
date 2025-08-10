import sqlite3

# Initialize SQLite database for memory system
def initialize_memory_db():
    conn = sqlite3.connect('memory.db')
    cursor = conn.cursor()

    # Create memories table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            agent_name TEXT,
            memory TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

# Add a memory to the database
def add_memory(agent_name, memory):
    conn = sqlite3.connect('memory.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO memories (agent_name, memory)
        VALUES (?, ?)
    ''', (agent_name, memory))

    conn.commit()
    conn.close()

# Retrieve memories for an agent
def get_memories(agent_name):
    conn = sqlite3.connect('memory.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT memory, timestamp FROM memories
        WHERE agent_name = ?
        ORDER BY timestamp DESC
    ''', (agent_name,))

    memories = cursor.fetchall()
    conn.close()
    return memories

# Initialize the database
initialize_memory_db()
