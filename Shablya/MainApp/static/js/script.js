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

