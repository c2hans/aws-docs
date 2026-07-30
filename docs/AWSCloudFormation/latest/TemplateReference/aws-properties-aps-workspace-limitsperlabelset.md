---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-workspace-limitsperlabelset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::Workspace LimitsPerLabelSet
<a name="aws-properties-aps-workspace-limitsperlabelset"></a>

This defines a label set for the workspace, and defines the ingestion limit for active time series that match that label set. Each label name in a label set must be unique.

## Syntax
<a name="aws-properties-aps-workspace-limitsperlabelset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-workspace-limitsperlabelset-syntax.json"></a>

```
{
  "[LabelSet](#cfn-aps-workspace-limitsperlabelset-labelset)" : {{[ Label, ... ]}},
  "[Limits](#cfn-aps-workspace-limitsperlabelset-limits)" : {{LimitsPerLabelSetEntry}}
}
```

### YAML
<a name="aws-properties-aps-workspace-limitsperlabelset-syntax.yaml"></a>

```
  [LabelSet](#cfn-aps-workspace-limitsperlabelset-labelset): {{
    - Label}}
  [Limits](#cfn-aps-workspace-limitsperlabelset-limits): {{
    LimitsPerLabelSetEntry}}
```

## Properties
<a name="aws-properties-aps-workspace-limitsperlabelset-properties"></a>

`LabelSet`  <a name="cfn-aps-workspace-limitsperlabelset-labelset"></a>
This defines one label set that will have an enforced ingestion limit. You can set ingestion limits on time series that match defined label sets, to help prevent a workspace from being overwhelmed with unexpected spikes in time series ingestion.
Label values accept all UTF-8 characters with one exception. If the label name is metric name label `__name__`, then the *metric* part of the name must conform to the following pattern: `[a-zA-Z_:][a-zA-Z0-9_:]*`
*Required*: Yes
*Type*: Array of [Label](aws-properties-aps-workspace-label.md)
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Limits`  <a name="cfn-aps-workspace-limitsperlabelset-limits"></a>
This structure contains the information about the limits that apply to time series that match this label set.
*Required*: Yes
*Type*: [LimitsPerLabelSetEntry](aws-properties-aps-workspace-limitsperlabelsetentry.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
