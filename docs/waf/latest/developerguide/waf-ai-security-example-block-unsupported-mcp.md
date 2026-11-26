---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-ai-security-example-block-unsupported-mcp.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Blocking MCP requests at unsupported protocol versions

The rule group recognizes MCP traffic at protocol versions `2025-06-18`, `2025-11-25`, and `2026-07-28` only. It labels a request at any other version `traffic:not_recognized`. It doesn't check that request for protocol compliance or send it for assessment. To keep clients from reaching your MCP server without these checks, block these requests. You can add a rule of your own that matches the label on your MCP endpoint, or, for a stricter setting, override the rule group's `Not_Recognized` rule to Block.

**Block unrecognized requests to your MCP endpoint.** The following rule blocks requests whose URI path starts with `/mcp` and that carry the `traffic:not_recognized` label.

```json
{
  "Name": "Block-unsupported-mcp-versions",
  "Priority": 150,
  "Statement": {
    "AndStatement": {
      "Statements": [
        {
          "ByteMatchStatement": {
            "FieldToMatch": { "UriPath": {} },
            "PositionalConstraint": "STARTS_WITH",
            "SearchString": "/mcp",
            "TextTransformations": [
              { "Priority": 0, "Type": "NONE" }
            ]
          }
        },
        {
          "LabelMatchStatement": {
            "Scope": "LABEL",
            "Key": "awswaf:managed:aws:ai-security:traffic:not_recognized"
          }
        }
      ]
    }
  },
  "Action": { "Block": {} },
  "VisibilityConfig": {
    "SampledRequestsEnabled": true,
    "CloudWatchMetricsEnabled": true,
    "MetricName": "Block-unsupported-mcp-versions"
  }
}
```

The rule blocks the following requests to the path:
+ A request whose `MCP-Protocol-Version` header names a version that the rule group doesn't recognize, such as `2025-03-26`.
+ A request that has no `MCP-Protocol-Version` header and names no supported version in its body. Clients at `2025-03-26` and earlier don't send this header.
+ An `initialize` request whose `params.protocolVersion` is an earlier version.

The rule doesn't block an `initialize` request at a supported version that has no `MCP-Protocol-Version` header. The rule group reads the version from `params.protocolVersion` in the body.

The rule also blocks any other request to the path that the rule group doesn't recognize. Replace `/mcp` with the path of your MCP endpoint, and keep other paths, such as `/.well-known/`, out of the match. Place the rule after the rule group. The rule group adds the label only to requests that it evaluates, so if the rule group has a scope-down statement, make sure that the statement includes the path.

**Block every request that the rule group doesn't recognize.** The following override sets the rule group's `Not_Recognized` rule to Block.

```json
"RuleActionOverrides": [
  {
    "Name": "Not_Recognized",
    "ActionToUse": { "Block": {} }
  }
]
```

The override blocks every request that the rule group evaluates and doesn't recognize. Besides MCP requests at earlier versions, this includes A2A 0.3 requests, requests to LLM operations that the rule group doesn't recognize, and any other traffic in the rule group's scope. Use the override only when a scope-down statement limits the rule group to your agentic endpoints. For an example, see [Scoping the rule group to your agentic endpoints](waf-ai-security-example-scope-down.md).

With either option, start in Count. Set your rule's action to Count, or leave `Not_Recognized` at its default Count action. Review the matches in your logs, and move your clients to a supported version before you block.
