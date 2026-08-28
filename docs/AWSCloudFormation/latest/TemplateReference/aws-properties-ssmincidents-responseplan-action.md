---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssmincidents-responseplan-action.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMIncidents::ResponsePlan Action
<a name="aws-properties-ssmincidents-responseplan-action"></a>

The `Action` property type specifies the configuration to launch.

## Syntax
<a name="aws-properties-ssmincidents-responseplan-action-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssmincidents-responseplan-action-syntax.json"></a>

```
{
  "[SsmAutomation](#cfn-ssmincidents-responseplan-action-ssmautomation)" : {{SsmAutomation}}
}
```

### YAML
<a name="aws-properties-ssmincidents-responseplan-action-syntax.yaml"></a>

```
  [SsmAutomation](#cfn-ssmincidents-responseplan-action-ssmautomation): {{
    SsmAutomation}}
```

## Properties
<a name="aws-properties-ssmincidents-responseplan-action-properties"></a>

`SsmAutomation`  <a name="cfn-ssmincidents-responseplan-action-ssmautomation"></a>
Details about the Systems Manager automation document that will be used as a runbook during an incident.
*Required*: No
*Type*: [SsmAutomation](aws-properties-ssmincidents-responseplan-ssmautomation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
