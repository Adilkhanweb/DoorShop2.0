searchForm = document.querySelector('.search-form');

document.querySelector('#search-box').addEventListener('click', function () {
    searchForm.classList.toggle('active');
});

let loginForm = document.querySelector('#login-form-container');
let registerForm = document.querySelector('#register-form-container');
let reg_btn = document.querySelector('#create_acc');
let log_btn = document.querySelector('#log_btn');

document.querySelector('#login-btn').onclick = () => {
    loginForm.classList.toggle('active');
}

document.querySelector('.close-login-btn').onclick = () => {
    loginForm.classList.remove('active');
    registerForm.classList.remove('active');
}
document.querySelector('.close-register-btn').onclick = () => {
    loginForm.classList.remove('active');
    registerForm.classList.remove('active');
}

document.getElementById('close-login-btn').onclick = () => {
    loginForm.classList.remove('active');
    registerForm.classList.remove('active');
}

reg_btn.addEventListener('click', function (e) {
    e.preventDefault();
    if (loginForm.classList.contains('active')) {
        this.classList.remove('active')
    }
    registerForm.classList.toggle('active')
    loginForm.classList.toggle('active')
});

log_btn.addEventListener('click', function (e) {
    e.preventDefault();
    if (registerForm.classList.contains('active')) {
        this.classList.remove('active')
    }
    registerForm.classList.toggle('active')
    loginForm.classList.toggle('active')
});

window.onscroll = () => {

    searchForm.classList.remove('active');

    if (window.scrollY > 80) {
        document.querySelector('.header .header-2').classList.add('active');
    } else {
        document.querySelector('.header .header-2').classList.remove('active');
    }

}

window.onload = () => {

    if (window.scrollY > 80) {
        document.querySelector('.header .header-2').classList.add('active');
    } else {
        document.querySelector('.header .header-2').classList.remove('active');
    }

    fadeOut();

}

function loader() {
    document.querySelector('.loader-container').classList.add('active');
}

function fadeOut() {
    setTimeout(loader, 0);
}

var swiper = new Swiper(".books-slider", {
    loop: true,
    centeredSlides: true,
    autoplay: {
        delay: 9500,
        disableOnInteraction: false,
    },
    breakpoints: {
        0: {
            slidesPerView: 1,
        },
        768: {
            slidesPerView: 2,
        },
        1024: {
            slidesPerView: 3,
        },
    },
});

var swiper = new Swiper(".featured-slider", {
    spaceBetween: 10,
    loop: true,
    centeredSlides: true,
    autoplay: {
        delay: 9500,
        disableOnInteraction: false,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    breakpoints: {
        0: {
            slidesPerView: 1,
        },
        450: {
            slidesPerView: 2,
        },
        768: {
            slidesPerView: 3,
        },
        1024: {
            slidesPerView: 4,
        },
    },
});

var swiper = new Swiper(".arrivals-slider", {
    spaceBetween: 10,
    loop: true,
    centeredSlides: true,
    autoplay: {
        delay: 9500,
        disableOnInteraction: false,
    },
    breakpoints: {
        0: {
            slidesPerView: 1,
        },
        768: {
            slidesPerView: 2,
        },
        1024: {
            slidesPerView: 3,
        },
    },
});

var swiper = new Swiper(".reviews-slider", {
    spaceBetween: 10,
    grabCursor: true,
    loop: true,
    centeredSlides: true,
    autoplay: {
        delay: 9500,
        disableOnInteraction: false,
    },
    breakpoints: {
        0: {
            slidesPerView: 1,
        },
        768: {
            slidesPerView: 2,
        },
        1024: {
            slidesPerView: 3,
        },
    },
});

var swiper = new Swiper(".blogs-slider", {
    spaceBetween: 10,
    grabCursor: true,
    loop: true,
    centeredSlides: true,
    autoplay: {
        delay: 9500,
        disableOnInteraction: false,
    },
    breakpoints: {
        0: {
            slidesPerView: 1,
        },
        768: {
            slidesPerView: 2,
        },
        1024: {
            slidesPerView: 3,
        },
    },
});