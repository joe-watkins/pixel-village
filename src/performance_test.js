// Performance test for animation with 25–50 active agents
const agents = [];

function createAgents(count) {
    for (let i = 0; i < count; i++) {
        const agent = {
            id: i,
            x: Math.random() * 800,
            y: Math.random() * 600,
            sprite: 'ai-' + ((i % 6) + 1)
        };
        agents.push(agent);
    }
}

function updateAgents() {
    agents.forEach(agent => {
        agent.x += Math.random() * 2 - 1;
        agent.y += Math.random() * 2 - 1;
        console.log(`Agent ${agent.id} position: (${agent.x}, ${agent.y})`);
    });
}

createAgents(50);
setInterval(updateAgents, 16); // Approx. 60 FPS

console.log("Performance test started with 50 agents.");
