from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<title>Muhittin Can Karataş | Toptan Satış</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- WhatsApp Icon -->
<link rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

<style>

body {
    margin: 0;
    font-family: system-ui, Arial;
    background: linear-gradient(135deg,#0f172a,#1e293b,#334155);
    color: white;
}

/* HERO */
.hero {
    padding: 70px 20px 40px;
    text-align: center;
}

.hero-card {
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(12px);
    border-radius: 24px;
    padding: 40px;
    max-width: 720px;
    margin: auto;
    box-shadow: 0 20px 40px rgba(0,0,0,0.35);
}

.hero h1 {
    margin: 0;
    font-size: 36px;
}

.hero p {
    margin-top: 10px;
    opacity: 0.9;
    font-size: 18px;
}

.tag {
    margin-top: 18px;
    display: inline-block;
    background: #22c55e;
    color: #052e16;
    padding: 8px 18px;
    border-radius: 999px;
    font-weight: 600;
}

/* CONTENT */
.section {
    padding: 30px 20px 60px;
    max-width: 900px;
    margin: auto;
}

.card {
    background: white;
    color: #111;
    border-radius: 18px;
    padding: 26px;
    margin-bottom: 20px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.15);
}

/* FOOTER NAME */
.footer-name {
    position: fixed;
    left: 15px;
    bottom: 15px;
    background: black;
    padding: 10px 14px;
    border-radius: 10px;
    font-size: 14px;
}

/* WHATSAPP */
.whatsapp-btn {
    position: fixed;
    right: 20px;
    bottom: 20px;
    background: #25D366;
    color: white;
    padding: 14px 20px;
    border-radius: 50px;
    text-decoration: none;
    font-size: 16px;
    display: flex;
    align-items: center;
    gap: 10px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.3);
}

.whatsapp-btn i {
    font-size: 20px;
}

</style>
</head>

<body>

<div class="hero">
    <div class="hero-card">
        <h1>Can Karataş</h1>
        <p>Toptan Ticaret</p>
        <div class="tag">CK TOPTAN </div>
    </div>
</div>

<div class="section">

<div class="card">
<h2>Hakkımızda</h2>
Uygun fiyatlı ve sürekli stoklu çakmak ile bebek oyuncakları toptan satışı yapılır.
</div>

<div class="card">
<h2>Ürün Grupları</h2>
<ul>
<li>🔥 Çakmak Çeşitleri</li>
<li>🕶️ Güneş Gözlükleri</li>
<li>🧸 Pelüş Anahtarlık</li>
<li>🔌 Şarj Aletleri</li>


</ul>
</div>

</div>

<a class="whatsapp-btn"
href="https://wa.me/905305869097?text=Merhaba%20ürünler%20hakkında%20bilgi%20almak%20istiyorum"
target="_blank">
<i class="fa-brands fa-whatsapp"></i>
WhatsApp
</a>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
