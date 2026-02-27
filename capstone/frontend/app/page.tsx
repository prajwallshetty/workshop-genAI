"use client"

import { useState } from "react"
import { sendQuery } from "@/services/api"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Card } from "@/components/ui/card"
import { ScrollArea } from "@/components/ui/scroll-area"
import { Separator } from "@/components/ui/separator"

const modes = [
  { id: "academic", label: "🎓 Academic" },
  { id: "placement", label: "💼 Placement" },
  { id: "research", label: "📄 Research" },
  { id: "debug", label: "💻 Debug" },
  { id: "startup", label: "🚀 Startup" },
]

export default function Home() {
  const [mode, setMode] = useState("academic")
  const [query, setQuery] = useState("")
  const [messages, setMessages] = useState<any[]>([])
  const [loading, setLoading] = useState(false)

  const handleSubmit = async () => {
    if (!query) return

    const newMessages = [
      ...messages,
      { role: "user", content: query },
    ]

    setMessages(newMessages)
    setQuery("")
    setLoading(true)

    const data = await sendQuery(mode, query)

    setMessages([
      ...newMessages,
      { role: "assistant", content: data.response },
    ])

    setLoading(false)
  }

  return (
    <div className="flex h-screen bg-muted/40">

      {/* Sidebar */}
      <div className="w-64 border-r bg-background p-6">
        <h1 className="text-xl font-semibold mb-6">CampusAI</h1>

        <div className="space-y-2">
          {modes.map((m) => (
            <Button
              key={m.id}
              variant={mode === m.id ? "default" : "ghost"}
              className="w-full justify-start"
              onClick={() => setMode(m.id)}
            >
              {m.label}
            </Button>
          ))}
        </div>
      </div>

      {/* Chat Section */}
      <div className="flex flex-col flex-1">

        {/* Header */}
        <div className="p-4">
          <h2 className="text-lg font-medium capitalize">
            {mode} Assistant
          </h2>
          <Separator className="mt-4" />
        </div>

        {/* Messages */}
        <ScrollArea className="flex-1 px-6">
          <div className="space-y-4 py-4">
            {messages.map((msg, index) => (
              <div
                key={index}
                className={`flex ${
                  msg.role === "user" ? "justify-end" : "justify-start"
                }`}
              >
                <Card
                  className={`px-4 py-3 max-w-xl ${
                    msg.role === "user"
                      ? "bg-primary text-primary-foreground"
                      : "bg-muted"
                  }`}
                >
                  {msg.content}
                </Card>
              </div>
            ))}

            {loading && (
              <Card className="px-4 py-3 w-fit bg-muted">
                Thinking...
              </Card>
            )}
          </div>
        </ScrollArea>

        {/* Input */}
        <div className="p-4 border-t bg-background">
          <div className="flex gap-3">
            <Input
              placeholder="Ask something..."
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && handleSubmit()}
            />

            <Button onClick={handleSubmit}>
              Send
            </Button>
          </div>
        </div>

      </div>
    </div>
  )
}