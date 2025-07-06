# 🎨 FaceCrafter - Emoji Mood Generator

A fun and creative Python GUI application that generates custom emoji faces based on your current mood. Choose how you're feeling, and FaceCrafter draws a unique emoji for you — which you can save and collect!

![FaceCrafter Demo](demo/facecrafter_demo.gif)
*Generate custom emojis based on your mood!*

## ✨ Features

### 🎭 Mood-Based Generation
- **8 Different Moods**: Happy, Sad, Angry, Excited, Sleepy, Surprised, Cool, Confused
- Each mood features unique facial expressions, colors, and characteristics
- Randomized elements ensure variety in every generation

### 🎨 Advanced Emoji Creation
- **Custom Drawing Engine**: Built with PIL for detailed, high-quality emoji faces
- **Dynamic Features**: Customizable eyes, eyebrows, mouths, cheeks, and special effects
- **Mood-Specific Elements**: 
  - 😎 Sunglasses for "Cool" mood
  - ✨ Sparkles for "Excited" mood
  - 💤 Z's floating for "Sleepy" mood
  - And much more!

### 📁 Collection System
- **Save & Organize**: Build your personal emoji collection
- **Gallery View**: Browse all saved emojis with timestamps and mood information
- **Persistent Storage**: Automatic saving with JSON database and PNG files

### 💾 Export Options
- **High-Quality PNG Export**: Save emojis as crisp PNG files
- **Custom File Naming**: Automatic timestamped filenames
- **Flexible Saving**: Choose your preferred save location

### 🖥️ User-Friendly Interface
- **Clean Modern GUI**: Intuitive tkinter-based interface
- **Real-Time Preview**: Instant emoji generation and display
- **Collection Statistics**: Track your growing emoji collection
- **Responsive Design**: Scrollable collection viewer for large collections

## 📸 Screenshots

| Main Interface | Mood Selection | Collection View |
|----------------|----------------|-----------------|
| ![Main](screenshots/main_interface.png) | ![Moods](screenshots/mood_selection.png) | ![Collection](screenshots/collection_view.png) |

## 🚀 Quick Start

### Prerequisites

Make sure you have Python 3.7+ installed on your system.

### Installation

1. **Clone the repository**
   \`\`\`bash
   git clone https://github.com/yourusername/facecrafter.git
   cd facecrafter
   \`\`\`

2. **Install required dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. **Run FaceCrafter**
   \`\`\`bash
   python facecrafter.py
   \`\`\`

## 📋 Requirements

\`\`\`
Pillow>=8.0.0
tkinter (usually included with Python)
\`\`\`

Create a `requirements.txt` file with:
\`\`\`
Pillow>=8.0.0
\`\`\`

## 🎮 How to Use

### Basic Usage

1. **Launch the Application**
   \`\`\`bash
   python facecrafter.py
   \`\`\`

2. **Select Your Mood**
   - Choose from 8 different mood options in the left panel
   - Each mood has a unique emoji indicator

3. **Generate Your Emoji**
   - Click "🎲 Generate New Face" for variations
   - The emoji appears instantly in the preview area

4. **Save to Collection**
   - Click "💾 Save to Collection" to add favorites
   - Emojis are automatically organized with timestamps

5. **Export Your Creation**
   - Use "📤 Export as PNG" to save individual emojis
   - Choose your preferred location and filename

6. **Browse Your Collection**
   - Click "📁 View Collection" to see all saved emojis
   - Scroll through your creations with mood and date info

### Advanced Features

- **Randomization**: Each generation includes random elements for uniqueness
- **Mood Consistency**: All features align with the selected emotional state
- **Auto-Save**: Collection data is automatically preserved between sessions

## 📁 Project Structure

\`\`\`
facecrafter/
├── facecrafter.py          # Main application file
├── README.md               # This file
├── requirements.txt        # Python dependencies
├── emoji_collections/      # Auto-created directory
│   ├── collection.json     # Collection database
│   └── *.png              # Saved emoji files
├── screenshots/           # Demo images
└── demo/                 # Demo GIFs and videos
\`\`\`

## 🎨 Mood Reference

| Mood | Face Color | Special Features |
|------|------------|------------------|
| 😊 **Happy** | Golden Yellow | Smile, rosy cheeks, raised eyebrows |
| 😢 **Sad** | Sky Blue | Frown, droopy eyes, downward eyebrows |
| 😠 **Angry** | Red | Gritted teeth, angry eyes, sharp eyebrows |
| 🤩 **Excited** | Bright Yellow | Wide eyes, big smile, sparkle effects |
| 😴 **Sleepy** | Soft Purple | Half-closed eyes, small mouth, floating Z's |
| 😲 **Surprised** | Peach | Wide eyes, O-shaped mouth, raised eyebrows |
| 😎 **Cool** | Turquoise | Sunglasses, smirk, relaxed expression |
| 😕 **Confused** | Light Yellow | Mixed expressions, wavy mouth, tilted features |

## 🛠️ Development

### Setting Up Development Environment

1. **Fork the repository**
2. **Create a virtual environment**
   \`\`\`bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   \`\`\`
3. **Install dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

### Code Structure

- **Main Class**: `FaceCrafter` - Handles GUI and main application logic
- **Drawing Methods**: Individual methods for each facial feature
- **Mood Configuration**: Dictionary-based mood definitions
- **Collection Management**: JSON-based storage system

### Adding New Moods

To add a new mood:

1. Add mood configuration to `self.moods` dictionary
2. Implement drawing logic for unique features
3. Add mood emoji to `get_mood_emoji()` method
4. Update UI elements as needed

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Ways to Contribute

- 🐛 **Bug Reports**: Found a bug? Open an issue!
- 💡 **Feature Requests**: Have an idea? We'd love to hear it!
- 🎨 **New Moods**: Add more emotional expressions
- 🖼️ **UI Improvements**: Enhance the user interface
- 📚 **Documentation**: Help improve docs and examples

### Contribution Process

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add comments for complex logic
- Test new features thoroughly
- Update documentation as needed

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

\`\`\`
MIT License

Copyright (c) 2024 FaceCrafter

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
\`\`\`

## 🙋‍♂️ Support

### Getting Help

- 📖 **Documentation**: Check this README and code comments
- 🐛 **Issues**: Open an issue on GitHub for bugs
- 💬 **Discussions**: Use GitHub Discussions for questions
- 📧 **Contact**: Reach out via email for other inquiries

### Frequently Asked Questions

**Q: Can I add custom moods?**
A: Yes! The mood system is easily extensible. Check the Development section for details.

**Q: Where are my emojis saved?**
A: Emojis are saved in the `emoji_collections/` directory in PNG format.

**Q: Can I use these emojis commercially?**
A: Yes, under the MIT license you can use generated emojis for any purpose.

**Q: What Python versions are supported?**
A: Python 3.7+ is required due to tkinter and PIL dependencies.

## 🎯 Roadmap

### Upcoming Features

- [ ] **Animation Support**: Animated emoji generation
- [ ] **Custom Colors**: User-defined color palettes
- [ ] **Emoji Sharing**: Direct social media integration
- [ ] **Batch Generation**: Create multiple emojis at once
- [ ] **Advanced Expressions**: More detailed facial features
- [ ] **Theme System**: Dark mode and custom themes
- [ ] **Plugin System**: Extensible mood and feature plugins

### Version History

- **v1.0.0** - Initial release with 8 moods and collection system
- **v1.1.0** - Added export functionality and improved UI
- **v1.2.0** - Enhanced randomization and special effects

## 🌟 Acknowledgments

- **PIL/Pillow**: For excellent image processing capabilities
- **tkinter**: For the GUI framework
- **Python Community**: For inspiration and support
- **Contributors**: Thanks to all who help improve FaceCrafter!

## 📊 Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/facecrafter?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/facecrafter?style=social)
![GitHub issues](https://img.shields.io/github/issues/yourusername/facecrafter)
![GitHub license](https://img.shields.io/github/license/yourusername/facecrafter)
![Python version](https://img.shields.io/badge/python-3.7+-blue.svg)

---

**Made with ❤️ and Python** | **Happy Emoji Crafting!** 🎨✨
