// ==================== PASTERCHEF APP.JS ====================

document.addEventListener('DOMContentLoaded', () => {
    console.log('🧁 PasterChef App Loaded!');

    initCarousel();
    initChat();
    initNoteSaving();
    initRecipeCompletion();
    initIngredientChecks();
});

// ==================== CAROUSEL ====================
function initCarousel() {
    const track = document.getElementById('carouselTrack');
    if (!track) return;

    const slides = track.querySelectorAll('.carousel-slide');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const dots = document.querySelectorAll('.dot');

    let currentIndex = 0;
    const totalSlides = slides.length;

    function updateCarousel() {
        const width = slides[0]?.getBoundingClientRect().width || 0;
        track.style.transform = `translateX(-${currentIndex * width}px)`;

        // Update dots
        dots.forEach((dot, index) => {
            dot.classList.toggle('active', index === currentIndex);
        });
    }

    function goToSlide(index) {
        currentIndex = Math.max(0, Math.min(index, totalSlides - 1));
        updateCarousel();
    }

    prevBtn?.addEventListener('click', () => {
        goToSlide(currentIndex - 1);
    });

    nextBtn?.addEventListener('click', () => {
        goToSlide(currentIndex + 1);
    });

    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => goToSlide(index));
    });

    // Auto-advance every 5 seconds
    setInterval(() => {
        currentIndex = (currentIndex + 1) % totalSlides;
        updateCarousel();
    }, 5000);

    // Handle resize
    window.addEventListener('resize', updateCarousel);

    // Touch support for mobile
    let touchStartX = 0;
    let touchEndX = 0;

    track.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
    });

    track.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        if (touchStartX - touchEndX > 50) {
            goToSlide(currentIndex + 1);
        } else if (touchEndX - touchStartX > 50) {
            goToSlide(currentIndex - 1);
        }
    });
}

// ==================== CHAT ====================
function initChat() {
    const chatInput = document.getElementById('chatInput');
    const sendBtn = document.getElementById('sendChat');
    const chatBody = document.getElementById('chatBody');
    const toggleBtn = document.getElementById('toggleChat');

    if (!chatInput || !sendBtn || !chatBody) return;

    const recipeId = chatInput.dataset.recipeId;

    async function sendMessage() {
        const message = chatInput.value.trim();
        if (!message) return;

        // Add user message
        addMessage(message, 'user');
        chatInput.value = '';

        // Show typing indicator
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message bot typing';
        typingDiv.innerHTML = `
            <span class="bot-avatar">👨‍🍳</span>
            <div class="message-content">Sto pensando...</div>
        `;
        chatBody.appendChild(typingDiv);
        chatBody.scrollTop = chatBody.scrollHeight;

        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message, recipe_id: recipeId })
            });

            const data = await response.json();

            // Remove typing indicator
            typingDiv.remove();

            // Add bot response
            addMessage(data.response, 'bot');
        } catch (error) {
            console.error('Chat error:', error);
            typingDiv.remove();
            addMessage("Scusa, ho un problema in cucina! Riprova più tardi.", 'bot');
        }
    }

    function addMessage(text, sender) {
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ${sender}`;

        if (sender === 'bot') {
            msgDiv.innerHTML = `
                <span class="bot-avatar">👨‍🍳</span>
                <div class="message-content">${text}</div>
            `;
        } else {
            msgDiv.innerHTML = `
                <div class="message-content">${text}</div>
            `;
        }

        chatBody.appendChild(msgDiv);
        chatBody.scrollTop = chatBody.scrollHeight;
    }

    sendBtn.addEventListener('click', sendMessage);
    chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') sendMessage();
    });

    // Toggle chat visibility
    toggleBtn?.addEventListener('click', () => {
        const chatWidget = document.querySelector('.chat-widget');
        chatWidget.classList.toggle('minimized');
        toggleBtn.textContent = chatWidget.classList.contains('minimized') ? '+' : '−';
    });
}

// ==================== NOTE SAVING ====================
function initNoteSaving() {
    const textarea = document.getElementById('chefNotes');
    const saveBtn = document.getElementById('saveNotesBtn');

    if (!textarea || !saveBtn) return;

    const recipeId = textarea.dataset.recipeId;
    let saveTimeout;

    async function saveNotes() {
        const notes = textarea.value;

        try {
            const response = await fetch('/api/save-notes', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ recipe_id: recipeId, notes })
            });

            const data = await response.json();

            if (data.success) {
                saveBtn.textContent = '✓ Salvato!';
                saveBtn.style.background = 'linear-gradient(135deg, #4caf50 0%, #81c784 100%)';

                setTimeout(() => {
                    saveBtn.textContent = '💾 Salva Note';
                    saveBtn.style.background = '';
                }, 2000);
            }
        } catch (error) {
            console.error('Save error:', error);
            saveBtn.textContent = '❌ Errore';
            setTimeout(() => {
                saveBtn.textContent = '💾 Salva Note';
            }, 2000);
        }
    }

    saveBtn.addEventListener('click', saveNotes);

    // Auto-save after 2 seconds of inactivity
    textarea.addEventListener('input', () => {
        clearTimeout(saveTimeout);
        saveTimeout = setTimeout(saveNotes, 2000);
    });
}

// ==================== RECIPE COMPLETION ====================
function initRecipeCompletion() {
    const completeBtn = document.getElementById('completeBtn');

    if (!completeBtn) return;

    const recipeId = completeBtn.dataset.recipeId;

    completeBtn.addEventListener('click', async () => {
        completeBtn.disabled = true;
        completeBtn.textContent = '⏳ Infornando...';

        try {
            const response = await fetch('/api/complete-recipe', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ recipe_id: parseInt(recipeId) })
            });

            const data = await response.json();

            if (data.success) {
                // Show completion popup
                showCompletionPopup(data);

                // Update button
                completeBtn.textContent = '✓ Ricetta Completata!';
                completeBtn.classList.add('completed');

                // Check for milestone
                if (data.milestone && data.new_badge) {
                    setTimeout(() => {
                        showMilestonePopup(data.milestone, data.new_badge);
                    }, 2000);
                }
            }
        } catch (error) {
            console.error('Completion error:', error);
            completeBtn.disabled = false;
            completeBtn.textContent = '❌ Errore - Riprova';
        }
    });
}

function showCompletionPopup(data) {
    const popup = document.getElementById('completionPopup');
    const message = document.getElementById('completionMessage');

    if (popup) {
        message.textContent = `Hai guadagnato ${data.xp_earned} XP! Sei al livello ${data.new_level}.`;
        popup.classList.remove('hidden');
    }
}

function closeCompletionPopup() {
    const popup = document.getElementById('completionPopup');
    if (popup) {
        popup.classList.add('hidden');
    }
}

function showMilestonePopup(milestone, badge) {
    const popup = document.getElementById('milestonePopup');
    const badgeIcon = document.getElementById('newBadgeIcon');
    const badgeName = document.getElementById('newBadgeName');
    const message = document.getElementById('milestoneMessage');

    if (popup) {
        badgeIcon.textContent = badge.icon;
        badgeName.textContent = badge.name;
        message.textContent = `Hai raggiunto il livello ${milestone}!`;
        popup.classList.remove('hidden');

        // Play celebration sound (if available)
        playSound('celebration');
    }
}

function closeMilestonePopup() {
    const popup = document.getElementById('milestonePopup');
    if (popup) {
        popup.classList.add('hidden');
        // Redirect to roadmap
        window.location.href = '/';
    }
}

// Make popup functions global
window.closeCompletionPopup = closeCompletionPopup;
window.closeMilestonePopup = closeMilestonePopup;

// ==================== INGREDIENT CHECKS ====================
function initIngredientChecks() {
    const checkboxes = document.querySelectorAll('.ingredient-check');

    checkboxes.forEach(checkbox => {
        // Load saved state
        const key = `ingredient_${checkbox.closest('li').querySelector('.ingredient-text')?.textContent}`;
        const saved = localStorage.getItem(key);
        if (saved === 'true') {
            checkbox.checked = true;
        }

        // Save on change
        checkbox.addEventListener('change', () => {
            localStorage.setItem(key, checkbox.checked);
        });
    });
}

// ==================== SOUND EFFECTS ====================
function playSound(type) {
    // Placeholder for sound effects
    // In production, you would load and play actual audio files
    console.log(`🔊 Playing sound: ${type}`);
}

// ==================== UTILITY FUNCTIONS ====================

// Smooth scroll to element
function scrollToElement(element) {
    element.scrollIntoView({
        behavior: 'smooth',
        block: 'center'
    });
}

// Animate element
function animateElement(element, animation, duration = 1000) {
    element.style.animation = `${animation} ${duration}ms ease`;
    setTimeout(() => {
        element.style.animation = '';
    }, duration);
}

// Format number with commas
function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

// Debounce function
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// ==================== PAGE VISIBILITY API ====================
document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
        console.log('🌙 PasterChef is sleeping...');
    } else {
        console.log('☀️ PasterChef is awake!');
    }
});

// ==================== SERVICE WORKER (for PWA) ====================
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        // Service worker registration would go here for PWA support
        console.log('📱 PWA support available');
    });
}

console.log('✅ PasterChef App.js fully loaded');
