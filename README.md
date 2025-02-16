# Multimodal AI - Image Captioning Project

## 📌 Project Overview
This project uses BLIP (Bootstrapped Language-Image Pretraining) to generate captions for images. 
It combines **Computer Vision (CNNs) and Natural Language Processing (NLP)** to create textual descriptions of images.

## 🛠 Installation & Setup
1. **Clone the repository** (if not already cloned):
   ```sh
   git clone https://github.com/rnaltami/multimodal-ai-descriptions.git
   cd multimodal-ai-descriptions
   ```

2. **Set up a virtual environment** (recommended):
   ```sh
   python3 -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate    # Windows
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## 🚀 How to Run the Script
1. **Ensure you have images inside the `images/` folder.**
2. Run the script:
   ```sh
   python scripts/test_blip.py
   ```
3. **Follow the prompts** to enter the image filename.
4. The script will generate and print a caption for the image.

## 🔍 Example Output
```
📝 Generated Caption: "a grassy hillside with trees and bushes"
```

## 🔧 Future Improvements
- ✅ Add a **web interface** using Flask or Gradio.
- ✅ Experiment with **fine-tuning BLIP on custom datasets**.
- ✅ Extend to **multi-image captioning**.

---
Created by **rnaltami** - 2025 🚀

