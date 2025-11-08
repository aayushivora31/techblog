// Custom JavaScript for TechBlog

// Debug function to check if script is loaded
console.log('TechBlog script loaded');

// Check if Bootstrap is loaded
if (typeof bootstrap === 'undefined') {
    console.warn('Bootstrap is not loaded. Some components may not work properly.');
}

// Throttle function to limit scroll event frequency
function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    }
}

// Improved function to check if element is in viewport
function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    const windowHeight = window.innerHeight || document.documentElement.clientHeight;
    // Element is in viewport when it's partially visible (more performant)
    return (
        rect.top <= windowHeight * 1.2 &&
        rect.bottom >= 0
    );
}

// Optimized function to animate elements when they come into view
function animateOnScroll() {
    const elements = document.querySelectorAll('.fade-in-up:not(.animated)');
    
    elements.forEach(element => {
        if (isInViewport(element)) {
            // Use requestAnimationFrame for better performance
            requestAnimationFrame(() => {
                element.classList.add('animated');
            });
        }
    });
}

// Debounced scroll handler
const throttledAnimateOnScroll = throttle(animateOnScroll, 100);

// Function to initialize dropdowns
function initializeDropdowns() {
    try {
        // Check if Bootstrap is available
        if (typeof bootstrap === 'undefined') {
            console.warn('Bootstrap is not available, skipping dropdown initialization');
            return;
        }
        
        var dropdownElementList = [].slice.call(document.querySelectorAll('.dropdown-toggle'));
        var dropdownList = dropdownElementList.map(function (dropdownToggleEl) {
            return new bootstrap.Dropdown(dropdownToggleEl);
        });
        console.log('Dropdowns initialized');
    } catch (error) {
        console.log('Dropdown initialization error:', error);
    }
}

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM fully loaded and parsed');
    
    // Initialize tooltips
    try {
        var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
        console.log('Tooltips initialized');
    } catch (error) {
        console.log('Tooltip initialization error:', error);
    }
    
    // Initialize dropdowns
    initializeDropdowns();
    
    // Scroll to top button
    try {
        const scrollToTopButton = document.createElement('button');
        scrollToTopButton.className = 'scroll-to-top btn btn-primary';
        scrollToTopButton.innerHTML = '<i class="fas fa-arrow-up"></i>';
        scrollToTopButton.setAttribute('aria-label', 'Scroll to top');
        scrollToTopButton.style.position = 'fixed';
        scrollToTopButton.style.bottom = '30px';
        scrollToTopButton.style.right = '30px';
        scrollToTopButton.style.zIndex = '1000';
        document.body.appendChild(scrollToTopButton);
        console.log('Scroll to top button created');
        
        // Show/hide scroll to top button with throttling
        const throttledScrollHandler = throttle(function() {
            if (window.pageYOffset > 300) {
                scrollToTopButton.classList.add('visible');
            } else {
                scrollToTopButton.classList.remove('visible');
            }
        }, 100);
        
        window.addEventListener('scroll', throttledScrollHandler);
        
        // Scroll to top functionality
        scrollToTopButton.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    } catch (error) {
        console.log('Scroll to top button error:', error);
    }
    
    // Loading animation
    try {
        const loadingOverlay = document.createElement('div');
        loadingOverlay.className = 'loading-overlay';
        loadingOverlay.innerHTML = '<div class="loading-spinner"></div>';
        document.body.appendChild(loadingOverlay);
        console.log('Loading overlay created');
        
        // Hide loading animation when page is fully loaded
        window.addEventListener('load', function() {
            setTimeout(function() {
                loadingOverlay.style.opacity = '0';
                setTimeout(function() {
                    loadingOverlay.style.display = 'none';
                }, 300);
            }, 500);
        });
    } catch (error) {
        console.log('Loading overlay error:', error);
    }
    
    // Form validation
    try {
        const forms = document.querySelectorAll('.needs-validation');
        Array.from(forms).forEach(form => {
            form.addEventListener('submit', function(event) {
                if (!form.checkValidity()) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
        console.log('Form validation initialized');
    } catch (error) {
        console.log('Form validation error:', error);
    }
    
    // Smooth scrolling for anchor links
    try {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
        console.log('Smooth scrolling initialized');
    } catch (error) {
        console.log('Smooth scrolling error:', error);
    }
    
    // Add fade-in animation to cards with better performance
    try {
        const cards = document.querySelectorAll('.fade-in-up');
        cards.forEach((card, index) => {
            // Use CSS variables for staggered delays instead of inline styles
            card.style.setProperty('--animation-delay', (index * 0.1) + 's');
        });
        console.log('Card animations applied to', cards.length, 'cards');
        
        // Trigger animation check immediately
        // Also check after a short delay to ensure elements are rendered
        setTimeout(animateOnScroll, 100);
        setTimeout(animateOnScroll, 500);
    } catch (error) {
        console.log('Card animation error:', error);
    }
    
    // Initialize clipboard.js for copy buttons
    try {
        if (typeof ClipboardJS !== 'undefined') {
            new ClipboardJS('.copy-btn');
            console.log('Clipboard.js initialized');
            
            // Show success message on copy
            document.querySelectorAll('.copy-btn').forEach(button => {
                button.addEventListener('click', function() {
                    const originalText = this.innerHTML;
                    this.innerHTML = '<i class="fas fa-check me-1"></i>Copied!';
                    this.classList.remove('btn-outline-primary');
                    this.classList.add('btn-success');
                    
                    setTimeout(() => {
                        this.innerHTML = originalText;
                        this.classList.remove('btn-success');
                        this.classList.add('btn-outline-primary');
                    }, 2000);
                });
            });
        } else {
            console.log('Clipboard.js not loaded');
        }
    } catch (error) {
        console.log('Clipboard.js error:', error);
    }
    
    // Add scroll event listener for animations with throttling
    window.addEventListener('scroll', throttledAnimateOnScroll);
    
    // Trigger animation check on load
    setTimeout(animateOnScroll, 100);
});

// Fallback for older browsers
if (!document.addEventListener) {
    console.log('addEventListener not supported, using attachEvent');
    document.attachEvent('onreadystatechange', function() {
        if (document.readyState === 'complete') {
            // Initialize components here for older browsers
        }
    });
}