import csv
import tablib
import os
import sys
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('front.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print (result)
      print("Print a result req2  ")
      print (result['req2'])
      

      with open(r'C:\Users\surbh\Desktop\majorcodes\RankedData.csv', 'w') as f:
         f.write("%s,%s\n"%("Requirement","Ranking"))
         f.write("%s,%s\n"%(result['req1'], result['rank1']))
         f.write("%s,%s\n"%(result['req2'], result['rank2']))
         f.write("%s,%s\n"%(result['req3'], result['rank3']))
         f.write("%s,%s\n"%(result['req4'], result['rank4']))
         f.write("%s,%s\n"%(result['req5'], result['rank5']))
         f.write("%s,%s\n"%(result['req6'], result['rank6']))
         f.write("%s,%s\n"%(result['req7'], result['rank7']))
         f.write("%s,%s\n"%(result['req8'], result['rank8']))
         f.write("%s,%s\n"%(result['req9'], result['rank9']))
         f.write("%s,%s\n"%(result['req10'], result['rank10']))

      #sys.path.append("/home/astha/Desktop/major3/")
	  
      import svm
      svm.main()
      print("..........svm imported........")
      import intersection
      print("..........intersection imported........")
      dataset = tablib.Dataset()
      with open(os.path.join(os.path.dirname(__file__),'intersect.csv')) as f:
         dataset.csv = f.read()

      data=dataset.html
      return render_template("result.html",data=data)

if __name__ == '__main__':
   app.jinja_env.auto_reload = True
   app.config['TEMPLATES_AUTO_RELOAD'] = True
   app.run(debug = True)
