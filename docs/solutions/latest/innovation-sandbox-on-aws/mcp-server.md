---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/mcp-server.html
---

# Remote MCP server

The solution provides a remote Model Context Protocol (MCP) server so that you can use the solution from AI coding tools such as Kiro, Claude Code, Codex, and Cursor. From the AI coding tool, you can list lease templates, request leases, and check the status and budget of your leases. You sign in with your Innovation Sandbox account, and you don’t need AWS credentials of your own. For how the server works, see [MCP server](mcp-server-architecture.md).

The MCP server is for interactive use in an AI coding tool. To call the solution API from scripts, CI/CD pipelines, or scheduled jobs, use [Machine-to-machine (M2M) access](m2m-access.md) instead.

The AI coding tool connects to the remote MCP server through a client script, `isb_mcp.py`, that runs on your computer. The script signs you in and signs each request. It’s available in the [`scripts/mcp` folder](https://github.com/aws-solutions/innovation-sandbox-on-aws/tree/main/scripts/mcp) of the GitHub repository.

## Prerequisites
<a name="mcp-server-prerequisites"></a>
+ Python 3.10 or later.
+  [uv](https://docs.astral.sh/uv/getting-started/installation/). To check that uv is installed, run `uvx --version`.
+ The `isb_mcp.py` script from the [`scripts/mcp` folder](https://github.com/aws-solutions/innovation-sandbox-on-aws/tree/main/scripts/mcp).
+ The URL of your Innovation Sandbox web UI. For how to find it, see [Logging into the web UI](log-in-webui.md).
+ An Innovation Sandbox user with the Admin, Manager, or User role.

The script uses `uvx` to run the open-source [MCP Proxy for AWS](https://github.com/aws/mcp-proxy-for-aws) on the GitHub website in an isolated environment, so nothing is installed into your system Python.

## Connect an AI coding tool
<a name="mcp-server-connect"></a>

1. Set the `ISB_URL` environment variable to the URL of your web UI. Replace `<your-web-ui-domain>` with the domain of your web UI.

   ```bash
   export ISB_URL='https://<your-web-ui-domain>'
   ```

   The script reads everything else it needs, such as the [Amazon Cognito](https://aws.amazon.com/cognito/) settings and the gateway URL, from the deployment’s public `/config.json` file.

1. Sign in. A browser opens, and you sign in the same way as to the web UI. On a computer without a browser, see [Sign in on a remote computer](#mcp-server-remote-sign-in).

   ```bash
   python3 isb_mcp.py login
   ```

1. (Optional) Check the connection. The following command lists the tools that your role can use and makes one read-only call:

   ```bash
   python3 isb_mcp.py probe
   ```

1. Add the server to the MCP configuration file of your AI coding tool. Use the absolute path to the script, and replace `<your-web-ui-domain>` with the domain of your web UI. For Codex, add the same values as a TOML table. The following entry works for Kiro, Claude Code, and Cursor:

   ```json
   {
     "mcpServers": {
       "isb": {
         "command": "python3",
         "args": ["/absolute/path/to/isb_mcp.py", "serve"],
         "env": { "ISB_URL": "https://<your-web-ui-domain>" }
       }
     }
   }
   ```

   The following table lists the configuration file for each AI coding tool.

<table>
<thead>
  <tr><th>AI coding tool</th><th>Configuration file</th></tr>
</thead>
<tbody>
  <tr><td>Kiro</td><td> <code>~/.kiro/settings/mcp.json</code> </td></tr>
  <tr><td>Claude Code</td><td> <code>~/.claude.json</code>, or add the server with <code>claude mcp add</code> </td></tr>
  <tr><td>Cursor</td><td> <code>~/.cursor/mcp.json</code> </td></tr>
  <tr><td>Codex</td><td> <code>~/.codex/config.toml</code>, as an <code>[mcp_servers.isb]</code> table with the same <code>command</code>, <code>args</code>, and <code>env</code> values</td></tr>
</tbody>
</table>

1. Restart the AI coding tool so that it loads the server.

1. Ask the tool a question, for example, *"List my Innovation Sandbox leases."*

Your sign-in lasts 7 days by default. When it expires, the server prompts you to sign in again the next time it starts, or you can run the `login` command again.

## Client script commands
<a name="mcp-server-commands"></a>

The following table describes the commands of the client script.

| Command | Description |
| --- | --- |
|  `serve`  | Runs the MCP server connection over standard input and output. Your AI coding tool runs this command. If you aren’t signed in, it opens a browser, and it stops waiting after 45 seconds. |
|  `login`  | Signs you in from a terminal. Run it before you first use the server. |
|  `login --manual-callback`  | Signs you in with a browser on another computer or in a private window. For more information, see [Sign in on a remote computer](#mcp-server-remote-sign-in). |
|  `logout`  | Signs you out and deletes your sign-in from the computer. A running server keeps working for up to one hour, so restart it to stop it immediately. |
|  `status`  | Shows the account and role that you’re signed in with. |
|  `probe`  | Connects, lists your tools, and makes one read-only tool call. |

The script stores your sign-in in `~/.config/innovation-sandbox/mcp/` (`%APPDATA%\innovation-sandbox\mcp` on Windows), in a file that only you can read.

## Sign in on a remote computer
<a name="mcp-server-remote-sign-in"></a>

On a computer without a browser, such as a server that you connect to over Secure Shell (SSH), sign in with a browser on your own computer:

1. On the remote computer, run the following command. It prints a sign-in URL and waits at a `>` prompt.

   ```bash
   python3 isb_mcp.py login --manual-callback
   ```

1. Open the URL in a browser on your own computer, and sign in.

1. The browser opens `http://localhost:29367/callback?code=…​` and the page fails to load. This is expected, because the sign-in result is in the address bar.

1. Copy the full URL from the address bar, and paste it at the `>` prompt on the remote computer.

Complete these steps within a few minutes. The code in the URL works only once and expires quickly. If it expires, run the command again.

**Tip**
If you connect with `ssh`, you can forward the callback ports instead. The client script uses the first free port of 29367, 29368, and 29369, so forward all three:

```bash
ssh -L 29367:localhost:29367 -L 29368:localhost:29368 -L 29369:localhost:29369 <host>
```
Replace `<host>` with the host name or address of the remote computer. Then run `python3 isb_mcp.py login` on the remote computer, and open the printed URL on your own computer. If the sign-in doesn’t complete, use `login --manual-callback` instead.

## Tools available to each role
<a name="mcp-server-tools"></a>

Each operation of the solution’s REST API is a tool. You see only the tools for the operations that your role can perform. For the actions of each role, see [Available actions per role](use-the-solution.md#available-actions-per-role). Actions that don’t use the REST API, such as chatting in a Sandbox Space, have no tool. If you call a tool that your role doesn’t allow, the call fails with a 403 error. To check your role, run the `status` command.

## Deploy resources in your sandbox account
<a name="mcp-server-deploy-resources"></a>

Your AI coding tool can use the MCP server only to access the solution. No tool returns AWS credentials for your sandbox account. To create resources in your sandbox account from the AI coding tool, configure an AWS CLI profile that signs in through IAM Identity Center. For example, use the `aws configure sso` command. Then ask the tool to use that profile. For how to access your sandbox account, see [Logging in to an account](user-section.md#account-log-in).

For instructions on troubleshooting the client script, see the README file in the [`scripts/mcp` folder](https://github.com/aws-solutions/innovation-sandbox-on-aws/tree/main/scripts/mcp).
