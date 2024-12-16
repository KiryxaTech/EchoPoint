from flask import Flask, render_template_string, request, redirect, jsonify
import threading
from typing import Callable

class YandexServer:
    def __init__(self, client_id, client_secret, redirect_uri, base_auth_url, process_token: Callable):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.base_auth_url = base_auth_url
        self.process_token = process_token  # Функция для обработки токена
        self.app = Flask(__name__, static_folder="../static", template_folder="../templates")
        self._setup_routes()

    def _setup_routes(self):
        @self.app.route('/')
        def index():
            if 'code' in request.args:
                auth_code = request.args.get('code')
                try:
                    # Вызываем переданную функцию для обработки токена
                    html_content = self.process_token(auth_code)
                    return render_template_string(html_content)
                except Exception as e:
                    return jsonify({"error": str(e)}), 400
            else:
                auth_url = (
                    f"{self.base_auth_url}?response_type=code&client_id={self.client_id}&redirect_uri={self.redirect_uri}&force_confirm=true"
                )
                return redirect(auth_url)

    def run(self, host="127.0.0.1", port=4545):
        self.app.run(host=host, port=port)

    def run_in_thread(self, host="127.0.0.1", port=4545):
        threading.Thread(target=self.run, args=(host, port), daemon=True).start()