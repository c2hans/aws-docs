---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::DistributionConfiguration FastLaunchConfiguration
<a name="aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration"></a>

Defines and configures EC2 Fast Launch for output Windows AMIs.

## Syntax
<a name="aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration-syntax.json"></a>

```
{
  "[AccountId](#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-accountid)" : {{String}},
  "[Enabled](#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-enabled)" : {{Boolean}},
  "[LaunchTemplate](#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-launchtemplate)" : {{FastLaunchLaunchTemplateSpecification}},
  "[MaxParallelLaunches](#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-maxparallellaunches)" : {{Integer}},
  "[SnapshotConfiguration](#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-snapshotconfiguration)" : {{FastLaunchSnapshotConfiguration}}
}
```

### YAML
<a name="aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration-syntax.yaml"></a>

```
  [AccountId](#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-accountid): {{String}}
  [Enabled](#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-enabled): {{Boolean}}
  [LaunchTemplate](#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-launchtemplate): {{
    FastLaunchLaunchTemplateSpecification}}
  [MaxParallelLaunches](#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-maxparallellaunches): {{Integer}}
  [SnapshotConfiguration](#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-snapshotconfiguration): {{
    FastLaunchSnapshotConfiguration}}
```

## Properties
<a name="aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration-properties"></a>

`AccountId`  <a name="cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-accountid"></a>
The owner account ID for the fast-launch enabled Windows AMI.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-enabled"></a>
Specifies whether to enable Windows fast launch on the output AMI during distribution. A value of `false` means Image Builder takes no fast-launch action for this configuration.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LaunchTemplate`  <a name="cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-launchtemplate"></a>
The launch template that the fast-launch enabled Windows AMI uses when it launches Windows instances to create pre-provisioned snapshots.
*Required*: No
*Type*: [FastLaunchLaunchTemplateSpecification](aws-properties-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxParallelLaunches`  <a name="cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-maxparallellaunches"></a>
The maximum number of parallel instances that are launched for creating resources.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapshotConfiguration`  <a name="cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-snapshotconfiguration"></a>
Configuration settings for managing the number of snapshots that are created from pre-provisioned instances for the Windows AMI when Windows fast launch is enabled.
*Required*: No
*Type*: [FastLaunchSnapshotConfiguration](aws-properties-imagebuilder-distributionconfiguration-fastlaunchsnapshotconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
