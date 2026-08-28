---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-datapathcolor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis DataPathColor
<a name="aws-properties-quicksight-analysis-datapathcolor"></a>

The color map that determines the color options for a particular element.

## Syntax
<a name="aws-properties-quicksight-analysis-datapathcolor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-datapathcolor-syntax.json"></a>

```
{
  "[Color](#cfn-quicksight-analysis-datapathcolor-color)" : {{String}},
  "[Element](#cfn-quicksight-analysis-datapathcolor-element)" : {{DataPathValue}},
  "[TimeGranularity](#cfn-quicksight-analysis-datapathcolor-timegranularity)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-datapathcolor-syntax.yaml"></a>

```
  [Color](#cfn-quicksight-analysis-datapathcolor-color): {{String}}
  [Element](#cfn-quicksight-analysis-datapathcolor-element): {{
    DataPathValue}}
  [TimeGranularity](#cfn-quicksight-analysis-datapathcolor-timegranularity): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-datapathcolor-properties"></a>

`Color`  <a name="cfn-quicksight-analysis-datapathcolor-color"></a>
The color that needs to be applied to the element.
*Required*: Yes
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Element`  <a name="cfn-quicksight-analysis-datapathcolor-element"></a>
The element that the color needs to be applied to.
*Required*: Yes
*Type*: [DataPathValue](aws-properties-quicksight-analysis-datapathvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeGranularity`  <a name="cfn-quicksight-analysis-datapathcolor-timegranularity"></a>
The time granularity of the field that the color needs to be applied to.
*Required*: No
*Type*: String
*Allowed values*: `YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | MILLISECOND`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
