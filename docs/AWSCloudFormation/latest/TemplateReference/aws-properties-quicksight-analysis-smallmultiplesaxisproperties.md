---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-smallmultiplesaxisproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis SmallMultiplesAxisProperties
<a name="aws-properties-quicksight-analysis-smallmultiplesaxisproperties"></a>

Configures the properties of a chart's axes that are used by small multiples panels.

## Syntax
<a name="aws-properties-quicksight-analysis-smallmultiplesaxisproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-smallmultiplesaxisproperties-syntax.json"></a>

```
{
  "[Placement](#cfn-quicksight-analysis-smallmultiplesaxisproperties-placement)" : {{String}},
  "[Scale](#cfn-quicksight-analysis-smallmultiplesaxisproperties-scale)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-smallmultiplesaxisproperties-syntax.yaml"></a>

```
  [Placement](#cfn-quicksight-analysis-smallmultiplesaxisproperties-placement): {{String}}
  [Scale](#cfn-quicksight-analysis-smallmultiplesaxisproperties-scale): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-smallmultiplesaxisproperties-properties"></a>

`Placement`  <a name="cfn-quicksight-analysis-smallmultiplesaxisproperties-placement"></a>
Defines the placement of the axis. By default, axes are rendered `OUTSIDE` of the panels. Axes with `INDEPENDENT` scale are rendered `INSIDE` the panels.
*Required*: No
*Type*: String
*Allowed values*: `OUTSIDE | INSIDE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scale`  <a name="cfn-quicksight-analysis-smallmultiplesaxisproperties-scale"></a>
Determines whether scale of the axes are shared or independent. The default value is `SHARED`.
*Required*: No
*Type*: String
*Allowed values*: `SHARED | INDEPENDENT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
