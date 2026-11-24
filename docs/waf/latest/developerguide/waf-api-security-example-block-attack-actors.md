---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-security-example-block-attack-actors.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Blocking a client that has attacked anywhere on your protection pack (web ACL)

The rule group already blocks an identity carrying an identity label at high confidence. An identity carrying `attack:actor_identity:medium` triggered an attack-stage detection at medium confidence somewhere on this protection pack (web ACL), which the rule group only counts. This rule blocks it as well, stopping its other requests, including requests to endpoints where it has done nothing yet.

Use this only where your own metrics show medium-confidence attack findings are reliable on your traffic.

```json
{
  "Name": "block-api-security-attack-actors",
  "Priority": 120,
  "Statement": {
    "LabelMatchStatement": {
      "Scope": "LABEL",
      "Key": "awswaf:managed:aws:api-security:attack:actor_identity:medium"
    }
  },
  "Action": {
    "Block": {}
  },
  "VisibilityConfig": {
    "SampledRequestsEnabled": true,
    "CloudWatchMetricsEnabled": true,
    "MetricName": "block-api-security-attack-actors"
  }
}
```
