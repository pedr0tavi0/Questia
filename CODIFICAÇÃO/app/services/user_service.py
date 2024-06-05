def get_emblema_url(pontos):
    if pontos < 10:
        return "{{ url_for('static', filename='images/rank/1.png') }}"
    elif pontos < 20:
        return "{{ url_for('static', filename='images/rank/2.png') }}"
    elif pontos < 30:
        return "{{ url_for('static', filename='images/rank/3.png') }}"
    # Adicione mais condições conforme necessário para definir os emblemas com base nos pontos
    else:
        return "{{ url_for('static', filename='images/rank/default.png') }}"  # Emblema padrão para pontuações mais altas