---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-billing-transition.html
---

# Pricing transition
<a name="next-gen-billing-transition"></a>

The following table shows how pricing components map from AWS Resilience Hub v1 to the next generation of Resilience Hub.

| Component | AWS Resilience Hub v1 | Next generation Resilience Hub |
| --- | --- | --- |
| Base fee | $15/application/month | $15/service/month |
| Assessments included | Unlimited | 2 per month |
| Resource overage | None | $0.10/resource above 150 per assessment |
| Dependency discovery | Not available | $10/service/month (optional) |

The $15 entry price is preserved. Most customers (services with 150 or fewer resources using 2 or fewer assessments per month) pay the same amount.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
