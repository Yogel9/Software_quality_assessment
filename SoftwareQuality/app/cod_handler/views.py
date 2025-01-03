from django.shortcuts import render

# Create your views here.


def index(request):
    """Страница с расчётом параметров кода"""
    context = {
        "title": "Обработчик кода",
        "code_params": {
            "Unic_operand": 0,
            "Unic_operator": 0,
            "All_operand": 0,
            "All_operator": 0,
        },
        "form": {"code_text": "", "operant_dict": ""},
    }

    if request.method == "POST":
        form_data = request.POST.dict()
        print(form_data)
        code = form_data["code_text"]
        operands = form_data["operant_dict"].split(",")
        context["form"]["code_text"] = code
        context["form"]["operant_dict"] = form_data["operant_dict"]

        NotOperatorOperand_list = [":", "\r", "\n"]
        for item in NotOperatorOperand_list:
            code = code.replace(str(item), "")

        for operand in operands:
            operand_count = code.count(str(operand))
            if operand_count != 0:
                context["code_params"]["Unic_operator"] += 1
                context["code_params"]["All_operator"] += operand_count
            code = code.replace(str(operand), "")
        operators = code.replace("   ", " ").replace("  ", " ").split(" ")
        context["code_params"]["All_operand"] = len(operators)
        context["code_params"]["Unic_operand"] = len(set(operators))

    return render(
        request,
        "cod_handler.html",
        {
            "context": context,
        },
    )
