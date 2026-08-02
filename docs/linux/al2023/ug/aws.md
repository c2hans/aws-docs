---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/aws.html
---

# Using AL2023 on AWS
<a name="aws"></a>

You can set up AL2023 for use with other AWS services. For example, you can choose an AL2023 AMI when you launch an [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) (Amazon EC2) instance.

For these setup procedures, you use the AWS Identity and Access Management (IAM) service. For complete information about IAM, see the following reference materials:
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/iam/)
+ [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/)

**Topics**
+ [Getting started with AWS](#getting-started-aws)
+ [AL2023 on Amazon EC2](ec2.md)
+ [Using AL2023 in containers](container.md)
+ [AL2023 on AWS Elastic Beanstalk](beanstalk.md)
+ [Using AL2023 in AWS CloudShell](cloudshell.md)
+ [Using AL2023 based Amazon ECS AMIs to host containerized workloads](ecs.md)
+ [Using Amazon Elastic File System on AL2023](efs.md)
+ [Using Amazon EMR built on AL2023](emr.md)
+ [Using AL2023 in AWS Lambda](lambda.md)

## Getting started with AWS
<a name="getting-started-aws"></a>

### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com//accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

### Granting programmatic access
<a name="install-aws-prereq.programmatic-access"></a>

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.

****

| Which user needs programmatic access? | To | By |
| --- | --- | --- |
| IAM | (Recommended) Use console credentials as temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.[See the AWS documentation website for more details](http://docs.aws.amazon.com/linux/al2023/ug/aws.html) |
| Workforce identity<br />(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.[See the AWS documentation website for more details](http://docs.aws.amazon.com/linux/al2023/ug/aws.html) |
| IAM | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions in [Using temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) in the IAM User Guide. |
| IAM | (Not recommended)Use long-term credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.[See the AWS documentation website for more details](http://docs.aws.amazon.com/linux/al2023/ug/aws.html) |
