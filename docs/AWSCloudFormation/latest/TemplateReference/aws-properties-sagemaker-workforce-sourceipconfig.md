---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-workforce-sourceipconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Workforce SourceIpConfig
<a name="aws-properties-sagemaker-workforce-sourceipconfig"></a>

A list of IP address ranges ([CIDRs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html)). Used to create an allow list of IP addresses for a private workforce. Workers will only be able to log in to their worker portal from an IP address within this range. By default, a workforce isn't restricted to specific IP addresses.

## Syntax
<a name="aws-properties-sagemaker-workforce-sourceipconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-workforce-sourceipconfig-syntax.json"></a>

```
{
  "[Cidrs](#cfn-sagemaker-workforce-sourceipconfig-cidrs)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-workforce-sourceipconfig-syntax.yaml"></a>

```
  [Cidrs](#cfn-sagemaker-workforce-sourceipconfig-cidrs): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-workforce-sourceipconfig-properties"></a>

`Cidrs`  <a name="cfn-sagemaker-workforce-sourceipconfig-cidrs"></a>
A list of one to ten [Classless Inter-Domain Routing](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html) (CIDR) values.
Maximum: Ten CIDR values
The following Length Constraints apply to individual CIDR values in the CIDR value list.
*Required*: Yes
*Type*: Array of String
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
