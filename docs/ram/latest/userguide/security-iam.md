---
source_url: https://docs.aws.amazon.com/ram/latest/userguide/security-iam.html
---

# Identity and access management for AWS Resource Access Manager
<a name="security-iam"></a>

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. Administrators in IAM control who can be *authenticated* (signed in) and *authorized* (have permissions) to use AWS resources. By using IAM, you create principals, such as roles, users, and groups in your AWS account. You control the permissions that those principals have to perform tasks using AWS resources. You can use IAM for no additional charge. For more information about managing and creating custom IAM policies, see [Managing IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html) in the *IAM User Guide*.

**Topics**
+ [How AWS RAM works with IAM](security-iam-policies.md)
+ [AWS managed policies for AWS Resource Access Manager](security-iam-awsmanpol.md)
+ [Using service-linked roles for AWS RAM](using-service-linked-roles.md)
+ [Example IAM policies for AWS RAM](security-iam-policies-examples.md)
+ [Example service control policies for AWS Organizations and AWS RAM](security-scp.md)
+ [Disabling resource sharing with AWS Organizations](security-disable-sharing-with-orgs.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RAM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ram` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
