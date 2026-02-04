# Contributing to ScriptSavant 🚀

First off, thank you for considering contributing to ScriptSavant! It’s people like you that make this a great utility belt for everyone.

Whether you are fixing a bug, adding a new social media downloader, or sharing a Windows system tweak, we welcome your help.

## 📜 Table of Contents
1. [How Can I Contribute?](#how-can-i-contribute)
2. [Folder Structure](#folder-structure)
3. [Script Standards](#script-standards)
4. [How to Submit a Pull Request](#how-to-submit-a-pull-request)

---

## 🛠 How Can I Contribute?

### 1. Adding New Scripts
We are looking for scripts in three main categories:
* **Media Tools:** Downloaders/Uploaders for YouTube, Insta, FB, TikTok, etc.
* **Windows Utils:** Debloaters, registry fixes, and automation for Windows.
* **Productivity Hacks:** PDF tools, file organizers, and document automation.

### 2. Improving Existing Scripts
Adding error handling, faster processing, or better CLI interfaces to existing tools.

---

## 📂 Folder Structure

Please place your scripts in the appropriate directory:
* `/media_tools` - Web and social media scripts.
* `/windows_utils` - OS-specific fixes and tools.
* `/productivity_hacks` - Document and file management.

If your script requires specific libraries, add them to the main `requirements.txt` file in the root directory.

---

## 🐍 Script Standards

To keep ScriptSavant clean and easy to use, please follow these rules:
1.  **Language:** All scripts should be written in **Python 3.10+**.
2.  **Comments:** Include a brief description at the top of your script explaining what it does.
3.  **Readability:** Use clear variable names (e.g., `video_url` instead of `v`).
4.  **No Hardcoding:** If a script requires a path or a link, ask for user input via the terminal.
5.  **Clean Exit:** Ensure your script handles errors (like no internet connection) gracefully.

---

## 🚀 How to Submit a Pull Request

1.  **Fork** the repository.
2.  **Clone** your fork to your local machine.
3.  Create a **Branch** for your feature: `git checkout -b feature/NewAwesomeScript`.
4.  **Commit** your changes: `git commit -m 'Add YouTube to MP3 script'`.
5.  **Push** to the branch: `git push origin feature/NewAwesomeScript`.
6.  Open a **Pull Request** and describe what your script does!

---

## ⚖️ License
By contributing, you agree that your contributions will be licensed under the **MIT License**.
