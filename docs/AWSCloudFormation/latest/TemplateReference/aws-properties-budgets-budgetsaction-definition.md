---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-budgets-budgetsaction-definition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Budgets::BudgetsAction Definition
<a name="aws-properties-budgets-budgetsaction-definition"></a>

The definition is where you specify all of the type-specific parameters.

## Syntax
<a name="aws-properties-budgets-budgetsaction-definition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-budgets-budgetsaction-definition-syntax.json"></a>

```
{
  "[IamActionDefinition](#cfn-budgets-budgetsaction-definition-iamactiondefinition)" : {{IamActionDefinition}},
  "[ScpActionDefinition](#cfn-budgets-budgetsaction-definition-scpactiondefinition)" : {{ScpActionDefinition}},
  "[SsmActionDefinition](#cfn-budgets-budgetsaction-definition-ssmactiondefinition)" : {{SsmActionDefinition}}
}
```

### YAML
<a name="aws-properties-budgets-budgetsaction-definition-syntax.yaml"></a>

```
  [IamActionDefinition](#cfn-budgets-budgetsaction-definition-iamactiondefinition): {{
    IamActionDefinition}}
  [ScpActionDefinition](#cfn-budgets-budgetsaction-definition-scpactiondefinition): {{
    ScpActionDefinition}}
  [SsmActionDefinition](#cfn-budgets-budgetsaction-definition-ssmactiondefinition): {{
    SsmActionDefinition}}
```

## Properties
<a name="aws-properties-budgets-budgetsaction-definition-properties"></a>

`IamActionDefinition`  <a name="cfn-budgets-budgetsaction-definition-iamactiondefinition"></a>
The AWS Identity and Access Management (IAM) action definition details.
*Required*: No
*Type*: [IamActionDefinition](aws-properties-budgets-budgetsaction-iamactiondefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScpActionDefinition`  <a name="cfn-budgets-budgetsaction-definition-scpactiondefinition"></a>
The service control policies (SCP) action definition details.
*Required*: No
*Type*: [ScpActionDefinition](aws-properties-budgets-budgetsaction-scpactiondefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SsmActionDefinition`  <a name="cfn-budgets-budgetsaction-definition-ssmactiondefinition"></a>
The Amazon EC2 Systems Manager (SSM) action definition details.
*Required*: No
*Type*: [SsmActionDefinition](aws-properties-budgets-budgetsaction-ssmactiondefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
