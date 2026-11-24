---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-ai-security-example-rollout-overrides.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Overriding the blocking rules during rollout

The following overrides set each of the blocking rules to Count. Because each rule has its own override, you can later remove the overrides one rule at a time.

```json
"RuleActionOverrides": [
  {
    "Name": "Compliance_BaselineMCP",
    "ActionToUse": { "Count": {} }
  },
  {
    "Name": "Compliance_BaselineA2A",
    "ActionToUse": { "Count": {} }
  },
  {
    "Name": "Request_GuardrailsPromptAttackHighSeverity",
    "ActionToUse": { "Count": {} }
  },
  {
    "Name": "Response_GuardrailsPromptAttackHighSeverity",
    "ActionToUse": { "Count": {} }
  }
]
```

An override of a `Response_` rule must be Count, or Block without a custom response. AWS WAF rejects any other override of these rules, and the error names the rule.
