---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-ai-security-example-scope-down.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Scoping the rule group to your agentic endpoints

The following rule limits the rule group to requests whose URI path starts with `/v1/chat/completions` or `/mcp`.

```json
{
  "Name": "AI-Security",
  "Priority": 100,
  "Statement": {
    "ManagedRuleGroupStatement": {
      "VendorName": "AWS",
      "Name": "AWSManagedRulesAISecurityRuleSet",
      "ManagedRuleGroupConfigs": [
        {
          "AWSManagedRulesAISecurityRuleSet": {
            "BedrockGuardrails": {
              "ProtectRequestAndResponse": {
                "RoleArn": "arn:aws:iam::111122223333:role/AWSWAFAISecurityRole"
              }
            }
          }
        }
      ],
      "ScopeDownStatement": {
        "OrStatement": {
          "Statements": [
            {
              "ByteMatchStatement": {
                "FieldToMatch": { "UriPath": {} },
                "PositionalConstraint": "STARTS_WITH",
                "SearchString": "/v1/chat/completions",
                "TextTransformations": [
                  { "Priority": 0, "Type": "NONE" }
                ]
              }
            },
            {
              "ByteMatchStatement": {
                "FieldToMatch": { "UriPath": {} },
                "PositionalConstraint": "STARTS_WITH",
                "SearchString": "/mcp",
                "TextTransformations": [
                  { "Priority": 0, "Type": "NONE" }
                ]
              }
            }
          ]
        }
      }
    }
  },
  "OverrideAction": { "None": {} },
  "VisibilityConfig": {
    "SampledRequestsEnabled": true,
    "CloudWatchMetricsEnabled": true,
    "MetricName": "AI-Security"
  }
}
```

AWS WAF evaluates the rule group only for requests that match the scope-down statement. A request that the statement excludes isn't charged the additional fee for this rule group. Replace the paths with the paths of your own endpoints.
