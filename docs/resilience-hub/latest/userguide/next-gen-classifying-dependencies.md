---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-classifying-dependencies.html
---

# Classifying dependencies as hard or soft
<a name="next-gen-classifying-dependencies"></a>

After reviewing discovered dependencies, classify each one to indicate its failure impact:

```
aws resiliencehubv2 update-dependency \
  --service-arn "arn:aws:resiliencehub:..." \
  --dependency-id "{{dependency-id}}" \
  --criticality "HARD" \
  --comment "Payment processing fails completely without Stripe"
```

Use the following guidelines to classify dependencies:

| Classify as | When | Example |
| --- | --- | --- |
| Hard | Your service fails completely if this dependency is unavailable | Primary database, payment gateway, authentication service |
| Soft | Your service degrades but continues operating without this dependency | Analytics API, feature flags, recommendation engine |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
