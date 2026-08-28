---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::DistributionConfiguration AmiDistributionConfiguration
<a name="aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration"></a>

Define and configure the output AMIs of the pipeline.

## Syntax
<a name="aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration-syntax.json"></a>

```
{
  "[AmiTags](#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-amitags)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Description](#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-description)" : {{String}},
  "[KmsKeyId](#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-kmskeyid)" : {{String}},
  "[LaunchPermissionConfiguration](#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-launchpermissionconfiguration)" : {{LaunchPermissionConfiguration}},
  "[Name](#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-name)" : {{String}},
  "[TargetAccountIds](#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-targetaccountids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration-syntax.yaml"></a>

```
  [AmiTags](#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-amitags): {{
    {{Key}}: {{Value}}}}
  [Description](#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-description): {{String}}
  [KmsKeyId](#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-kmskeyid): {{String}}
  [LaunchPermissionConfiguration](#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-launchpermissionconfiguration): {{
    LaunchPermissionConfiguration}}
  [Name](#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-name): {{String}}
  [TargetAccountIds](#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-targetaccountids): {{
    - String}}
```

## Properties
<a name="aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration-properties"></a>

`AmiTags`  <a name="cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-amitags"></a>
The tags to apply to AMIs distributed to this Region.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-description"></a>
The description of the AMI distribution configuration. Minimum and maximum length are in characters.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-kmskeyid"></a>
The Amazon Resource Name (ARN) that uniquely identifies the KMS key used to encrypt the distributed image. This can be either the Key ARN or the Alias ARN. For more information, see [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) in the *AWS Key Management Service Developer Guide*.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LaunchPermissionConfiguration`  <a name="cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-launchpermissionconfiguration"></a>
Launch permissions can be used to configure which AWS accounts can use the AMI to launch instances.
*Required*: No
*Type*: [LaunchPermissionConfiguration](aws-properties-imagebuilder-distributionconfiguration-launchpermissionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-name"></a>
The name of the output AMI.
*Required*: No
*Type*: String
*Pattern*: `^[-_A-Za-z0-9{][-_A-Za-z0-9\s:{}\.]+[-_A-Za-z0-9}]$`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetAccountIds`  <a name="cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-targetaccountids"></a>
The ID of an account to which you want to distribute an image.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1536`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
