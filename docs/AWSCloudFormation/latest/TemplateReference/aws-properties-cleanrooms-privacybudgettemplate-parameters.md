---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-privacybudgettemplate-parameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::PrivacyBudgetTemplate Parameters
<a name="aws-properties-cleanrooms-privacybudgettemplate-parameters"></a>

Specifies the epsilon and noise parameters for the privacy budget template.

## Syntax
<a name="aws-properties-cleanrooms-privacybudgettemplate-parameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-privacybudgettemplate-parameters-syntax.json"></a>

```
{
  "[BudgetParameters](#cfn-cleanrooms-privacybudgettemplate-parameters-budgetparameters)" : {{[ BudgetParameter, ... ]}},
  "[Epsilon](#cfn-cleanrooms-privacybudgettemplate-parameters-epsilon)" : {{Integer}},
  "[ResourceArn](#cfn-cleanrooms-privacybudgettemplate-parameters-resourcearn)" : {{String}},
  "[UsersNoisePerQuery](#cfn-cleanrooms-privacybudgettemplate-parameters-usersnoiseperquery)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-cleanrooms-privacybudgettemplate-parameters-syntax.yaml"></a>

```
  [BudgetParameters](#cfn-cleanrooms-privacybudgettemplate-parameters-budgetparameters): {{
    - BudgetParameter}}
  [Epsilon](#cfn-cleanrooms-privacybudgettemplate-parameters-epsilon): {{Integer}}
  [ResourceArn](#cfn-cleanrooms-privacybudgettemplate-parameters-resourcearn): {{String}}
  [UsersNoisePerQuery](#cfn-cleanrooms-privacybudgettemplate-parameters-usersnoiseperquery): {{Integer}}
```

## Properties
<a name="aws-properties-cleanrooms-privacybudgettemplate-parameters-properties"></a>

`BudgetParameters`  <a name="cfn-cleanrooms-privacybudgettemplate-parameters-budgetparameters"></a>
Property description not available.
*Required*: No
*Type*: Array of [BudgetParameter](aws-properties-cleanrooms-privacybudgettemplate-budgetparameter.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Epsilon`  <a name="cfn-cleanrooms-privacybudgettemplate-parameters-epsilon"></a>
The epsilon value that you want to use.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceArn`  <a name="cfn-cleanrooms-privacybudgettemplate-parameters-resourcearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UsersNoisePerQuery`  <a name="cfn-cleanrooms-privacybudgettemplate-parameters-usersnoiseperquery"></a>
Noise added per query is measured in terms of the number of users whose contributions you want to obscure. This value governs the rate at which the privacy budget is depleted.
*Required*: No
*Type*: Integer
*Minimum*: `10`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
