from sklearn.svm import SVC
import joblib

def train_model():
    X_train, y_train = joblib.load('data/X_train.pkl')

    model = SVC(max_iter=200)
    model.fit(X_train, y_train)
    
    return model

if __name__ == "__main__":
    train_model()
    print("Model training complete.")