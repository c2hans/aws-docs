---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-projectprofile-environmentconfigurationparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::ProjectProfile EnvironmentConfigurationParameter
<a name="aws-properties-datazone-projectprofile-environmentconfigurationparameter"></a>

The environment configuration parameter.

## Syntax
<a name="aws-properties-datazone-projectprofile-environmentconfigurationparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-projectprofile-environmentconfigurationparameter-syntax.json"></a>

```
{
  "[IsEditable](#cfn-datazone-projectprofile-environmentconfigurationparameter-iseditable)" : {{Boolean}},
  "[Name](#cfn-datazone-projectprofile-environmentconfigurationparameter-name)" : {{String}},
  "[Value](#cfn-datazone-projectprofile-environmentconfigurationparameter-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-projectprofile-environmentconfigurationparameter-syntax.yaml"></a>

```
  [IsEditable](#cfn-datazone-projectprofile-environmentconfigurationparameter-iseditable): {{Boolean}}
  [Name](#cfn-datazone-projectprofile-environmentconfigurationparameter-name): {{String}}
  [Value](#cfn-datazone-projectprofile-environmentconfigurationparameter-value): {{String}}
```

## Properties
<a name="aws-properties-datazone-projectprofile-environmentconfigurationparameter-properties"></a>

`IsEditable`  <a name="cfn-datazone-projectprofile-environmentconfigurationparameter-iseditable"></a>
Specifies whether the environment parameter is editable.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-datazone-projectprofile-environmentconfigurationparameter-name"></a>
The name of the environment configuration parameter.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z_][a-zA-Z0-9_]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-datazone-projectprofile-environmentconfigurationparameter-value"></a>
The value of the environment configuration parameter.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
