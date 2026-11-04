---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-osis-pipelineendpoint-vpcoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OSIS::PipelineEndpoint VpcOptions
<a name="aws-properties-osis-pipelineendpoint-vpcoptions"></a>

Options that specify the subnets and security groups for an OpenSearch Ingestion VPC endpoint.

## Syntax
<a name="aws-properties-osis-pipelineendpoint-vpcoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-osis-pipelineendpoint-vpcoptions-syntax.json"></a>

```
{
  "[SecurityGroupIds](#cfn-osis-pipelineendpoint-vpcoptions-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-osis-pipelineendpoint-vpcoptions-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-osis-pipelineendpoint-vpcoptions-syntax.yaml"></a>

```
  [SecurityGroupIds](#cfn-osis-pipelineendpoint-vpcoptions-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-osis-pipelineendpoint-vpcoptions-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-osis-pipelineendpoint-vpcoptions-properties"></a>

`SecurityGroupIds`  <a name="cfn-osis-pipelineendpoint-vpcoptions-securitygroupids"></a>
A list of security groups associated with the VPC endpoint.
*Required*: No
*Type*: Array of String
*Minimum*: `11 | 1`
*Maximum*: `20 | 12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-osis-pipelineendpoint-vpcoptions-subnetids"></a>
A list of subnet IDs associated with the VPC endpoint.
*Required*: No
*Type*: Array of String
*Minimum*: `15 | 1`
*Maximum*: `24 | 12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
