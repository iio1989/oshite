const inputClearBtn = document.getElementById('input__clear__btn');
inputClearBtn.onclick = function () {
    let textarea = document.getElementById("example__form__control__textarea");
    textarea.value = "";
};

// TODO:文字を変換する前は、ボタンが存在せずにJSエラーとなる。
const imnDownload = document.getElementById('oshite__img__download');
imnDownload.onclick = async function () {
    let textarea = document.getElementById("example__form__control__textarea").value;
    console.log('textarea:' + textarea);
    await fetch("/download", {
        method: "POST",
        body: JSON.stringify({
            input_kana: textarea,
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8",
        },
    })
        .then(response => response.blob()) //blobで読み込む
        .then(blob => {
            //DOMでダウンロードファイルを添付したアンカー要素を生成
            let anchor = document.createElement("a");
            anchor.download = String(Date.now()) + '.png'
            anchor.href = window.URL.createObjectURL(blob);
            //アンカーを発火
            anchor.click();
        })
        .catch(function (err) {
            console.log("err=" + err);
        });
};
