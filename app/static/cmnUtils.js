
function checkedValueOfRadioButton(radioName) {
    // name="input_rube"のラジオボタンを全て取得
    var radios = document.querySelectorAll('input[name="' + radioName + '"]');

    // チェックされているラジオボタンの値を取得
    var checkedValue;
    for (var i = 0; i < radios.length; i++) {
        if (radios[i].checked) {
            checkedValue = radios[i].value;
            break;
        }
    }
    return checkedValue;
}