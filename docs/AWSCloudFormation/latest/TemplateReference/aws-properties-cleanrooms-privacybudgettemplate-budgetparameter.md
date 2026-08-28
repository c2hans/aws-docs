---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-privacybudgettemplate-budgetparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::PrivacyBudgetTemplate BudgetParameter
<a name="aws-properties-cleanrooms-privacybudgettemplate-budgetparameter"></a>

Individual budget parameter configuration that defines specific budget allocation settings for access budgets.

## Syntax
<a name="aws-properties-cleanrooms-privacybudgettemplate-budgetparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-privacybudgettemplate-budgetparameter-syntax.json"></a>

```
{
  "[AutoRefresh](#cfn-cleanrooms-privacybudgettemplate-budgetparameter-autorefresh)" : {{String}},
  "[Budget](#cfn-cleanrooms-privacybudgettemplate-budgetparameter-budget)" : {{Integer}},
  "[Type](#cfn-cleanrooms-privacybudgettemplate-budgetparameter-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-privacybudgettemplate-budgetparameter-syntax.yaml"></a>

```
  [AutoRefresh](#cfn-cleanrooms-privacybudgettemplate-budgetparameter-autorefresh): {{String}}
  [Budget](#cfn-cleanrooms-privacybudgettemplate-budgetparameter-budget): {{Integer}}
  [Type](#cfn-cleanrooms-privacybudgettemplate-budgetparameter-type): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-privacybudgettemplate-budgetparameter-properties"></a>

`AutoRefresh`  <a name="cfn-cleanrooms-privacybudgettemplate-budgetparameter-autorefresh"></a>
Whether this individual budget parameter automatically refreshes when the budget period resets.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Budget`  <a name="cfn-cleanrooms-privacybudgettemplate-budgetparameter-budget"></a>
The budget allocation amount for this specific parameter.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-cleanrooms-privacybudgettemplate-budgetparameter-type"></a>
The type of budget parameter being configured.
*Required*: Yes
*Type*: String
*Allowed values*: `CALENDAR_DAY | CALENDAR_MONTH | CALENDAR_WEEK | LIFETIME`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
