from flask import Flask, render_template, jsonify
import time
import random
import psutil

app = Flask(__name__)

start_time = time.time()


# ------------------------
#   ROUTES
# ------------------------

@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/items")
def items():
    return render_template("items.html")


@app.route("/blocks")
def blocks():
    return render_template("blocks.html")


@app.route("/mobs")
def mobs():
    return render_template("mobs.html")


@app.route("/seeds")
def seeds():
    return render_template("seeds.html")


@app.route("/seedconverter")
def seedconverter():
    return render_template("seedconverter.html")


@app.route("/redstone")
def redstone():
    return render_template("redstone.html")


# ------------------------
#   API
# ------------------------

@app.route("/old_dashboard") 
def old_dashboard():
    return render_template("dashboard_neon.html")

@app.route("/oldest_dashboard")
def oldest_dashboard():
    return render_template("dashboard.html")

@app.route("/dashboard")
def dashboard():
    return render_template("shader_ui_dashboard.html")


@app.route("/api/uptime")
def api_uptime():
    uptime = round(time.time() - start_time, 2)
    return jsonify({"uptime_seconds": uptime})

@app.route("/api/cpu")
def api_cpu():
    cpu_use = psutil.cpu_percent(interval=0.3)
    return jsonify({"cpu_percent": cpu_use})

@app.route("/api/test")
def api_test():
    return jsonify({"status": "ok", "message": "API çalışıyor :) "})

@app.route("/api/mini_log")
def api_log():
    return jsonify({
        "recent": [
            "Seed converter çağırıldı",
            "Dashboard yenilendi",
            "API ping test başarılı"
        ]
    })

@app.route("/api/ping")
def api_ping():
    return jsonify({"status": "online", "latency_ms": round(random.uniform(10, 40), 2)})


# ------------------------
#   RUN
# ------------------------

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
