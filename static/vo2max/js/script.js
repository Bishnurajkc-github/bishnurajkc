// Dark mode toggle
const toggleBtn = document.getElementById("toggleModeBtn");

toggleBtn.addEventListener("click", () => {
  document.body.classList.toggle("dark");

  if (document.body.classList.contains("dark")) {
    toggleBtn.innerText = "☀️ Light Mode";
  } else {
    toggleBtn.innerText = "🌙 Dark Mode";
  }
});

// Copy summary button
const copyBtn = document.getElementById("copyBtn");
const copyMsg = document.getElementById("copyMsg");

copyBtn.addEventListener("click", () => {
  const summaryText = `
VO₂ Max = शरीरको oxygen प्रयोग गर्ने अधिकतम क्षमता
40+ मा VO₂ Max घट्न थाल्छ, त्यसैले training जरूरी
VO₂ Max training ले heart health, stamina, longevity बढाउँछ
Strength training ले muscle, bone, joint health बढाउँछ
Best result = strength + VO₂ max दुबै combine गर्नु
  `;

  navigator.clipboard.writeText(summaryText.trim());

  copyMsg.innerText = "✅ Summary copied successfully!";
  setTimeout(() => {
    copyMsg.innerText = "";
  }, 2500);
});
