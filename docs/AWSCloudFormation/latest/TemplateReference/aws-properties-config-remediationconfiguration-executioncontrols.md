---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-config-remediationconfiguration-executioncontrols.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::RemediationConfiguration ExecutionControls
<a name="aws-properties-config-remediationconfiguration-executioncontrols"></a>

An ExecutionControls object.

## Syntax
<a name="aws-properties-config-remediationconfiguration-executioncontrols-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-config-remediationconfiguration-executioncontrols-syntax.json"></a>

```
{
  "[SsmControls](#cfn-config-remediationconfiguration-executioncontrols-ssmcontrols)" : {{SsmControls}}
}
```

### YAML
<a name="aws-properties-config-remediationconfiguration-executioncontrols-syntax.yaml"></a>

```
  [SsmControls](#cfn-config-remediationconfiguration-executioncontrols-ssmcontrols): {{
    SsmControls}}
```

## Properties
<a name="aws-properties-config-remediationconfiguration-executioncontrols-properties"></a>

`SsmControls`  <a name="cfn-config-remediationconfiguration-executioncontrols-ssmcontrols"></a>
A SsmControls object.
*Required*: No
*Type*: [SsmControls](aws-properties-config-remediationconfiguration-ssmcontrols.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
