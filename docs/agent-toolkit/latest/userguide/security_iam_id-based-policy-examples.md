---
source_url: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/security_iam_id-based-policy-examples.html
---

# Identity-based policy examples for AWS MCP Server
<a name="security_iam_id-based-policy-examples"></a>

The following examples show how to use IAM policies with the MCP condition context keys to control access through AWS MCP Server. Each example shows the policy statement to include within your IAM policy document.

**Topics**
+ [Deny all actions through any AWS managed MCP server](#security_iam_id-based-policy-examples-deny-all-mcp)
+ [Deny destructive actions through AWS MCP Server](#security_iam_id-based-policy-examples-deny-destructive)
+ [Restrict actions to a specific MCP server](#security_iam_id-based-policy-examples-restrict-specific-server)

## Deny all actions through any AWS managed MCP server
<a name="security_iam_id-based-policy-examples-deny-all-mcp"></a>

The following SCP or IAM policy denies all actions when the request originates from any AWS managed MCP server. Use this to completely block MCP server access across an organization or for specific principals.

```
{
    "Sid": "DenyAllActionsViaMCP",
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

## Deny destructive actions through AWS MCP Server
<a name="security_iam_id-based-policy-examples-deny-destructive"></a>

The following policy allows read operations but denies destructive actions when the request comes through AWS MCP Server. This lets AI agents inspect resources without being able to delete them.

```
[
    {
        "Sid": "AllowS3ReadOperations",
        "Effect": "Allow",
        "Action": [
            "s3:GetObject",
            "s3:ListBucket"
        ],
        "Resource": "*"
    },
    {
        "Sid": "DenyDeleteWhenAccessedViaMCP",
        "Effect": "Deny",
        "Action": [
            "s3:DeleteObject",
            "s3:DeleteBucket"
        ],
        "Resource": "*",
        "Condition": {
            "StringEquals": {
                "aws:CalledViaAWSMCP": "aws-mcp.amazonaws.com"
            }
        }
    }
]
```

## Restrict actions to a specific MCP server
<a name="security_iam_id-based-policy-examples-restrict-specific-server"></a>

The following policy denies all actions when the request comes specifically through AWS MCP Server, while allowing requests from other AWS managed MCP servers or direct API calls.

```
{
    "Sid": "DenyActionsViaAWSMCPServer",
    "Effect": "Deny",
    "Action": "*",
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "aws:CalledViaAWSMCP": "aws-mcp.amazonaws.com"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Agent Toolkit for AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agent-toolkit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
