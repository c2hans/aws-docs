---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/mcp-server-architecture.html
---

# MCP server

The Model Context Protocol (MCP) is an open protocol that lets AI applications discover and call tools. The solution provides a remote MCP server so that AI coding tools such as Kiro, Claude Code, Codex, and Cursor can call the solution API as tools. A remote MCP server runs in AWS and is accessed over HTTPS, instead of running on the user’s computer. The solution hosts it on [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) Gateway, a managed service that exposes APIs as MCP tools. For setup instructions, see [Remote MCP server](mcp-server.md).

The MCP server consists of the following components:
+ The **gateway** uses IAM authorization, and the solution’s AWS KMS key encrypts it. The gateway is named `ISB-<namespace>-SandboxAgentGateway`.
+ One **gateway target** comes from the OpenAPI definition of the solution API. Each API operation becomes one tool, so the tools follow the REST API.
+ A **policy engine** in enforce mode holds one Cedar policy for each role: User, Manager, and Admin. Each policy permits the tools that the API allows for that role, and the engine denies every other tool. The gateway also lists only the permitted tools to the caller. For the tools of each role, see [Tools available to each role](mcp-server.md#mcp-server-tools).
+ The **client script**, `isb_mcp.py`, runs on the user’s computer. The AI coding tool starts the script, which connects the tool to the remote MCP server through the open-source [MCP Proxy for AWS](https://github.com/aws/mcp-proxy-for-aws) on the GitHub website. The script signs in the user and signs each request. It doesn’t host any tools itself.
+ A public **Amazon Cognito app client** in the Data stack, named `<namespace>-isb-mcp`, handles the sign-in.

A tool call follows this path:

1. The user runs the `login` command. The script opens a browser, where the user signs in through IAM Identity Center. The app client returns the result to a loopback address on port 29367, 29368, or 29369 of the user’s computer. The script stores the Cognito refresh token on the computer in a file that only the user reads. The refresh token is valid for 7 days by default.

1. When the AI coding tool starts the script, the script reads the Cognito and gateway settings from the `/config.json` file of the web UI.

1. For each request, the script obtains a current ID token and temporary credentials from the Cognito identity pool. The credentials map to the User, Manager, or Admin tier as they do for the web UI. The script signs the request with SigV4 and adds the ID token in the `x-isb-identity` header.

1. The gateway checks the IAM authorization, and then evaluates the Cedar policy for the caller’s role. The identity pool role of each tier has permission to invoke the gateway.

1. The gateway calls the REST API with its own execution role, which has permission to invoke only this REST API, and forwards the `x-isb-identity` header.

1. The Lambda function behind the operation verifies the ID token and enforces role-based access through the same middleware as for web UI requests. A role that the API does not allow receives a 403 error.

**Note**
The MCP server exposes only solution API operations. No tool returns AWS credentials for a sandbox account, so an AI coding tool deploys resources through an AWS CLI profile that the user signs in to through IAM Identity Center. For more information, see [Deploy resources in your sandbox account](mcp-server.md#mcp-server-deploy-resources). The Sandbox Spaces agent does not call the MCP server.
