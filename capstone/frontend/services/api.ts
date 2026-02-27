export async function sendQuery(mode: string, query: string) {
  const response = await fetch("http://localhost:8000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ mode, query }),
  });

  return response.json();
}