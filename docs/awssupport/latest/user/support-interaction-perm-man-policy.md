---
source_url: https://docs.aws.amazon.com/awssupport/latest/user/support-interaction-perm-man-policy.html
---

# Option 1: Use the AWS managed policy (recommended)
<a name="support-interaction-perm-man-policy"></a>

If you currently have the AWSSupportAccess managed policy attached, no additional permissions are required. However, to continue to use the functions included in the [Support Center Console API](aws-support-console.md), you must add the Support Center Console operations to your IAM policies before November 2, 2026, if you don't already have them. To do this, update the AWS Support managed policy to include the `support-console:*` actions. For more information, see [Adding IAM policies for the Support Center Console API operations](support-console-access-control.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awssupport` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
