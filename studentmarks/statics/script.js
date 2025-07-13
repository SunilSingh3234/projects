document.getElementById('predictionForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const hours = document.getElementById('hours').value;
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = "Predicting...";

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ hours: parseFloat(hours) })
        });

        const data = await response.json();
        if (response.ok) {
            resultDiv.innerHTML = `Predicted Marks: ${data.marks.toFixed(2)}`;
        } else {
            resultDiv.innerHTML = `Error: ${data.error}`;
        }
    } catch (err) {
        resultDiv.innerHTML = `Error: ${err.message}`;
    }
});
