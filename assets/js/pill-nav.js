document.addEventListener("DOMContentLoaded", () => {
  const nav = document.querySelector("nav");
  const links = nav.querySelectorAll("a");

  // Função para saber se é mobile
  const isMobile = () => window.innerWidth < 768;

  const movePill = (target) => {
    if (isMobile()) return; // 🔥 não cria nem move o pill no mobile

    // Criar elemento pill se não existir
    let pillEl = nav.querySelector(".pill");
    if (!pillEl) {
      pillEl = document.createElement("span");
      pillEl.classList.add("pill");
      nav.appendChild(pillEl);
    }

    const rect = target.getBoundingClientRect();
    const navRect = nav.getBoundingClientRect();

    // Atualiza posição/tamanho
    pillEl.style.width = `${rect.width}px`;
    pillEl.style.height = `${rect.height - 6}px`;
    pillEl.style.left = `${rect.left - navRect.left}px`;
    pillEl.style.top = `10px`;
  };

  // CSS inicial do pill
  const style = document.createElement("style");
  style.innerHTML = `
    nav .pill {
      position: absolute;
      top: 10px;
      left: 0;
      background-color: var(--color-pink);
      border-radius: 50px;
      z-index: 0;
      transition: all 0.3s ease;
    }
  `;
  document.head.appendChild(style);

  // Inicializar no ativo (somente desktop)
  const active = nav.querySelector("a.active") || links[0];
  movePill(active);

  // Atualiza ao clicar (somente desktop)
  links.forEach(link => {
    link.addEventListener("click", e => {
      links.forEach(l => l.classList.remove("active"));
      e.target.classList.add("active");
      movePill(e.target);
    });
  });

  // Remove o pill quando redimensionar para mobile
  window.addEventListener("resize", () => {
    const pillEl = nav.querySelector(".pill");
    if (isMobile() && pillEl) pillEl.remove();
  });
});
