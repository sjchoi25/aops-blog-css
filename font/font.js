document.addEventListener("DOMContentLoaded", () => {
    const urlParams = new URLSearchParams(window.location.search);

    const font = urlParams.get('family');
    const css = `@import url('https://fonts.googleapis.com/css2?family=${font.split(" ").join("+")}&display=swap');
    
/**   Font  **/

/* Credits to pog */
body, .btn-primary, #navigation_box a, 
.inputbox, input.button2, .cmty-post-textarea, 
.cmty-subject-input, .cmty-items-input.ui-autocomplete-input, 
div.cmty-item-tag, button.btn.btn-run, button.btn.btn-reset,
button.btn.btn-link.btn-pop, div.cmty-topic-cell-post, 
div.cmty-topic-cell-subtitle, 
span.cmty-color-main.cmty-topic-cell-username, 
div.cmty-topic-cell-subject, div.cmty-topic-watchers, 
div.cmty-topic-cell-left-bottom, div.cmty-topic-cell-source, 
div.cmty-topic-cell-second-row, select, 
input#login-username.form-control, 
input#login-password.form-control, button#login-cancel-button.btn, 
div.cmty-topic-subject, input.cmty-submit-button.btn.btn-primary, 
textarea {
    font-family: '${font}';
    letter-spacing: 0.8px; 
    word-spacing: 1.6px;
    font-size: 16px;
}
.cmty-reply-window input.cmty-submit-button.btn.btn-primary {
    font-size: 12px;
}`;

    if (font === null)
    {
        css = "";
    }
    document.querySelector('pre').innerHTML = css;
});
