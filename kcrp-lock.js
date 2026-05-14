// Update this value to change the lightweight K-CRP access password.
window.KCRP_PASSWORD = window.KCRP_PASSWORD || "kcrp2026";

(function () {
  var STORAGE_KEY = "engis_kcrp_access_granted";

  function hasAccess() {
    try {
      return window.sessionStorage.getItem(STORAGE_KEY) === "true";
    } catch (error) {
      return false;
    }
  }

  function grantAccess() {
    try {
      window.sessionStorage.setItem(STORAGE_KEY, "true");
    } catch (error) {
      // Ignore session storage failures in lightweight client-side mode.
    }
  }

  function requestAccess() {
    if (hasAccess()) {
      return true;
    }

    var input = window.prompt("K-CRP 자료는 비밀번호가 필요합니다.");
    if (input === null) {
      return false;
    }

    if (input === window.KCRP_PASSWORD) {
      grantAccess();
      return true;
    }

    window.alert("비밀번호가 올바르지 않습니다.");
    return false;
  }

  function guardPage(options) {
    if (requestAccess()) {
      return true;
    }

    var fallback = (options && options.fallbackHref) || "../business-decks.html";
    window.location.replace(fallback);
    return false;
  }

  function attachProtectedLinks(selector) {
    document.querySelectorAll(selector).forEach(function (link) {
      link.addEventListener("click", function (event) {
        if (requestAccess()) {
          return;
        }
        event.preventDefault();
      });
    });
  }

  window.kcrpAccess = {
    attachProtectedLinks: attachProtectedLinks,
    guardPage: guardPage,
    requestAccess: requestAccess,
  };
})();
