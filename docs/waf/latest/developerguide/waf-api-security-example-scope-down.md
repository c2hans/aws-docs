---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-security-example-scope-down.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Limiting evaluation to your API paths

A scope-down statement narrows the requests the rule group evaluates. It is the primary cost control for this rule group. Scoping to the paths that serve your APIs also keeps your web front end out of the behavioral baseline.

Excluded traffic is excluded from the baseline as well as from billing. Scope to the endpoints you want to protect, rather than to a sample of them.

```json
{
  "Name": "AWS-AWSManagedRulesAPISecurityRuleSet",
  "Priority": 100,
  "Statement": {
    "ManagedRuleGroupStatement": {
      "VendorName": "AWS",
      "Name": "AWSManagedRulesAPISecurityRuleSet",
      "ScopeDownStatement": {
        "ByteMatchStatement": {
          "SearchString": "/api/",
          "FieldToMatch": {
            "UriPath": {}
          },
          "TextTransformations": [
            {
              "Priority": 0,
              "Type": "NONE"
            }
          ],
          "PositionalConstraint": "STARTS_WITH"
        }
      }
    }
  },
  "OverrideAction": {
    "None": {}
  },
  "VisibilityConfig": {
    "SampledRequestsEnabled": true,
    "CloudWatchMetricsEnabled": true,
    "MetricName": "AWS-AWSManagedRulesAPISecurityRuleSet"
  }
}
```
