---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choose-iac-tool/choose-tool.html
---

# Choosing an IaC tool
<a name="choose-tool"></a>

So, which tool should you choose?

With so many different tool options and varying business requirements, there's no one-size-fits-all approach. In addition to the advantages and disadvantages for each tool discussed in this guide, consider the following recommendations for your business requirements and operating model:
+ If you are managing or deploying a serverless AWS solution with minimal dependency or dependents, AWS Serverless Application Model (AWS SAM) might be a good option for you. It has all the same features as AWS CloudFormation. It also simplifies testing and deployment of serverless applications to the AWS Cloud.
+ If you are managing your infrastructure entirely on AWS, then AWS CloudFormation and the AWS Cloud Development Kit (AWS CDK) are good options. They provide out-of-the-box state management, and you can also natively use new features or AWS resources.
+ If you want a multi-provider utility, especially for managing multi-cloud or hybrid-cloud infrastructure, Terraform might be a good choice because it is platform agnostic. With Terraform, you can also use a wide range of plugins, and it has a large community with enterprise support options.
+ If you have a top-down distribution with best practices and if you have orchestration where you create, publish, and distribute reusable modules by using common programming languages, then the AWS CDK might be a good option.
+ If your organization can tolerate a high level of risk and needs to support multi-cloud or hybrid-cloud environments, consider using Pulumi.
