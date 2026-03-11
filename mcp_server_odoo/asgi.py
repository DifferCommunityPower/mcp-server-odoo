"""ASGI entry point for running OdooMCPServer with an external server.

Usage with uvicorn:
    uvicorn mcp_server_odoo.asgi:app --host 0.0.0.0 --port 8000

Or with gunicorn + uvicorn workers:
    gunicorn mcp_server_odoo.asgi:app -w 1 -k uvicorn.workers.UvicornWorker

The lifespan (Odoo connection setup/teardown) is handled automatically
by the Starlette app returned from FastMCP.http_app().
"""

from .config import load_config
from .server import OdooMCPServer

_server = OdooMCPServer(load_config())
app = _server.http_app()
