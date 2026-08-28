---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cases-caserule-requiredcaserule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cases::CaseRule RequiredCaseRule
<a name="aws-properties-cases-caserule-requiredcaserule"></a>

Required rule type, used to indicate whether a field is required. In the Connect Customer admin website, case rules are known as *case field conditions*. For more information about case field conditions, see [Add case field conditions to a case template](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html).

## Syntax
<a name="aws-properties-cases-caserule-requiredcaserule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cases-caserule-requiredcaserule-syntax.json"></a>

```
{
  "[Conditions](#cfn-cases-caserule-requiredcaserule-conditions)" : {{[ BooleanCondition, ... ]}},
  "[DefaultValue](#cfn-cases-caserule-requiredcaserule-defaultvalue)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cases-caserule-requiredcaserule-syntax.yaml"></a>

```
  [Conditions](#cfn-cases-caserule-requiredcaserule-conditions): {{
    - BooleanCondition}}
  [DefaultValue](#cfn-cases-caserule-requiredcaserule-defaultvalue): {{Boolean}}
```

## Properties
<a name="aws-properties-cases-caserule-requiredcaserule-properties"></a>

`Conditions`  <a name="cfn-cases-caserule-requiredcaserule-conditions"></a>
List of conditions for the required rule; the first condition to evaluate to true dictates the value of the rule.
*Required*: Yes
*Type*: Array of [BooleanCondition](aws-properties-cases-caserule-booleancondition.md)
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultValue`  <a name="cfn-cases-caserule-requiredcaserule-defaultvalue"></a>
The value of the rule (that is, whether the field is required) should none of the conditions evaluate to true.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
