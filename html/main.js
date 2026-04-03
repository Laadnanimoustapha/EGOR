const API_URL = "https://dfifa-egor.hf.space";
const API_KEY = "FUCK-ISREAL-76034217-LAERSI-KCUF";

// 90% MAID BY LAADNANI  10% BY AI (GEMINI 3.1 THINKING)

async function GeneratePassword() {
    const length = document.getElementById("length").value;

    try {
        const response = await fetch(`${API_URL}/generate?length=${length}`, {
            method: "GET",
            headers: {
                "x-api-key": API_KEY
            }
        });

        const data = await response.json();

        document.getElementById("result").value = data.password;

    } catch (error) {
        alert("Error connecting to API ");
        console.error(error);
    }
}

function copyPassword() {
    const result = document.getElementById("result");

    result.select();
    document.execCommand("copy");

    alert("Copied! ");
}