---
source_url: https://docs.aws.amazon.com/partner-central/latest/crm/link-pc-mkt-accounts.html
---

# Linking your AWS Partner Central and AWS Marketplace accounts
<a name="link-pc-mkt-accounts"></a>

The following steps explain how to link your AWS Partner Central and AWS Marketplace seller accounts. You must have Salesforce alliance lead permissions to complete these steps. You must link the accounts before you can create any type of CRM integration.

**To link the accounts**

1. Do the following:
   + Sign in to your AWS Partner Central account as an alliance lead or cloud administrator.
   + Sign in to your AWS Marketplace seller account.

1. On the Partner Central home page, in the In the upper-right corner, choose **Link accounts**.

   The **Account linking prerequisites** dialog box appears.

1. Choose **Continue to account linking**, then choose **Initiate account linking**.

   That takes you to the AWS Console and your AWS Marketplace seller account.

1. Do the following:

   1. Ensure the correct value appears under **AWS account ID**.

   1. In the **Legal business name** box, enter the legal name of your business.

   1. Choose **Next**.

   That returns you to Partner Central and the **Standard IAM roles** page.

1. Select the following checkboxes:
   + Under **Cloud admin IAM role**, choose **Assign PartnerCentralRoleForCloudAdmin-\#\#\# role to the AWS Partner Central alliance lead and all active cloud admin users**.
   + Under **Alliance team IAM role**, choose **Assign PartnerCentralRoleForAlliance-\#\#\# role to all active AWS Partner Central alliance team users**.
   + Under **ACE IAM role**, choose **Assign PartnerCentralRoleForAce-\#\#\# role to the AWS Partner Central ACE managers and users.**.

1. Choose **Next**, then choose **Link accounts**.

Success messages appear when the linking process finishes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
