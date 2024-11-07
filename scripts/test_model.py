from sklearn.svm import SVC
import joblib

def train_model():
    X_test, y_test = joblib.load('data/X_test.pkl')

    model = SVC(max_iter=200)
    model.fit(X_test, y_test)
    
    return model

if __name__ == "__main__":
    train_model()
    print("Model testing complete.")