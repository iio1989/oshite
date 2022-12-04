const inputClearBtn = document.getElementById('input__clear__btn');
inputClearBtn.onclick = function () {
    let textarea = document.getElementById("example__form__control__textarea");
    textarea.value = "";
};