let translateTofrench = () => {
  textToTranslate = document.getElementById("textToTranslate").value;

  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("translated_text").innerHTML = xhttp.responseText;
    }
  };
  xhttp.open(
    "POST",
    "englishToFrench?textToTranslate" + "=" + textToTranslate,
    true
  );
  xhttp.send();
};

let translateToEnglish = () => {
  textToTranslate = document.getElementById("textToTranslate").value;

  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("translated_text").innerHTML = xhttp.responseText;
    }
  };
  xhttp.open(
    "POST",
    "frenchToEnglish?textToTranslate" + "=" + textToTranslate,
    true
  );
  xhttp.send();
};
