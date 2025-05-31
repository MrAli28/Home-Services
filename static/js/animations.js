// Animation handlers for HomeFix website

document.addEventListener('DOMContentLoaded', function() {
    // Add animation classes to elements when page loads
    animateOnLoad();
    
    // Initialize scroll animations
    initScrollAnimations();
    
    // Initialize navbar animations
    initNavbarAnimations();
    
    // Initialize form animations
    initFormAnimations();
    
    // Initialize card hover effects
    initCardEffects();
});

// Apply initial animations when page loads
function animateOnLoad() {
    // Animate navbar brand
    const navbarBrand = document.querySelector('.navbar-brand');
    if (navbarBrand) {
        navbarBrand.classList.add('animate-fade-in');
    }
    
    // Animate hero section elements with a delay
    const heroElements = document.querySelectorAll('.hero-section *');
    heroElements.forEach((el, index) => {
        setTimeout(() => {
            el.classList.add('animate-fade-in');
        }, 100 * index);
    });
    
    // Animate service cards with staggered delay
    const serviceCards = document.querySelectorAll('.service-card');
    serviceCards.forEach((card, index) => {
        setTimeout(() => {
            card.classList.add('animate-slide-up');
        }, 150 * index);
    });
}

// Initialize scroll animations
function initScrollAnimations() {
    // Get all elements with data-scroll attribute
    const scrollElements = document.querySelectorAll('[data-scroll]');
    
    // Set initial state
    scrollElements.forEach(el => {
        el.setAttribute('data-scroll', 'out');
    });
    
    // Function to check if element is in viewport
    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        return (
            rect.top <= (window.innerHeight || document.documentElement.clientHeight) * 0.8 &&
            rect.bottom >= 0
        );
    }
    
    // Function to handle scroll events
    function handleScrollAnimation() {
        scrollElements.forEach(el => {
            if (isElementInViewport(el)) {
                el.setAttribute('data-scroll', 'in');
            } else {
                el.setAttribute('data-scroll', 'out');
            }
        });
    }
    
    // Add scroll event listener
    window.addEventListener('scroll', handleScrollAnimation);
    
    // Trigger once on load
    handleScrollAnimation();
}

// Initialize navbar animations
function initNavbarAnimations() {
    const navbar = document.querySelector('.navbar');
    const navLinks = document.querySelectorAll('.nav-link');
    
    // Add hover animation to nav links
    navLinks.forEach(link => {
        link.addEventListener('mouseenter', function() {
            this.classList.add('animate-pulse');
        });
        
        link.addEventListener('mouseleave', function() {
            this.classList.remove('animate-pulse');
        });
    });
    
    // Change navbar on scroll
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }
    });
}

// Initialize form animations
function initFormAnimations() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        // Add loading state to submit buttons
        form.addEventListener('submit', function() {
            const submitBtn = this.querySelector('[type="submit"]');
            if (submitBtn) {
                submitBtn.classList.add('loading');
                submitBtn.setAttribute('disabled', true);
                
                // Add a spinner to the button if not already present
                if (!submitBtn.querySelector('.spinner-border')) {
                    const spinner = document.createElement('span');
                    spinner.className = 'spinner-border';
                    spinner.setAttribute('role', 'status');
                    spinner.innerHTML = '<span class="visually-hidden">Loading...</span>';
                    submitBtn.appendChild(spinner);
                }
            }
        });
        
        // Add animation to form inputs on focus
        const formControls = form.querySelectorAll('.form-control');
        formControls.forEach(input => {
            input.addEventListener('focus', function() {
                this.parentElement.classList.add('focused');
            });
            
            input.addEventListener('blur', function() {
                this.parentElement.classList.remove('focused');
            });
        });
    });
}

// Initialize card hover effects
function initCardEffects() {
    const cards = document.querySelectorAll('.card');
    
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.classList.add('card-hover');
        });
        
        card.addEventListener('mouseleave', function() {
            this.classList.remove('card-hover');
        });
    });
    
    // Special animation for testimonial cards
    const testimonialCards = document.querySelectorAll('.testimonial-card');
    testimonialCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.classList.add('animate-pulse');
        });
        
        card.addEventListener('mouseleave', function() {
            this.classList.remove('animate-pulse');
        });
    });
    
    // Special animation for service icons
    const serviceIcons = document.querySelectorAll('.service-icon');
    serviceIcons.forEach(icon => {
        icon.addEventListener('mouseenter', function() {
            this.classList.add('animate-bounce');
        });
        
        icon.addEventListener('mouseleave', function() {
            this.classList.remove('animate-bounce');
        });
    });
}
