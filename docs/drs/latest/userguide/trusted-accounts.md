---
source_url: https://docs.aws.amazon.com/drs/latest/userguide/trusted-accounts.html
---

# Trusted accounts
<a name="trusted-accounts"></a>

Trusted accounts provide enhanced account management capabilities and visibility, including the ability to easily create multiple IAM roles for different users. Use this feature to quickly add the roles you need to use various AWS Elastic Disaster Recovery features and see the permissions of different accounts from a single screen.

Roles created via CloudFormation (Failback and in-AWS right-sizing roles), should be deleted from the CloudFormation console.

## AWS DRS trusted account page
<a name="trusted-accounts-page"></a>

The **Trusted accounts** page allows you to automatically create IAM roles that are required in order to utilize specific features and capabilities.

This page provides visibility into the existing roles assigned to each trusted account.

To edit or delete these roles, go to the IAM console. Deleting the IAM role will automatically remove the trusted account from the AWS Elastic Disaster Recovery console.

![Table showing five trusted accounts with their staging, network, and failback roles.](http://docs.aws.amazon.com/drs/latest/userguide/images/trusted-accounts-main.png)

**Note**
Commercial AWS accounts can only be trusted to other Commercial AWS accounts and GovCloud AWS accounts can only be trusted to other GovCloud AWS accounts.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
