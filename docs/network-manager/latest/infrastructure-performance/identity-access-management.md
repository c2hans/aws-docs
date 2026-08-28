---
source_url: https://docs.aws.amazon.com/network-manager/latest/infrastructure-performance/identity-access-management.html
---

# Identity and access management for Infrastructure Performance
<a name="identity-access-management"></a>

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use Infrastructure Performance resources. IAM is an AWS service that you can use with no additional charge.

To use Infrastructure Performance, you'll need an AWS account and AWS credentials. To increase the security of your AWS account, we recommend that you use an IAM user to provide access credentials instead of using your AWS account credentials. For more information, see [AWS security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html) and [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

The following sections provide details on how an IAM administrator can use IAM to help secure your AWS resources, by controlling who can perform Infrastructure Performance actions.

**Topics**
+ [How Infrastructure Performance works with IAM](security_iam_service-with-iam.md)
+ [Allow IAM users or groups to access Infrastructure Performance](security_iam_create-iam-policy.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
