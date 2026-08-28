---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-personalize-metricattribution-metricattribute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::MetricAttribution MetricAttribute
<a name="aws-properties-personalize-metricattribution-metricattribute"></a>

Contains information on a metric that a metric attribution reports on. For more information, see [Measuring impact of recommendations](https://docs.aws.amazon.com/personalize/latest/dg/measuring-recommendation-impact.html).

## Syntax
<a name="aws-properties-personalize-metricattribution-metricattribute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-personalize-metricattribution-metricattribute-syntax.json"></a>

```
{
  "[EventType](#cfn-personalize-metricattribution-metricattribute-eventtype)" : {{String}},
  "[Expression](#cfn-personalize-metricattribution-metricattribute-expression)" : {{String}},
  "[MetricName](#cfn-personalize-metricattribution-metricattribute-metricname)" : {{String}}
}
```

### YAML
<a name="aws-properties-personalize-metricattribution-metricattribute-syntax.yaml"></a>

```
  [EventType](#cfn-personalize-metricattribution-metricattribute-eventtype): {{String}}
  [Expression](#cfn-personalize-metricattribution-metricattribute-expression): {{String}}
  [MetricName](#cfn-personalize-metricattribution-metricattribute-metricname): {{String}}
```

## Properties
<a name="aws-properties-personalize-metricattribution-metricattribute-properties"></a>

`EventType`  <a name="cfn-personalize-metricattribution-metricattribute-eventtype"></a>
The metric's event type.
*Required*: Yes
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Expression`  <a name="cfn-personalize-metricattribution-metricattribute-expression"></a>
The attribute's expression. Available functions are `SUM()` or `SAMPLECOUNT()`. For SUM() functions, provide the dataset type (either Interactions or Items) and column to sum as a parameter. For example SUM(Items.PRICE).
*Required*: Yes
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MetricName`  <a name="cfn-personalize-metricattribution-metricattribute-metricname"></a>
The metric's name. The name helps you identify the metric in Amazon CloudWatch or Amazon S3.
*Required*: Yes
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
