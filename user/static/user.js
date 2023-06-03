function likePost() {
    var likeCount = parseInt($('.like-count').text());
    likeCount++;
    $('.like-count').text(likeCount);
  }