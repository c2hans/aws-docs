---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cases-caserule-hiddencaserule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cases::CaseRule HiddenCaseRule
<a name="aws-properties-cases-caserule-hiddencaserule"></a>

A rule that controls field visibility based on conditions. Fields can be shown or hidden dynamically based on values in other fields.

## Syntax
<a name="aws-properties-cases-caserule-hiddencaserule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cases-caserule-hiddencaserule-syntax.json"></a>

```
{
  "[Conditions](#cfn-cases-caserule-hiddencaserule-conditions)" : {{[ BooleanCondition, ... ]}},
  "[DefaultValue](#cfn-cases-caserule-hiddencaserule-defaultvalue)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cases-caserule-hiddencaserule-syntax.yaml"></a>

```
  [Conditions](#cfn-cases-caserule-hiddencaserule-conditions): {{
    - BooleanCondition}}
  [DefaultValue](#cfn-cases-caserule-hiddencaserule-defaultvalue): {{Boolean}}
```

## Properties
<a name="aws-properties-cases-caserule-hiddencaserule-properties"></a>

`Conditions`  <a name="cfn-cases-caserule-hiddencaserule-conditions"></a>
A list of conditions that determine field visibility.
*Required*: Yes
*Type*: Array of [BooleanCondition](aws-properties-cases-caserule-booleancondition.md)
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultValue`  <a name="cfn-cases-caserule-hiddencaserule-defaultvalue"></a>
Whether the field is hidden when no conditions match.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
