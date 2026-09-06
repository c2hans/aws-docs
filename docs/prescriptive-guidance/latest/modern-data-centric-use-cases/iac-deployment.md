---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-centric-use-cases/iac-deployment.html
---

# IaC deployment
<a name="iac-deployment"></a>

Modern architecture is incomplete without a mechanism for an infrastructure as code (IaC) deployment. The following diagram shows the AWS services related to IaC deployment.

![IaC deployment diagram](http://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-centric-use-cases/images/guide-img/058e3d2f-f726-4dc0-989b-0f15dcd3bc33/images/a9309ae1-8a02-4a4d-8448-69d0da7d0890.png)

We recommend that any deployed infrastructure is always backed by code using IaC tools. For example, you can use [AWS CloudFormation](https://aws.amazon.com/cloudformation/) or [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html). AWS CDK is a wrapper around CloudFormation.

As a best practice, we recommend that you push your code to a code repository of your choice. It's also a best practice to use source control in your code repository so that you have versioning and collaboration capabilities that enable multiple team members to work simultaneously on the same code base, while ensuring that the code integration from different developers into the main branch doesn't result in any conflicts. [AWS CodeCommit](https://aws.amazon.com/codecommit/) is a controlled source code repository that provides a version control mechanism.
