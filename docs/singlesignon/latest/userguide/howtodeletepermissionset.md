---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/howtodeletepermissionset.html
---

# Delete permission sets in IAM Identity Center
<a name="howtodeletepermissionset"></a>

Before you can delete a permission set from IAM Identity Center, you should [remove](howtoremovepermissionset.md) it from all AWS accounts that use the permission set. To check existing user and group access, see [View and change a permission set](howtoviewandchangepermissionset.md).

**Considerations**
+ To use permission sets, you'll need to use an Organization instance of IAM Identity Center. For more information, see [Organization and account instances of IAM Identity Center](identity-center-instances.md).
+ If you want to revoke an active permission set session, see [View and end active sessions for your workforce users](end-active-sessions.md).
+ You should remove permission sets and applications assignments from users or groups you want to delete before deleting them. Otherwise, you'll have unassigned and unused permission sets and applications in IAM Identity Center.

Use the following procedure to delete one or more permission sets so that they can no longer be used by any AWS account in the organization.

**Important**
All users and groups that have been assigned this permission set, regardless of what AWS account is using it, will no longer be able to sign in. To check existing user and group access, see [View and change a permission set](howtoviewandchangepermissionset.md).

**To delete a permission set from an AWS account**

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon).

1. Under **Multi-account permissions**, choose **Permission sets**.

1. Select the permission set that you want to delete, and then choose **Delete**.

1. In the **Delete permission set** dialog box, type the name of the permission set to confirm deletion, and then choose **Delete**. The name is case-sensitive.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
