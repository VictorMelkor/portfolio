document.addEventListener("DOMContentLoaded", () => {
  const nav = document.querySelector("nav");
  const links = nav.querySelectorAll("a");

  // Função para saber se é mobile
  const isMobile = () => window.innerWidth < 768;

  // Aplica a classe active com base no caminho da URL
  const setActiveLinkByURL = () => {
    links.forEach(link => link.classList.remove("active"));
    const currentPage = window.location.pathname.split("/").pop();
    const activeLink = Array.from(links).find(link => {
      const href = link.getAttribute("href");
      return href === currentPage;
    });
    if (activeLink) {
      activeLink.classList.add("active");
    } else {
      // fallback: ativa o primeiro link
      links[0].classList.add("active");
    }
  };

  // Move e cria o pill na posição do target
  const movePill = (target, instant = false) => {
    if (isMobile()) return; // não cria nem move no mobile

    let pillEl = nav.querySelector(".pill");
    if (!pillEl) {
      pillEl = document.createElement("span");
      pillEl.classList.add("pill");
      nav.appendChild(pillEl);
    }

    // Desativa transição temporariamente se instant == true
    if (instant) {
      pillEl.style.transition = "none";
    } else {
      pillEl.style.transition = "all 0.3s ease";
    }

    const rect = target.getBoundingClientRect();
    const navRect = nav.getBoundingClientRect();

    // Atualiza posição/tamanho
    pillEl.style.width = `${rect.width}px`;
    pillEl.style.height = `${rect.height - 6}px`;
    pillEl.style.left = `${rect.left - navRect.left}px`;
    pillEl.style.top = `10px`;

    // Se foi desativada a transição, força repaint e ativa após frame
    if (instant) {
      requestAnimationFrame(() => {
        pillEl.style.transition = "all 0.3s ease";
      });
    }
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
      pointer-events: none;
    }
  `;
  document.head.appendChild(style);

  // Aplica a classe active baseado na URL atual
  setActiveLinkByURL();

  // Inicializa o pill no link ativo sem animação
  const active = nav.querySelector("a.active") || links[0];
  movePill(active, true);

  // Atualiza o pill ao clicar em links
  links.forEach(link => {
    link.addEventListener("click", e => {
      e.preventDefault(); // previne navegação para teste local
      links.forEach(l => l.classList.remove("active"));
      e.target.classList.add("active");
      movePill(e.target);
    });
  });

  // Remove o pill no mobile, reposiciona no resize desktop
  window.addEventListener("resize", () => {
    const pillEl = nav.querySelector(".pill");
    if (isMobile()) {
      if (pillEl) pillEl.remove();
    } else {
      const activeLink = nav.querySelector("a.active") || links[0];
      movePill(activeLink, true);
    }
  });
});
