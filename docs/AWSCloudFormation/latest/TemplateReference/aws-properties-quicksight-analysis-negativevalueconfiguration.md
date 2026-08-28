---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-negativevalueconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis NegativeValueConfiguration
<a name="aws-properties-quicksight-analysis-negativevalueconfiguration"></a>

The options that determine the negative value configuration.

## Syntax
<a name="aws-properties-quicksight-analysis-negativevalueconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-negativevalueconfiguration-syntax.json"></a>

```
{
  "[DisplayMode](#cfn-quicksight-analysis-negativevalueconfiguration-displaymode)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-negativevalueconfiguration-syntax.yaml"></a>

```
  [DisplayMode](#cfn-quicksight-analysis-negativevalueconfiguration-displaymode): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-negativevalueconfiguration-properties"></a>

`DisplayMode`  <a name="cfn-quicksight-analysis-negativevalueconfiguration-displaymode"></a>
Determines the display mode of the negative value configuration.
*Required*: Yes
*Type*: String
*Allowed values*: `POSITIVE | NEGATIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
