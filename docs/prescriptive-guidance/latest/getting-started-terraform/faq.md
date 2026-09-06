---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/getting-started-terraform/faq.html
---

# FAQ
<a name="faq"></a>

## When should I use Terraform instead of CloudFormation?
<a name="faq1"></a>

In general, if your workloads are primarily based in AWS, AWS CloudFormation provides a level of native support that Terraform can't match. However, if your workloads include quite a few third-party processes or they're spread out among multiple cloud providers, Terraform is a tool that you might want to consider.

## When should I use the AWS CDK instead of CloudFormation?
<a name="faq2"></a>

When you use the AWS Cloud Development Kit (AWS CDK), you're also using CloudFormation. The AWS CDK allows you to use a common programming language to generate CloudFormation templates. If you're experienced in any of the programming languages that the AWS CDK [supports](https://docs.aws.amazon.com/cdk/v2/guide/languages.html), the AWS CDK can reduce the time required to generate CloudFormation templates.

## Is there a tool like the AWS CDK that generates Terraform configurations?
<a name="faq3"></a>

Compared to the AWS CDK, the [CDK for Terraform (CDKTF) ](https://aws.amazon.com/blogs/opensource/announcing-cdk-for-terraform-on-aws/)uses the same construct library to provision resources and the same [jsii](https://aws.github.io/jsii/specification/1-introduction/) engine to support multiple programming languages. You can use it to generate Terraform configurations in the same way that the AWS CDK generates CloudFormation templates.

## How do I learn more about Terraform?
<a name="faq4"></a>

For more information about advanced Terraform concepts, see the [Terraform documentation](https://developer.hashicorp.com/terraform/docs). It also describes the components of all major providers and open source modules.
