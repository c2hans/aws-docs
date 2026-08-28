---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-assessment-history.html
---

# Assessment history and trends
<a name="next-gen-assessment-history"></a>

Next generation Resilience Hub retains assessment history for 2 years, enabling you to:
+ Track how your resilience posture improves over time.
+ See which findings have been resolved versus remain open.
+ Identify recurring issues across assessments.
+ Generate compliance reports showing improvement trends.

**To view assessment history (CLI)**

```
aws resiliencehubv2 list-failure-mode-assessments \
  --service-arn "arn:aws:resiliencehub:..."
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
