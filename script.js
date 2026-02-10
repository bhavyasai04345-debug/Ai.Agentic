const backendUrl = "https://ai-agentic.onrender.com";

async function reviewCode() {
    const codeInput = document.getElementById("codeInput").value;

    try {
        const response = await fetch(`${backendUrl}/review`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code: codeInput })
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const result = await response.json();
        document.getElementById("output").innerText = result.review;
    } catch (error) {
        document.getElementById("output").innerText = "Error: " + error.message;
    }
}