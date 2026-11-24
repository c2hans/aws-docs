---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-security-example-rule-overrides.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Overriding the action on individual rules

Use `RuleActionOverrides` to change the action on named rules while leaving the rest as configured. This is the targeted alternative to overriding the entire rule group.

The following example blocks two posture rules that count by default: `Method_Unsafe_Method`, because a production API has no reason to serve the `TRACE` or `TRACK` method, and `MissingExpiry_JWT_Payload`.

The behavioral rules can be overridden the same way, one detection at one confidence (for example, `APISecurityCredStuffingHigh`). Rule names are the API contract. AWS WAF ignores an override that names a rule the group doesn't ship, so a misspelled name saves without error and configures nothing. Take names from the rules listing at [AWS WAF API Security rule group](aws-managed-rule-groups-api-security.md).

```json
{
  "Name": "AWS-AWSManagedRulesAPISecurityRuleSet",
  "Priority": 100,
  "Statement": {
    "ManagedRuleGroupStatement": {
      "VendorName": "AWS",
      "Name": "AWSManagedRulesAPISecurityRuleSet",
      "RuleActionOverrides": [
        {
          "Name": "Method_Unsafe_Method",
          "ActionToUse": {
            "Block": {}
          }
        },
        {
          "Name": "MissingExpiry_JWT_Payload",
          "ActionToUse": {
            "Block": {}
          }
        }
      ]
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
