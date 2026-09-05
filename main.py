from flask import Flask

app = Flask(__name__)


@app.route("/")
def homepage():
    # IMPORTANTE: Mude o número abaixo para o SEU WhatsApp (Ex: 5583999999999)
    meu_whats = "5581998029204"
    msg = "Olá! Gostaria de fazer um pedido de frutas e verduras frescas."
    link_final = f"https://wa.me{meu_whats}?text={msg.replace(' ', '+')}"

    return f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hortifruti Fresco - Peça pelo WhatsApp</title>
        <style>
            body {{ font-family: 'Segoe UI', Arial, sans-serif; background-color: #f9fbf9; color: #333; margin: 0; padding: 0; }}
            header {{ background-color: #27ae60; color: white; padding: 30px 20px; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.05); }}
            header h1 {{ margin: 0; font-size: 2.3em; }}
            header p {{ margin: 5px 0 0 0; font-size: 1.1em; opacity: 0.9; }}
            .container {{ max-width: 1000px; margin: 30px auto; padding: 0 20px; text-align: center; }}
            .grid-produtos {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; margin-top: 30px; }}
            .card {{ background: white; padding: 15px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); text-align: center; transition: 0.3s; border: 1px solid #eef2ee; }}
            .card:hover {{ transform: translateY(-5px); box-shadow: 0 6px 15px rgba(0,0,0,0.1); }}
            .card img {{ width: 100%; height: 160px; object-fit: cover; border-radius: 8px; }}
            .card h3 {{ margin: 12px 0 5px 0; color: #2c3e50; font-size: 1.2em; }}
            .tag {{ background-color: #e8f5e9; color: #2e7d32; padding: 3px 10px; border-radius: 20px; font-size: 0.85em; font-weight: bold; display: inline-block; margin-bottom: 10px; }}
            .preco {{ font-size: 1.25em; color: #27ae60; font-weight: bold; margin: 5px 0 15px 0; }}
            .btn-whats {{ display: inline-block; width: 85%; padding: 10px; background-color: #25d366; color: white; text-decoration: none; font-weight: bold; border-radius: 6px; transition: 0.2s; }}
            .btn-whats:hover {{ background-color: #128c7e; }}
            .footer-fixo {{ position: fixed; bottom: 0; left: 0; width: 100%; background: white; padding: 15px 0; box-shadow: 0 -4px 10px rgba(0,0,0,0.08); text-align: center; z-index: 100; }}
            .btn-pedir-geral {{ display: inline-block; padding: 12px 40px; background-color: #25d366; color: white; text-decoration: none; font-size: 1.2em; font-weight: bold; border-radius: 30px; box-shadow: 0 4px 10px rgba(37,211,102,0.3); }}
            .spacer {{ height: 80px; }}
        </style>
    </head>
    <body>

        <header>
            <h1>Sacolão & Hortifruti Delivery 🍉</h1>
            <p>Frutas e verduras fresquinhas direto na sua casa!</p>
        </header>

        <div class="container">
            <h2>Nossos Produtos da Semana</h2>

            <div class="grid-produtos">

                <!-- Produto 1 -->
                <div class="card">
                    <span class="tag">Fruta</span>
                    <img src="/static/banana.jpg" alt="Banana">
                    <h3>Banana Prata (Kg)</h3>
                    <div class="preco">R$ 5,90</div>
                    <a href="{link_final}" target="_blank" class="btn-whats">Pedir no Whats</a>
                </div>

                <!-- Produto 2 -->
                <div class="card">
                    <span class="tag">Fruta</span>
                    <img src="/static/maca.jpg" alt="Maçã">
                    <h3>Maçã Nacional (Kg)</h3>
                    <div class="preco">R$ 8,90</div>
                    <a href="{link_final}" target="_blank" class="btn-whats">Pedir no Whats</a>
                </div>

                <!-- Produto 3 -->
                <div class="card">
                    <span class="tag">Verdura</span>
                    <img src="/static/alface.jpg" alt="Alface">
                    <h3>Alface Crespa (Unid)</h3>
                    <div class="preco">R$ 3,50</div>
                    <a href="{link_final}" target="_blank" class="btn-whats">Pedir no Whats</a>
                </div>

                <!-- Produto 4 -->
                <div class="card">
                    <span class="tag">Legume</span>
                    <img src="/static/tomate.jpg" alt="Tomate">
                    <h3>Tomate Italiano (Kg)</h3>
                    <div class="preco">R$ 7,40</div>
                    <a href="{link_final}" target="_blank" class="btn-whats">Pedir no Whats</a>
                </div>

                <!-- Produto 5 -->
                <div class="card">
                    <span class="tag">Legume</span>
                    <img src="/static/batata.jpg" alt="Batata">
                    <h3>Batata Inglesa (Kg)</h3>
                    <div class="preco">R$ 6,20</div>
                    <a href="{link_final}" target="_blank" class="btn-whats">Pedir no Whats</a>
                </div>

                <!-- Produto 6 -->
                <div class="card">
                    <span class="tag">Verdura</span>
                    <img src="/static/repolho.jpg" alt="Repolho">
                    <h3>Repolho Verde (Unid)</h3>
                    <div class="preco">R$ 4,50</div>
                    <a href="{link_final}" target="_blank" class="btn-whats">Pedir no Whats</a>
                </div>

            </div>
        </div>

        <div class="spacer"></div>

        <div class="footer-fixo">
            <a href="{link_final}" target="_blank" class="btn-pedir-geral">
                🟢 MONTAR PEDIDO NO WHATSAPP
            </a>
        </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)

