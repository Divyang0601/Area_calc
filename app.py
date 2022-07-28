from flask import Flask, render_template, request,url_for,redirect
import numpy as np
import pickle
import os
import glob
import re
import sys


###############




import cv2
import numpy as np
#img = cv2.imread('img.jpeg')
#height = img.shape[0]
#width = img.shape[1]
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY)
#cv2.imshow("Mask", thresh)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#ave = cv2.mean(thresh)[0]/255
#print(ave)
#area = ave*height*width
#print(area)
#px = 2.54/96
#ans = area*px**2
#print(ans)

#######################


#Get the app.py directory to built database there
basedir = os.path.abspath(os.path.dirname(__file__))

from tensorflow.keras.preprocessing import image



UPLOAD_FOLDER = 'uploads'
###############################################################

app = Flask(__name__)








@app.route('/')
def home_view():
    return render_template('area.html')






@app.route('/find_area',methods=['POST'])
def find_area():
    if request.method == 'POST':
        f = request.files['file']
        file_path = os.path.join(UPLOAD_FOLDER,f.filename)
        f.save(file_path)
        img = cv2.imread(file_path)

        height = img.shape[0]
        width = img.shape[1]
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY)

        ave = cv2.mean(thresh)[0]/255
        area = ave*height*width
        px = 2.54/96
        ans = area*px**2
        ans1 = str(ans)
        return render_template('results.html',result_text=ans1)


@app.route('/pnemonia_view')
def pnemonia_view():
    return render_template('pneumonia.html')

################################################################

if __name__ == "__main__":
    app.run()

################################################################
