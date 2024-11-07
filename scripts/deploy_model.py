import joblib
from train_model import train_model

def deploy_model():
    model = train_model()
    joblib.dump(model, 'models/SVC_model.pkl')

if __name__ == "__main__":
    deploy_model()
    print("Model is successfully deployed.")