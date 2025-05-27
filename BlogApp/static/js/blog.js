const $pages = $('.page');
const $pageCounter = $('#pageCounter');
const $prevBtn = $('#prevBtn');
const $nextBtn = $('#nextBtn');
let currentPage = 0;

function flipPage(direction) {
  $pages.eq(currentPage).removeClass('page-active').addClass('page-hidden');

  currentPage = Math.min(Math.max(currentPage + direction, 0), $pages.length - 1);

  $pages.eq(currentPage).removeClass('page-hidden').addClass('page-active');

  updateControls();
}

function updateControls() {
  $pageCounter.text(`Page ${currentPage + 1} of ${$pages.length}`);
  $prevBtn.toggle(currentPage !== 0);
  $nextBtn.toggle(currentPage !== $pages.length - 1);
}

// Attach event handlers using jQuery
$prevBtn.on('click', () => flipPage(-1));
$nextBtn.on('click', () => flipPage(1));

// Initialize
updateControls();