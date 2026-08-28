---
source_url: https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/visible-regions-services-prereqs.html
---

# Prerequisites for configuring visible Regions and services
<a name="visible-regions-services-prereqs"></a>

To view and change visible Regions and services settings, you need specific IAM permissions.
+ To view the settings, you need the `uxc:GetAccountCustomizations` permission.
+ To change the settings, you need the `uxc:UpdateAccountCustomizations` permission.

The AWS managed policies `AWSManagementConsoleBasicUserAccess` and `AWSManagementConsoleAdministratorAccess` include these permissions.

For more information, see [AWS managed policies for the AWS Management Console](security-iam-awsmanpol.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Management Console. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awsconsolehelpdocs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
