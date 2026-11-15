import pandas as pd, numpy as np, re, unicodedata, json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
df=pd.read_csv(ROOT/'data/raw/idosos_medicacao.csv').drop_duplicates()
n0=len(df)
def norm(x): return unicodedata.normalize('NFKD',str(x).strip().lower()).encode('ascii','ignore').decode()
def yn(x):
    if pd.isna(x): return np.nan
    return {'sim':1,'s':1,'nao':0,'n':0}.get(norm(x),np.nan)
for c in ['mora_sozinho','tem_cuidador','usa_alarme']: df[c]=df[c].map(yn)
df['sexo']=df.sexo.str.strip().str.lower().str[0].str.upper()
def esc(x):
    if pd.isna(x): return np.nan
    s=norm(x)
    if 'anal' in s or 'sem' in s or 'nenhuma' in s: return 'Sem escolaridade'
    if 'fund' in s: return 'Fundamental'
    if 'med' in s: return 'Médio'
    if 'sup' in s: return 'Superior'
df['escolaridade']=df.escolaridade.map(esc)
num={'sessenta':60,'setenta':70,'oitenta':80,'noventa':90}
uni={'um':1,'dois':2,'tres':3,'quatro':4,'cinco':5,'seis':6,'sete':7,'oito':8,'nove':9}
def age(x):
    if pd.isna(x): return np.nan
    s=norm(x); m=re.search(r'\d+',s)
    if m: v=int(m.group())
    else:
        p=s.split(' e '); v=num.get(p[0].strip(),np.nan)
        if len(p)>1 and v==v: v+=uni.get(p[1].strip(),0)
    return v if 55<=v<=105 else np.nan
df['idade']=df.idade.map(age)
df['n_medicamentos']=df.n_medicamentos.where(df.n_medicamentos<=20)
bad=(df.doses_esquecidas_semana<0)|(df.doses_esquecidas_semana>df.doses_prescritas_semana)
nbad=int(bad.sum()); df=df[~bad].copy()
df['data_cadastro']=pd.to_datetime(df.data_cadastro,format='mixed',dayfirst=False,errors='coerce')
df['taxa_esquecimento']=(df.doses_esquecidas_semana/df.doses_prescritas_semana).round(4)
df['esquece_alguma']=(df.doses_esquecidas_semana>0).astype(int)
df['baixa_adesao']=(df.taxa_esquecimento>=0.2).astype(int)
df.to_csv(ROOT/'data/processed/idosos_medicacao_limpo.csv',index=False)
N=len(df)
out={'n0':n0,'n':N,'removidos_incoerentes':nbad,
 'alguma':round(df.esquece_alguma.mean()*100,1),'baixa':round(df.baixa_adesao.mean()*100,1),'taxa':round(df.taxa_esquecimento.mean()*100,1)}
def g(col,labels=None):
    r=df.groupby(col).agg(n=('baixa_adesao','size'),baixa=('baixa_adesao','mean'),alguma=('esquece_alguma','mean'),taxa=('taxa_esquecimento','mean'))
    return [[str(labels.get(k,k)) if labels else str(k),int(v.n),round(v.baixa*100,1),round(v.alguma*100,1),round(v.taxa*100,1)] for k,v in r.iterrows()]
yn_l={0:'Não',1:'Sim'}
out['sozinho']=g('mora_sozinho',yn_l);out['cuidador']=g('tem_cuidador',yn_l);out['alarme']=g('usa_alarme',yn_l)
out['cogn']=g('comprometimento_cognitivo')
df['fi']=pd.cut(df.idade,[54,69,79,105],labels=['60-69','70-79','80+']);out['idade']=g('fi')
df['fm']=pd.cut(df.n_medicamentos,[0,2,4,6,20],labels=['1-2','3-4','5-6','7+']);out['meds']=g('fm')
out['esc']=g('escolaridade');out['sexo']=g('sexo',{'F':'Feminino','M':'Masculino'})
h=df[df.horario_mais_esquecido!='Nenhum'].horario_mais_esquecido.value_counts()
out['horario']=[[k,int(v),round(v/h.sum()*100,1)] for k,v in h.items()]
df['risco']=(df.mora_sozinho==1).astype(int)+(df.tem_cuidador==0).astype(int)+(df.comprometimento_cognitivo!='Nenhum').astype(int)
out['risco']=g('risco')
df['alarme_cog']=df.comprometimento_cognitivo.ne('Nenhum').map({True:'Com comprometimento',False:'Sem comprometimento'})
out['alarme_x_cog']=[[k,int(len(v)),round(v.usa_alarme.mean()*100,1)] for k,v in df.groupby('alarme_cog')]
print(json.dumps(out,ensure_ascii=False))
