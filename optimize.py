import optuna
import os
import math

def objective(trial):
    # パラメータの定義
    x = trial.suggest_float('x', -10, 10)   # xは-10から10の連続値
    y = trial.suggest_float('y', -10, 10)   # yも同様
    z = trial.suggest_int('z', 1, 100)      # zは1から100の整数

    # 目的関数（例: 複雑な非線形関数）
    result = (
        math.sin(x) * math.cos(y) +         # サインとコサインの積
        0.1 * z +                          # zの影響をスケーリング
        (x - 2) ** 2 + (y + 3) ** 2        # 二次項でx, yを中心に引きつける
    )

    # 最小化対象
    return result

if __name__ == "__main__":
    # SQLiteを使ったストレージ
    db_path = "sqlite:///optuna_complex.db"

    # スタディ作成または読み込み
    study = optuna.create_study(
        study_name="complex-example-study",
        direction="minimize",
        storage=db_path,
        load_if_exists=True
    )

    # 最適化の実行
    study.optimize(objective, n_trials=100)

    # 最適化結果の表示
    print("Best Value:", study.best_value)
    print("Best Params:", study.best_params)
