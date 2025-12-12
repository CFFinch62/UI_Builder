# MD UI Builder

**Design your UI visually. Let AI build it.**

---

## What It Does

MD UI Builder is a visual drag-and-drop interface designer that exports your layouts as clean, structured Markdown. Hand that Markdown to any AI agent—Claude, ChatGPT, Copilot—and watch it generate working code in PyQt, CustomTkinter, HTML/CSS, or any framework you choose.

## The Problem It Solves

Describing a UI layout in words is frustrating. You say "put the login button below the password field, aligned right" and the AI gives you something... close. Then you iterate. And iterate. And iterate.

MD UI Builder eliminates the guesswork. Instead of describing what you want, you *show* it. The AI gets a precise, hierarchical specification it can actually interpret—no more "that's not quite what I meant."

## Key Features

- **Visual Drag-and-Drop** — Build layouts by clicking and placing, not coding
- **Container-Based Design** — Nest horizontal and vertical containers for any layout pattern
- **Rich Element Library** — Buttons, labels, text inputs, dropdowns, checkboxes, sliders, and more
- **Markdown Export** — Clean, human-readable output that AI agents understand perfectly
- **Framework-Agnostic** — One design works for PyQt, CustomTkinter, HTML/CSS, React, and beyond
- **No Lock-In** — Markdown files are plain text you can edit, version control, and share
- **Live Editing** — See your layout take shape in real-time

## Who It's For

- **Developers** who use AI assistants to speed up UI implementation
- **Designers** who want to communicate layouts precisely to developers or AI
- **Students** learning UI development who want to understand structure before code
- **Anyone** tired of the back-and-forth of describing layouts to AI agents

## Platform Support

- Windows
- Linux
- macOS

## Getting Started

1. Run `python main.py` to launch the builder
2. Add containers (vertical/horizontal) to structure your layout
3. Drag UI elements from the palette into your containers
4. Set properties like text, size, and position
5. Click "Export to Markdown" and share with your AI agent

**Example prompt for your AI:**
> "Implement this UI in PyQt6. Here's the layout specification: [paste markdown]"

## Technology

Built with Python and CustomTkinter. Outputs plain Markdown—no proprietary formats, no cloud dependencies, no subscriptions.

---

**Fragillidae Software** — Old School meets New School
