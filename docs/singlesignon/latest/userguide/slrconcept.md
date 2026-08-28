---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/slrconcept.html
---

# Understanding service-linked roles in IAM Identity Center
<a name="slrconcept"></a>

[Service-linked roles](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html?icmpid=docs_iam_console#iam-term-service-linked-role) are predefined IAM permissions that allow IAM Identity Center to delegate and enforce which users have single sign-on access to specific AWS accounts in your organization in AWS Organizations. The service enables this functionality by provisioning a service-linked role in every AWS account within its organization. The service then allows other AWS services like IAM Identity Center to leverage those roles to perform service-related tasks. For more information, see [AWS Organizations and service-linked roles](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html#orgs_integrate_services-using_slrs).

When you enable IAM Identity Center, IAM Identity Center creates a service-linked role in all accounts within the organization in AWS Organizations. IAM Identity Center also creates the same service-linked role in every account that is subsequently added to your organization. This role allows IAM Identity Center to access each account's resources on your behalf. For more information, see [Configure access to AWS accounts](manage-your-accounts.md).

Service-linked roles that are created in each AWS account are named `AWSServiceRoleForSSO`. For more information, see [Using service-linked roles for IAM Identity Center](using-service-linked-roles.md).

**Notes**
If you are signed in to the AWS Organizations management account, it uses your currently signed-in role and not the service-linked role. This prevents the escalation of privileges.
When IAM Identity Center performs any IAM operations in the AWS Organizations management account, all operations happen using the credentials of the IAM principal. This enables the logs in CloudTrail to provide visibility of who made all privilege changes in the management account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
