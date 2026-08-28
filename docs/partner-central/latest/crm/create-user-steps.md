---
source_url: https://docs.aws.amazon.com/partner-central/latest/crm/create-user-steps.html
---

# Creating the IAM user
<a name="create-user-steps"></a>

Follow these steps to create the IAM user in your AWS Marketplace seller account.

1. In the AWS Marketplace portal, sign in to your seller account.

1. In the navigation pane, choose **Users**, then **Create user**.

1. In the **User name** box, enter **apn-ace-***CompanyName***-AccessUser-prod**, where *CompanyName* is the name of your company, then choose **Next**.

1. On the **Set permissions** page, choose **Attach policies directly**, then choose **Next**.

   The **Permissions policies** section appears.

1. Search for **AWSPartnerCentralOpportunityManagement**.

   The policy appears in the search results.

1. Select the checkbox next to the policy, then choose **Next**.
**Important**
Do not add other policies or permissions.

1. On the **Review and create** page, choose **Create user**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
