---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-workspace-workspaceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::Workspace WorkspaceConfiguration
<a name="aws-properties-aps-workspace-workspaceconfiguration"></a>

Use this structure to define label sets and the ingestion limits for time series that match label sets, and to specify the retention period of the workspace.

## Syntax
<a name="aws-properties-aps-workspace-workspaceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-workspace-workspaceconfiguration-syntax.json"></a>

```
{
  "[LimitsPerLabelSets](#cfn-aps-workspace-workspaceconfiguration-limitsperlabelsets)" : {{[ LimitsPerLabelSet, ... ]}},
  "[OutOfOrderTimeWindowInSeconds](#cfn-aps-workspace-workspaceconfiguration-outofordertimewindowinseconds)" : {{Integer}},
  "[RetentionPeriodInDays](#cfn-aps-workspace-workspaceconfiguration-retentionperiodindays)" : {{Integer}},
  "[RuleQueryOffsetInSeconds](#cfn-aps-workspace-workspaceconfiguration-rulequeryoffsetinseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-aps-workspace-workspaceconfiguration-syntax.yaml"></a>

```
  [LimitsPerLabelSets](#cfn-aps-workspace-workspaceconfiguration-limitsperlabelsets): {{
    - LimitsPerLabelSet}}
  [OutOfOrderTimeWindowInSeconds](#cfn-aps-workspace-workspaceconfiguration-outofordertimewindowinseconds): {{Integer}}
  [RetentionPeriodInDays](#cfn-aps-workspace-workspaceconfiguration-retentionperiodindays): {{Integer}}
  [RuleQueryOffsetInSeconds](#cfn-aps-workspace-workspaceconfiguration-rulequeryoffsetinseconds): {{Integer}}
```

## Properties
<a name="aws-properties-aps-workspace-workspaceconfiguration-properties"></a>

`LimitsPerLabelSets`  <a name="cfn-aps-workspace-workspaceconfiguration-limitsperlabelsets"></a>
This is an array of structures, where each structure defines a label set for the workspace, and defines the ingestion limit for active time series for each of those label sets. Each label name in a label set must be unique.
*Required*: No
*Type*: Array of [LimitsPerLabelSet](aws-properties-aps-workspace-limitsperlabelset.md)
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutOfOrderTimeWindowInSeconds`  <a name="cfn-aps-workspace-workspaceconfiguration-outofordertimewindowinseconds"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetentionPeriodInDays`  <a name="cfn-aps-workspace-workspaceconfiguration-retentionperiodindays"></a>
Specifies how many days that metrics will be retained in the workspace.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleQueryOffsetInSeconds`  <a name="cfn-aps-workspace-workspaceconfiguration-rulequeryoffsetinseconds"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
