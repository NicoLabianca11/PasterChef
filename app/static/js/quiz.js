// ==================== PASTERCHEF QUIZ.JS ====================

document.addEventListener('DOMContentLoaded', () => {
    console.log('🎯 PasterChef Quiz Loaded!');

    if (!window.QUIZ_DATA) {
        console.error('Quiz data not found!');
        return;
    }

    initQuiz();
});

// ==================== QUIZ STATE ====================

const QuizState = {
    currentQuestion: 0,
    answers: [],
    isSubmitting: false,
    isComplete: false
};

// ==================== QUIZ INITIALIZATION ====================

// ==================== QUIZ INITIALIZATION ====================

function initQuiz() {
    console.log('🚀 Initializing Quiz...');
    const { recipeId } = window.QUIZ_DATA;

    // Show loading state
    const quizCard = document.getElementById('quizCard');
    if (quizCard) {
        quizCard.innerHTML = '<div style="text-align:center; padding: 2rem;"><h3>⏳ Caricamento domande...</h3></div>';
    }

    // Fetch questions from API
    fetch(`/api/get-quiz/${recipeId}`)
        .then(response => {
            if (!response.ok) throw new Error('Errore nel caricamento del quiz');
            return response.json();
        })
        .then(data => {
            console.log('📦 Quiz data received:', data);

            // Update global data
            window.QUIZ_DATA.questions = data.questions;
            window.QUIZ_DATA.totalQuestions = data.totalQuestions;

            // Try to restore saved progress from localStorage
            restoreProgress();

            // Render first question
            renderQuestion(QuizState.currentQuestion);
            updateProgress();
        })
        .catch(error => {
            console.error('❌ Error fetching quiz:', error);
            if (quizCard) {
                quizCard.innerHTML = `
                    <div style="text-align:center; color: #e53935; padding: 2rem;">
                        <h3>⚠️ Errore di caricamento</h3>
                        <p>Non siamo riusciti a caricare le domande. Riprova più tardi.</p>
                        <button onclick="location.reload()" class="btn-primary" style="margin-top:1rem;">Ricarica</button>
                    </div>`;
            }
        });

    // Setup retry button
    const retryBtn = document.getElementById('retryQuizBtn');
    if (retryBtn) {
        retryBtn.addEventListener('click', resetQuiz);
    }

    // Keyboard navigation
    document.addEventListener('keydown', handleKeyboard);
}

// ==================== QUESTION RENDERING ====================

// ==================== QUESTION RENDERING ====================

function renderQuestion(index) {
    const { questions } = window.QUIZ_DATA;
    const question = questions[index];
    const quizCard = document.getElementById('quizCard');

    if (!question || !quizCard) return;

    // Determine button text (Next or Finish)
    const isLast = index === questions.length - 1;
    const btnText = isLast ? 'Vedi Risultati 🎉' : 'Prossima Domanda →';

    // Animate out current content
    quizCard.classList.add('slide-out');

    setTimeout(() => {
        quizCard.innerHTML = `
            <div class="question-header">
                <span class="question-number">Domanda ${index + 1}</span>
            </div>
            <h2 class="question-text">${question.question}</h2>
            <div class="quiz-options" id="quizOptions">
                ${question.options_with_emoji.map((opt, i) => `
                    <button class="quiz-option" 
                            data-index="${i}" 
                            tabindex="0"
                            aria-label="Opzione ${String.fromCharCode(65 + i)}: ${opt.text}">
                        <span class="option-letter">${String.fromCharCode(65 + i)}</span>
                        <span class="option-emoji">${opt.emoji}</span>
                        <span class="option-text">${opt.text}</span>
                    </button>
                `).join('')}
            </div>
            
            <div class="quiz-footer" style="margin-top: 2rem; text-align: right; min-height: 50px;">
                <button id="nextQuestionBtn" class="btn-primary hidden">
                    ${btnText}
                </button>
            </div>
        `;

        // Animate in
        quizCard.classList.remove('slide-out');
        quizCard.classList.add('slide-in');

        // Clean up animation class
        setTimeout(() => {
            quizCard.classList.remove('slide-in');
        }, 300);

        // Add click handlers to options
        const options = quizCard.querySelectorAll('.quiz-option');
        options.forEach(opt => {
            opt.addEventListener('click', () => selectAnswer(parseInt(opt.dataset.index)));
        });

        // Add click handler to Next button
        const nextBtn = document.getElementById('nextQuestionBtn');
        if (nextBtn) {
            nextBtn.addEventListener('click', handleNext);
        }

        // Focus first option for keyboard nav if not previously answered
        if (options[0]) {
            // options[0].focus(); // Optional: might be annoying on mobile
        }
    }, 150);
}

// ==================== ANSWER SELECTION ====================

function selectAnswer(answerIndex) {
    // Prevent changing answer if already selected (unless we want to allow changing before 'Next')
    // For now, let's lock it once selected to show immediate feedback as per requirements
    // Check if already answered this specific question
    // But QuizState.answers is array. 

    // Check if we already have an answer for this question index
    if (QuizState.answers[QuizState.currentQuestion] !== undefined) return;

    const { questions } = window.QUIZ_DATA;
    const question = questions[QuizState.currentQuestion];
    const isCorrect = answerIndex === question.correct;

    // Store answer
    QuizState.answers[QuizState.currentQuestion] = answerIndex;

    // Show feedback
    showFeedback(answerIndex, question.correct, isCorrect, question.explanation);

    // Save progress
    saveProgress();

    // Show Next Button
    const nextBtn = document.getElementById('nextQuestionBtn');
    if (nextBtn) {
        nextBtn.classList.remove('hidden');
        nextBtn.focus();
    }
}

function showFeedback(selectedIndex, correctIndex, isCorrect, explanation) {
    const options = document.querySelectorAll('.quiz-option');

    // Disable all options
    options.forEach(opt => {
        opt.disabled = true;
        opt.classList.add('disabled');
    });

    // Mark selected answer
    if (options[selectedIndex]) {
        options[selectedIndex].classList.add(isCorrect ? 'correct' : 'wrong');
    }

    // Always show correct answer
    if (!isCorrect && options[correctIndex]) {
        options[correctIndex].classList.add('correct');
    }

    // Add feedback icon
    const selectedOpt = options[selectedIndex];
    if (selectedOpt) {
        const feedbackIcon = document.createElement('span');
        feedbackIcon.className = 'feedback-icon';
        feedbackIcon.textContent = isCorrect ? '✓' : '✗';
        selectedOpt.appendChild(feedbackIcon);
    }

    // Optional: Show explanation text if needed somewhere
    // For now, the icon is enough as per design, but user requested "Spiegazione qui" in initial prompt
    // Let's create a feedback box below options if not exists
    let feedbackBox = document.getElementById('feedbackBox');
    if (!feedbackBox) {
        feedbackBox = document.createElement('div');
        feedbackBox.id = 'feedbackBox';
        feedbackBox.className = `feedback ${isCorrect ? 'correct' : 'wrong'}`;
        feedbackBox.innerHTML = `
            <span class="feedback-icon-lg">${isCorrect ? '✓' : '✗'}</span>
            <p class="feedback-text">${explanation || (isCorrect ? 'Risposta corretta!' : 'Risposta sbagliata!')}</p>
        `;
        document.getElementById('quizOptions').after(feedbackBox);
    }
}

function handleNext() {
    const { questions } = window.QUIZ_DATA;

    if (QuizState.currentQuestion < questions.length - 1) {
        QuizState.currentQuestion++;
        renderQuestion(QuizState.currentQuestion);
        updateProgress();
    } else {
        submitQuiz();
    }
}

// ==================== PROGRESS ====================

function updateProgress() {
    const { totalQuestions } = window.QUIZ_DATA;
    const progressPercent = ((QuizState.currentQuestion + 1) / totalQuestions) * 100;

    const progressFill = document.getElementById('progressFill');
    const progressText = document.getElementById('progressText');

    if (progressFill) {
        progressFill.style.width = `${progressPercent}%`;
    }
    if (progressText) {
        progressText.textContent = `Domanda ${QuizState.currentQuestion + 1} di ${totalQuestions}`;
    }
}

// ==================== SUBMIT QUIZ ====================

async function submitQuiz() {
    if (QuizState.isSubmitting) return;

    QuizState.isSubmitting = true;
    QuizState.isComplete = true;

    const { recipeId, totalQuestions } = window.QUIZ_DATA;

    try {
        const response = await fetch('/api/submit-quiz', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                recipe_id: recipeId,
                answers: QuizState.answers
            })
        });

        const data = await response.json();

        if (data.success) {
            // Clear saved progress
            clearProgress();

            // Show results
            showResults(data);

            // Trigger confetti if passed
            if (data.passed) {
                triggerConfetti();
            }
        } else {
            console.error('Quiz submission error:', data.error);
        }
    } catch (error) {
        console.error('Quiz submission failed:', error);
        QuizState.isSubmitting = false;
        QuizState.isComplete = false;
    }
}

// ==================== RESULTS ====================

function showResults(data) {
    const quizCard = document.getElementById('quizCard');
    const quizResults = document.getElementById('quizResults');

    if (quizCard) quizCard.classList.add('hidden');
    if (quizResults) quizResults.classList.remove('hidden');

    // Update results content
    const resultsIcon = document.getElementById('resultsIcon');
    const resultsTitle = document.getElementById('resultsTitle');
    const scoreNumber = document.getElementById('scoreNumber');
    const resultsXp = document.getElementById('resultsXp');
    const resultsMessage = document.getElementById('resultsMessage');

    if (resultsIcon) {
        if (data.correct_count === data.total_questions) {
            resultsIcon.textContent = '🏆';
        } else if (data.passed) {
            resultsIcon.textContent = '🎉';
        } else {
            resultsIcon.textContent = '💪';
        }
    }

    if (resultsTitle) {
        resultsTitle.textContent = data.passed ? 'Quiz Superato!' : 'Quiz Completato';
    }

    if (scoreNumber) {
        // Animate score counting
        animateNumber(scoreNumber, 0, data.correct_count, 800);
    }

    if (resultsXp) {
        if (data.xp_earned > 0) {
            resultsXp.innerHTML = `<span class="xp-badge">+${data.xp_earned} XP</span>`;
        } else if (data.first_time === false) {
            resultsXp.innerHTML = `<span class="xp-badge no-xp">XP già assegnati</span>`;
        } else {
            resultsXp.innerHTML = '';
        }
    }

    if (resultsMessage) {
        resultsMessage.textContent = data.message;
    }

    // Animate results card
    const resultsCard = quizResults.querySelector('.results-card');
    if (resultsCard) {
        resultsCard.classList.add('pop-in');
    }
}

function animateNumber(element, start, end, duration) {
    const range = end - start;
    const startTime = performance.now();

    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);

        // Easing
        const easeOut = 1 - Math.pow(1 - progress, 3);
        const current = Math.round(start + range * easeOut);

        element.textContent = current;

        if (progress < 1) {
            requestAnimationFrame(update);
        }
    }

    requestAnimationFrame(update);
}

// ==================== CONFETTI ====================

function triggerConfetti() {
    const container = document.getElementById('confettiContainer');
    if (!container) return;

    container.classList.remove('hidden');

    const colors = ['#e91e63', '#ffd700', '#4caf50', '#2196f3', '#ff9800', '#9c27b0'];
    const confettiCount = 50;

    for (let i = 0; i < confettiCount; i++) {
        const confetti = document.createElement('div');
        confetti.className = 'confetti-piece';
        confetti.style.left = `${Math.random() * 100}%`;
        confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        confetti.style.animationDelay = `${Math.random() * 0.5}s`;
        confetti.style.animationDuration = `${2 + Math.random() * 2}s`;
        container.appendChild(confetti);
    }

    // Clean up after animation
    setTimeout(() => {
        container.innerHTML = '';
        container.classList.add('hidden');
    }, 4000);
}

// ==================== RESET QUIZ ====================

function resetQuiz() {
    QuizState.currentQuestion = 0;
    QuizState.answers = [];
    QuizState.isSubmitting = false;
    QuizState.isComplete = false;

    // Hide results, show quiz
    const quizCard = document.getElementById('quizCard');
    const quizResults = document.getElementById('quizResults');

    if (quizResults) quizResults.classList.add('hidden');
    if (quizCard) quizCard.classList.remove('hidden');

    // Re-render first question
    renderQuestion(0);
    updateProgress();

    // Clear saved progress
    clearProgress();
}

// ==================== LOCAL STORAGE ====================

function saveProgress() {
    const { recipeId } = window.QUIZ_DATA;
    const progressData = {
        currentQuestion: QuizState.currentQuestion,
        answers: QuizState.answers,
        timestamp: Date.now()
    };

    try {
        localStorage.setItem(`quiz_progress_${recipeId}`, JSON.stringify(progressData));
    } catch (e) {
        console.warn('Could not save quiz progress:', e);
    }
}

function restoreProgress() {
    const { recipeId } = window.QUIZ_DATA;

    try {
        const saved = localStorage.getItem(`quiz_progress_${recipeId}`);
        if (saved) {
            const progressData = JSON.parse(saved);

            // Only restore if less than 1 hour old
            const oneHour = 60 * 60 * 1000;
            if (Date.now() - progressData.timestamp < oneHour) {
                QuizState.currentQuestion = progressData.currentQuestion || 0;
                QuizState.answers = progressData.answers || [];
                console.log('📂 Restored quiz progress');
            } else {
                clearProgress();
            }
        }
    } catch (e) {
        console.warn('Could not restore quiz progress:', e);
    }
}

function clearProgress() {
    const { recipeId } = window.QUIZ_DATA;

    try {
        localStorage.removeItem(`quiz_progress_${recipeId}`);
    } catch (e) {
        console.warn('Could not clear quiz progress:', e);
    }
}

// ==================== KEYBOARD NAVIGATION ====================

function handleKeyboard(e) {
    if (QuizState.isComplete || QuizState.isSubmitting) return;

    const options = document.querySelectorAll('.quiz-option:not(.disabled)');
    if (!options.length) return;

    // A, B, C, D keys or 1, 2, 3, 4
    const keyMap = {
        'a': 0, 'A': 0, '1': 0,
        'b': 1, 'B': 1, '2': 1,
        'c': 2, 'C': 2, '3': 2,
        'd': 3, 'D': 3, '4': 3
    };

    if (keyMap.hasOwnProperty(e.key)) {
        e.preventDefault();
        const index = keyMap[e.key];
        if (options[index]) {
            selectAnswer(index);
        }
    }

    // Enter to confirm focused option
    if (e.key === 'Enter') {
        const focused = document.activeElement;
        if (focused && focused.classList.contains('quiz-option')) {
            e.preventDefault();
            selectAnswer(parseInt(focused.dataset.index));
        }
    }

    // Arrow keys for navigation
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
        e.preventDefault();
        const focused = document.activeElement;
        const optionsArray = Array.from(options);
        let currentIndex = optionsArray.indexOf(focused);

        if (e.key === 'ArrowDown') {
            currentIndex = (currentIndex + 1) % optionsArray.length;
        } else {
            currentIndex = (currentIndex - 1 + optionsArray.length) % optionsArray.length;
        }

        optionsArray[currentIndex]?.focus();
    }
}

console.log('✅ Quiz.js fully loaded');
