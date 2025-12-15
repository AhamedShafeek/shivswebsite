document.addEventListener('DOMContentLoaded', function() {
    // Initialize AOS (Animate on Scroll)
    AOS.init({ duration: 800, once: true, offset: 50 });

    const header = document.getElementById('header');
    const headerLogo = document.getElementById('header-logo');
    // Define the paths for both logo versions
    const logoWhite = "Shiv's Photography Logo (White) (1).png";
    const logoBlack = 'shiv_s_photography_logo.jpeg';

    // Back to Top button & Header Scroll Effect
    const backToTop = document.getElementById('backToTop');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            backToTop.classList.remove('opacity-0', 'pointer-events-none');
            header.classList.add('bg-white', 'text-charcoal', 'shadow-md');
            header.classList.remove('text-white');
            // Switch to the black logo when scrolled
            if (headerLogo) headerLogo.src = logoBlack;
        } else {
            backToTop.classList.add('opacity-0', 'pointer-events-none');
            header.classList.remove('bg-white', 'text-charcoal', 'shadow-md');
            header.classList.add('text-white');
            // Switch back to the white logo at the top
            if (headerLogo) headerLogo.src = logoWhite;
        }
    });

    // Initialize other features
    initializeWorkflowAnimation();
});

// Mobile Menu Toggle
function toggleMobileMenu() {
    const menu = document.getElementById('mobileMenu');
    menu.classList.toggle('translate-x-full');
}

// Scroll to Top
function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            let headerOffset = 0;
            const header = document.getElementById('header');
            if(header) {
                headerOffset = header.offsetHeight;
            }
            const elementPosition = targetElement.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
            window.scrollTo({ top: offsetPosition, behavior: 'smooth' });
            
            const mobileMenu = document.getElementById('mobileMenu');
            if (mobileMenu && !mobileMenu.classList.contains('translate-x-full')) {
                toggleMobileMenu();
            }
        }
    });
});

// Initialize on-scroll animation for the Workflow section
function initializeWorkflowAnimation() {
    const workflowContainer = document.querySelector('.workflow-container');

    if (!workflowContainer) {
        return;
    }

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                workflowContainer.classList.add('is-active');
                // Stop observing after the animation is triggered once
                observer.unobserve(entry.target);
            }
        });
    }, {
        root: null, // relative to the viewport
        rootMargin: '0px',
        threshold: 0.5 // trigger when 50% of the element is visible
    });

    observer.observe(workflowContainer);
}