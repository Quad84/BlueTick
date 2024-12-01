AOS.init()

const persianDigits = document.querySelectorAll(".persian_digits");

persianDigits.forEach((item) => {

    const char = {0:'۰', 1:'۱', 2:'۲', 3:'۳', 4:'۴', 5:'۵'
        ,6:'۶', 7:'۷', 8:'۸', 9:'۹'};

    for (let i = 0;i <= 9;i++){
        const reg = new RegExp(i,'g');
        item.innerHTML = item.innerHTML.replace(reg,char[i]);
    }

});

var swiper = new Swiper(".mySwiper", {
    loop : true,
    autoplay: {
        delay: 5000,
    },    
    pagination: {
      el: ".swiper-pagination",
      dynamicBullets: true,
    },
});

const darkBtn = document.querySelector('.dark-btn');

darkBtn.addEventListener('click',() => {
    // if set via local storage previously
    if (localStorage.getItem('color-theme')) {
        if (localStorage.getItem('color-theme') === 'light') {
            document.documentElement.classList.add('dark');
            darkBtn.children[0].className = "bi bi-sun";
            localStorage.setItem('color-theme', 'dark');
        } else {
            document.documentElement.classList.remove('dark');
            darkBtn.children[0].className = "bi bi-moon";
            localStorage.setItem('color-theme', 'light');
        }

    // if NOT set via local storage previously
    } else {
        if (document.documentElement.classList.contains('dark')) {
            document.documentElement.classList.remove('dark');
            darkBtn.children[0].className = "bi bi-sun";
            localStorage.setItem('color-theme', 'light');
        } else {
            document.documentElement.classList.add('dark');
            darkBtn.children[0].className = "bi bi-sun";
            localStorage.setItem('color-theme', 'dark');
        }
    }
})

// On page load or when changing themes, best to add inline in `head` to avoid FOUC
if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    document.documentElement.classList.add('dark');
    darkBtn.children[0].className = "bi bi-sun";    
} else {
    document.documentElement.classList.remove('dark');
    darkBtn.children[0].className = "bi bi-moon";
}