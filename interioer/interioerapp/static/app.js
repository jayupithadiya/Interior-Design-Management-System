// Scroll Animation
        window.addEventListener('scroll', reveal);
        function reveal() {
            var reveals = document.querySelectorAll('.reveal');
            for (var i = 0; i < reveals.length; i++) {
                var windowHeight = window.innerHeight;
                var revealTop = reveals[i].getBoundingClientRect().top;
                if (revealTop < windowHeight - 100) {
                    reveals[i].classList.add('active');
                }
            }
        }
        reveal(); 

        // Menu Toggle
        const hamburger = document.querySelector(".hamburger");
        const navMenu = document.querySelector(".nav-menu");
        function toggleMenu() {
            hamburger.classList.toggle("active");
            navMenu.classList.toggle("active");
        }
        function closeMenu() {
            hamburger.classList.remove("active");
            navMenu.classList.remove("active");
        }

// Page load hote hi Portfolio tab open
    document.addEventListener("DOMContentLoaded", function () {
        switchTab('home');
    });

