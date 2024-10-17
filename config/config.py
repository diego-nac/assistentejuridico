import vertexai.preview.generative_models as generative_models


PROMPT_DADOS = """Identifique e extraia exatamente as informações abaixo.
- Número do processo judicial
- Nome do preposto da empresa que acompanhou a audiência
- Nome do advogado da empresa que acompanhou a audiência
- Nome do Juiz
- CPF ou CNPJ
- Conta contrato ou instalação
- Resumo dos fatos
- Data do fato gerador do processo
- Valor da CNR questionada
- Sentença do processo (julgado procedente, julgado improcedente, ausência da parte autora, incompetência de juizo...)
- Se houve ou não o pagamento de danos morais/materiais/indébito
- Analisar se a decisão do juiz foi favorável para empresa ou não

{tonalidade}

Devolva no formato JSON {{"numero_processo":"", "preposto_empresa":"", "advogado_empresa":"", "juiz":"", "cpf_cnpj":"", "conta_contrato_instalacao":"", "resumo_fatos":"", "data_fato_gerador":"", "valor_cnr":"", "sentenca_processo":"", "pagamento_danos":"", "decisao_favoravel_empresa":""}}"""

PROMPT_MOTIVO = """Classifique o motivo da reclassificação do processo encerrado, selecionando todas as categorias aplicáveis da lista abaixo. Devolva no formato JSON com valores booleanos.

**Motivos:**
- Reclassificação por erro na sentença
- Reclassificação por pagamento incorreto
- Reclassificação por recurso negado
- Outros motivos não especificados

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