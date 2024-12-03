from optuna_dashboard import app
import optuna

# SQLiteデータベースのパス
db_path = "sqlite:///optuna_complex.db"

# Flask アプリケーションを作成
application = app.create_app(storage=db_path)

# ローカル環境で実行する場合
if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8000, debug=True)
