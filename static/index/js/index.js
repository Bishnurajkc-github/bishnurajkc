// Homepage greeting
document.addEventListener("DOMContentLoaded", () => {
    const header = document.querySelector("header p");
    const greetings = [
        "Welcome to my learning projects!",
        "Explore my Calculator and Blog.",
        "Flask and Web Development Enthusiast."
    ];

    let i = 0;

    function showGreeting() {
        header.textContent = greetings[i];
        i = (i + 1) % greetings.length;
    }

    // Change greeting every 3 seconds
    showGreeting();
    setInterval(showGreeting, 3000);
});

