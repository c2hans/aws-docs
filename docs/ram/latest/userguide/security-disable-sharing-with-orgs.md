---
source_url: https://docs.aws.amazon.com/ram/latest/userguide/security-disable-sharing-with-orgs.html
---

# Disabling resource sharing with AWS Organizations
<a name="security-disable-sharing-with-orgs"></a>

If you previously enabled sharing with AWS Organizations and you no longer need to share resources with your entire organization or organizational units (OUs), you can disable sharing. When you disable sharing with AWS Organizations, all organizations or OUs are removed from the resource shares that you have created and they lose access to the shared resources. External accounts (accounts added to the resource share via invitation) will not be impacted, and will continue to be associated with the resource share.

**To disable sharing with AWS Organizations**

1. Disable trusted access to AWS Organizations using the AWS Organizations [disable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/disable-aws-service-access.html) AWS CLI command.

   ```
   $  aws organizations disable-aws-service-access --service-principal ram.amazonaws.com
   ```
**Important**
When you disable trusted access to AWS Organizations, principals within your organizations are removed from all resource shares and lose access to those shared resources.

1. Use the IAM console, the AWS CLI, or the IAM API operations to delete the **AWSServiceRoleForResourceAccessManager** service-linked role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RAM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ram` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
