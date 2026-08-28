---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-capacityprovider-rootvolumeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::CapacityProvider RootVolumeConfiguration
<a name="aws-properties-bedrockagentcore-capacityprovider-rootvolumeconfiguration"></a>

<a name="aws-properties-bedrockagentcore-capacityprovider-rootvolumeconfiguration-description"></a>The `RootVolumeConfiguration` property type specifies Property description not available. for an [AWS::BedrockAgentCore::CapacityProvider](aws-resource-bedrockagentcore-capacityprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-capacityprovider-rootvolumeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-capacityprovider-rootvolumeconfiguration-syntax.json"></a>

```
{
  "[Encrypted](#cfn-bedrockagentcore-capacityprovider-rootvolumeconfiguration-encrypted)" : {{Boolean}},
  "[FreeSpaceGiB](#cfn-bedrockagentcore-capacityprovider-rootvolumeconfiguration-freespacegib)" : {{Integer}},
  "[Iops](#cfn-bedrockagentcore-capacityprovider-rootvolumeconfiguration-iops)" : {{Integer}},
  "[KmsKeyId](#cfn-bedrockagentcore-capacityprovider-rootvolumeconfiguration-kmskeyid)" : {{String}},
  "[Throughput](#cfn-bedrockagentcore-capacityprovider-rootvolumeconfiguration-throughput)" : {{Integer}},
  "[VolumeType](#cfn-bedrockagentcore-capacityprovider-rootvolumeconfiguration-volumetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-capacityprovider-rootvolumeconfiguration-syntax.yaml"></a>

```
  [Encrypted](#cfn-bedrockagentcore-capacityprovider-rootvolumeconfiguration-encrypted): {{Boolean}}
  [FreeSpaceGiB](#cfn-bedrockagentcore-capacityprovider-rootvolumeconfiguration-freespacegib): {{Integer}}
  [Iops](#cfn-bedrockagentcore-capacityprovider-rootvolumeconfiguration-iops): {{Integer}}
  [KmsKeyId](#cfn-bedrockagentcore-capacityprovider-rootvolumeconfiguration-kmskeyid): {{String}}
  [Throughput](#cfn-bedrockagentcore-capacityprovider-rootvolumeconfiguration-throughput): {{Integer}}
  [VolumeType](#cfn-bedrockagentcore-capacityprovider-rootvolumeconfiguration-volumetype): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-capacityprovider-rootvolumeconfiguration-properties"></a>

`Encrypted`  <a name="cfn-bedrockagentcore-capacityprovider-rootvolumeconfiguration-encrypted"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FreeSpaceGiB`  <a name="cfn-bedrockagentcore-capacityprovider-rootvolumeconfiguration-freespacegib"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `2`
*Maximum*: `65000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Iops`  <a name="cfn-bedrockagentcore-capacityprovider-rootvolumeconfiguration-iops"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `100`
*Maximum*: `256000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyId`  <a name="cfn-bedrockagentcore-capacityprovider-rootvolumeconfiguration-kmskeyid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:kms:[a-z0-9-]+:[0-9]{12}:key/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Throughput`  <a name="cfn-bedrockagentcore-capacityprovider-rootvolumeconfiguration-throughput"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `125`
*Maximum*: `2000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VolumeType`  <a name="cfn-bedrockagentcore-capacityprovider-rootvolumeconfiguration-volumetype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `standard | io1 | io2 | gp2 | sc1 | st1 | gp3`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
