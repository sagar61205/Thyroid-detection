from flask import Flask, request, render_template
from flask import Response
import os
from flask_cors import CORS, cross_origin
from prediction_Validation_Insertion import pred_validation
from trainingModel import trainModel
from training_Validation_Insertion import train_validation
import flask_monitoringdashboard as dashboard
from predictFromModel import prediction
import numpy as np
import pickle

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
dashboard.bind(app)
CORS(app)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('home.html')


@app.route("/batch_prediction", methods=['GET'])
@cross_origin()
def batch_prediction():
    return render_template('batch_prediction.html')


# thyroid_model_path = 'models\RandomForest3\RandomForest3.sav'
# thyroid_model = pickle.load(
#     open(thyroid_model_path, 'rb'))


# @ app.route('/value-prediction', methods=['GET'])
# def value_prediction():
#     title = 'Thyroid detection'
#     return render_template('value-based-prediction.html', title=title)
#
#
# @ app.route('/value-prediction-result', methods=['POST'])
# def value_prediction_result():
#     title = 'Thyroid detection'
#
#     if request.method == 'POST':
#         age = int(request.form['age'])
#         sex = request.form['sex']
#         on_thyroxine = request.form['onthyroxine']
#         query_on_thyroxine = request.form['qthyroxine']
#         on_antithyroid_medication = request.form['medication']
#         sick = request.form['sick']
#         pregnant = request.form['pregnant']
#         I131_treatment = request.form['I131']
#         query_hypothyroid = request.form['hypothyroid']
#         query_hyperthyroid = request.form['hyperthyroid']
#         lithium = request.form['lithium']
#         goitre = request.form['goitre']
#         tumor = request.form['tumor']
#         hypopituitary = request.form['hypopituitary']
#         psych = request.form['psych']
#         TSH = float(request.form['TSH'])
#         T3 = float(request.form['T3'])
#         TT4 = float(request.form['TT4'])
#         T4U = float(request.form['T4U'])
#         FTI = float(request.form['FTI'])
#
#
#
#
#         data = np.array([[age, sex, on_thyroxine, query_on_thyroxine,
#                           on_antithyroid_medication, sick, pregnant, I131_treatment,
#                           query_hypothyroid, query_hyperthyroid, lithium, goitre, tumor,
#                           hypopituitary, psych, TSH, T3, TT4, T4U, FTI]])
#
#         data[sex] = data[sex].map({'M':0,'F':1},axis=1)
#         for feature in data[[on_thyroxine, query_on_thyroxine,
#                           on_antithyroid_medication, sick, pregnant, I131_treatment,
#                           query_hypothyroid, query_hyperthyroid, lithium, goitre, tumor,
#                           hypopituitary, psych]]:
#             data[feature] = data[feature].map({'True':1,'False':0},axis=1)
#
#         my_prediction = thyroid_model.predict(data)
#         final_prediction = my_prediction[0]
#
#         return render_template('value-result.html', prediction=final_prediction, title=title)
#
#     else:
#
#         return render_template('try_again.html', title=title)

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRouteClient():
    try:
        if request.json is not None:
            path = request.json['filepath']

            pred_val = pred_validation(path) #object initialization

            pred_val.prediction_validation() #calling the prediction_validation function

            pred = prediction(path) #object initialization

            # predicting for dataset present in database
            path = pred.predictionFromModel()
            return Response("Prediction File created at %s!!!" % path)
        elif request.form is not None:
            path = request.form['filepath']

            pred_val = pred_validation(path) #object initialization

            pred_val.prediction_validation() #calling the prediction_validation function

            pred = prediction(path) #object initialization

            # predicting for dataset present in database
            path = pred.predictionFromModel()
            return Response("Prediction File created at %s!!!" % path)

    except ValueError:
        return Response("Error Occurred! %s" %ValueError)
    except KeyError:
        return Response("Error Occurred! %s" %KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" %e)



@app.route("/train", methods=['POST'])
@cross_origin()
def trainRouteClient():

    try:
        if request.json['folderPath'] is not None:
            path = request.json['folderPath']
            train_valObj = train_validation(path) #object initialization
            train_valObj.train_validation()#calling the training_validation function

            trainModelObj = trainModel() #object initialization
            trainModelObj.trainingModel() #training the model for the files in the table
        elif request.form is not None:
            path = request.json['folderPath']
            train_valObj = train_validation(path)  # object initialization

            train_valObj.train_validation()  # calling the training_validation function
            trainModelObj = trainModel()  # object initialization




    except ValueError:

        return Response("Error Occurred! %s" % ValueError)

    except KeyError:

        return Response("Error Occurred! %s" % KeyError)

    except Exception as e:

        return Response("Error Occurred! %s" % e)
    return Response("Training successfull!!")

