---
source_url: https://docs.aws.amazon.com/braket/latest/developerguide/braket-slr.html
---

# Amazon Braket service-linked role
<a name="braket-slr"></a>

When you enable Amazon Braket, a *service-linked role* is created in your account.

A service-linked role is a unique type of IAM role that, in this case, is linked directly to Amazon Braket. The Amazon Braket service-linked role is predefined to include all the permissions that Braket requires when calling other AWS services on your behalf.

A service-linked role makes setting up Amazon Braket easier because you don't have to add the necessary permissions manually. Amazon Braket defines the permissions of its service-linked roles. Unless you change these definitions, only Amazon Braket can assume its roles. The defined permissions include the *trust policy* and the *permissions policy*. The permissions policy cannot be attached to any other IAM entity.

The service-linked role that Amazon Braket sets up is part of the AWS Identity and Access Management (IAM) [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#id_roles_terms-and-concepts) capability. For information about other AWS services that support service-linked roles, see [AWS Services That Work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes **in the **Service-Linked Role** column. Choose a **Yes ** with a link to view the service-linked role documentation for that service.

For more information on the AWS managed policy for service-linked roles, see [AmazonBraketServiceRolePolicy](security-iam-aws-managed-policies.md#about-amazonbraketservicerolepolicy).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
