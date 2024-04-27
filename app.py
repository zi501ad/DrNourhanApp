from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

messages = []  # قائمة لحفظ الرسائل

@app.route('/')
def home():
    return "مرحباً بكم في موقع تهنئة الدكتورة نورهان حسن!"

@app.route('/congrats', methods=['GET', 'POST'])
def congrats():
    if request.method == 'POST':
        name = request.form.get('name') or "مجهول"
        message = request.form.get('message')
        messages.append({'name': name, 'message': message})
        return redirect(url_for('congrats'))
    return render_template('congrats.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
