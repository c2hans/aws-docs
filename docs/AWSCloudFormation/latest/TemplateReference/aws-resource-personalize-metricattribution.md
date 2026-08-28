---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-personalize-metricattribution.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::MetricAttribution
<a name="aws-resource-personalize-metricattribution"></a>

Creates a metric attribution. A metric attribution creates reports on the data that you import into Amazon Personalize. Depending on how you imported the data, you can view reports in Amazon CloudWatch or Amazon S3. For more information, see [Measuring impact of recommendations](https://docs.aws.amazon.com/personalize/latest/dg/measuring-recommendation-impact.html).

## Syntax
<a name="aws-resource-personalize-metricattribution-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-personalize-metricattribution-syntax.json"></a>

```
{
  "Type" : "AWS::Personalize::MetricAttribution",
  "Properties" : {
      "[DatasetGroupArn](#cfn-personalize-metricattribution-datasetgrouparn)" : {{String}},
      "[Metrics](#cfn-personalize-metricattribution-metrics)" : {{[ MetricAttribute, ... ]}},
      "[MetricsOutputConfig](#cfn-personalize-metricattribution-metricsoutputconfig)" : {{MetricsOutputConfig}},
      "[Name](#cfn-personalize-metricattribution-name)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-personalize-metricattribution-syntax.yaml"></a>

```
Type: AWS::Personalize::MetricAttribution
Properties:
  [DatasetGroupArn](#cfn-personalize-metricattribution-datasetgrouparn): {{String}}
  [Metrics](#cfn-personalize-metricattribution-metrics): {{
    - MetricAttribute}}
  [MetricsOutputConfig](#cfn-personalize-metricattribution-metricsoutputconfig): {{
    MetricsOutputConfig}}
  [Name](#cfn-personalize-metricattribution-name): {{String}}
```

## Properties
<a name="aws-resource-personalize-metricattribution-properties"></a>

`DatasetGroupArn`  <a name="cfn-personalize-metricattribution-datasetgrouparn"></a>
The metric attribution's dataset group Amazon Resource Name (ARN).
*Required*: Yes
*Type*: String
*Pattern*: `^arn:([a-z\d-]+):personalize:.*:.*:.+$`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Metrics`  <a name="cfn-personalize-metricattribution-metrics"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [MetricAttribute](aws-properties-personalize-metricattribution-metricattribute.md)
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MetricsOutputConfig`  <a name="cfn-personalize-metricattribution-metricsoutputconfig"></a>
The metric attribution's output configuration.
*Required*: Yes
*Type*: [MetricsOutputConfig](aws-properties-personalize-metricattribution-metricsoutputconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-personalize-metricattribution-name"></a>
The metric attribution's name.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-personalize-metricattribution-return-values"></a>

### Ref
<a name="aws-resource-personalize-metricattribution-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-personalize-metricattribution-return-values-fn--getatt"></a>

####
<a name="aws-resource-personalize-metricattribution-return-values-fn--getatt-fn--getatt"></a>

`MetricAttributionArn`  <a name="MetricAttributionArn-fn::getatt"></a>
The metric attribution's Amazon Resource Name (ARN).

`Status`  <a name="Status-fn::getatt"></a>
The metric attribution's status.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
