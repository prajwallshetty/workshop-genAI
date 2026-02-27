# 🎨 CampusAI Frontend

Modern AI chat interface built with Next.js 16, Tailwind CSS, and shadcn/ui.

---

## 🛠 Tech Stack

- Next.js 16 (App Router)
- TypeScript
- Tailwind CSS
- shadcn/ui
- Fetch API

---

## 📁 Project Structure

frontend/
│── app/  
│── components/  
│── services/  
│── public/  

---

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies

```bash
npm install
```

---

### 2️⃣ Run Development Server

```bash
npm run dev
```

App runs at:

```
http://localhost:3000
```

---

## 🔗 Backend Connection

Make sure backend is running at:

```
http://127.0.0.1:8000
```

Inside `services/api.ts`:

```ts
export async function sendQuery(mode: string, query: string) {
  const res = await fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      mode,
      query,
    }),
  });

  return res.json();
}
```

---

## 💬 Features

- Multiple AI Modes (Academic, Placement, Research, Debug, Startup)
- Chat interface with shadcn UI components
- Loading indicator
- Responsive layout
- Clean modern design

---

## 🎨 UI Components Used

Installed via:

```bash
npx shadcn@latest add button input card separator scroll-area
```

Components:
- Button
- Input
- Card
- Separator
- ScrollArea

---

## 🚀 Future Improvements

- Dark/Light theme toggle
- Streaming AI responses
- Authentication
- Chat history persistence
- Deployment (Vercel + Render)

---

## 👨‍💻 Project

CampusAI Capstone Frontend