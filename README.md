# TDS Solver - LLM-based API

## Overview
TDS Solver is a FastAPI-based application designed to automatically answer graded assignment questions for IIT Madras' Online Degree in Data Science. It accepts questions via a POST request with optional file attachments and returns a JSON response containing the answer.

## Features
- Accepts questions via HTTP POST requests
- Supports optional file attachments (ZIP containing CSV)
- Utilizes the Llama-3.2-1B-Instruct model for inference
- Returns structured JSON responses

## Installation & Setup

### Prerequisites
Ensure you have the following installed:
- Python 3.12+
- pip (Python package manager)
- Git
- FastAPI
- Uvicorn
- Git LFS (for handling large files)

### Clone the Repository
```sh
git clone https://github.com/optimusprime009/Project-2---TDS-Solver.git
cd Project-2---TDS-Solver
```

### Setup Virtual Environment
```sh
python -m venv venv
source venv/bin/activate   # On Linux/macOS
venv\Scripts\activate      # On Windows
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Configure Git LFS for Large Files
```sh
git lfs install
git lfs track "*.llamafile"
git add .gitattributes
```

## Running the API Server
```sh
uvicorn main:app --host 0.0.0.0 --port 8000
```

## API Usage
### Endpoint: `POST /`
#### Request Parameters:
- `question` (string, required): The question to be answered
- `file` (optional, ZIP file containing a CSV)

#### Example Request Using `curl`:
```sh
curl -X POST "http://127.0.0.1:8000/" -F "question=What is machine learning?"
```

#### Example Response:
```json
{
  "answer": "Machine learning is a branch of artificial intelligence that allows computers to learn from data."
}
```

## Handling Large Models
If the `Llama-3.2-1B-Instruct.Q6_K.llamafile` file is too large for GitHub, consider storing it externally (Google Drive, AWS S3) and updating the README with download instructions.

## Deployment
To deploy the API publicly, consider using services like:
- AWS EC2 / Lambda
- Google Cloud Run
- Railway.app
- Render.com

## Contributing
Feel free to submit issues or pull requests to enhance functionality!

## License
MIT License. See `LICENSE` for details.

