---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-distributionconfiguration-fastlaunchsnapshotconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::DistributionConfiguration FastLaunchSnapshotConfiguration
<a name="aws-properties-imagebuilder-distributionconfiguration-fastlaunchsnapshotconfiguration"></a>

Configuration settings for creating and managing pre-provisioned snapshots for a fast-launch enabled Windows AMI.

## Syntax
<a name="aws-properties-imagebuilder-distributionconfiguration-fastlaunchsnapshotconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-distributionconfiguration-fastlaunchsnapshotconfiguration-syntax.json"></a>

```
{
  "[TargetResourceCount](#cfn-imagebuilder-distributionconfiguration-fastlaunchsnapshotconfiguration-targetresourcecount)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-imagebuilder-distributionconfiguration-fastlaunchsnapshotconfiguration-syntax.yaml"></a>

```
  [TargetResourceCount](#cfn-imagebuilder-distributionconfiguration-fastlaunchsnapshotconfiguration-targetresourcecount): {{Integer}}
```

## Properties
<a name="aws-properties-imagebuilder-distributionconfiguration-fastlaunchsnapshotconfiguration-properties"></a>

`TargetResourceCount`  <a name="cfn-imagebuilder-distributionconfiguration-fastlaunchsnapshotconfiguration-targetresourcecount"></a>
The number of pre-provisioned snapshots to keep on hand for a fast-launch enabled Windows AMI.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
