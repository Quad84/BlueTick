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

