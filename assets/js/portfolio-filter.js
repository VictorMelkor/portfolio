document.addEventListener("DOMContentLoaded", () => {
    const filterButtons = document.querySelectorAll(".filter-btn");
    const portfolioCards = document.querySelectorAll(".portfolio-card");

    // 🔹 Aplica evento a todos os botões de filtro
    filterButtons.forEach(button => {
        button.addEventListener("click", () => {
            // Remove 'active' do botão anterior e adiciona ao atual
            filterButtons.forEach(btn => btn.classList.remove("active"));
            button.classList.add("active");

            const filter = button.getAttribute("data-filter");

            portfolioCards.forEach(card => {
                const category = card.getAttribute("data-category");

                // Lógica de exibição com animação
                if (filter === "all" || category === filter) {
                    card.style.display = "block";
                    card.style.opacity = "0";
                    setTimeout(() => card.style.opacity = "1", 100);
                } else {
                    card.style.opacity = "0";
                    setTimeout(() => card.style.display = "none", 300);
                }
            });
        });
    });
});
