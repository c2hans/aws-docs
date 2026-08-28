---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-dataaccessor-actionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::DataAccessor ActionConfiguration
<a name="aws-properties-qbusiness-dataaccessor-actionconfiguration"></a>

Specifies an allowed action and its associated filter configuration.

## Syntax
<a name="aws-properties-qbusiness-dataaccessor-actionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-dataaccessor-actionconfiguration-syntax.json"></a>

```
{
  "[Action](#cfn-qbusiness-dataaccessor-actionconfiguration-action)" : {{String}},
  "[FilterConfiguration](#cfn-qbusiness-dataaccessor-actionconfiguration-filterconfiguration)" : {{ActionFilterConfiguration}}
}
```

### YAML
<a name="aws-properties-qbusiness-dataaccessor-actionconfiguration-syntax.yaml"></a>

```
  [Action](#cfn-qbusiness-dataaccessor-actionconfiguration-action): {{String}}
  [FilterConfiguration](#cfn-qbusiness-dataaccessor-actionconfiguration-filterconfiguration): {{
    ActionFilterConfiguration}}
```

## Properties
<a name="aws-properties-qbusiness-dataaccessor-actionconfiguration-properties"></a>

`Action`  <a name="cfn-qbusiness-dataaccessor-actionconfiguration-action"></a>
The Amazon Q Business action that is allowed.
*Required*: Yes
*Type*: String
*Pattern*: `^qbusiness:[a-zA-Z]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterConfiguration`  <a name="cfn-qbusiness-dataaccessor-actionconfiguration-filterconfiguration"></a>
The filter configuration for the action, if any.
*Required*: No
*Type*: [ActionFilterConfiguration](aws-properties-qbusiness-dataaccessor-actionfilterconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
