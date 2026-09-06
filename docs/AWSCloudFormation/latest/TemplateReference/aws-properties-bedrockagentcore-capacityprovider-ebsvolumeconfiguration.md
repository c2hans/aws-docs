---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-capacityprovider-ebsvolumeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::CapacityProvider EbsVolumeConfiguration
<a name="aws-properties-bedrockagentcore-capacityprovider-ebsvolumeconfiguration"></a>

<a name="aws-properties-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-description"></a>The `EbsVolumeConfiguration` property type specifies Property description not available. for an [AWS::BedrockAgentCore::CapacityProvider](aws-resource-bedrockagentcore-capacityprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-syntax.json"></a>

```
{
  "[Encrypted](#cfn-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-encrypted)" : {{Boolean}},
  "[Iops](#cfn-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-iops)" : {{Integer}},
  "[KmsKeyId](#cfn-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-kmskeyid)" : {{String}},
  "[Name](#cfn-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-name)" : {{String}},
  "[SizeGiB](#cfn-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-sizegib)" : {{Integer}},
  "[SnapshotId](#cfn-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-snapshotid)" : {{String}},
  "[Throughput](#cfn-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-throughput)" : {{Integer}},
  "[VolumeType](#cfn-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-volumetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-syntax.yaml"></a>

```
  [Encrypted](#cfn-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-encrypted): {{Boolean}}
  [Iops](#cfn-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-iops): {{Integer}}
  [KmsKeyId](#cfn-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-kmskeyid): {{String}}
  [Name](#cfn-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-name): {{String}}
  [SizeGiB](#cfn-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-sizegib): {{Integer}}
  [SnapshotId](#cfn-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-snapshotid): {{String}}
  [Throughput](#cfn-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-throughput): {{Integer}}
  [VolumeType](#cfn-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-volumetype): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-properties"></a>

`Encrypted`  <a name="cfn-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-encrypted"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Iops`  <a name="cfn-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-iops"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `100`
*Maximum*: `256000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyId`  <a name="cfn-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-kmskeyid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:kms:[a-z0-9-]+:[0-9]{12}:key/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_-]{0,47}$`
*Minimum*: `1`
*Maximum*: `48`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SizeGiB`  <a name="cfn-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-sizegib"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65536`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SnapshotId`  <a name="cfn-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-snapshotid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^snap-[a-f0-9]{8,17}$`
*Minimum*: `13`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Throughput`  <a name="cfn-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-throughput"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `125`
*Maximum*: `2000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VolumeType`  <a name="cfn-bedrockagentcore-capacityprovider-ebsvolumeconfiguration-volumetype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `standard | io1 | io2 | gp2 | sc1 | st1 | gp3`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
