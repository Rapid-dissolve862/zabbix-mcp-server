#
# Zabbix MCP Server
# Copyright (C) 2026 initMAX s.r.o.
#

"""Zabbix server status views — read-only overview + connection test."""

from __future__ import annotations

import asyncio
import logging

from starlette.requests import Request
from starlette.responses import JSONResponse, RedirectResponse, Response

logger = logging.getLogger("zabbix_mcp.admin")


async def servers_view(request: Request) -> Response:
    admin_app = request.app.state.admin_app
    session = admin_app.require_auth(request)
    if not session:
        return RedirectResponse("/login", status_code=303)

    client_manager = admin_app.client_manager
    servers = []

    for name in client_manager.server_names:
        srv_config = client_manager.get_server_config(name)
        try:
            version = client_manager.get_version(name)
            status = "online"
            error_msg = None
        except Exception as e:
            version = None
            status = "error"
            error_msg = str(e)

        servers.append({
            "name": name,
            "url": srv_config.url,
            "status": status,
            "version": version,
            "read_only": srv_config.read_only,
            "verify_ssl": srv_config.verify_ssl,
            "error": error_msg,
        })

    return admin_app.render("servers.html", request, {
        "active": "servers",
        "servers": servers,
    })


async def server_test(request: Request) -> Response:
    """Test connection to a specific Zabbix server (HTMX endpoint)."""
    admin_app = request.app.state.admin_app
    session = admin_app.require_auth(request)
    if not session:
        return JSONResponse({"error": "Unauthorized"}, status_code=401)

    server_name = request.path_params["server_name"]
    client_manager = admin_app.client_manager

    try:
        await asyncio.to_thread(client_manager.check_connection, server_name)
        version = client_manager.get_version(server_name)
        return JSONResponse({
            "status": "online",
            "version": version,
            "message": f"Connected to Zabbix {version}",
        })
    except Exception as e:
        return JSONResponse({
            "status": "error",
            "message": str(e),
        }, status_code=200)  # 200 so HTMX processes the response
