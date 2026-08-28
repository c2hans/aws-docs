---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-project-environmentparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Project EnvironmentParameter
<a name="aws-properties-datazone-project-environmentparameter"></a>

The parameter details of an evironment profile.

## Syntax
<a name="aws-properties-datazone-project-environmentparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-project-environmentparameter-syntax.json"></a>

```
{
  "[Name](#cfn-datazone-project-environmentparameter-name)" : {{String}},
  "[Value](#cfn-datazone-project-environmentparameter-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-project-environmentparameter-syntax.yaml"></a>

```
  [Name](#cfn-datazone-project-environmentparameter-name): {{String}}
  [Value](#cfn-datazone-project-environmentparameter-value): {{String}}
```

## Properties
<a name="aws-properties-datazone-project-environmentparameter-properties"></a>

`Name`  <a name="cfn-datazone-project-environmentparameter-name"></a>
The name of an environment profile parameter.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-datazone-project-environmentparameter-value"></a>
The value of an environment profile parameter.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
