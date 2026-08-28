---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-metric-availablefilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Metric AvailableFilter
<a name="aws-properties-connect-metric-availablefilter"></a>

A filter that is available for use with the metric. Part of an AvailableFilterList that describes the filters that are available for use with the metric.

## Syntax
<a name="aws-properties-connect-metric-availablefilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-metric-availablefilter-syntax.json"></a>

```
{
  "[Id](#cfn-connect-metric-availablefilter-id)" : {{String}},
  "[Type](#cfn-connect-metric-availablefilter-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-metric-availablefilter-syntax.yaml"></a>

```
  [Id](#cfn-connect-metric-availablefilter-id): {{String}}
  [Type](#cfn-connect-metric-availablefilter-type): {{String}}
```

## Properties
<a name="aws-properties-connect-metric-availablefilter-properties"></a>

`Id`  <a name="cfn-connect-metric-availablefilter-id"></a>
The identifier of the filter.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-connect-metric-availablefilter-type"></a>
The type of the filter. Valid values: `METRIC_LEVEL` \| `RESOURCE_LEVEL`.
*Required*: Yes
*Type*: String
*Allowed values*: `METRIC_LEVEL | RESOURCE_LEVEL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
