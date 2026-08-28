---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-budgets-budgetsaction-scpactiondefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Budgets::BudgetsAction ScpActionDefinition
<a name="aws-properties-budgets-budgetsaction-scpactiondefinition"></a>

The service control policies (SCP) action definition details.

## Syntax
<a name="aws-properties-budgets-budgetsaction-scpactiondefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-budgets-budgetsaction-scpactiondefinition-syntax.json"></a>

```
{
  "[PolicyId](#cfn-budgets-budgetsaction-scpactiondefinition-policyid)" : {{String}},
  "[TargetIds](#cfn-budgets-budgetsaction-scpactiondefinition-targetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-budgets-budgetsaction-scpactiondefinition-syntax.yaml"></a>

```
  [PolicyId](#cfn-budgets-budgetsaction-scpactiondefinition-policyid): {{String}}
  [TargetIds](#cfn-budgets-budgetsaction-scpactiondefinition-targetids): {{
    - String}}
```

## Properties
<a name="aws-properties-budgets-budgetsaction-scpactiondefinition-properties"></a>

`PolicyId`  <a name="cfn-budgets-budgetsaction-scpactiondefinition-policyid"></a>
The policy ID attached.
*Required*: Yes
*Type*: String
*Pattern*: `^p-[0-9a-zA-Z_]{8,128}$`
*Minimum*: `10`
*Maximum*: `130`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetIds`  <a name="cfn-budgets-budgetsaction-scpactiondefinition-targetids"></a>
A list of target IDs.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
