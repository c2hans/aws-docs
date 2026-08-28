---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-arcconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template ArcConfiguration
<a name="aws-properties-quicksight-template-arcconfiguration"></a>

The arc configuration of a `GaugeChartVisual`.

## Syntax
<a name="aws-properties-quicksight-template-arcconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-arcconfiguration-syntax.json"></a>

```
{
  "[ArcAngle](#cfn-quicksight-template-arcconfiguration-arcangle)" : {{Number}},
  "[ArcThickness](#cfn-quicksight-template-arcconfiguration-arcthickness)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-arcconfiguration-syntax.yaml"></a>

```
  [ArcAngle](#cfn-quicksight-template-arcconfiguration-arcangle): {{Number}}
  [ArcThickness](#cfn-quicksight-template-arcconfiguration-arcthickness): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-arcconfiguration-properties"></a>

`ArcAngle`  <a name="cfn-quicksight-template-arcconfiguration-arcangle"></a>
The option that determines the arc angle of a `GaugeChartVisual`.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ArcThickness`  <a name="cfn-quicksight-template-arcconfiguration-arcthickness"></a>
The options that determine the arc thickness of a `GaugeChartVisual`.
*Required*: No
*Type*: String
*Allowed values*: `SMALL | MEDIUM | LARGE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
