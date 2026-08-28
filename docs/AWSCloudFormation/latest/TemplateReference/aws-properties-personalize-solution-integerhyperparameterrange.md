---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-personalize-solution-integerhyperparameterrange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::Solution IntegerHyperParameterRange
<a name="aws-properties-personalize-solution-integerhyperparameterrange"></a>

Provides the name and range of an integer-valued hyperparameter.

## Syntax
<a name="aws-properties-personalize-solution-integerhyperparameterrange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-personalize-solution-integerhyperparameterrange-syntax.json"></a>

```
{
  "[MaxValue](#cfn-personalize-solution-integerhyperparameterrange-maxvalue)" : {{Integer}},
  "[MinValue](#cfn-personalize-solution-integerhyperparameterrange-minvalue)" : {{Integer}},
  "[Name](#cfn-personalize-solution-integerhyperparameterrange-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-personalize-solution-integerhyperparameterrange-syntax.yaml"></a>

```
  [MaxValue](#cfn-personalize-solution-integerhyperparameterrange-maxvalue): {{Integer}}
  [MinValue](#cfn-personalize-solution-integerhyperparameterrange-minvalue): {{Integer}}
  [Name](#cfn-personalize-solution-integerhyperparameterrange-name): {{String}}
```

## Properties
<a name="aws-properties-personalize-solution-integerhyperparameterrange-properties"></a>

`MaxValue`  <a name="cfn-personalize-solution-integerhyperparameterrange-maxvalue"></a>
The maximum allowable value for the hyperparameter.
*Required*: No
*Type*: Integer
*Maximum*: `1000000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MinValue`  <a name="cfn-personalize-solution-integerhyperparameterrange-minvalue"></a>
The minimum allowable value for the hyperparameter.
*Required*: No
*Type*: Integer
*Minimum*: `-1000000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-personalize-solution-integerhyperparameterrange-name"></a>
The name of the hyperparameter.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
