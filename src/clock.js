// Simulated 24-hour clock system
let currentHour = 0;

function updateClock() {
    currentHour = (currentHour + 1) % 24;
    console.log(`Current Hour: ${currentHour}`);
}

setInterval(updateClock, 1000); // Update every second for simulation purposes

export { currentHour, updateClock };
