let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                document.getElementById("system_response").innerHTML = xhttp.responseText;
            } else {
                document.getElementById("system_response").innerHTML = "Error: " + this.statusText;
            }
        }
    };

    let url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict";
    let headers = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" };
    let inputJson = JSON.stringify({ "raw_document": { "text": textToAnalyze } });

    xhttp.open("POST", url, true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.setRequestHeader("grpc-metadata-mm-model-id", headers["grpc-metadata-mm-model-id"]);
    xhttp.send(inputJson);
};