---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-ai-security-example-block-unassessed.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Blocking messages that AWS WAF couldn't assess

By default, when a call to Amazon Bedrock fails, the rule group counts the message and the message passes without assessment. The following override blocks these messages instead.

```json
"RuleActionOverrides": [
  {
    "Name": "Guardrails_CallFailed",
    "ActionToUse": { "Block": {} }
  }
]
```

The override applies in both the request phase and the response phase. It also blocks messages whose calls AWS WAF held back and labeled with the reason `service_unavailable`.
