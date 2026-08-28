---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/quick-suite-access-approach/conclusion.html
---

# Conclusion
<a name="conclusion"></a>

This guide reviews a number of different approaches that you can use to provision user access to Amazon Quick. In some cases, you can even combine more than one approach to support different use cases. However, each additional approach adds complexity.

If all options are possible for your deployment, the recommended approach is to use the AWS IAM Identity Center built-in integration with Quick. To review this approach in more detail and determine whether any of the current feature limitations apply to your situation, see [Using IAM Identity Center](https://docs.aws.amazon.com/quicksuite/latest/userguide/setting-up-sso.html) in the Quick documentation.

When you choose an approach, consider how it will affect the user sign-in experience, security, and how to support it with access management operations and processes in your organization. Switching to a different approach in the future might be costly, or it might not be possible. Before setting up Quick, take the necessary time to assess what is best for your organization.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
