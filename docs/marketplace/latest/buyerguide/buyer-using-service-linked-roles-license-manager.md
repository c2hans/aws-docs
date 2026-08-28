---
source_url: https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-using-service-linked-roles-license-manager.html
---

# Service-linked role to share entitlements for AWS Marketplace
<a name="buyer-using-service-linked-roles-license-manager"></a>

To share your AWS Marketplace subscriptions to other accounts in your AWS organization with AWS License Manager, you must give AWS Marketplace permissions for each account you want to share with. Do this by using the **AWSServiceRoleForMarketplaceLicenseManagement** role. This role provides AWS Marketplace with permissions to create and manage licenses in AWS License Manager for the products that you subscribe to in AWS Marketplace.

The `AWSServiceRoleForMarketplaceLicenseManagement` service-linked role trusts the following service to perform actions in License Manager on your behalf:
+ `license-management.marketplace.amazonaws.com`

The `AWSMarketplaceLicenseManagementServiceRolePolicy` allows AWS Marketplace to complete the following actions on the specified resources:
+ Actions:
  + `"organizations:DescribeOrganization"`
  + `"license-manager:ListReceivedGrants"`
  + `"license-manager:ListDistributedGrants"`
  + `"license-manager:GetGrant"`
  + `"license-manager:CreateGrant"`
  + `"license-manager:CreateGrantVersion"`
  + `"license-manager:DeleteGrant"`
  + `"license-manager:AcceptGrant"`
+ Resources:
  + All resources (`"*"`)

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [ Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
