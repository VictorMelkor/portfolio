document.addEventListener("DOMContentLoaded", () => {
    const skills = document.querySelectorAll(".skill");

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const skill = entry.target;
                const percent = skill.dataset.percent;
                const progress = skill.querySelector(".progress");
                const percentText = skill.querySelector(".percent");

                // animação da barra
                progress.style.width = percent + "%";

                // animação do número
                let current = 0;
                const interval = setInterval(() => {
                    if (current < percent) {
                        current++;
                        percentText.textContent = current + "%";
                    } else {
                        clearInterval(interval);
                    }
                }, 15);

                observer.unobserve(skill); // anima só uma vez
            }
        });
    }, { threshold: 0.5 });

    skills.forEach(skill => observer.observe(skill));
});