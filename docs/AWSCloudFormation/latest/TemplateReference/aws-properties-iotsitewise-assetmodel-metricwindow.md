---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-assetmodel-metricwindow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::AssetModel MetricWindow
<a name="aws-properties-iotsitewise-assetmodel-metricwindow"></a>

Contains a time interval window used for data aggregate computations (for example, average, sum, count, and so on).

## Syntax
<a name="aws-properties-iotsitewise-assetmodel-metricwindow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-assetmodel-metricwindow-syntax.json"></a>

```
{
  "[Tumbling](#cfn-iotsitewise-assetmodel-metricwindow-tumbling)" : {{TumblingWindow}}
}
```

### YAML
<a name="aws-properties-iotsitewise-assetmodel-metricwindow-syntax.yaml"></a>

```
  [Tumbling](#cfn-iotsitewise-assetmodel-metricwindow-tumbling): {{
    TumblingWindow}}
```

## Properties
<a name="aws-properties-iotsitewise-assetmodel-metricwindow-properties"></a>

`Tumbling`  <a name="cfn-iotsitewise-assetmodel-metricwindow-tumbling"></a>
The tumbling time interval window.
*Required*: No
*Type*: [TumblingWindow](aws-properties-iotsitewise-assetmodel-tumblingwindow.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
