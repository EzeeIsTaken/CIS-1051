import ratemyprofessor
from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/pokeProfessor", methods=['GET'])
def getPokeProfessor():
    if request.method == 'GET':
        professorName = request.args.get('name', None)

        #get school object
        templeUniversity = ratemyprofessor.get_school_by_name("Temple University")
        
        #find the professor
        professor = ratemyprofessor.get_professor_by_school_and_name(templeUniversity, professorName)
        
        #build json response with the fields u want from professor (e.g. name, rating, etc.)
        response = json.dumps({'name': professor.name, 'rating': professor.rating, 'difficulty': professor.difficulty})
        return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)
