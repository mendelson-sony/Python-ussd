from flask import Flask, request

app = Flask(__name__)

@app.route('/ussd', methods=['GET', 'POST'])
def ussd():
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    if text == "":
        # Primeira tela do menu
        response = "CON Bem-vindo à SOFTSON\n"
        response += "1. Designer\n"
        response += "2. Criação de Websites\n"
        response += "3. Marketing\n"
        response += "4. KitGest\n"
    elif text == "1":
        # Submenu Designer
        response = "CON Escolha uma opção de Designer:\n"
        response += "1. Logotipos\n"
        response += "2. Banners\n"
        response += "3. Voltar ao menu principal\n"
    elif text == "1*1":
        response = "END Você escolheu Logotipos. Entraremos em contato em breve!"
    elif text == "1*2":
        response = "END Você escolheu Banners. Entraremos em contato em breve!"
    elif text == "1*3":
        return ussd()
    elif text == "2":
        # Submenu Criação de Websites
        response = "CON Escolha uma opção de Criação de Websites:\n"
        response += "1. Websites Pessoais\n"
        response += "2. Websites Empresariais\n"
        response += "3. Voltar ao menu principal\n"
    elif text == "2*1":
        response = "END Você escolheu Websites Pessoais. Entraremos em contato em breve!"
    elif text == "2*2":
        response = "END Você escolheu Websites Empresariais. Entraremos em contato em breve!"
    elif text == "2*3":
        return ussd()
    elif text == "3":
        # Submenu Marketing
        response = "CON Escolha uma opção de Marketing:\n"
        response += "1. Redes Sociais\n"
        response += "2. E-mail Marketing\n"
        response += "3. Voltar ao menu principal\n"
    elif text == "3*1":
        response = "END Você escolheu Redes Sociais. Entraremos em contato em breve!"
    elif text == "3*2":
        response = "END Você escolheu E-mail Marketing. Entraremos em contato em breve!"
    elif text == "3*3":
        return ussd()
    elif text == "4":
        # Submenu KitGest
        response = "END Você escolheu KitGest. Entraremos em contato em breve!"
    else:
        response = "END Opção inválida. Tente novamente."

    return response

if __name__ == '__main__':
    app.run(debug=True)
