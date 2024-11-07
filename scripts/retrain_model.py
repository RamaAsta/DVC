import joblib
from train_model import train_model
from evaluate_model import evaluate_model

def check_and_retrain():
    accuracy = evaluate_model()
    if accuracy < 0.50:
        print("Accuracy below 50%, retraining model...")
        model = train_model()
        joblib.dump(model, 'models/SVC_model.pkl')
        print("Model retraining complete.")
    else:
        print("Model accuracy is satisfactory.")

if __name__ == "__main__":
    check_and_retrain()
