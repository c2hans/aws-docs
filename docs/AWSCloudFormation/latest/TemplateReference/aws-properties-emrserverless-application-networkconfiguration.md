---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-application-networkconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::Application NetworkConfiguration
<a name="aws-properties-emrserverless-application-networkconfiguration"></a>

The network configuration for customer VPC connectivity.

## Syntax
<a name="aws-properties-emrserverless-application-networkconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-application-networkconfiguration-syntax.json"></a>

```
{
  "[SecurityGroupIds](#cfn-emrserverless-application-networkconfiguration-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-emrserverless-application-networkconfiguration-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-emrserverless-application-networkconfiguration-syntax.yaml"></a>

```
  [SecurityGroupIds](#cfn-emrserverless-application-networkconfiguration-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-emrserverless-application-networkconfiguration-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-emrserverless-application-networkconfiguration-properties"></a>

`SecurityGroupIds`  <a name="cfn-emrserverless-application-networkconfiguration-securitygroupids"></a>
The array of security group Ids for customer VPC connectivity.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`SubnetIds`  <a name="cfn-emrserverless-application-networkconfiguration-subnetids"></a>
The array of subnet Ids for customer VPC connectivity.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `16`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)
