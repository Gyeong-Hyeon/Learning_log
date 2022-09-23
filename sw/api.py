from flask import request, Flask
from flask import render_template
from utils import return_history, insert_question, update_answer

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    나의 첫 api 서버입니다
    """
    if request.method == "POST":
        name = request.form['name']
        question = request.form['question']
        insert_question(name, question)
        histories = return_history()
        return render_template('customer.html', histories=histories)
    histories = return_history()
    return render_template('customer.html', histories=histories)

@app.route("/admin", methods=["GET","POST"])
def return_result():
    if request.method == "POST":
        ques_id = request.form['ques_id']
        answer = request.form['answer']
        update_answer(ques_id, answer)
        histories = return_history()
        return render_template('admin.html', histories=histories)
    histories = return_history()
    return render_template('admin.html', histories=histories)   

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug=True)
