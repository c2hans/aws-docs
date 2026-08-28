---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-billing-change-account.html
---

Amazon CodeCatalyst will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For more information, see [Migrating from Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/migration.html).

# Changing a billing account
<a name="managing-billing-change-account"></a>

You can change the AWS account that you want to specify as the billing account for your CodeCatalyst space.

**Important**
You cannot delete the connection for an account that is designated as the billing account for your space.

You must have the **Space administrator** role to manage billing and accounts for your space.

**To change the AWS account for a CodeCatalyst space for billing**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Navigate to your CodeCatalyst space. Choose **Settings**, and then choose **Billing**.

   The **Billing details** page displays.

1. Choose the **Edit** button next to the **AWS account name** field. The **Change AWS billing account** page displays.

1. In **Choose from AWS accounts already associated with your space**, choose the name of another added account that you want to designate as the billing account for your CodeCatalyst space. The account name must be for an account that has been added to your space and is listed in the **AWS accounts** tab for your space.

1. Choose **Change billing account**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
