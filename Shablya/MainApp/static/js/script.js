function toggleLike(button) {
    var likeIcon = button.querySelector('.like-icon');
    var likedIcon = button.querySelector('.liked-icon');
    likeIcon.classList.toggle('hidden');
    likedIcon.classList.toggle('hidden');
}

