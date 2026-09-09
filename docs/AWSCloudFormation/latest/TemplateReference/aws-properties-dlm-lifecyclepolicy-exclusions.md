---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dlm-lifecyclepolicy-exclusions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DLM::LifecyclePolicy Exclusions
<a name="aws-properties-dlm-lifecyclepolicy-exclusions"></a>

**[Default policies only]** Specifies exclusion parameters for volumes or instances for which you do not want to create snapshots or AMIs. The policy will not create snapshots or AMIs for target resources that match any of the specified exclusion parameters.

## Syntax
<a name="aws-properties-dlm-lifecyclepolicy-exclusions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dlm-lifecyclepolicy-exclusions-syntax.json"></a>

```
{
  "[ExcludeBootVolumes](#cfn-dlm-lifecyclepolicy-exclusions-excludebootvolumes)" : {{Boolean}},
  "[ExcludeTags](#cfn-dlm-lifecyclepolicy-exclusions-excludetags)" : {{[ Tag, ... ]}},
  "[ExcludeVolumeTypes](#cfn-dlm-lifecyclepolicy-exclusions-excludevolumetypes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-dlm-lifecyclepolicy-exclusions-syntax.yaml"></a>

```
  [ExcludeBootVolumes](#cfn-dlm-lifecyclepolicy-exclusions-excludebootvolumes): {{Boolean}}
  [ExcludeTags](#cfn-dlm-lifecyclepolicy-exclusions-excludetags): {{
    - Tag}}
  [ExcludeVolumeTypes](#cfn-dlm-lifecyclepolicy-exclusions-excludevolumetypes): {{
    - String}}
```

## Properties
<a name="aws-properties-dlm-lifecyclepolicy-exclusions-properties"></a>

`ExcludeBootVolumes`  <a name="cfn-dlm-lifecyclepolicy-exclusions-excludebootvolumes"></a>
**[Default policies for EBS snapshots only]** Indicates whether to exclude volumes that are attached to instances as the boot volume. If you exclude boot volumes, only volumes attached as data (non-boot) volumes will be backed up by the policy. To exclude boot volumes, specify `true`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExcludeTags`  <a name="cfn-dlm-lifecyclepolicy-exclusions-excludetags"></a>
**[Default policies for EBS-backed AMIs only]** Specifies whether to exclude volumes that have specific tags.
*Required*: No
*Type*: Array of [Tag](aws-properties-dlm-lifecyclepolicy-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExcludeVolumeTypes`  <a name="cfn-dlm-lifecyclepolicy-exclusions-excludevolumetypes"></a>
**[Default policies for EBS snapshots only]** Specifies the volume types to exclude. Volumes of the specified types will not be targeted by the policy.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `6`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
