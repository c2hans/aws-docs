---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-personalize-metricattribution-metricsoutputconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::MetricAttribution MetricsOutputConfig
<a name="aws-properties-personalize-metricattribution-metricsoutputconfig"></a>

<a name="aws-properties-personalize-metricattribution-metricsoutputconfig-description"></a>The `MetricsOutputConfig` property type specifies Property description not available. for an [AWS::Personalize::MetricAttribution](aws-resource-personalize-metricattribution.md).

## Syntax
<a name="aws-properties-personalize-metricattribution-metricsoutputconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-personalize-metricattribution-metricsoutputconfig-syntax.json"></a>

```
{
  "[RoleArn](#cfn-personalize-metricattribution-metricsoutputconfig-rolearn)" : {{String}},
  "[S3DataDestination](#cfn-personalize-metricattribution-metricsoutputconfig-s3datadestination)" : {{S3DataDestination}}
}
```

### YAML
<a name="aws-properties-personalize-metricattribution-metricsoutputconfig-syntax.yaml"></a>

```
  [RoleArn](#cfn-personalize-metricattribution-metricsoutputconfig-rolearn): {{String}}
  [S3DataDestination](#cfn-personalize-metricattribution-metricsoutputconfig-s3datadestination): {{
    S3DataDestination}}
```

## Properties
<a name="aws-properties-personalize-metricattribution-metricsoutputconfig-properties"></a>

`RoleArn`  <a name="cfn-personalize-metricattribution-metricsoutputconfig-rolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:([a-z\d-]+):iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3DataDestination`  <a name="cfn-personalize-metricattribution-metricsoutputconfig-s3datadestination"></a>
Property description not available.
*Required*: No
*Type*: [S3DataDestination](aws-properties-personalize-metricattribution-s3datadestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
