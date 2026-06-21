import os
import subprocess
from pathlib import Path
from flask import Flask, redirect, render_template, request, url_for
from .email_sender import EmailSender
from .subscribers import Subscriber, SubscriberManager


def create_app() -> Flask:
    # Ensure Flask finds the project's top-level `templates/` directory
    template_dir = Path(__file__).resolve().parent.parent / "templates"
    app = Flask(__name__, template_folder=str(template_dir))
    manager = SubscriberManager()
    sender = EmailSender()

    @app.route("/")
    def index() -> str:
        return render_template("index.html", subscribers=manager.list())

    @app.route("/subscribe", methods=["POST"])
    def subscribe() -> str:
        email = request.form.get("email", "")
        name = request.form.get("name", "")
        success = manager.add(Subscriber(email=email, name=name))
        if success:
            return redirect(url_for("index"))
        return render_template("index.html", subscribers=manager.list(), error="Invalid or duplicate email")

    @app.route("/send", methods=["POST"])
    def send_email() -> str:
        recipient = request.form.get("recipient", "")
        subject = request.form.get("subject", "")
        body = request.form.get("body", "")
        html = request.form.get("html", "") or None
        result = sender.send(recipient, subject, body, html=html)
        if result.success:
            return redirect(url_for("index"))
        return render_template("index.html", subscribers=manager.list(), error=result.error)

    @app.route("/tests")
    def tests_page() -> str:
        return render_template("tests.html", result=None)

    @app.route("/run-tests", methods=["POST"])
    def run_tests() -> str:
        # Run pytest in a subprocess and capture output
        try:
            proc = subprocess.run(
                ["python", "-m", "pytest", "-vv", "-rA"],
                capture_output=True,
                text=True,
                timeout=300,
            )
            output = proc.stdout
            if proc.stderr:
                output += "\n" + proc.stderr
            passed = proc.returncode == 0
        except subprocess.TimeoutExpired as exc:
            output = f"Tests timed out: {exc}"
            passed = False

        result = {"passed": passed, "output": output}
        return render_template("tests.html", result=result)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=True)
