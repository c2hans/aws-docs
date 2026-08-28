---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-federation-space-view-users-groups.html
---

Amazon CodeCatalyst will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For more information, see [Migrating from Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/migration.html).

# Viewing SSO users and groups for a space
<a name="managing-federation-space-view-users-groups"></a>

You must have the **Space administrator** role and access to the billing account for your space to view SSO users and groups for your space. You cannot directly add or remove SSO users or groups in CodeCatalyst.

**Note**
Users or groups that are added to IAM Identity Center assignments usually appear in CodeCatalyst within two hours. Depending on the amount of data being synchronized, this process might take longer.

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. To view users in each group, choose the group. To view application details in the AWS Management Console, choose **View application**.

   To view information in IAM Identity Center, choose **IAM Identity Center**. You will be taken to IAM Identity Center, where you can work with your Identity federation administrator to configure SSO users and groups for your instance in IAM Identity Center.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
