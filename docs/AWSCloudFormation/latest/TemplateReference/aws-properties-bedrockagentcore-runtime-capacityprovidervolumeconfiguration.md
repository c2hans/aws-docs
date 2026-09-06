---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-runtime-capacityprovidervolumeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Runtime CapacityProviderVolumeConfiguration
<a name="aws-properties-bedrockagentcore-runtime-capacityprovidervolumeconfiguration"></a>

<a name="aws-properties-bedrockagentcore-runtime-capacityprovidervolumeconfiguration-description"></a>The `CapacityProviderVolumeConfiguration` property type specifies Property description not available. for an [AWS::BedrockAgentCore::Runtime](aws-resource-bedrockagentcore-runtime.md).

## Syntax
<a name="aws-properties-bedrockagentcore-runtime-capacityprovidervolumeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-runtime-capacityprovidervolumeconfiguration-syntax.json"></a>

```
{
  "[MountPath](#cfn-bedrockagentcore-runtime-capacityprovidervolumeconfiguration-mountpath)" : {{String}},
  "[VolumeName](#cfn-bedrockagentcore-runtime-capacityprovidervolumeconfiguration-volumename)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-runtime-capacityprovidervolumeconfiguration-syntax.yaml"></a>

```
  [MountPath](#cfn-bedrockagentcore-runtime-capacityprovidervolumeconfiguration-mountpath): {{String}}
  [VolumeName](#cfn-bedrockagentcore-runtime-capacityprovidervolumeconfiguration-volumename): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-runtime-capacityprovidervolumeconfiguration-properties"></a>

`MountPath`  <a name="cfn-bedrockagentcore-runtime-capacityprovidervolumeconfiguration-mountpath"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^/mnt/[a-zA-Z0-9._-]+/?$`
*Minimum*: `6`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VolumeName`  <a name="cfn-bedrockagentcore-runtime-capacityprovidervolumeconfiguration-volumename"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_-]{0,47}$`
*Minimum*: `1`
*Maximum*: `48`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
