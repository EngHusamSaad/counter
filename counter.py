from flask import Flask, render_template, request, redirect ,session



app = Flask(__name__)
app.secret_key = 'Husam 1333'



@app.route('/',methods=['GET'])
def show():
    count=session.get('count',0)
    session['count']=count+1
    return render_template('index.html',count=session['count'])
  
@app.route('/destroy_session' , methods=['POST'] )
def destroy_session():
    session.clear()
    return redirect('/')


@app.route('/add2' , methods=['POST'] )
def add2():
    count=session.get('count',0)
    # الرقم 0 هنا هو القيمة الافتراضية التي سيتم إرجاعها إذا لم يكن هناك قيمة موجودة
    session['count']=count+1
    return redirect('/')


    # need check
@app.route('/add' , methods=['POST'] )
def addtimes():
    count=session.get('count',0)
    times=request.form.get("times")
    print(times) 
    session['count']=count+times 
    return redirect('/')



if __name__ == '__main__':
  app.run(debug=True) 
