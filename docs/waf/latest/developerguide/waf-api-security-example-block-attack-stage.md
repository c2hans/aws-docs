---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-security-example-block-attack-stage.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Blocking every request where attack-stage activity was detected

Matching the stage alone blocks any request carrying any attack-stage detection, regardless of the finding and regardless of the confidence. Use this when you want one rule expressing "act on everything the rule group considers an attack" rather than one rule per finding. Keep the rule group's own rules in Count so the decision lives in your rule.

```json
{
  "Name": "block-api-security-attack-stage",
  "Priority": 111,
  "Statement": {
    "LabelMatchStatement": {
      "Scope": "NAMESPACE",
      "Key": "awswaf:managed:aws:api-security:attack:"
    }
  },
  "Action": {
    "Block": {}
  },
  "VisibilityConfig": {
    "SampledRequestsEnabled": true,
    "CloudWatchMetricsEnabled": true,
    "MetricName": "block-api-security-attack-stage"
  }
}
```
