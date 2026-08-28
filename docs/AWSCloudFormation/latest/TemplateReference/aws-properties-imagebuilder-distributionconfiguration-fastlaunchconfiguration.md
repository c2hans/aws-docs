---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::DistributionConfiguration FastLaunchConfiguration
<a name="aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration"></a>

Define and configure faster launching for output Windows AMIs.

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
A Boolean that represents the current state of faster launching for the Windows AMI. Set to `true` to start using Windows faster launching, or `false` to stop using it.
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
Configuration settings for managing the number of snapshots that are created from pre-provisioned instances for the Windows AMI when faster launching is enabled.
*Required*: No
*Type*: [FastLaunchSnapshotConfiguration](aws-properties-imagebuilder-distributionconfiguration-fastlaunchsnapshotconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
