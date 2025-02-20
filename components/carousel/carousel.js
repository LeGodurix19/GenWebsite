document.addEventListener("DOMContentLoaded", function() {
    const timeout = 5000;
    const slides = document.getElementById("carousel-slides");
    const leftButton = document.getElementById("left_event_move");
    const rightButton = document.getElementById("right_event_move");
    let index = 0;
    
    function moveSlide(direction) {
        const totalSlides = slides.children.length;
        index = (index + direction + totalSlides) % totalSlides;
        slides.style.transform = `translateX(-${index * 100}%)`;
    }

    setInterval(() => moveSlide(1), timeout);

    leftButton.addEventListener("click", () => moveSlide(-1));
    rightButton.addEventListener("click", () => moveSlide(1));
});