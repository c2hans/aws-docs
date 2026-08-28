---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/wkld-01.html
---

# WKLD.01 Use IAM roles for compute environment permissions
<a name="wkld-01"></a>

In AWS Identity and Access Management (IAM), a *role* represents a set of permissions that can be assumed by an IAM user, an AWS service, or a federated identity for a configurable period of time. Using roles removes the need to store or manage long-term credentials, which reduces the chance of unintended use. Assign an IAM role directly to Amazon Elastic Compute Cloud (Amazon EC2) instances, AWS Fargate tasks and services, AWS Lambda functions, and other AWS compute services that support IAM roles. Applications that use an AWS SDK and run in these compute environments automatically use the IAM role credentials for authentication.

For instructions on using IAM roles with services, see the following documentation:
+ [IAM roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) in the Amazon EC2 documentation
+ [IAM roles for tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the Amazon Elastic Container Service (Amazon ECS) documentation
+ [Lambda execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) in the AWS Lambda documentation
+ For other AWS compute services, refer to the *Security* section of the [AWS service documentation](https://docs.aws.amazon.com/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
