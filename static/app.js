document.addEventListener("DOMContentLoaded", () => {
    const sendButton = document.getElementById("sendButton");
    const commandInput = document.getElementById("commandInput");
    const responseOutput = document.getElementById("responseOutput");

    sendButton.addEventListener("click", async () => {
        const command = commandInput.value.trim();
        if (!command) {
            responseOutput.textContent = "Please enter a command before sending.";
            return;
        }

        responseOutput.textContent = "Sending command to backend...";

        try {
            const response = await fetch("/api/command", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ command })
            });
            const data = await response.json();

            if (!data.success) {
                responseOutput.innerHTML = `<span class='error'>Error: ${data.error || 'Unknown error'}</span>`;
                return;
            }

            responseOutput.textContent = data.result || "Command completed successfully.";
        } catch (error) {
            responseOutput.innerHTML = `<span class='error'>Request failed: ${error.message}</span>`;
        }
    });
});

function useExample(command) {
    const commandInput = document.getElementById("commandInput");
    commandInput.value = command;
    commandInput.focus();
}
