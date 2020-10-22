#https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#folder-structure
import azure.functions as func
import os
import logging
import json
import pickle
import sys
import pkgutil
from joblib import dump, load
from sklearn.tree import DecisionTreeClassifier
classifier = load("grammar/grammar.v14.joblib")

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP triggered')
    token = req.params.get('token')
    logging.info(f'Python HTTP triggered function processed:{token}')
    if not token:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            token = req_body.get('token')
    
    try:
        if token:
            result = predict(count_special_character(token))
            func.HttpResponse.mimetype = 'text/plain'
            func.HttpResponse.charset = 'utf-8'
            return func.HttpResponse(result)
        else:
            func.HttpResponse.mimetype = 'text/html'
            func.HttpResponse.charset = 'utf-8'
            mySeparator = "\r\n"
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            modules = mySeparator.join([f"<li>{module_name[1]}</li>" for module_name in pkgutil.iter_modules()])
            version = sys.version
            return func.HttpResponse(
                f"Please pass a token on the query string or in the request body<br/>{BASE_DIR}<hr/> <b>Python {version}</b> <h3>Installed Modules:</h3>{modules}", status_code=400
            )
    except Exception as e:
            func.HttpResponse.mimetype = 'application/json'
            func.HttpResponse.charset = 'utf-8'
            return func.HttpResponse(
                str(e)
            )


def count_special_character(string): 
    #length,spaces,alpha,numeric,specialchars,hyphen,fslah,bslah,parens,at,dot,plus
    # Declaring variable for special characters 
    vector = [len(string),0,0,0,0,0,0,0,0,0,0,0]
   
    for i in range(0, len(string)):  
    # len(string) function to count the 
    # number of characters in given string.
      
        ch = string[i]

        #.isalpha() function checks whether character 
        #is alphabet or not.
        if (ch.isalpha()):  
            vector[2] += 1
        
        #.isdigit() function checks whether character 
        #is a number or not.
        elif (ch.isdigit()):
            vector[3] += 1
            
        else:
            vector[4] += 1
            if (ch == " "):
                vector[1] += 1
            elif (ch == "-"):
                vector[5] += 1
            elif (ch == "/"):
                vector[6] += 1
            elif (ch == "\\"):
                vector[7] += 1
            elif (ch == "("  or ch == ")"):
                vector[8] += 1
            elif (ch == "@"):
                vector[9] += 1
            elif (ch == "."):
                vector[10] += 1
            elif (ch == "+"):
                vector[11] += 1
    return vector


def predict(vector) :
    result = classifier.predict([vector])
    print(result)
    return result[0]