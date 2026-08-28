---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-missingdataconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis MissingDataConfiguration
<a name="aws-properties-quicksight-analysis-missingdataconfiguration"></a>

The configuration options that determine how missing data is treated during the rendering of a line chart.

## Syntax
<a name="aws-properties-quicksight-analysis-missingdataconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-missingdataconfiguration-syntax.json"></a>

```
{
  "[TreatmentOption](#cfn-quicksight-analysis-missingdataconfiguration-treatmentoption)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-missingdataconfiguration-syntax.yaml"></a>

```
  [TreatmentOption](#cfn-quicksight-analysis-missingdataconfiguration-treatmentoption): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-missingdataconfiguration-properties"></a>

`TreatmentOption`  <a name="cfn-quicksight-analysis-missingdataconfiguration-treatmentoption"></a>
The treatment option that determines how missing data should be rendered. Choose from the following options:
+ `INTERPOLATE`: Interpolate missing values between the prior and the next known value.
+ `SHOW_AS_ZERO`: Show missing values as the value `0`.
+ `SHOW_AS_BLANK`: Display a blank space when rendering missing data.
*Required*: No
*Type*: String
*Allowed values*: `INTERPOLATE | SHOW_AS_ZERO | SHOW_AS_BLANK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
