# Thyroid Detection
An ML based application which raised accuracy by 40% in identifying patient thyroid type compared to manual  clinical diagnosis.

A simple ML based website which predicts the thyroid type out of the 4 classes - "negative", "compensated hypothyroid", "primary hypothyroid", "secondary hypothyroid” using various thyroid tests such as 'TSH', 'T3', 'TT4' etc., where negative class means no thyroid related condition.

## Application interface screenshot:
![Screenshot 2021-07-05 205949](https://user-images.githubusercontent.com/5305547/127063302-2b8e0c7f-aa8b-4d91-9e2f-4b6f36b34319.png)


## Application screenshot showing what the application does:
![Screenshot 2021-07-05 210014](https://user-images.githubusercontent.com/5305547/127063333-04ef13a9-40bd-4886-95ba-9365a77b3e9d.png)


# Features:
<b>1. age</b> - Shows the age of the patient. <br/>
<b>2. sex</b> - Shows the gender of the patient. <br/>
<b>3. on_thyroxine</b> - Shows whether the patient is on Thyroxine treatment or not. <br/>
<b>4. query_on_thyroxine</b> - Shows whether the patient has raised any queries regarding their thyroxine treatment/hormone or not. <br/>
<b>5. on_antithyroid_medication</b> - Shows whether the patient is on antithyroid_medication or not. <br/>
<b>6. sick</b> - Shows whether the patient is sick or not. <br/>
<b>7. pregnant</b> - Shows whether the patient is pregnant or not. <br/>
<b>8. thyroid_surgery</b> - Shows whether the patient has gone through Thyroid surgery or not <br/>
<b>9. I131_treatment</b> - Shows whether the patient is going through Radioactive Iodine(I-131) treatment or not. <br/>
<b>10. query_hypothyroid</b> - Shows whether the patient has raised any query regarding hypothyroid or not. Hypothyroid means thyroid is less than the optimum amounts. <br/>
<b>11. query_hyperthyroid</b> - Shows whether the patient has raised any query regarding hyperthyroid or not. Hyperthyroid means thyroid is more than the optimum amounts. <br/>
<b>12. lithium</b> - Shows whether the patient is on Lithium treatment or not. <br/>
<b>13. goitre</b> - Shows whether the patient is suffering from Goitre or not. <br/>
<b>14. tumor</b> - Shows whether the patient has any tumor or not. Tumor can either be benign or malignant. <br/>
<b>15. hypopituitary</b> - Shows whether the patient is on hypopituitary gland related treatment or not.
<b>16. psych</b> - Shows the patient's psych evaluation. <br/>
<b>17. TSH_measured</b> - Shows whether the thyroid stimulating hormone(TSH) has been measured or not. <br/>
<b>18. TSH</b> - If TSH has been measured then this columm shows the value of the TSH. <br/>
<b>19. T3_measured</b> - T3 is one of two major hormones made by your thyroid. Shows whether T3 of the patient has been measured or not. <br/>
<b>20. T3</b> - If T3 has been measured then this columm shows the value of the T3. <br/>
<b>21. TT4_measured</b> - T4 is another one of two major hormones made by your thyroid. Shows whether T4 of the patient has been measured or not. <br/>
<b>22. TT4</b> - If T3 has been measured then this columm shows the value of the T4. <br/>
<b>23. T4U_measured </b> - Shows whether T4U has been measured or not. <br/>
<b>24. T4U </b> - If measured, the value of the same. <br/>
<b>25. FTI_measured </b> - Shows Whether FTI(Free Thyroxine Index) for the patient has been measured or not. <br/>
<b>26. FTI</b> - If FTI has been measured then this columm shows the value of the FTI. <br/>
<b>27. TBG_measured</b> - Shows whether Thyroxine-Binding Globulin Deficiency has been measured or not. <br/>
<b>28. TBG</b> - If TBG is measured then it shows value of the same. <br/>
<b>29. referral_source</b> - Shows the organization/hospital from where the patient has been refferred. <br/>
<b>30. Class</b> - This is the Dependent feature. It consists of 4 classes 'negative', 'compensated hypothoroid', 'primary hypothoroid', 'secondary hypothoroid'. <br/>
<br/>
This is a POC(Proof of concept) kind-of project. The data used here comes up with no guarantee from the creator. So, please don't use it for detecting Thyroid class type for a patient. If you do so, the creator is not responsible for anything. However, this project presents the idea that how we can use ML into practice for healthcare sector.

## MOTIVATION 💪
Healthcare domain has a lot of issue and Thyroid is one of the glands which gets impacted by diseases and makes a large part of the polulation go for testing, medication and surgery for the treatment of Thyroid related disorders. This is a small and humble project which is using multiple datasets and merges those to create a model and predict the type of Thyroid condition the patient has namely; "negative", "compensated hypothyroid", "primary hypothyroid", "secondary hypothyroid”.
In this project, I present a website in which the predictions are implemented as; Batch File PRediction(which predicts and generates a new file with predicted values based in the pre-trained model. 
For the visibility predicting application, the user can input the data and the application will predict the class of Thyroid out of the 4 classes - "negative", "compensated hypothyroid", "primary hypothyroid", "secondary hypothyroid”.

## Built with 🛠️
<p align="left"> <a href="https://www.arduino.cc/" target="_blank"> <img src="https://cdn.worldvectorlogo.com/logos/arduino-1.svg" alt="arduino" width="40" height="40"/> </a> <a href="https://www.gnu.org/software/bash/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/gnu_bash/gnu_bash-icon.svg" alt="bash" width="40" height="40"/> </a> <a href="https://getbootstrap.com" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a><a href="https://flask.palletsprojects.com/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://heroku.com" target="_blank"> <img src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" alt="heroku" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a><a href="https://postman.com" target="_blank"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a><a href="https://scikit-learn.org/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="40" height="40"/> </a></p>       

    

## DEPLOYMENT 🚀
Deployment is done using deploy branch.<br/>
This website is deployed at AWS.<br/>
Github page: https://sagar61205.github.io/Thyroid-detection/ <br/>
How to use? <br/>
Value-based-prediction ==> enter the corresponding values and it will fetch the number of calories burnt.<br/>
File-based-prediction  ==> Click in 'default file prediction' to see the prediction on the already trained model OR Enter an absolute file path and clixk on 'Custom file predict'.'.



## Application screenshot for the 'About' section.
![Screenshot 2021-07-05 210029](https://user-images.githubusercontent.com/5305547/127064493-b63dfa5f-8f72-4b12-a4da-8d66c321b106.png)

## Application screenshot showing types of Thyroid disorders:
![Screenshot 2021-07-05 210050](https://user-images.githubusercontent.com/5305547/127064589-46b6bd3d-5af0-4168-afa1-f349cbc95297.png)

## Application screenshot for batch file prediction. Here deafult prediction takes place on pre-trained dataset. A custom file file prediction can also be done.
![Screenshot 2021-07-05 210119](https://user-images.githubusercontent.com/5305547/127064657-ed43e5a7-528b-4ab8-abf7-081d39e2eb76.png)

## Application screenshot for the important information section:
![Screenshot 2021-07-05 210134](https://user-images.githubusercontent.com/5305547/127064694-5edd41bb-679f-4f42-b350-b28feeae413a.png)

## Prediction(Batch file):
![thyroid prediction](https://user-images.githubusercontent.com/5305547/127065188-4317a3cc-8f7d-4857-8f92-ada26e97d3cd.png)
