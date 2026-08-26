import os
import sys

import pytest

# La prueba corre sobre el codigo fuente del repositorio (ANTES del despliegue),
# no contra la API que ya esta publicada en produccion.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backend'))

from app import app  # noqa: E402


@pytest.fixture
def cliente():
    app.config['TESTING'] = True
    with app.test_client() as cliente:
        yield cliente


def test_ruta_principal_devuelve_200(cliente):
    """Una peticion GET a la ruta principal (/) debe devolver exactamente 200 OK."""
    respuesta = cliente.get('/')
    assert respuesta.status_code == 200
