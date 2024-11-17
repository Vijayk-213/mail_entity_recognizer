import spacy

# Load a pretrained spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to extract entities from text
def extract_entities(text):
    # Process the text using the pretrained model
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Sample email text for testing
f = open("sample_text.txt", "r")
sample_text =f.read()

# Extract entities from the sample text
entities = extract_entities(sample_text)

# Print the extracted entities
print("Extracted Entities:")
for entity in entities:
    print(f"Text: {entity[0]}, Label: {entity[1]}")
