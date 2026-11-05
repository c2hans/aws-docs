---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/agent-access-mcp-server-session-cleanup.html
---

# Session cleanup
<a name="agent-access-mcp-server-session-cleanup"></a>

When your agent finishes its work, it ends its connection to the Model Context Protocol (MCP) server. Session cleanup controls what happens to the underlying streaming session at that point: you can let it keep running until the disconnect timeout, or expire it right away.

You control this by setting the `x-amzn-agentaccess-expire-streaming-session-on-delete` header on your MCP requests. The following values are available:
+ **true**: when your agent sends an explicit HTTP `DELETE` request, the MCP server expires the WorkSpaces Applications streaming session as part of cleanup. This terminates the underlying streaming instance and triggers the fleet's configured autoscaling policy. For more information, see [Fleet Auto Scaling for Amazon WorkSpaces Applications](autoscaling.md).
+ **false** (default): the streaming session continues running until the disconnect timeout is reached. For more information about the disconnect timeout, see [Create a Fleet in Amazon WorkSpaces Applications](set-up-stacks-fleets-create.md).

**Note**
By default, an `mcp-proxy-for-aws` MCP client handles the `DELETE` request for you when you properly end the client lifecycle.
