# Mail Entity Recognizer

This project is a **Named Entity Recognition (NER)** application that uses a **pretrained spaCy model** to extract entities like names, organizations, dates, and other important information from email content. It leverages the `en_core_web_sm` model, which is optimized for general-purpose English text analysis.

## 📋 Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Example Output](#example-output)
- [Dependencies](#dependencies)
- [Project Structure](#project-structure)


## 📌 Introduction

Named Entity Recognition (NER) is a key task in Natural Language Processing (NLP) where specific entities like names, organizations, dates, and locations are extracted from a given text. This project focuses on extracting such entities from email text using a pretrained spaCy model.

## ✨ Features

- Utilizes spaCy's pretrained **`en_core_web_sm`** model for NER.
- Recognizes entities like:
  - **PERSON** (People's Names)
  - **ORG** (Organizations)
  - **DATE** (Dates)
  - **MONEY** (Monetary Values)
  - **EMAIL** (Email Addresses)
  - **GPE** (Geopolitical Entities like cities and countries)
- Simple and easy-to-use Python script.

## 📝 Example Output

Extracted Entities:
- Text: John, Label: PERSON
- Text: Jane, Label: PERSON
- Text: Microsoft, Label: ORG
- Text: next Wednesday, Label: DATE
- Text: Tesla, Label: ORG
- Text: December 5th, Label: DATE
- Text: Michael, Label: PERSON

## ⚙️ Setup

### Prerequisites

- Python 3.8+
- Virtual Environment (recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/mail_entity_recognizer.git
cd mail_entity_recognizer
