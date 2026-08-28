---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/auth-and-access-control.html
---

# Identity and Access Management for Application Auto Scaling
<a name="auth-and-access-control"></a>

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use Application Auto Scaling resources. IAM is an AWS service that you can use with no additional charge.

For complete IAM documentation, see the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/).

## Access control
<a name="access-control"></a>

You can have valid credentials to authenticate your requests, but unless you have permissions you cannot create or access Application Auto Scaling resources. For example, you must have permissions to create scaling policies, configure scheduled scaling, and so on.

The following sections provide details on how an IAM administrator can use IAM to help secure your AWS resources, by controlling who can perform Application Auto Scaling API actions.

**Topics**
+ [Access control](#access-control)
+ [How Application Auto Scaling works with IAM](security_iam_service-with-iam.md)
+ [AWS managed policies](security-iam-awsmanpol.md)
+ [Service-linked roles](application-auto-scaling-service-linked-roles.md)
+ [Identity-based policy examples](security_iam_id-based-policy-examples.md)
+ [Troubleshooting](security_iam_troubleshoot.md)
+ [Permissions validation](security_iam_permission_validation.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
