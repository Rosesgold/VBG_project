
function toggleLike(button) {
    var likeIcon = button.querySelector('.like-icon');
    var likedIcon = button.querySelector('.liked-icon');
    likeIcon.classList.toggle('hidden');
    likedIcon.classList.toggle('hidden');
}

function toggleSave(button) {
    var saveIcon = button.querySelector('.save-icon');
    var savedIcon = button.querySelector('.saved-icon');
    saveIcon.classList.toggle('hidden');
    savedIcon.classList.toggle('hidden');
}

function createCards(cardCount) {
    var wrapper = document.querySelector('.wrapper-second-part');

    for (var i = 0; i < cardCount; i++) {
        var card = document.createElement('div');
        card.className = 'card';

        var topCard = document.createElement('div');
        topCard.className = 'top-card';
        topCard.innerHTML = '<h2>Т-84 БМ "ОПЛОТ"</h2>';

        var middleCard = document.createElement('div');
        middleCard.className = 'middle-card';

        var img = document.createElement('img');
        img.src = 'images/Latest_time_(1914-)/oplot_ukr.png';
        img.alt = 'Логотип';
        img.style.width = '100%';
        img.style.height = '100%';

        middleCard.appendChild(img);

        var bottomCard = document.createElement('div');
        bottomCard.className = 'bottom-card';

        var iconsContainer = document.createElement('div');
        iconsContainer.className = 'icons-container';

        var likeIcon = document.createElement('div');
        likeIcon.className = 'icon';

        var likeButton = document.createElement('button');
        likeButton.className = 'like-button';
        likeButton.onclick = function() {
            toggleLike(this);
        };

        var likeImg = document.createElement('img');
        likeImg.src = '/static/images/like.png';
        likeImg.alt = 'Логотип';
        likeImg.className = 'like-icon';

        var likedImg = document.createElement('img');
        likedImg.src = '/static/images/liked.png';
        likedImg.alt = 'Логотип';
        likedImg.className = 'liked-icon hidden';

        likeButton.appendChild(likeImg);
        likeButton.appendChild(likedImg);
        likeIcon.appendChild(likeButton);

        var saveIcon = document.createElement('div');
        saveIcon.className = 'icon';

        var saveButton = document.createElement('button');
        saveButton.className = 'save-button';
        saveButton.onclick = function() {
            toggleSave(this);
        };

        var saveImg = document.createElement('img');
        saveImg.src = '/static/images/save.png';
        saveImg.alt = 'Логотип';
        saveImg.className = 'save-icon';

        var savedImg = document.createElement('img');
        savedImg.src = '/static/images/saved.png';
        savedImg.alt = 'Логотип';
        savedImg.className = 'saved-icon hidden';

        saveButton.appendChild(saveImg);
        saveButton.appendChild(savedImg);
        saveIcon.appendChild(saveButton);

        iconsContainer.appendChild(likeIcon);
        iconsContainer.appendChild(saveIcon);

        bottomCard.appendChild(iconsContainer);

        card.appendChild(topCard);
        card.appendChild(middleCard);
        card.appendChild(bottomCard);

        card.classList.add('card-appear');

        wrapper.appendChild(card);
    }
}




