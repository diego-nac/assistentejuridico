import vertexai.preview.generative_models as generative_models

PROMPT_DADOS = """Identifique e extraia exatamente as informações abaixo.
- Número do Processo Judicial: Identificador do processo que foi recentemente iniciado.
- Nome da Parte Autora: Nome da pessoa ou empresa que iniciou o processo.
- CPF ou CNPJ: Número de identificação fiscal da parte autora.
- Conta Contrato ou Instalação: Referência ao contrato ou local de instalação que motivou o processo.
- Resumo dos Fatos: Breve descrição dos eventos que motivaram o processo judicial.
- Data do Fato Gerador: Data em que ocorreu o evento que levou ao processo judicial, como o corte de energia, fraude ou aumento de consumo.
- Assunto Principal da Reclamação: Identificação da principal queixa do cliente, como fraude, corte indevido de serviços, aumento injustificado no consumo ou falta de energia.

{tonalidade}

Devolva no formato JSON {{"numero_processo_judicial":"", "nome_parte_autora":"", "cpf_cnpj":"", "conta_contrato_instalacao":"", "resumo_fatos":"", "data_fato_gerador":"", "assunto_principal_reclamacao":""}}"""

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