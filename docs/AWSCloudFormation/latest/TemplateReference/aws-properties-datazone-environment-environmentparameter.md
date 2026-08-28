---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-environment-environmentparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Environment EnvironmentParameter
<a name="aws-properties-datazone-environment-environmentparameter"></a>

The parameter details of the environment.

## Syntax
<a name="aws-properties-datazone-environment-environmentparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-environment-environmentparameter-syntax.json"></a>

```
{
  "[Name](#cfn-datazone-environment-environmentparameter-name)" : {{String}},
  "[Value](#cfn-datazone-environment-environmentparameter-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-environment-environmentparameter-syntax.yaml"></a>

```
  [Name](#cfn-datazone-environment-environmentparameter-name): {{String}}
  [Value](#cfn-datazone-environment-environmentparameter-value): {{String}}
```

## Properties
<a name="aws-properties-datazone-environment-environmentparameter-properties"></a>

`Name`  <a name="cfn-datazone-environment-environmentparameter-name"></a>
The name of the environment parameter.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-datazone-environment-environmentparameter-value"></a>
The value of the environment parameter.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
