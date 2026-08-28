---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-stackset-parameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::StackSet Parameter
<a name="aws-properties-cloudformation-stackset-parameter"></a>

The Parameter data type.

## Syntax
<a name="aws-properties-cloudformation-stackset-parameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudformation-stackset-parameter-syntax.json"></a>

```
{
  "[ParameterKey](#cfn-cloudformation-stackset-parameter-parameterkey)" : {{String}},
  "[ParameterValue](#cfn-cloudformation-stackset-parameter-parametervalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudformation-stackset-parameter-syntax.yaml"></a>

```
  [ParameterKey](#cfn-cloudformation-stackset-parameter-parameterkey): {{String}}
  [ParameterValue](#cfn-cloudformation-stackset-parameter-parametervalue): {{String}}
```

## Properties
<a name="aws-properties-cloudformation-stackset-parameter-properties"></a>

`ParameterKey`  <a name="cfn-cloudformation-stackset-parameter-parameterkey"></a>
The key associated with the parameter. If you don't specify a key and value for a particular parameter, CloudFormation uses the default value that's specified in your template.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterValue`  <a name="cfn-cloudformation-stackset-parameter-parametervalue"></a>
The input value associated with the parameter.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
