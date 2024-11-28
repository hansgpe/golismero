# requests_ntlm/__init__.py

# Función para hacer la importación perezosa de HttpNtlmAuth
def get_http_ntlm_auth():
    from . import HttpNtlmAuth  # Importación local dentro de la función
    return HttpNtlmAuth

# Definir __all__ para exportar la función que proporciona HttpNtlmAuth
__all__ = ['get_http_ntlm_auth']
