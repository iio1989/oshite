const inputClearBtn = document.getElementById('input__clear__btn');
inputClearBtn.onclick = function () {
    let textarea = document.getElementById("example__form__control__textarea");
    textarea.value = "";
};

const imnDownload = document.getElementById('oshite__img__download');
if (imnDownload !== null) {
    imnDownload.onclick = async function () {
        let textarea = document.getElementById("example__form__control__textarea").value;
        await fetch("/download", {
            method: "POST",
            body: JSON.stringify({
                input_kana: textarea,
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8",
            },
        })
            .then(response => response.blob())
            .then(blob => {
                let anchor = document.createElement("a");
                anchor.download = 'ヲシテ画像.png'
                anchor.href = window.URL.createObjectURL(blob);
                anchor.click();
            })
            .catch(function (err) {
                console.log("err=" + err);
            });
    };
}
