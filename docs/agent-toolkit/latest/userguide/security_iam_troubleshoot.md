---
source_url: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/security_iam_troubleshoot.html
---

# Troubleshooting AWS MCP Server identity and access
<a name="security_iam_troubleshoot"></a>

Use the following information to help you diagnose and fix common issues when working with AWS MCP Server and IAM.

**Topics**
+ [I get an access denied error when using AWS MCP Server](#security_iam_troubleshoot-access-denied)
+ [My Deny policy using aws-mcp actions no longer blocks access](#security_iam_troubleshoot-deprecated-actions)

## I get an access denied error when using AWS MCP Server
<a name="security_iam_troubleshoot-access-denied"></a>

If you receive an `AccessDenied` error when AWS MCP Server calls a downstream AWS service on your behalf, check the following:
+ Verify that your IAM role or user has the required permissions for the target AWS service action. AWS MCP Server uses your credentials, so you need the same permissions as you would for a direct API call.
+ Check whether any SCPs or permission boundaries include Deny statements that use `aws:ViaAWSMCPService` or `aws:CalledViaAWSMCP` conditions that block MCP server access.
+ If you previously used `aws-mcp:InvokeMcp` in Allow statements, note that these actions no longer have any effect. Your permissions for the downstream service are what matter.

## My Deny policy using aws-mcp actions no longer blocks access
<a name="security_iam_troubleshoot-deprecated-actions"></a>

If you previously used Deny statements with `aws-mcp:InvokeMcp`, `aws-mcp:CallReadOnlyTool`, or `aws-mcp:CallReadWriteTool` to block access to AWS MCP Server, these actions no longer have any effect. Update your policies to use the condition context keys instead:

```
{
    "Effect": "Deny",
    "Action": "*",
    "Resource": "*",
    "Condition": {
        "Bool": {
            "aws:ViaAWSMCPService": "true"
        }
    }
}
```
