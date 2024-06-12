function startRecognition() {
    if (!('SpeechRecognition' in window) && !('webkitSpeechRecognition' in window)) {
        alert('La reconnaissance vocale n\'est pas supportée par ce navigateur.');
        return;
    }

    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'fr-FR';
    recognition.interimResults = false;

    recognition.onstart = function() {
        console.log('Reconnaissance vocale démarrée.');
        document.getElementById('response').innerText = 'Écoute en cours...';
    };

    recognition.onresult = function(event) {
        const command = event.results[0][0].transcript;
        console.log('Résultat de la reconnaissance vocale :', command);
        sendCommand(command, recognition);
    };

    recognition.onerror = function(event) {
        console.error('Erreur de reconnaissance vocale :', event.error);
        document.getElementById('response').innerText = 'Erreur de reconnaissance vocale : ' + event.error;
        recognition.start(); 
    };

    recognition.start();
}

function sendCommand(command, recognition) {
    fetch('/commande', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'command=' + encodeURIComponent(command)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = data.response;

       

        // Redémarrer la reconnaissance vocale sauf si la commande est "au revoir"
        if (command.toLowerCase().includes('au revoir')) {
            recognition.stop();
        } else {
            recognition.start();
        }
    });
}

// Popup functionality
document.querySelectorAll('.popupButton').forEach(button => {
    button.addEventListener('click', () => {
        button.parentElement.querySelector('.overlay').style.display = 'block';
    });
});

document.querySelectorAll('.closeButton').forEach(button => {
    button.addEventListener('click', () => {
        button.closest('.overlay').style.display = 'none';
    });
});

// Menu dropdown functionality
document.querySelectorAll('.menu-title').forEach(menuTitle => {
    menuTitle.addEventListener('click', (event) => {
        event.stopPropagation();
        const dropdown = menuTitle.nextElementSibling;
        const isVisible = dropdown.style.display === 'block';

        document.querySelectorAll('.menu-dropdown').forEach(dropdown => {
            dropdown.style.display = 'none';
        });

        dropdown.style.display = isVisible ? 'none' : 'block';
    });
});

document.addEventListener('click', () => {
    document.querySelectorAll('.menu-dropdown').forEach(dropdown => {
        dropdown.style.display = 'none';
    });
});