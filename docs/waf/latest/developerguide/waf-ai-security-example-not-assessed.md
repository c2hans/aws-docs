---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-ai-security-example-not-assessed.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Finding recognized traffic that AWS WAF didn't assess

The following rule counts requests that carry a traffic recognition label and the not-assessed label. These requests reach the rule group, but AWS WAF sends no text from them for assessment.

```json
{
  "Name": "Count-recognized-but-not-assessed",
  "Priority": 140,
  "Statement": {
    "AndStatement": {
      "Statements": [
        {
          "LabelMatchStatement": {
            "Scope": "NAMESPACE",
            "Key": "awswaf:managed:aws:ai-security:traffic:"
          }
        },
        {
          "LabelMatchStatement": {
            "Scope": "LABEL",
            "Key": "awswaf:managed:aws:ai-security:guardrails:not_assessed"
          }
        }
      ]
    }
  },
  "Action": { "Count": {} },
  "VisibilityConfig": {
    "SampledRequestsEnabled": true,
    "CloudWatchMetricsEnabled": true,
    "MetricName": "Count-recognized-but-not-assessed"
  }
}
```

This rule doesn't count recognized operations that AWS WAF never sends for assessment, such as MCP methods other than `tools/call`. Those requests get no outcome label.
