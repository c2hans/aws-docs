---
source_url: https://docs.aws.amazon.com/datasync/latest/userguide/iam.html
---

# Identity and access management in AWS DataSync
<a name="iam"></a>

AWS uses security credentials to identify you and to grant you access to your AWS resources. You can use features of AWS Identity and Access Management (IAM) to allow other users, services, and applications to use your AWS resources fully or in a limited way, without sharing your security credentials.

By default, IAM identities (users, groups, and roles) don't have permission to create, view, or modify AWS resources. To allow users, groups, and roles to access AWS DataSync resources and interact with the DataSync console and API, we recommend that you use an IAM policy that grants them permission to use the specific resources and API actions that they will need. You then attach the policy to the IAM identity that requires access. For an overview of the basic elements for a policy, see [Access management for AWS DataSync](managing-access-overview.md).

**Topics**
+ [Access management for AWS DataSync](managing-access-overview.md)
+ [AWS managed policies for AWS DataSync](security-iam-awsmanpol.md)
+ [IAM customer managed policies for AWS DataSync](using-identity-based-policies.md)
+ [Using service-linked roles for DataSync](using-service-linked-roles.md)
+ [Permissions for tagging DataSync resources during creation](supported-iam-actions-tagging.md)
+ [Cross-service confused deputy prevention](cross-service-confused-deputy-prevention.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
