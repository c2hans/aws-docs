---
source_url: https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/aws-cdk.html
---

# AWS Cloud Development Kit (AWS CDK)
<a name="aws-cdk"></a>

The [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk) is an open source software development framework to model and provision your cloud application resources using familiar programming languages. AWS CDK enables you to model application infrastructure using TypeScript, Python, Java, and .NET. Developers can leverage their existing Integrated Development Environment (IDE), using tools such as autocomplete and in-line documentation to accelerate development of infrastructure.

AWS CDK utilizes CloudFormation in the background to provision resources in a safe, repeatable manner. Constructs are the basic building blocks of CDK code. A construct represents a cloud component and encapsulates everything CloudFormation needs to create the component. The AWS CDK includes the [AWS Construct Library](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html), containing constructs representing many AWS services. By combining constructs together, you can quickly and easily create complex architectures for deployment in AWS.
