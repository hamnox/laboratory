from flask import Flask, render_template, request

from glob import glob
import simplejson as json
from random import shuffle 

app = Flask(__name__)

# def getPicBox(boxarray, filepath):
#     for index, files in boxarray:
#         if filepath in files:
#             return index
#     raise KeyError
    
@app.route('/')
def index():
    return 'test worked'

@app.route('/hair', methods=['GET','POST'])
def hairy():
    error = None
    hairpics = glob('static/hair/*.jpg')
    hairdict = {}
    for pic in hairpics:
        substr = pic.replace('static/hair/','').split()[0]
        if substr in hairdict.keys():
            hairdict[substr].append(pic)
        else:
            hairdict[substr] = [pic]

    if request.method == 'POST':
        try:
            with open('static/hair/results.json','w') as fp:
                json.dump(request.form.to_dict(), fp)
        except IOError:
            return 'So, that failed.'
        return json.dumps(request.form.to_dict())
    else:
        return render_template('ratepics.html', imagedict=hairdict, count=5)

if __name__ == '__main__':
    app.run(debug=True)
