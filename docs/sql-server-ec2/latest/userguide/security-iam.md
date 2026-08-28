---
source_url: https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/security-iam.html
---

# Identity and access management for Microsoft SQL Server on Amazon EC2
<a name="security-iam"></a>

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use SQL Server on EC2 resources. IAM is an AWS service that you can use with no additional charge.

Your security credentials identify you to services in AWS and grant you access to AWS resources, such as your Amazon EC2 resources. You can use features of Amazon EC2 and IAM to allow other users, services, and applications to use your Amazon EC2 resources without sharing your security credentials. You can use IAM to control how other users use resources in your AWS account, and you can use security groups to control access to your Amazon EC2 instances. You can choose to allow full or limited use of your Amazon EC2 resources.

If you are a developer, you can use IAM roles to manage the security credentials needed by the applications that you run on your EC2 instances. After you attach an IAM role to your instance, your applications running on the instance can retrieve the credentials from the Instance Metadata Service (IMDS).

For best practices for securing your AWS resources using IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

**Topics**
+ [AWS managed policies for Microsoft SQL Server on Amazon EC2](security-iam-awsmanpol.md)
+ [Service-linked role for Microsoft SQL Server on Amazon EC2](slr-sql-ha.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SQL Server on Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sql-server-ec2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
