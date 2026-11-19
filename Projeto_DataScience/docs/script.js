const D = {
    sozinho: [["Não", 1100, 3.2, 69.9, 5.9], ["Sim", 379, 20.1, 82.8, 12.6]],
    cuidador: [["Não", 771, 12.3, 80.7, 10.1], ["Sim", 682, 2.3, 64.4, 5.0]],
    alarme: [["Não", 985, 10.2, 77.3, 8.8], ["Sim", 494, 2.2, 65.2, 5.4]],
    cogn: [["Nenhum", 1162, 3.6, 70.5, 6.3], ["Leve", 206, 17.0, 80.1, 11.1], ["Moderado", 111, 30.6, 89.2, 15.7]],
    idade: [["60-69", 399, 1.5, 61.4, 4.9], ["70-79", 696, 6.9, 73.3, 7.5], ["80 ou mais", 322, 17.1, 88.2, 11.6]],
    meds: [["1-2", 527, 4.7, 50.1, 5.5], ["3-4", 606, 6.9, 82.2, 7.9], ["5-6", 235, 11.9, 96.6, 10.4], ["7 ou mais", 59, 20.3, 98.3, 14.0]],
    esc: [["Sem escolaridade", 290, 8.6, 77.6, 7.8], ["Fundamental", 619, 8.1, 73.8, 7.7], ["Médio", 333, 6.6, 71.2, 7.7], ["Superior", 133, 6.0, 71.4, 7.7]],
    sexo: [["Feminino", 862, 7.9, 74.0, 7.7], ["Masculino", 617, 7.0, 72.1, 7.5]],
    risco: [["0 fatores", 492, 0.6], ["1 fator", 577, 2.6], ["2 fatores", 340, 15.9], ["3 fatores", 70, 55.7]]
};
const G = [["Mora sozinho", "sozinho"], ["Tem cuidador", "cuidador"], ["Usa alarme", "alarme"], ["Comprometimento cognitivo", "cogn"], ["Faixa etária", "idade"], ["Número de medicamentos", "meds"], ["Escolaridade", "esc"], ["Sexo", "sexo"]];
const MD = { 2: "Percentual de idosos que esquecem 20% ou mais das doses da semana.", 3: "Percentual de idosos que esquecem pelo menos uma dose na semana.", 4: "Média de doses esquecidas em relação às doses prescritas." };
const f = v => v.toFixed(1).replace(".", ",") + "%";
let m = 2;
function draw() {
    const max = Math.max(...G.flatMap(([, k]) => D[k].map(r => r[m])));
    document.getElementById("grid").innerHTML = G.map(([t, k]) => `<div class="card"><h3>${t}</h3>` + D[k].map(r => `<div class="row"><span>${r[0]}</span><div class="tr"><i style="width:${r[m] / max * 100}%"></i></div><b>${f(r[m])}</b><small>${r[1]} idosos</small></div>`).join("") + "</div>").join("");
    document.getElementById("mdesc").textContent = MD[m];
}
document.querySelectorAll(".tog button").forEach(b => b.onclick = () => { m = +b.dataset.m; document.querySelectorAll(".tog button").forEach(x => x.setAttribute("aria-pressed", x === b)); draw() });
const mx = Math.max(...D.risco.map(r => r[2]));
document.getElementById("risk").innerHTML = D.risco.map(r => `<div class="col"><b>${f(r[2])}</b><i style="height:${r[2] / mx * 80}%"></i></div>`).join("");
document.getElementById("riskl").innerHTML = D.risco.map(r => `<div>${r[0]}<br>${r[1]} idosos</div>`).join("");


const fatoresModelo = [
    ["Comprometimento cognitivo moderado", 2.14],
    ["Morar sozinho", 2.13],
    ["Idade", 1.93],
    ["Comprometimento cognitivo leve", 1.86],
    ["Número de medicamentos", 1.24],
    ["Número de doenças crônicas", 1.17],
    ["Ter cuidador", 0.52],
    ["Usar alarme", 0.37]
];

function mostrarModelo() {
    const elemento = document.getElementById("modelo");

    const maior = Math.max(...fatoresModelo.map(f => f[1]));

    elemento.innerHTML = fatoresModelo.map(([nome, valor]) => {
        const largura = (valor / maior) * 100;
        const cor = valor >= 1 ? "var(--alert)" : "var(--teal)";

        return `
            <div style="margin:14px 0">
                <div style="display:flex; justify-content:space-between;
                    gap:10px; margin-bottom:5px">
                    <span>${nome}</span>
                    <strong>${valor.toFixed(2).replace(".", ",")}</strong>
                </div>

                <div style="height:12px; background:var(--line);
                    border-radius:8px; overflow:hidden">
                    <div style="height:100%; width:${largura}%;
                        background:${cor}; border-radius:8px">
                    </div>
                </div>
            </div>
        `;
    }).join("");
}

mostrarModelo();

draw();
