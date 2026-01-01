from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
        return redirect("/")
    
    return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:index>", methods=["GET"])
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect("/")

@app.route("/edit/<int:index>", methods=["GET"])
def edit(index):
    if 0 <= index < len(tasks):
        return render_template("edit.html", task=tasks[index], index=index)
    return redirect("/")

@app.route("/update/<int:index>", methods=["POST"])
def update(index):
    if 0 <= index < len(tasks):
        updated_task = request.form.get("task")
        if updated_task:
            tasks[index] = updated_task
    return redirect("/")

if __name__ == "__main__":  
    app.run()
