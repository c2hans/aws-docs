---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-security-example-block-threat-family.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Blocking one threat family at any confidence

Confidence sits last in the label precisely so that you can match a stage and finding as a namespace and catch every confidence in one rule. This is the composition the label order was designed for.

The following rule blocks object level authorization abuse at the attack stage, regardless of the confidence the rule group assigned, without affecting any other finding.

The trade-off of this ordering is the reverse case: you can't prefix-match every high-confidence finding across the rule group in a single rule, because confidence is the last position rather than the first.

```json
{
  "Name": "block-api-security-attack-object-level",
  "Priority": 110,
  "Statement": {
    "LabelMatchStatement": {
      "Scope": "NAMESPACE",
      "Key": "awswaf:managed:aws:api-security:attack:object_level:"
    }
  },
  "Action": {
    "Block": {}
  },
  "VisibilityConfig": {
    "SampledRequestsEnabled": true,
    "CloudWatchMetricsEnabled": true,
    "MetricName": "block-api-security-attack-object-level"
  }
}
```
