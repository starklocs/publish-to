import pytest
import os
from unittest.mock import MagicMock
import google.generativeai as genai

# Importa a função do seu arquivo principal
from src.main import init_gemini, generate_documentation

# Simula a chave da API para evitar chamadas reais durante o teste
os.environ["GEMINI_API_KEY"] = "fake-api-key"

def test_init_gemini_returns_model():
    """Testa se a função init_gemini retorna uma instância do modelo."""
    model = init_gemini()
    assert isinstance(model, genai.GenerativeModel)
    assert model.model_name == "models/gemini-1.5-flash"

def test_generate_documentation_returns_text_on_success(mocker):
    """Testa se a função de geração retorna texto com um prompt válido."""
    # Mocka (simula) a resposta da API do Gemini
    mock_model = MagicMock()
    mock_response = MagicMock()
    mock_response.text = "Código documentado."
    mock_model.generate_content.return_value = mock_response
    
    # Substitui a chamada real da API pela versão mockada
    mocker.patch('src.main.genai.GenerativeModel', return_value=mock_model)
    
    code_prompt = "def my_function():\n    return 1"
    response_text = generate_documentation(mock_model, code_prompt)
    
    assert response_text == "Código documentado."

def test_generate_documentation_returns_error_on_exception(mocker):
    """Testa se a função lida com exceções e retorna uma mensagem de erro."""
    mock_model = MagicMock()
    mock_model.generate_content.side_effect = Exception("API error")
    
    mocker.patch('src.main.genai.GenerativeModel', return_value=mock_model)
    
    code_prompt = "código de teste"
    response_text = generate_documentation(mock_model, code_prompt)
    
    assert "Erro ao gerar documentação" in response_text