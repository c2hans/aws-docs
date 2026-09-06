---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-networkconnector-config.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::NetworkConnector Config
<a name="aws-properties-lambda-networkconnector-config"></a>

Configuration for a VPC egress network connector. Specifies the subnets, security groups, and network protocol for routing outbound traffic through your VPC.

## Syntax
<a name="aws-properties-lambda-networkconnector-config-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-networkconnector-config-syntax.json"></a>

```
{
  "[VpcEgressConfiguration](#cfn-lambda-networkconnector-config-vpcegressconfiguration)" : {{VpcEgressConfiguration}}
}
```

### YAML
<a name="aws-properties-lambda-networkconnector-config-syntax.yaml"></a>

```
  [VpcEgressConfiguration](#cfn-lambda-networkconnector-config-vpcegressconfiguration): {{
    VpcEgressConfiguration}}
```

## Properties
<a name="aws-properties-lambda-networkconnector-config-properties"></a>

`VpcEgressConfiguration`  <a name="cfn-lambda-networkconnector-config-vpcegressconfiguration"></a>
The VPC egress configuration for the network connector.
*Required*: Yes
*Type*: [VpcEgressConfiguration](aws-properties-lambda-networkconnector-vpcegressconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
