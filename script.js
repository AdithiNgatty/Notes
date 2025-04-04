const apiURL = "http://localhost:8000/notes";

async function fetchNotes() {
    const response = await fetch(apiURL);
    const notes = await response.json();
    const notesList = document.getElementById("notesList");
    notesList.innerHTML = notes.map(note => `<li>${note.text}</li>`).join("");
}

async function addNote() {
    const text = document.getElementById("noteInput").value;
    await fetch(apiURL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
    });
    document.getElementById("noteInput").value = "";
    fetchNotes();
}

async function clearNotes() {
    await fetch("http://localhost:8000/notes", {
        method: "DELETE",
    });
    fetchNotes();  // Refresh the list after deleting
}


fetchNotes();
