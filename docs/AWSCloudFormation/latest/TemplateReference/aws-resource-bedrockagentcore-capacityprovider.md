---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-capacityprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::CapacityProvider
<a name="aws-resource-bedrockagentcore-capacityprovider"></a>

<a name="aws-resource-bedrockagentcore-capacityprovider-description"></a>The `AWS::BedrockAgentCore::CapacityProvider` resource Property description not available. for BedrockAgentCore.

## Syntax
<a name="aws-resource-bedrockagentcore-capacityprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-capacityprovider-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::CapacityProvider",
  "Properties" : {
      "[ComputeConfiguration](#cfn-bedrockagentcore-capacityprovider-computeconfiguration)" : {{ComputeConfiguration}},
      "[Description](#cfn-bedrockagentcore-capacityprovider-description)" : {{String}},
      "[Name](#cfn-bedrockagentcore-capacityprovider-name)" : {{String}},
      "[PermissionsConfiguration](#cfn-bedrockagentcore-capacityprovider-permissionsconfiguration)" : {{PermissionsConfiguration}},
      "[Tags](#cfn-bedrockagentcore-capacityprovider-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-capacityprovider-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::CapacityProvider
Properties:
  [ComputeConfiguration](#cfn-bedrockagentcore-capacityprovider-computeconfiguration): {{
    ComputeConfiguration}}
  [Description](#cfn-bedrockagentcore-capacityprovider-description): {{String}}
  [Name](#cfn-bedrockagentcore-capacityprovider-name): {{String}}
  [PermissionsConfiguration](#cfn-bedrockagentcore-capacityprovider-permissionsconfiguration): {{
    PermissionsConfiguration}}
  [Tags](#cfn-bedrockagentcore-capacityprovider-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-bedrockagentcore-capacityprovider-properties"></a>

`ComputeConfiguration`  <a name="cfn-bedrockagentcore-capacityprovider-computeconfiguration"></a>
Property description not available.
*Required*: Yes
*Type*: [ComputeConfiguration](aws-properties-bedrockagentcore-capacityprovider-computeconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-bedrockagentcore-capacityprovider-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrockagentcore-capacityprovider-name"></a>
The name of the capacity provider.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_]{0,47}$`
*Minimum*: `1`
*Maximum*: `48`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PermissionsConfiguration`  <a name="cfn-bedrockagentcore-capacityprovider-permissionsconfiguration"></a>
Property description not available.
*Required*: Yes
*Type*: [PermissionsConfiguration](aws-properties-bedrockagentcore-capacityprovider-permissionsconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-bedrockagentcore-capacityprovider-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-bedrockagentcore-capacityprovider-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrockagentcore-capacityprovider-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-capacityprovider-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-capacityprovider-return-values-fn--getatt"></a>

####
<a name="aws-resource-bedrockagentcore-capacityprovider-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CapacityProviderId`  <a name="CapacityProviderId-fn::getatt"></a>
The unique identifier of the capacity provider.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Property description not available.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
The timestamp when the capacity provider was last updated.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the capacity provider. For possible values, see `CapacityProviderStatus`.
