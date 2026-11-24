---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-ai-security-example-config.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Configuring the rule group

**Assess requests and responses.** The following rule adds the rule group to a protection pack (web ACL) and sends both requests and responses to Amazon Bedrock Guardrails for assessment.

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
      ]
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

AWS WAF uses the role in `RoleArn` to call Amazon Bedrock Guardrails. The role must be in the same account as the protection pack (web ACL). The caller of `CreateWebACL` or `UpdateWebACL` needs `iam:PassRole` permission for the role. For the role's permissions and trust policy, see [The IAM role for AI Security](waf-ai-security-role.md).

`ManagedRuleGroupConfigs` takes exactly one `AWSManagedRulesAISecurityRuleSet` element. `BedrockGuardrails` takes exactly one of `ProtectRequestAndResponse`, `ProtectRequestOnly`, and `Disable`.

**Assess requests only.** The following configuration sends requests, but not responses, to Amazon Bedrock Guardrails. Use it in place of the `AWSManagedRulesAISecurityRuleSet` element in the previous example.

```json
{
  "AWSManagedRulesAISecurityRuleSet": {
    "BedrockGuardrails": {
      "ProtectRequestOnly": {
        "RoleArn": "arn:aws:iam::111122223333:role/AWSWAFAISecurityRole"
      }
    }
  }
}
```

With this configuration, the three response-phase prompt attack rules and the four sensitive information rules never match.

**Run only the checks that don't call Amazon Bedrock.** The following configuration sends nothing to Amazon Bedrock.

```json
{
  "AWSManagedRulesAISecurityRuleSet": {
    "BedrockGuardrails": {
      "Disable": {}
    }
  }
}
```

With `Disable`, the configuration names no role, so no `iam:PassRole` check runs. AWS WAF still charges the additional fee for each request that the rule group evaluates.
