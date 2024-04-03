# email-header-analysis
It's a basic python code of analyzing email headers whether it is spam or not (all spam mails here obviously). I will paste the link of the dataset I have used for this. So this dataset contains a list of Spam and Ham mails. Ham mail is generally a legitimate mail sent from known or recognized senders, colleagues, or businesses the recipient has interacted with. I have integrated this code with some beginner-friendly Machine Learning concepts (cause why not?). The analogy follows as,
 1. Adding our dataset path (.csv file) and then initializing the dataset using pandas.
 2. Then we perform the training and testing, it depends on how many columns our dataset file has. Here x=text data (email content) and y=contain the labels (spam or not spam).
 3. Later we use the 'CountVectorizer' is used to convert the email text data into a numerical format.
 4. This numerical format is our input for the Logistic Regression model.
 5. Lastly executing the prediction and accuracy. 
I have used the if-else statement in the end because it will give us a clean understandable output.
