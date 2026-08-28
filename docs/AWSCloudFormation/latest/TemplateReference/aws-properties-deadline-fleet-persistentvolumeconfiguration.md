---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-fleet-persistentvolumeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Fleet PersistentVolumeConfiguration
<a name="aws-properties-deadline-fleet-persistentvolumeconfiguration"></a>

Specifies the persistent EBS volume configuration for workers in a service managed fleet.

## Syntax
<a name="aws-properties-deadline-fleet-persistentvolumeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-fleet-persistentvolumeconfiguration-syntax.json"></a>

```
{
  "[Iops](#cfn-deadline-fleet-persistentvolumeconfiguration-iops)" : {{Integer}},
  "[LastUsedTtlHours](#cfn-deadline-fleet-persistentvolumeconfiguration-lastusedttlhours)" : {{Integer}},
  "[MountPath](#cfn-deadline-fleet-persistentvolumeconfiguration-mountpath)" : {{String}},
  "[SizeGiB](#cfn-deadline-fleet-persistentvolumeconfiguration-sizegib)" : {{Integer}},
  "[ThroughputMiB](#cfn-deadline-fleet-persistentvolumeconfiguration-throughputmib)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-deadline-fleet-persistentvolumeconfiguration-syntax.yaml"></a>

```
  [Iops](#cfn-deadline-fleet-persistentvolumeconfiguration-iops): {{Integer}}
  [LastUsedTtlHours](#cfn-deadline-fleet-persistentvolumeconfiguration-lastusedttlhours): {{Integer}}
  [MountPath](#cfn-deadline-fleet-persistentvolumeconfiguration-mountpath): {{String}}
  [SizeGiB](#cfn-deadline-fleet-persistentvolumeconfiguration-sizegib): {{Integer}}
  [ThroughputMiB](#cfn-deadline-fleet-persistentvolumeconfiguration-throughputmib): {{Integer}}
```

## Properties
<a name="aws-properties-deadline-fleet-persistentvolumeconfiguration-properties"></a>

`Iops`  <a name="cfn-deadline-fleet-persistentvolumeconfiguration-iops"></a>
The IOPS per persistent volume. The default is 3000.
*Required*: No
*Type*: Integer
*Minimum*: `100`
*Maximum*: `80000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LastUsedTtlHours`  <a name="cfn-deadline-fleet-persistentvolumeconfiguration-lastusedttlhours"></a>
The number of hours a persistent volume can remain unused before it is deleted. The default is 168 (7 days).
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `8760`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MountPath`  <a name="cfn-deadline-fleet-persistentvolumeconfiguration-mountpath"></a>
The file system path where the persistent volume is mounted on the worker instance.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SizeGiB`  <a name="cfn-deadline-fleet-persistentvolumeconfiguration-sizegib"></a>
The persistent volume size in GiB. The default is 250.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65536`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThroughputMiB`  <a name="cfn-deadline-fleet-persistentvolumeconfiguration-throughputmib"></a>
The throughput per persistent volume in MiB. The default is 125.
*Required*: No
*Type*: Integer
*Minimum*: `125`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
