---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-security-example-minimum.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Minimum viable configuration

The simplest configuration adds the rule group with its default settings. Every rule runs with the action configured inside the rule group: the rules that identify JWT attack techniques block, the posture and reconnaissance rules count, and the behavioral detections take the action set for the confidence they emit.

Use this configuration after you have completed testing. For a first deployment, use the counting example that follows.

```json
{
  "Name": "AWS-AWSManagedRulesAPISecurityRuleSet",
  "Priority": 100,
  "Statement": {
    "ManagedRuleGroupStatement": {
      "VendorName": "AWS",
      "Name": "AWSManagedRulesAPISecurityRuleSet"
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
