---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-workforce-workforcevpcconfigrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Workforce WorkforceVpcConfigRequest
<a name="aws-properties-sagemaker-workforce-workforcevpcconfigrequest"></a>

The VPC object you use to create or update a workforce.

## Syntax
<a name="aws-properties-sagemaker-workforce-workforcevpcconfigrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-workforce-workforcevpcconfigrequest-syntax.json"></a>

```
{
  "[SecurityGroupIds](#cfn-sagemaker-workforce-workforcevpcconfigrequest-securitygroupids)" : {{[ String, ... ]}},
  "[Subnets](#cfn-sagemaker-workforce-workforcevpcconfigrequest-subnets)" : {{[ String, ... ]}},
  "[VpcId](#cfn-sagemaker-workforce-workforcevpcconfigrequest-vpcid)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-workforce-workforcevpcconfigrequest-syntax.yaml"></a>

```
  [SecurityGroupIds](#cfn-sagemaker-workforce-workforcevpcconfigrequest-securitygroupids): {{
    - String}}
  [Subnets](#cfn-sagemaker-workforce-workforcevpcconfigrequest-subnets): {{
    - String}}
  [VpcId](#cfn-sagemaker-workforce-workforcevpcconfigrequest-vpcid): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-workforce-workforcevpcconfigrequest-properties"></a>

`SecurityGroupIds`  <a name="cfn-sagemaker-workforce-workforcevpcconfigrequest-securitygroupids"></a>
The VPC security group IDs, in the form `sg-xxxxxxxx`. The security groups must be for the same VPC as specified in the subnet.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subnets`  <a name="cfn-sagemaker-workforce-workforcevpcconfigrequest-subnets"></a>
The ID of the subnets in the VPC that you want to connect.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `16`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-sagemaker-workforce-workforcevpcconfigrequest-vpcid"></a>
The ID of the VPC that the workforce uses for communication.
*Required*: No
*Type*: String
*Pattern*: `vpc-[0-9a-z]*`
*Minimum*: `0`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
