---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-capacityprovider-ephemeralblockdevicemapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::CapacityProvider EphemeralBlockDeviceMapping
<a name="aws-properties-bedrockagentcore-capacityprovider-ephemeralblockdevicemapping"></a>

<a name="aws-properties-bedrockagentcore-capacityprovider-ephemeralblockdevicemapping-description"></a>The `EphemeralBlockDeviceMapping` property type specifies Property description not available. for an [AWS::BedrockAgentCore::CapacityProvider](aws-resource-bedrockagentcore-capacityprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-capacityprovider-ephemeralblockdevicemapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-capacityprovider-ephemeralblockdevicemapping-syntax.json"></a>

```
{
  "[DeviceName](#cfn-bedrockagentcore-capacityprovider-ephemeralblockdevicemapping-devicename)" : {{String}},
  "[Ebs](#cfn-bedrockagentcore-capacityprovider-ephemeralblockdevicemapping-ebs)" : {{EphemeralEBSVolumeConfiguration}},
  "[VirtualName](#cfn-bedrockagentcore-capacityprovider-ephemeralblockdevicemapping-virtualname)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-capacityprovider-ephemeralblockdevicemapping-syntax.yaml"></a>

```
  [DeviceName](#cfn-bedrockagentcore-capacityprovider-ephemeralblockdevicemapping-devicename): {{String}}
  [Ebs](#cfn-bedrockagentcore-capacityprovider-ephemeralblockdevicemapping-ebs): {{
    EphemeralEBSVolumeConfiguration}}
  [VirtualName](#cfn-bedrockagentcore-capacityprovider-ephemeralblockdevicemapping-virtualname): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-capacityprovider-ephemeralblockdevicemapping-properties"></a>

`DeviceName`  <a name="cfn-bedrockagentcore-capacityprovider-ephemeralblockdevicemapping-devicename"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9/._-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ebs`  <a name="cfn-bedrockagentcore-capacityprovider-ephemeralblockdevicemapping-ebs"></a>
Property description not available.
*Required*: No
*Type*: [EphemeralEBSVolumeConfiguration](aws-properties-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VirtualName`  <a name="cfn-bedrockagentcore-capacityprovider-ephemeralblockdevicemapping-virtualname"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^ephemeral[0-9]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
