const createExerciseLink = document.getElementById('create-exercise');
        const quizSection = document.getElementById('quiz-section');

        createExerciseLink.addEventListener('click', function() {
            quizSection.style.display = 'block';
        });

        function createExercise() {
            const selectedType = document.querySelector('input[name="exercise-type"]:checked').value;
            // Redirige vers la page appropriée en fonction du type d'exercice sélectionné
            if (selectedType === 'exercice') {
                window.location.href = 'page_creer_exercice.html';
            } else if (selectedType === 'quiz') {
                window.location.href = 'page_creer_quiz.html';
            }
        }