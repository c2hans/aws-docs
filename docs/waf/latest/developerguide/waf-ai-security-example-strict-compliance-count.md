---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-ai-security-example-strict-compliance-count.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Counting strict compliance violations without acting on them

The strict compliance rules count by default. The following rule matches the strict MCP level label, `protocol_compliance_level:strict:mcp`, and publishes the matches under its own metric name.

```json
{
  "Name": "Count-strict-mcp-compliance",
  "Priority": 130,
  "Statement": {
    "LabelMatchStatement": {
      "Scope": "LABEL",
      "Key": "awswaf:managed:aws:ai-security:protocol_compliance_level:strict:mcp"
    }
  },
  "Action": { "Count": {} },
  "VisibilityConfig": {
    "SampledRequestsEnabled": true,
    "CloudWatchMetricsEnabled": true,
    "MetricName": "Count-strict-mcp-compliance"
  }
}
```

The strict level includes the baseline checks, so this rule also counts requests that fail a baseline check. To count one individual check instead, match its per-check label, in the form `protocol_compliance_check:<check>`. The checks are listed on [AWS WAF AI Security rule group](aws-managed-rule-groups-ai-security.md).
