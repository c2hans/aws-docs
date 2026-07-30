---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-workspace-limitsperlabelsetentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::Workspace LimitsPerLabelSetEntry
<a name="aws-properties-aps-workspace-limitsperlabelsetentry"></a>

 This structure contains the limits that apply to time series that match one label set.

## Syntax
<a name="aws-properties-aps-workspace-limitsperlabelsetentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-workspace-limitsperlabelsetentry-syntax.json"></a>

```
{
  "[MaxSeries](#cfn-aps-workspace-limitsperlabelsetentry-maxseries)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-aps-workspace-limitsperlabelsetentry-syntax.yaml"></a>

```
  [MaxSeries](#cfn-aps-workspace-limitsperlabelsetentry-maxseries): {{Integer}}
```

## Properties
<a name="aws-properties-aps-workspace-limitsperlabelsetentry-properties"></a>

`MaxSeries`  <a name="cfn-aps-workspace-limitsperlabelsetentry-maxseries"></a>
The maximum number of active series that can be ingested that match this label set.
Setting this to 0 causes no label set limit to be enforced, but it does cause Amazon Managed Service for Prometheus to vend label set metrics to CloudWatch
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
