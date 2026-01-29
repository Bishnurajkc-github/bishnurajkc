document.addEventListener("DOMContentLoaded", () => {
    const posts = document.querySelectorAll(".blog-post");

    posts.forEach(post => {
        // Only add toggle if post text is long
        const fullText = post.querySelector("p").innerText;
        if (fullText.length > 100) {
            const shortText = fullText.substring(0, 100) + "...";

            post.querySelector("p").innerText = shortText;

            const button = document.createElement("button");
            button.innerText = "Read More";
            button.style.marginTop = "8px";
            button.style.padding = "5px 10px";
            button.style.border = "none";
            button.style.backgroundColor = "#1e90ff";
            button.style.color = "#fff";
            button.style.borderRadius = "6px";
            button.style.cursor = "pointer";

            post.appendChild(button);

            let expanded = false;
            button.addEventListener("click", () => {
                if (!expanded) {
                    post.querySelector("p").innerText = fullText;
                    button.innerText = "Show Less";
                    expanded = true;
                } else {
                    post.querySelector("p").innerText = shortText;
                    button.innerText = "Read More";
                    expanded = false;
                }
            });
        }
    });
});

