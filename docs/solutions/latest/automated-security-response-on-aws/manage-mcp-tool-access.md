---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/manage-mcp-tool-access.html
---

# Manage MCP tool access
<a name="manage-mcp-tool-access"></a>

You can deploy the optional Model Context Protocol (MCP) server. Set **EnableMcpServer** to `yes` (see [MCP server for AI clients](mcp-server.md)), then connect an AI client as one of your Web UI users. That client can call only the tools you granted that user. Managing these grants is an administrator-only task.

To manage a user’s tool access, open the **View Users** page in the Web UI and choose the user. Then use the **Tool Permissions** list. The list groups tools into seven categories: Discovery and triage, Reporting, Notifications, Remediation, Infrastructure and deployment, Policy and controls, and Other. You can grant or revoke an entire category at once, or grant or revoke an individual tool within it.

To grant a tool, select its **Granted** check box. To revoke the tool, clear the check box. A category’s check box grants or revokes every tool in that category. Choose **Save** to apply your changes.

The following screenshot shows the **Tool Permissions** list for a delegated administrator. Each category row shows a count of its granted tools, such as **0 of 3 granted**. Each tool row shows its minimum tier and a **Granted** check box.

 **Tool Permissions for a user on the View Users page**

![Tool Permissions list with per-category grant counts and each tool’s minimum tier and Granted check box.](https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/user-tool-permissions.png)

Each tool shows its minimum tier, the lowest role tier that you can grant it to. Grants are tier-scoped. You cannot grant an **Account Operator** a tool whose minimum tier is **Delegated Admin**. The list shows only the tools that the user’s role tier allows. Administrators receive every tool automatically and don’t need grants. A user can call a tool through the MCP server only when both of these conditions hold:
+ You granted the user that tool.
+ The user’s role tier includes that tool.

Revoking a grant takes effect for new tool calls. The MCP server checks the user’s current grants on each call. For how a user connects a client once you have granted them tools, see [Connect an AI client to the MCP server](connect-an-ai-client-to-the-mcp-server.md).
