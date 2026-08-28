---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::CapacityProvider EphemeralEBSVolumeConfiguration
<a name="aws-properties-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration"></a>

<a name="aws-properties-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-description"></a>The `EphemeralEBSVolumeConfiguration` property type specifies Property description not available. for an [AWS::BedrockAgentCore::CapacityProvider](aws-resource-bedrockagentcore-capacityprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-syntax.json"></a>

```
{
  "[EbsCardIndex](#cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-ebscardindex)" : {{Integer}},
  "[Encrypted](#cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-encrypted)" : {{Boolean}},
  "[Iops](#cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-iops)" : {{Integer}},
  "[KmsKeyId](#cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-kmskeyid)" : {{String}},
  "[SnapshotId](#cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-snapshotid)" : {{String}},
  "[Throughput](#cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-throughput)" : {{Integer}},
  "[VolumeInitializationRate](#cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-volumeinitializationrate)" : {{Integer}},
  "[VolumeSize](#cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-volumesize)" : {{Integer}},
  "[VolumeType](#cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-volumetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-syntax.yaml"></a>

```
  [EbsCardIndex](#cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-ebscardindex): {{Integer}}
  [Encrypted](#cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-encrypted): {{Boolean}}
  [Iops](#cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-iops): {{Integer}}
  [KmsKeyId](#cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-kmskeyid): {{String}}
  [SnapshotId](#cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-snapshotid): {{String}}
  [Throughput](#cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-throughput): {{Integer}}
  [VolumeInitializationRate](#cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-volumeinitializationrate): {{Integer}}
  [VolumeSize](#cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-volumesize): {{Integer}}
  [VolumeType](#cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-volumetype): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-properties"></a>

`EbsCardIndex`  <a name="cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-ebscardindex"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Encrypted`  <a name="cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-encrypted"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Iops`  <a name="cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-iops"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `100`
*Maximum*: `256000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyId`  <a name="cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-kmskeyid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:kms:[a-z0-9-]+:[0-9]{12}:key/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SnapshotId`  <a name="cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-snapshotid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^snap-[a-f0-9]{8,17}$`
*Minimum*: `13`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Throughput`  <a name="cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-throughput"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `125`
*Maximum*: `2000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VolumeInitializationRate`  <a name="cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-volumeinitializationrate"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `100`
*Maximum*: `300`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VolumeSize`  <a name="cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-volumesize"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65536`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VolumeType`  <a name="cfn-bedrockagentcore-capacityprovider-ephemeralebsvolumeconfiguration-volumetype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `standard | io1 | io2 | gp2 | sc1 | st1 | gp3`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
