---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/isv-troubleshooting.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Troubleshooting
<a name="isv-troubleshooting"></a>

If ISVs encounter issues with accessing the Amazon Q index, consider the following.

1. Verify the Identity and Access Management (IAM) role and permissions.

1. Check the configuration of the redirect URL for the oauth flow.

1. Confirm that the customer has granted the necessary access permissions to the ISV.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
