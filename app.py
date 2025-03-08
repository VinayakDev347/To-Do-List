from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)
wishlist = []

def list_append(item):
    global wishlist
    wishlist.append(item)

def list_delete(item):
    global wishlist
    wishlist.remove(item)

@app.route("/",methods = ['GET' , 'POST'])
def create_to_do():
    global wishlist
    if request.method == 'POST':
        item_added = request.form['item']
        print("added value",item_added)
        if item_added != '':
            list_append(item_added)
    return render_template('index.html',wishlist=wishlist)



@app.route("/delete/<item>")
def delete_item(item):
    list_delete(item)
    return redirect(url_for('create_to_do'))


app.run(debug=True)


# if __name__ = '__main__'
    # app.run(debug=True)