---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-least-privilege.html
---

# Least privilege recommendations
<a name="next-gen-least-privilege"></a>

Follow these recommendations to apply least privilege principles to your Next generation Resilience Hub configuration:

1. **Use ExternalId for cross-account roles** – The `ExternalId` condition in cross-account trust policies prevents confused deputy attacks.

1. **Use Organizations Service-Linked Roles** – Avoid manual cross-account role setup when possible. Service-Linked Roles provide automatically scoped, auditable access.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
