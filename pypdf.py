import random
from turtle import title
import requests
import os
from PyPDF2 import PdfReader, PdfWriter
from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def test():
    print('home pge of test')
    
    # GET request
    if request.method == 'GET':
        print('request.is_json')
        message = {'greeting':'Hello from Flask!'}
        return message  # serialize and use JSON headers
        #return jsonify(message)  # serialize and use JSON headers
    
    
    
    
    # POST requests   
    if request.method == 'POST':
        pathofpdf=request.get_json().get('currenturl')

        
        def deletepage():
            pagenotodelete=request.get_json().get('pagestodelete')
            print(pagenotodelete)
            newpagenotodelete= [int(i) for i in pagenotodelete]
            print(newpagenotodelete)
            url=pathofpdf
            print(url)
            x=requests.get(url)
            kx=random.randint(0,999999999999999999999999999999999999)
            
            with open(f'{kx}metadata.pdf', 'wb') as f:
                f.write(x.content)
            
            reader = PdfReader(f'{kx}metadata.pdf')
            writers=PdfWriter()
            number_of_pages = reader.getNumPages()
            zz=int(number_of_pages)

            for x in range(zz):
                if (x in newpagenotodelete)==True:
                    continue
                print(x)
                writers.add_page(reader.pages[x])
            
            print(number_of_pages)
            os.remove(f'{kx}metadata.pdf')
            
            with open('final.pdf', 'wb') as kkr:
                writers.write(kkr)
        
        deletepage()
        
        return 'Sucesss', 200

if __name__ =='__main__':
    app.run(debug=True)


    