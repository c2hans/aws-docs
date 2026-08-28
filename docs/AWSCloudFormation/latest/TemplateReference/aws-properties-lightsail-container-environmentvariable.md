---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lightsail-container-environmentvariable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::Container EnvironmentVariable
<a name="aws-properties-lightsail-container-environmentvariable"></a>

`EnvironmentVariable` is a property of the [Container](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-container.html) property. It describes the environment variables of a container on a container service which are key-value parameters that provide dynamic configuration of the application or script run by the container.

## Syntax
<a name="aws-properties-lightsail-container-environmentvariable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lightsail-container-environmentvariable-syntax.json"></a>

```
{
  "[Value](#cfn-lightsail-container-environmentvariable-value)" : {{String}},
  "[Variable](#cfn-lightsail-container-environmentvariable-variable)" : {{String}}
}
```

### YAML
<a name="aws-properties-lightsail-container-environmentvariable-syntax.yaml"></a>

```
  [Value](#cfn-lightsail-container-environmentvariable-value): {{String}}
  [Variable](#cfn-lightsail-container-environmentvariable-variable): {{String}}
```

## Properties
<a name="aws-properties-lightsail-container-environmentvariable-properties"></a>

`Value`  <a name="cfn-lightsail-container-environmentvariable-value"></a>
The environment variable value.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Variable`  <a name="cfn-lightsail-container-environmentvariable-variable"></a>
The environment variable key.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
