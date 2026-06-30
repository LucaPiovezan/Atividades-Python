import math
from flask import render_template, request


def calcular():
    try:
        num1 = float(request.form["num1"])
    except (ValueError, KeyError):
        return render_template(
            "calculadora.html",
            etapas="Valor inválido",
            resultados="informe um número válido",
        )

    operacao = request.form.get("operacao", "")

    if operacao == "sqrt":
        if num1 < 0:
            return render_template(
                "calculadora.html",
                etapas=f"Não existe raiz real de {num1}.",
                resultados="Erro: número negativo",
            )
        resultado = math.sqrt(num1)
        return render_template(
            "calculadora.html",
            etapas=f"√{num1}",
            resultados=resultado,
        )

    num2_str = request.form.get("num2", "").strip()
    if not num2_str:
        return render_template(
            "calculadora.html",
            etapas="Informe o segundo número para esta operação.",
            resultados="",
        )

    try:
        num2 = float(num2_str)
    except ValueError:
        return render_template(
            "calculadora.html",
            etapas="Valor inválido para o segundo número.",
            resultados="Erro: informe um número válido",
        )

    if operacao == "bhaskara":
        num3_str = request.form.get("num3", "").strip()
        if not num3_str:
            return render_template(
                "calculadora.html",
                etapas="Informe o coeficiente C para Bhaskara.",
                resultados="",
            )
        try:
            num3 = float(num3_str)
        except ValueError:
            return render_template(
                "calculadora.html",
                etapas="Valor inválido para o coeficiente C.",
                resultados="Erro: informe um número válido",
            )

        if num1 == 0:
            return render_template(
                "calculadora.html",
                etapas="O coeficiente 'A' não pode ser zero em uma equação quadrática.",
                resultados="Erro: Não é equação de 2º grau",
            )

        delta = (num2**2) - (4 * num1 * num3)

        if delta < 0:
            etapas = f"Δ = ({num2})² - 4·({num1})·({num3}) = {delta}"
            resultado = "Sem raízes reais (Δ < 0)"
        else:
            raiz_delta = math.sqrt(delta)
            x1 = (-num2 + raiz_delta) / (2 * num1)
            x2 = (-num2 - raiz_delta) / (2 * num1)
            etapas = f"Δ = {delta} | x = (-({num2}) ± √{delta}) / (2·{num1})"
            resultado = f"x₁ = {x1:.4f}  |  x₂ = {x2:.4f}"

        return render_template(
            "calculadora.html", etapas=etapas, resultados=resultado
        )

    if operacao == "+":
        resultado = num1 + num2
        etapas = f"{num1} + {num2} = {resultado}"

    elif operacao == "-":
        resultado = num1 - num2
        etapas = f"{num1} - {num2} = {resultado}"

    elif operacao == "*":
        resultado = num1 * num2
        etapas = f"{num1} x {num2} = {resultado}"

    elif operacao == "/":
        if num2 == 0:
            return render_template(
                "calculadora.html",
                etapas=f"{num1} / 0",
                resultados="Erro: divisão por zero",
            )
        resultado = num1 / num2
        etapas = f"{num1} ÷ {num2} = {resultado}"

    elif operacao == "**":
        resultado = num1**num2
        etapas = f"{num1} ** {num2} = {resultado}"

    elif operacao == "log":
        if num1 <= 0:
            return render_template(
                "calculadora.html",
                etapas=f"log base {num2} de {num1}",
                resultados="Erro: o número deve ser positivo",
            )
        if num2 <= 0 or num2 == 1:
            return render_template(
                "calculadora.html",
                etapas=f"log base {num2} de {num1}",
                resultados="Erro: a base deve ser > 0 e diferente de 1",
            )
        resultado = math.log(num1, num2)
        etapas = f"log base {num2} de {num1} = {resultado}"

    else:
        return render_template(
            "calculadora.html",
            etapas="Operação desconhecida.",
            resultados="Erro: operação inválida",
        )

    return render_template(
        "calculadora.html",
        etapas=etapas,
        resultados=resultado,
    )
