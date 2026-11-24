---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-ai-security-example-anonymous-clients.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Blocking a prompt attack only from unauthenticated clients

The following rule blocks a request that has a prompt attack finding at any severity and has no `Authorization` header.

```json
{
  "Name": "Block-prompt-attack-when-anonymous",
  "Priority": 120,
  "Statement": {
    "AndStatement": {
      "Statements": [
        {
          "LabelMatchStatement": {
            "Scope": "NAMESPACE",
            "Key": "awswaf:managed:aws:ai-security:request:guardrails:prompt_attack:"
          }
        },
        {
          "NotStatement": {
            "Statement": {
              "SizeConstraintStatement": {
                "FieldToMatch": {
                  "SingleHeader": { "Name": "authorization" }
                },
                "ComparisonOperator": "GT",
                "Size": 0,
                "TextTransformations": [
                  { "Priority": 0, "Type": "NONE" }
                ]
              }
            }
          }
        }
      ]
    }
  },
  "Action": { "Block": {} },
  "VisibilityConfig": {
    "SampledRequestsEnabled": true,
    "CloudWatchMetricsEnabled": true,
    "MetricName": "Block-prompt-attack-when-anonymous"
  }
}
```

The `LabelMatchStatement` matches the three request-phase prompt attack labels. The `NotStatement` matches a request whose `Authorization` header is missing or empty. For these requests, the rule blocks medium-severity and low-severity findings, which the rule group counts by default. If a proxy in front of your resource removes or renames the `Authorization` header, match the header your proxy sets.
