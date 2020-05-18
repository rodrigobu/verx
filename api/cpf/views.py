import json
import re
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView

from api import app

cpf = Blueprint('cpf', __name__)

@cpf.route('/')

class CpfView(MethodView):
    ''' View de validação do  CPF
    '''
    def validar_cpf(self, cpf):

        """ Efetua a validação do CPF.

        Parâmetros:
            cpf (str): CPF a ser validado

        Retorno:
            bool:
                - Falso, quando o CPF não possuir o formato 999.999.999-99 ou 99999999999;
                - Falso, quando o CPF não possuir 11 caracteres numéricos;
                - Verdadeiro, caso contrário.

        Exemplos:

        >>> validate('529.982.247-25')
        True
        >>> validate('52998224725')
        True
        >>> validate('529 982 247 25')
        True
        >>> validate('abc.11f.11c-1g')
        False
        >>> validate('')
        False
        """
        
        # Verifica a formatação do CPF
        cpf = ''.join(re.findall(r'\d', str(cpf)))
        
        # Verifica se o CPF possui 11 números:
        if (not cpf or len(cpf) < 11):
            return {"is_valid": False}
                
        return {"is_valid": True}
        
    def post(self):
        data = request.get_json()
        cpf = data.get('cpf')
        if cpf is None:
            return abort(401, 'chave não encontrada: cpf')
        return jsonify(self.validar_cpf(cpf))

cpf_view =  CpfView.as_view('cpf_view')
app.add_url_rule(
    '/cpf/', view_func=cpf_view, methods=['POST']
)


