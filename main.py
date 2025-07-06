import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageDraw, ImageTk
import random
import os
import json
from datetime import datetime

class FaceCrafter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("FaceCrafter - Emoji Mood Generator")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # Create directories for saving
        self.collections_dir = "emoji_collections"
        if not os.path.exists(self.collections_dir):
            os.makedirs(self.collections_dir)
        
        # Mood configurations
        self.moods = {
            "Happy": {
                "face_color": "#FFD700",
                "eye_type": "normal",
                "mouth_type": "smile",
                "cheek_color": "#FFB6C1",
                "eyebrow_type": "raised"
            },
            "Sad": {
                "face_color": "#87CEEB",
                "eye_type": "droopy",
                "mouth_type": "frown",
                "cheek_color": None,
                "eyebrow_type": "down"
            },
            "Angry": {
                "face_color": "#FF6B6B",
                "eye_type": "angry",
                "mouth_type": "angry",
                "cheek_color": "#FF4444",
                "eyebrow_type": "angry"
            },
            "Excited": {
                "face_color": "#FFD700",
                "eye_type": "wide",
                "mouth_type": "big_smile",
                "cheek_color": "#FF69B4",
                "eyebrow_type": "raised"
            },
            "Sleepy": {
                "face_color": "#DDA0DD",
                "eye_type": "sleepy",
                "mouth_type": "small",
                "cheek_color": None,
                "eyebrow_type": "relaxed"
            },
            "Surprised": {
                "face_color": "#FFE4B5",
                "eye_type": "wide",
                "mouth_type": "surprised",
                "cheek_color": "#FFB6C1",
                "eyebrow_type": "raised"
            },
            "Cool": {
                "face_color": "#40E0D0",
                "eye_type": "sunglasses",
                "mouth_type": "smirk",
                "cheek_color": None,
                "eyebrow_type": "normal"
            },
            "Confused": {
                "face_color": "#F0E68C",
                "eye_type": "confused",
                "mouth_type": "confused",
                "cheek_color": None,
                "eyebrow_type": "confused"
            }
        }
        
        self.current_emoji = None
        self.collection = self.load_collection()
        
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="🎨 FaceCrafter", 
            font=("Arial", 24, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        title_label.pack(pady=20)
        
        subtitle_label = tk.Label(
            self.root,
            text="Generate custom emoji faces based on your mood!",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#666"
        )
        subtitle_label.pack(pady=(0, 20))
        
        # Main frame
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Left panel - Controls
        left_panel = tk.Frame(main_frame, bg="#ffffff", relief="raised", bd=2)
        left_panel.pack(side="left", fill="y", padx=(0, 10))
        
        # Mood selection
        mood_label = tk.Label(
            left_panel,
            text="How are you feeling?",
            font=("Arial", 14, "bold"),
            bg="#ffffff"
        )
        mood_label.pack(pady=20)
        
        self.mood_var = tk.StringVar(value="Happy")
        
        for mood in self.moods.keys():
            mood_btn = tk.Radiobutton(
                left_panel,
                text=f"{self.get_mood_emoji(mood)} {mood}",
                variable=self.mood_var,
                value=mood,
                font=("Arial", 12),
                bg="#ffffff",
                command=self.generate_emoji
            )
            mood_btn.pack(anchor="w", padx=20, pady=5)
        
        # Generate button
        generate_btn = tk.Button(
            left_panel,
            text="🎲 Generate New Face",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            command=self.generate_emoji,
            relief="raised",
            bd=3
        )
        generate_btn.pack(pady=20, padx=20, fill="x")
        
        # Save button
        save_btn = tk.Button(
            left_panel,
            text="💾 Save to Collection",
            font=("Arial", 12, "bold"),
            bg="#2196F3",
            fg="white",
            command=self.save_emoji,
            relief="raised",
            bd=3
        )
        save_btn.pack(pady=10, padx=20, fill="x")
        
        # Collection button
        collection_btn = tk.Button(
            left_panel,
            text="📁 View Collection",
            font=("Arial", 12, "bold"),
            bg="#FF9800",
            fg="white",
            command=self.show_collection,
            relief="raised",
            bd=3
        )
        collection_btn.pack(pady=10, padx=20, fill="x")
        
        # Export button
        export_btn = tk.Button(
            left_panel,
            text="📤 Export as PNG",
            font=("Arial", 12, "bold"),
            bg="#9C27B0",
            fg="white",
            command=self.export_emoji,
            relief="raised",
            bd=3
        )
        export_btn.pack(pady=10, padx=20, fill="x")
        
        # Right panel - Emoji display
        right_panel = tk.Frame(main_frame, bg="#ffffff", relief="raised", bd=2)
        right_panel.pack(side="right", expand=True, fill="both")
        
        # Emoji canvas
        self.canvas = tk.Canvas(
            right_panel,
            width=400,
            height=400,
            bg="#ffffff"
        )
        self.canvas.pack(expand=True, pady=20)
        
        # Stats
        stats_frame = tk.Frame(right_panel, bg="#ffffff")
        stats_frame.pack(pady=10)
        
        self.stats_label = tk.Label(
            stats_frame,
            text=f"Collection: {len(self.collection)} emojis",
            font=("Arial", 10),
            bg="#ffffff",
            fg="#666"
        )
        self.stats_label.pack()
        
        # Generate initial emoji
        self.generate_emoji()
    
    def get_mood_emoji(self, mood):
        mood_emojis = {
            "Happy": "😊",
            "Sad": "😢",
            "Angry": "😠",
            "Excited": "🤩",
            "Sleepy": "😴",
            "Surprised": "😲",
            "Cool": "😎",
            "Confused": "😕"
        }
        return mood_emojis.get(mood, "😐")
    
    def generate_emoji(self):
        mood = self.mood_var.get()
        config = self.moods[mood]
        
        # Create image
        size = 300
        image = Image.new("RGBA", (size, size), (255, 255, 255, 0))
        draw = ImageDraw.Draw(image)
        
        # Face
        face_color = config["face_color"]
        face_margin = 30
        draw.ellipse(
            [face_margin, face_margin, size - face_margin, size - face_margin],
            fill=face_color,
            outline="#333",
            width=3
        )
        
        # Eyes
        self.draw_eyes(draw, size, config["eye_type"])
        
        # Eyebrows
        self.draw_eyebrows(draw, size, config["eyebrow_type"])
        
        # Mouth
        self.draw_mouth(draw, size, config["mouth_type"])
        
        # Cheeks
        if config["cheek_color"]:
            self.draw_cheeks(draw, size, config["cheek_color"])
        
        # Add some randomness
        self.add_random_features(draw, size, mood)
        
        # Convert to PhotoImage and display
        self.current_emoji = image
        photo = ImageTk.PhotoImage(image)
        
        self.canvas.delete("all")
        self.canvas.create_image(200, 200, image=photo)
        self.canvas.image = photo  # Keep a reference
    
    def draw_eyes(self, draw, size, eye_type):
        eye_y = size // 3
        left_eye_x = size // 3
        right_eye_x = 2 * size // 3
        
        if eye_type == "normal":
            # Normal circular eyes
            eye_size = 25
            draw.ellipse([left_eye_x - eye_size, eye_y - eye_size, 
                         left_eye_x + eye_size, eye_y + eye_size], fill="white", outline="black", width=2)
            draw.ellipse([right_eye_x - eye_size, eye_y - eye_size, 
                         right_eye_x + eye_size, eye_y + eye_size], fill="white", outline="black", width=2)
            # Pupils
            pupil_size = 10
            draw.ellipse([left_eye_x - pupil_size, eye_y - pupil_size, 
                         left_eye_x + pupil_size, eye_y + pupil_size], fill="black")
            draw.ellipse([right_eye_x - pupil_size, eye_y - pupil_size, 
                         right_eye_x + pupil_size, eye_y + pupil_size], fill="black")
        
        elif eye_type == "droopy":
            # Droopy eyes
            draw.arc([left_eye_x - 20, eye_y - 10, left_eye_x + 20, eye_y + 20], 
                    start=0, end=180, fill="black", width=3)
            draw.arc([right_eye_x - 20, eye_y - 10, right_eye_x + 20, eye_y + 20], 
                    start=0, end=180, fill="black", width=3)
        
        elif eye_type == "angry":
            # Angry slanted eyes
            draw.polygon([left_eye_x - 25, eye_y - 5, left_eye_x + 15, eye_y - 15,
                         left_eye_x + 25, eye_y + 5, left_eye_x - 15, eye_y + 15], 
                        fill="white", outline="black", width=2)
            draw.polygon([right_eye_x - 25, eye_y - 15, right_eye_x + 15, eye_y - 5,
                         right_eye_x + 25, eye_y + 15, right_eye_x - 15, eye_y + 5], 
                        fill="white", outline="black", width=2)
        
        elif eye_type == "wide":
            # Wide surprised eyes
            eye_size = 30
            draw.ellipse([left_eye_x - eye_size, eye_y - eye_size, 
                         left_eye_x + eye_size, eye_y + eye_size], fill="white", outline="black", width=3)
            draw.ellipse([right_eye_x - eye_size, eye_y - eye_size, 
                         right_eye_x + eye_size, eye_y + eye_size], fill="white", outline="black", width=3)
            # Large pupils
            pupil_size = 15
            draw.ellipse([left_eye_x - pupil_size, eye_y - pupil_size, 
                         left_eye_x + pupil_size, eye_y + pupil_size], fill="black")
            draw.ellipse([right_eye_x - pupil_size, eye_y - pupil_size, 
                         right_eye_x + pupil_size, eye_y + pupil_size], fill="black")
        
        elif eye_type == "sleepy":
            # Sleepy half-closed eyes
            draw.arc([left_eye_x - 20, eye_y - 5, left_eye_x + 20, eye_y + 15], 
                    start=180, end=360, fill="black", width=3)
            draw.arc([right_eye_x - 20, eye_y - 5, right_eye_x + 20, eye_y + 15], 
                    start=180, end=360, fill="black", width=3)
        
        elif eye_type == "sunglasses":
            # Cool sunglasses
            draw.ellipse([left_eye_x - 30, eye_y - 20, left_eye_x + 30, eye_y + 20], 
                        fill="black", outline="black")
            draw.ellipse([right_eye_x - 30, eye_y - 20, right_eye_x + 30, eye_y + 20], 
                        fill="black", outline="black")
            # Bridge
            draw.line([left_eye_x + 30, eye_y, right_eye_x - 30, eye_y], fill="black", width=5)
        
        elif eye_type == "confused":
            # One eye normal, one squinted
            eye_size = 25
            draw.ellipse([left_eye_x - eye_size, eye_y - eye_size, 
                         left_eye_x + eye_size, eye_y + eye_size], fill="white", outline="black", width=2)
            draw.ellipse([left_eye_x - 10, eye_y - 10, left_eye_x + 10, eye_y + 10], fill="black")
            # Squinted right eye
            draw.arc([right_eye_x - 20, eye_y - 5, right_eye_x + 20, eye_y + 15], 
                    start=180, end=360, fill="black", width=3)
    
    def draw_eyebrows(self, draw, size, eyebrow_type):
        eyebrow_y = size // 4
        left_brow_x = size // 3
        right_brow_x = 2 * size // 3
        
        if eyebrow_type == "raised":
            # Raised eyebrows
            draw.arc([left_brow_x - 25, eyebrow_y - 15, left_brow_x + 25, eyebrow_y + 5], 
                    start=180, end=360, fill="black", width=4)
            draw.arc([right_brow_x - 25, eyebrow_y - 15, right_brow_x + 25, eyebrow_y + 5], 
                    start=180, end=360, fill="black", width=4)
        
        elif eyebrow_type == "down":
            # Sad down eyebrows
            draw.line([left_brow_x - 20, eyebrow_y - 5, left_brow_x + 20, eyebrow_y + 5], 
                     fill="black", width=4)
            draw.line([right_brow_x - 20, eyebrow_y + 5, right_brow_x + 20, eyebrow_y - 5], 
                     fill="black", width=4)
        
        elif eyebrow_type == "angry":
            # Angry angled eyebrows
            draw.line([left_brow_x - 20, eyebrow_y + 5, left_brow_x + 20, eyebrow_y - 10], 
                     fill="black", width=5)
            draw.line([right_brow_x - 20, eyebrow_y - 10, right_brow_x + 20, eyebrow_y + 5], 
                     fill="black", width=5)
        
        elif eyebrow_type == "confused":
            # One raised, one normal
            draw.arc([left_brow_x - 25, eyebrow_y - 15, left_brow_x + 25, eyebrow_y + 5], 
                    start=180, end=360, fill="black", width=4)
            draw.line([right_brow_x - 20, eyebrow_y, right_brow_x + 20, eyebrow_y], 
                     fill="black", width=4)
    
    def draw_mouth(self, draw, size, mouth_type):
        mouth_y = 2 * size // 3
        mouth_x = size // 2
        
        if mouth_type == "smile":
            # Happy smile
            draw.arc([mouth_x - 40, mouth_y - 20, mouth_x + 40, mouth_y + 20], 
                    start=0, end=180, fill="black", width=4)
        
        elif mouth_type == "big_smile":
            # Big excited smile
            draw.arc([mouth_x - 50, mouth_y - 25, mouth_x + 50, mouth_y + 25], 
                    start=0, end=180, fill="black", width=5)
            # Teeth
            for i in range(-3, 4):
                draw.rectangle([mouth_x + i * 8 - 3, mouth_y - 5, mouth_x + i * 8 + 3, mouth_y + 5], 
                              fill="white", outline="black")
        
        elif mouth_type == "frown":
            # Sad frown
            draw.arc([mouth_x - 30, mouth_y - 10, mouth_x + 30, mouth_y + 30], 
                    start=180, end=360, fill="black", width=4)
        
        elif mouth_type == "angry":
            # Angry gritted teeth
            draw.line([mouth_x - 25, mouth_y, mouth_x + 25, mouth_y], fill="black", width=5)
            for i in range(-2, 3):
                draw.line([mouth_x + i * 8, mouth_y - 5, mouth_x + i * 8, mouth_y + 5], 
                         fill="black", width=2)
        
        elif mouth_type == "surprised":
            # Surprised O mouth
            draw.ellipse([mouth_x - 15, mouth_y - 15, mouth_x + 15, mouth_y + 15], 
                        fill="black", outline="black")
        
        elif mouth_type == "small":
            # Small sleepy mouth
            draw.ellipse([mouth_x - 8, mouth_y - 5, mouth_x + 8, mouth_y + 5], 
                        fill="black", outline="black")
        
        elif mouth_type == "smirk":
            # Cool smirk
            draw.arc([mouth_x - 20, mouth_y - 10, mouth_x + 40, mouth_y + 10], 
                    start=0, end=90, fill="black", width=4)
        
        elif mouth_type == "confused":
            # Wavy confused mouth
            points = []
            for i in range(-20, 21, 5):
                y_offset = 5 * (1 if (i // 5) % 2 == 0 else -1)
                points.extend([mouth_x + i, mouth_y + y_offset])
            if len(points) >= 4:
                draw.line(points, fill="black", width=3)
    
    def draw_cheeks(self, draw, size, cheek_color):
        cheek_y = size // 2
        left_cheek_x = size // 4
        right_cheek_x = 3 * size // 4
        
        # Blush circles
        draw.ellipse([left_cheek_x - 15, cheek_y - 10, left_cheek_x + 15, cheek_y + 10], 
                    fill=cheek_color)
        draw.ellipse([right_cheek_x - 15, cheek_y - 10, right_cheek_x + 15, cheek_y + 10], 
                    fill=cheek_color)
    
    def add_random_features(self, draw, size, mood):
        # Add some random sparkles or effects based on mood
        if mood == "Excited":
            # Add sparkles
            for _ in range(random.randint(3, 6)):
                x = random.randint(50, size - 50)
                y = random.randint(50, size - 50)
                sparkle_size = random.randint(3, 8)
                draw.line([x - sparkle_size, y, x + sparkle_size, y], fill="yellow", width=2)
                draw.line([x, y - sparkle_size, x, y + sparkle_size], fill="yellow", width=2)
        
        elif mood == "Sleepy":
            # Add Z's
            for i in range(2):
                x = size - 80 + i * 20
                y = 60 + i * 15
                draw.text((x, y), "Z", fill="gray")
    
    def save_emoji(self):
        if self.current_emoji:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            mood = self.mood_var.get()
            
            emoji_data = {
                "timestamp": timestamp,
                "mood": mood,
                "filename": f"emoji_{mood}_{timestamp}.png"
            }
            
            # Save image
            filepath = os.path.join(self.collections_dir, emoji_data["filename"])
            self.current_emoji.save(filepath, "PNG")
            
            # Add to collection
            self.collection.append(emoji_data)
            self.save_collection()
            
            # Update stats
            self.stats_label.config(text=f"Collection: {len(self.collection)} emojis")
            
            messagebox.showinfo("Saved!", f"Emoji saved to collection as {emoji_data['filename']}")
    
    def export_emoji(self):
        if self.current_emoji:
            filename = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
                title="Export Emoji"
            )
            if filename:
                self.current_emoji.save(filename, "PNG")
                messagebox.showinfo("Exported!", f"Emoji exported to {filename}")
    
    def show_collection(self):
        if not self.collection:
            messagebox.showinfo("Empty Collection", "No emojis in collection yet!")
            return
        
        # Create collection window
        collection_window = tk.Toplevel(self.root)
        collection_window.title("Emoji Collection")
        collection_window.geometry("600x400")
        
        # Create scrollable frame
        canvas = tk.Canvas(collection_window)
        scrollbar = ttk.Scrollbar(collection_window, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Display emojis
        for i, emoji_data in enumerate(reversed(self.collection)):  # Show newest first
            frame = tk.Frame(scrollable_frame, relief="raised", bd=2, bg="white")
            frame.pack(fill="x", padx=10, pady=5)
            
            # Load and display emoji
            try:
                filepath = os.path.join(self.collections_dir, emoji_data["filename"])
                if os.path.exists(filepath):
                    img = Image.open(filepath)
                    img.thumbnail((80, 80))
                    photo = ImageTk.PhotoImage(img)
                    
                    img_label = tk.Label(frame, image=photo, bg="white")
                    img_label.image = photo  # Keep reference
                    img_label.pack(side="left", padx=10, pady=10)
                    
                    # Info
                    info_frame = tk.Frame(frame, bg="white")
                    info_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)
                    
                    tk.Label(info_frame, text=f"Mood: {emoji_data['mood']}", 
                            font=("Arial", 12, "bold"), bg="white").pack(anchor="w")
                    tk.Label(info_frame, text=f"Created: {emoji_data['timestamp']}", 
                            font=("Arial", 10), bg="white", fg="gray").pack(anchor="w")
            except Exception as e:
                print(f"Error loading emoji: {e}")
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def load_collection(self):
        try:
            with open(os.path.join(self.collections_dir, "collection.json"), "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def save_collection(self):
        with open(os.path.join(self.collections_dir, "collection.json"), "w") as f:
            json.dump(self.collection, f, indent=2)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = FaceCrafter()
    app.run()
