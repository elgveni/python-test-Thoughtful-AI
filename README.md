# python-test-Thoughtful-AI

## Task
Implement a function to classify packages based on size and weight into:
- `STANDARD`
- `SPECIAL`
- `REJECTED`

## Classification Rules
- **Bulky**: Volume ≥ 1,000,000 cm³ OR any dimension ≥ 150 cm  
- **Heavy**: Mass ≥ 20 kg  
- **REJECTED**: If both bulky and heavy  
- **SPECIAL**: If either bulky or heavy  
- **STANDARD**: If neither

## How to Run
```bash
python3 main.py
