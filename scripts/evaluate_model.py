from sklearn.metrics import accuracy_score, classification_report
import joblib
from train_model import train_model

def evaluate_model():
    model = train_model()
    X_test, y_test = joblib.load('data/X_test.pkl')
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"Model accuracy: {accuracy}")
    
    report = classification_report(y_test, y_pred, target_names=['No Disease', 'Disease'])
    print("Model Evaluation Report:")
    print(report)
    
    return accuracy

if __name__ == "__main__":
    evaluate_model()

# from sklearn.metrics import classification_report 
# import joblib 
# from train_model import train_model 
 
# def evaluate_model(): 
#     model = train_model() 
#     X_test, y_test = joblib.load('data/X_test.pkl') 
#     y_pred = model.predict(X_test) 
     
 
#     report = classification_report(y_test, y_pred, 
# target_names=['setosa', 'versicolor', 'virginica']) 
     
#     print("Model Evaluation Report:") 
#     print(report) 
     
 
# if __name__ == "__main__": 
#     evaluate_model() 