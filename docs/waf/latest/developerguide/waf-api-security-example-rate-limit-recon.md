---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-security-example-rate-limit-recon.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Rate-limiting reconnaissance instead of blocking it

Reconnaissance on its own is weak evidence: a single probe against an endpoint that doesn't exist is something ordinary clients do. Reconnaissance at volume from one client is not.

This rule rate-limits clients labeled with reconnaissance-stage `enumeration`, so an occasional probe is unaffected and bulk enumeration is throttled. It provides the graduated response that a block-or-nothing rule can't express.

```json
{
  "Name": "rate-limit-api-security-recon-enumeration",
  "Priority": 112,
  "Statement": {
    "RateBasedStatement": {
      "Limit": 300,
      "EvaluationWindowSec": 300,
      "AggregateKeyType": "IP",
      "ScopeDownStatement": {
        "LabelMatchStatement": {
          "Scope": "NAMESPACE",
          "Key": "awswaf:managed:aws:api-security:recon:enumeration:"
        }
      }
    }
  },
  "Action": {
    "Block": {}
  },
  "VisibilityConfig": {
    "SampledRequestsEnabled": true,
    "CloudWatchMetricsEnabled": true,
    "MetricName": "rate-limit-api-security-recon-enumeration"
  }
}
```
