---

## **🎯 MVP Plan: Interactive Language Learning Tool**
### **1. Project Overview**
- **Goal**: Build a **simple, fun, and engaging** GTK+ activity to help children (ages 6-12) learn a new language.
- **Languages Supported (MVP)**: **English, Spanish, French**
- **Key Focus**: **Basic vocabulary, pronunciation, and simple sentences**
- **Offline Support**: No external database or online dependencies.

---

## **2. Features (MVP Scope)**
### **A. Basic Vocabulary & Flashcards**
✅ Show **images + word labels**  
✅ Play **audio pronunciation** (using `espeak` or `flite`)  
✅ Simple **drag-and-drop** word matching  

### **B. Simple Sentence Building**
✅ Jumbled words – Kids arrange words to form **correct sentences**  
✅ Basic **fill-in-the-blank** exercises  

### **C. Mini-Games**
✅ **Memory Game** – Match words with their images  
✅ **Word Search** – Find words from a small grid  

### **D. No Database, Only Hardcoded Data**
✅ Use **JSON files or Python lists** to store words and images instead of a database.

---

## **3. Tech Stack**
- **GUI Framework**: **GTK+ (PyGObject)**
- **TTS (Text-to-Speech)**: `espeak`, `flite`
- **Audio Playback**: `pygame.mixer`
- **Data Storage**: Simple **Python dictionaries** (instead of SQLite)

---

## **4. Development Roadmap**
### **1: Basic UI & Flashcards**
✅ Set up GTK+ window & navigation  
✅ Implement **flashcard system** (word + image + pronunciation)  

### **2: Sentence Building & Mini-Games**
✅ Develop **sentence construction (drag-and-drop)**  
✅ Add **basic mini-games (memory game, word search)**  

### **3: Testing & Packaging**
✅ Polish UI & animations  
✅ Package as **XO bundle** for Sugar Labs  

---

## **5. Next Steps**
1️⃣ **Set up GTK+ project structure**  
2️⃣ **Create Flashcard UI prototype**  
3️⃣ **Test basic TTS integration**  
