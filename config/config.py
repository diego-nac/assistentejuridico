import vertexai.preview.generative_models as generative_models

PROMPT_DADOS = """Identifique e extraia exatamente as informações abaixo.
- Número do Processo Judicial: Identificador que localiza o processo onde a liminar foi solicitada.
- Nome da Parte Autora: Nome da pessoa ou empresa que está solicitando a liminar.
- CPF ou CNPJ: Número de identificação fiscal da parte autora.
- Conta Contrato ou Instalação: Referência ao contrato ou ao local relacionado à liminar.
- Resumo dos Fatos: Breve descrição dos eventos que justificam o pedido de liminar.
- Cliente Home Care: Informação relevante para verificar se o cliente faz parte de um regime de atendimento prioritário, como no caso de cuidados domiciliares (Home Care).
- Causas do Pedido: Análise dos motivos apresentados pelo cliente na petição inicial, que justificam o pedido da liminar.
- Decisão Liminar: Descrição do que a empresa precisa fazer em resposta à liminar deferida, incluindo prazos e ações necessárias.

{tonalidade}

Devolva no formato JSON {{"numero_processo":"", "nome_parte_autora":"", "cpf_cnpj":"", "conta_contrato":"", "resumo_fatos":"", "cliente_home_care":"", "causas_pedido":"", "decisao_liminar":""}}"""


PROMPT_MOTIVO = """Classifique as causas do pedido da liminar, selecionando todas as categorias aplicáveis. Devolva no formato JSON com valores booleanos.

**Causas do Pedido:**
- Falta de Fornecimento de Energia
- Problemas de Faturamento
- Danos Morais
- Cliente em Home Care
- Outros

**Saída**: JSON com valores booleanos indicando as categorias aplicáveis
"""


PROMPT_TOM_CASUAL = "O tom dos resumos deve ser casual, amigável e fácil de entender, como se você estivesse explicando para um amigo que não é da área jurídica. Use linguagem simples, evite jargões e seja conciso"

PROMPT_TOM_FORMAL = "Escreva de forma jurídica para advogados experientes."

INSTRUCOES_SISTEMA = "Você é uma advogada muito experiente que trabalha na empresa Equatorial Energia. Você é muito detalhista, e proativa. Responda de forma minuciosa sobre o processo jurídico."

SAFETY_SETTINGS = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
}

GENERATION_CONFIG = {
    "max_output_tokens": 4048,
    "temperature": 0.0,
    "top_p": 0.8,
}