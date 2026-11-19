from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parent.parent
df = pd.read_csv(ROOT / "data/processed/idosos_medicacao_limpo.csv")

colunas = [
    "idade",
    "n_medicamentos",
    "n_doencas_cronicas",
    "mora_sozinho",
    "tem_cuidador",
    "usa_alarme",
]
X = df[colunas].copy()
X["cognicao_leve"] = (df.comprometimento_cognitivo == "Leve").astype(int)
X["cognicao_moderada"] = (df.comprometimento_cognitivo == "Moderado").astype(int)
y = df["baixa_adesao"]

Xtr, Xte, ytr, yte = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=42
)

modelo = make_pipeline(
    SimpleImputer(strategy="median"),
    StandardScaler(),
    LogisticRegression(
        C=0.1,
        class_weight="balanced",
        max_iter=1000
    ),
)
modelo.fit(Xtr, ytr)

prob = modelo.predict_proba(Xte)[:, 1]
print("AUC no teste:", round(roc_auc_score(yte, prob), 3))
print(
    classification_report(
        yte, modelo.predict(Xte), target_names=["adesão ok", "baixa adesão"]
    )
)

coef = modelo[-1].coef_[0]
imp = pd.Series(np.exp(coef), index=X.columns).sort_values(ascending=False)
print(
    "Razão de chances (variáveis padronizadas; "
    "acima de 1 aumenta o risco, abaixo de 1 protege):"
)
print(imp.round(2))