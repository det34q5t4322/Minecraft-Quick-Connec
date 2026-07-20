"""
Minecraft Quick Connect - Open Source Launcher
Pure, clean launcher for Minecraft server connections.
"""

import os
import sys
import tkinter as tk
from tkinter import ttk


class MinecraftLauncherUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Minecraft Quick Connect")
        self.root.geometry("520x300")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e24")

        # Center window
        self.root.update_idletasks()
        w, h = self.root.winfo_width(), self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (w // 2)
        y = (self.root.winfo_screenheight() // 2) - (h // 2)
        self.root.geometry(f"{w}x{h}+{x}+{y}")

        # Styles
        style = ttk.Style()
        style.theme_use("clam")

        title = tk.Label(root, text="MINECRAFT QUICK CONNECT", font=("Segoe UI", 16, "bold"), fg="#00e676", bg="#1e1e24")
        title.pack(pady=(25, 5))

        subtitle = tk.Label(root, text="Быстрый запуск и подключение к серверу", font=("Segoe UI", 9.5), fg="#a0a0b0", bg="#1e1e24")
        subtitle.pack(pady=(0, 20))

        # Status & Launch Button
        self.status = tk.Label(root, text="Готово к подключению", font=("Segoe UI", 10), fg="#ffffff", bg="#1e1e24")
        self.status.pack(pady=(10, 15))

        btn_launch = tk.Button(
            root,
            text="ИГРАТЬ ПО СЕТИ",
            font=("Segoe UI", 11, "bold"),
            fg="#ffffff",
            bg="#00c853",
            activebackground="#00e676",
            activeforeground="#ffffff",
            bd=0,
            padx=25,
            pady=10,
            cursor="hand2",
            command=self.on_play_click
        )
        btn_launch.pack(pady=10)

    def on_play_click(self):
        self.status.config(text="Запуск игры Minecraft...", fg="#00e676")


def main():
    root = tk.Tk()
    app = MinecraftLauncherUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
