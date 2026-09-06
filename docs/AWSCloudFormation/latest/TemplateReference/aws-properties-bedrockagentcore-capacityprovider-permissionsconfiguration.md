---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-capacityprovider-permissionsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::CapacityProvider PermissionsConfiguration
<a name="aws-properties-bedrockagentcore-capacityprovider-permissionsconfiguration"></a>

<a name="aws-properties-bedrockagentcore-capacityprovider-permissionsconfiguration-description"></a>The `PermissionsConfiguration` property type specifies Property description not available. for an [AWS::BedrockAgentCore::CapacityProvider](aws-resource-bedrockagentcore-capacityprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-capacityprovider-permissionsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-capacityprovider-permissionsconfiguration-syntax.json"></a>

```
{
  "[CapacityProviderOperatorRoleArn](#cfn-bedrockagentcore-capacityprovider-permissionsconfiguration-capacityprovideroperatorrolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-capacityprovider-permissionsconfiguration-syntax.yaml"></a>

```
  [CapacityProviderOperatorRoleArn](#cfn-bedrockagentcore-capacityprovider-permissionsconfiguration-capacityprovideroperatorrolearn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-capacityprovider-permissionsconfiguration-properties"></a>

`CapacityProviderOperatorRoleArn`  <a name="cfn-bedrockagentcore-capacityprovider-permissionsconfiguration-capacityprovideroperatorrolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
