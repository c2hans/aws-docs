---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lightsail-disk-autosnapshotaddon.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::Disk AutoSnapshotAddOn
<a name="aws-properties-lightsail-disk-autosnapshotaddon"></a>

`AutoSnapshotAddOn` is a property of the [AddOn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html) property. It describes the automatic snapshot add-on for a disk.

## Syntax
<a name="aws-properties-lightsail-disk-autosnapshotaddon-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lightsail-disk-autosnapshotaddon-syntax.json"></a>

```
{
  "[SnapshotTimeOfDay](#cfn-lightsail-disk-autosnapshotaddon-snapshottimeofday)" : {{String}}
}
```

### YAML
<a name="aws-properties-lightsail-disk-autosnapshotaddon-syntax.yaml"></a>

```
  [SnapshotTimeOfDay](#cfn-lightsail-disk-autosnapshotaddon-snapshottimeofday): {{String}}
```

## Properties
<a name="aws-properties-lightsail-disk-autosnapshotaddon-properties"></a>

`SnapshotTimeOfDay`  <a name="cfn-lightsail-disk-autosnapshotaddon-snapshottimeofday"></a>
The daily time when an automatic snapshot will be created.
Constraints:
+ Must be in `HH:00` format, and in an hourly increment.
+ Specified in Coordinated Universal Time (UTC).
+ The snapshot will be automatically created between the time specified and up to 45 minutes after.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{2}:00$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
