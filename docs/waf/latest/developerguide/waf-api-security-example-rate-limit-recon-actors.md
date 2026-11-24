---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-security-example-rate-limit-recon-actors.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Capping the combined request rate of clients flagged for reconnaissance

This rule sets one shared request budget for the clients that the rule group flagged for reconnaissance. The scope-down statement limits the rule to requests that carry a recon-stage identity label. When the combined rate of those requests at one confidence tier goes over the limit, the rule blocks requests at that tier from every flagged client, until the rate drops below the limit.

The aggregation key is a `LabelNamespace` custom key. For a label namespace key, AWS WAF groups requests by the label name under the namespace. Here, the label name is the tier: `high`, `medium`, or `low`. All flagged clients at one tier share one counter, so this rule doesn't limit any single client. One busy client can push its tier over the limit, and then requests from other flagged clients at that tier are blocked too.

Use this rule when you want a ceiling on the total traffic from flagged clients, for example to protect a backend from reconnaissance spread across many clients. To limit each client separately, aggregate on a key that identifies the client, such as the IP address, as in [Rate-limiting reconnaissance instead of blocking it](waf-api-security-example-rate-limit-recon.md), or a header that carries the client's credentials.

```json
{
  "Name": "rate-limit-api-security-recon-actors",
  "Priority": 121,
  "Statement": {
    "RateBasedStatement": {
      "Limit": 500,
      "EvaluationWindowSec": 300,
      "AggregateKeyType": "CUSTOM_KEYS",
      "CustomKeys": [
        {
          "LabelNamespace": {
            "Namespace": "awswaf:managed:aws:api-security:recon:actor_identity:"
          }
        }
      ],
      "ScopeDownStatement": {
        "LabelMatchStatement": {
          "Scope": "NAMESPACE",
          "Key": "awswaf:managed:aws:api-security:recon:actor_identity:"
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
    "MetricName": "rate-limit-api-security-recon-actors"
  }
}
```

Note that both namespace values above end with a colon. A namespace match is a raw string prefix, so a value ending mid-segment would match more broadly than you intend.
