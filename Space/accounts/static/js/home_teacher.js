const professorInfo = document.getElementById('professor-info');
const profileButton = document.getElementById('profile-button');
const logoutButton = document.getElementById('logout-button');
const createExerciseLink = document.getElementById('create-exercise');
const quizSection = document.getElementById('quiz-section');

// Exemple: nom du professeur (à remplacer par la logique d'authentification réelle)
const professorName = 'Nom du Professeur';

// Afficher le nom du professeur connecté
professorInfo.textContent = `Connecté en tant que: ${professorName}`;

// Exemple: Redirection vers la page de profil (à adapter à votre logique)
profileButton.addEventListener('click', function () {
    // window.location.href = 'page_profil.html';
    console.log("Redirection vers la page de profil");
});

// Exemple: Déconnexion (à adapter à votre logique)
logoutButton.addEventListener('click', function () {
    // Réalisez le processus de déconnexion ici (effacer les cookies, etc.)
    // window.location.href = 'page_deconnexion.html';
    console.log("Déconnexion en cours...");
});

createExerciseLink.addEventListener('click', function () {
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