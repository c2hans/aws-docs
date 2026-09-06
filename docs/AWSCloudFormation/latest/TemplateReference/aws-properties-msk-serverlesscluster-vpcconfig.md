---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-serverlesscluster-vpcconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::ServerlessCluster VpcConfig
<a name="aws-properties-msk-serverlesscluster-vpcconfig"></a>

<a name="aws-properties-msk-serverlesscluster-vpcconfig-description"></a>The `VpcConfig` property type specifies Property description not available. for an [AWS::MSK::ServerlessCluster](aws-resource-msk-serverlesscluster.md).

## Syntax
<a name="aws-properties-msk-serverlesscluster-vpcconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-serverlesscluster-vpcconfig-syntax.json"></a>

```
{
  "[SecurityGroups](#cfn-msk-serverlesscluster-vpcconfig-securitygroups)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-msk-serverlesscluster-vpcconfig-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-msk-serverlesscluster-vpcconfig-syntax.yaml"></a>

```
  [SecurityGroups](#cfn-msk-serverlesscluster-vpcconfig-securitygroups): {{
    - String}}
  [SubnetIds](#cfn-msk-serverlesscluster-vpcconfig-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-msk-serverlesscluster-vpcconfig-properties"></a>

`SecurityGroups`  <a name="cfn-msk-serverlesscluster-vpcconfig-securitygroups"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-msk-serverlesscluster-vpcconfig-subnetids"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
