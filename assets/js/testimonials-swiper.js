const swiper = new Swiper('.testimonials-swiper', {
    slidesPerView: 1,
    spaceBetween: 20,
    loop: true,
    speed: 2000, // Duração da transição em ms (1 segundo neste exemplo)
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    autoplay: {
        delay: 3000, // Tempo entre transições (3 segundos)
        pauseOnMouseEnter: true,
        disableOnInteraction: false,
    },
    breakpoints: {
        1024: {
            slidesPerView: 2,
            spaceBetween: 24,
        },
        1440: {
            slidesPerView: 3,
            spaceBetween: 32,
        }
    }
});