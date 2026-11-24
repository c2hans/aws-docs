---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-ai-security-example-single-category.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Acting on a single finding category

The rule group's own rules act on a safeguard and a tier. To act on one Amazon Bedrock category, match its category label in a rule of your own. The following rule blocks a jailbreak finding at high severity.

```json
{
  "Name": "Block-jailbreak-high",
  "Priority": 110,
  "Statement": {
    "LabelMatchStatement": {
      "Scope": "LABEL",
      "Key": "awswaf:managed:aws:ai-security:guardrails:prompt_attack:jailbreak:severity:high"
    }
  },
  "Action": { "Block": {} },
  "VisibilityConfig": {
    "SampledRequestsEnabled": true,
    "CloudWatchMetricsEnabled": true,
    "MetricName": "Block-jailbreak-high"
  }
}
```

If you also override `Request_GuardrailsPromptAttackHighSeverity` to Count, as in the rollout example, this rule blocks high-severity jailbreak findings, and the other high-severity prompt attack findings are counted.

Your own rules run in the request phase only. A rule that matches a finding label acts on request findings, not response findings. To act on a response finding, override the rule group's own `Response_` rule.

To cover the medium and low tiers as well, put one `LabelMatchStatement` for each tier in an `OrStatement`. The labels differ only in their last element.

Alternatively, match the shared prefix `awswaf:managed:aws:ai-security:guardrails:prompt_attack:jailbreak:` with `Scope` set to `NAMESPACE`. This matches every tier. A `NAMESPACE` key must end with a colon at an element boundary. A key without the trailing colon, or one that ends partway through an element, matches nothing.

To write the same rule for another category, substitute its name. The categories that AWS WAF requests are listed on [AWS WAF AI Security rule group](aws-managed-rule-groups-ai-security.md). What each one detects is described in the Amazon Bedrock User Guide under [Detect prompt attacks](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-prompt-attack.html), [content filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters.html), and [sensitive information filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html).
