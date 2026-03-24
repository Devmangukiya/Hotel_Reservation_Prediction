# Hotel Reservation Prediction

Predict cancellations for hotel reservations using machine learning. This project provides a complete pipeline and web interface for building, deploying, and serving ML models to predict whether a reservation will be canceled, based on customer and booking features.

## Features

- **End-to-End ML Pipeline**: Automated data ingestion, preprocessing, and model training.
- **Web Application**: Flask-based interface for real-time predictions.
- **Reproducible Environment**: Dockerized for consistent development and deployment.
- **CI/CD Integration**: Jenkins pipeline for automated builds and deployment.
- **Experiment Tracking**: MLflow support for managing experiments.
- **LightGBM & scikit-learn Models**: Modern and efficient ML algorithms.
- **Cloud & Local Support**: Ready to run on-premises or in the cloud (Google Cloud support scripts included).

## Directory Structure

```
.
├── application.py         # Flask app serving the ML model
├── src/                   # Core modules (data ingestion, preprocessing, model training)
├── notebook/              # Jupyter notebook(s) for EDA and prototyping
├── pipeline/              # Pipeline scripts (e.g., training_pipeline.py)
├── config/                # Configuration files and path configs
├── requirements.txt       # Python dependencies
├── Dockerfile             # Container build for app and training
├── Jenkinsfile            # CI/CD build instructions
├── templates/             # HTML files for the Flask app
└── static/                # Static web resources
```

## Installation

**Requirements:**
- Python 3.8+
- [Docker](https://www.docker.com/) (recommended for deployment)
- (Optional) Google Cloud credentials for cloud storage

**Clone the repository:**
```bash
git clone https://github.com/Devmangukiya/Hotel_Reservation_Prediction.git
cd Hotel_Reservation_Prediction
```

**Run with Docker (Recommended):**
Builds the container, installs dependencies, trains the model, and launches the web app on port 8080.

```bash
docker build -t hotel-reservation-prediction .
docker run -p 8080:8080 hotel-reservation-prediction
```

**Manual (Local) Setup:**
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Train the model:
    ```bash
    python pipeline/training_pipeline.py
    ```

3. Start the web application:
    ```bash
    python application.py
    ```
    Then access the app at [http://localhost:8080](http://localhost:8080)

## Usage

- Open the web interface.
- Input required reservation details (lead time, price, booking details, etc.).
- The app predicts if the reservation is likely to be canceled.

## Example Code (Web Inference)
```python
# application.py (snippet)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Parse submitted form data
        features = np.array([[...]])
        prediction = loaded_model.predict(features)
        return render_template('index.html', prediction=prediction[0])
    return render_template('index.html', prediction=None)
```

## Notebooks

- Main experiments and exploratory analysis are inside `notebook/notebook.ipynb`.

## ML Pipeline

Core pipeline code is in `src/`:
- `data_ingestion.py` — Load and split data sets
- `data_preprocessing.py` — Clean and preprocess data (handle missing, encode categoricals)
- `model_training.py` — Train LightGBM/scikit-learn classifiers and save the final model
- `custom_exception.py`, `logger.py` — Logging & error handling utilities

## Configuration

Edit values in `config/` for paths, model saving locations, or environment toggles.

## CI/CD

A `Jenkinsfile` automates building, testing, training, and deployment. Includes cloud environment step scripts and Docker image management for seamless CI on Jenkins.

## Requirements

```text
pandas
numpy
scikit-learn
lightgbm
imbalanced-learn
mlflow
flask
pyyaml
google-cloud-storage
```

## License

See LICENSE file or repository details.

## Authors

Maintained by [Devmangukiya](https://github.com/Devmangukiya/).

---

*For issues, please open a GitHub issue or pull request.*
