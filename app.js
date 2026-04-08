const header = document.querySelector(".site-header");

if ("scrollRestoration" in window.history) {
  window.history.scrollRestoration = "manual";
}

const resetInitialScroll = () => {
  if (window.location.hash) {
    return;
  }

  window.scrollTo(0, 0);
};

const syncHeaderState = () => {
  if (!header) {
    return;
  }

  header.classList.toggle("is-scrolled", window.scrollY > 12);
};

resetInitialScroll();
syncHeaderState();
window.addEventListener("pageshow", resetInitialScroll);
window.addEventListener("scroll", syncHeaderState, { passive: true });
