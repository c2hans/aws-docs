---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-daemontaskdefinition-keyvaluepair.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::DaemonTaskDefinition KeyValuePair
<a name="aws-properties-ecs-daemontaskdefinition-keyvaluepair"></a>

A key-value pair object.

## Syntax
<a name="aws-properties-ecs-daemontaskdefinition-keyvaluepair-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-daemontaskdefinition-keyvaluepair-syntax.json"></a>

```
{
  "[Name](#cfn-ecs-daemontaskdefinition-keyvaluepair-name)" : {{String}},
  "[Value](#cfn-ecs-daemontaskdefinition-keyvaluepair-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-daemontaskdefinition-keyvaluepair-syntax.yaml"></a>

```
  [Name](#cfn-ecs-daemontaskdefinition-keyvaluepair-name): {{String}}
  [Value](#cfn-ecs-daemontaskdefinition-keyvaluepair-value): {{String}}
```

## Properties
<a name="aws-properties-ecs-daemontaskdefinition-keyvaluepair-properties"></a>

`Name`  <a name="cfn-ecs-daemontaskdefinition-keyvaluepair-name"></a>
The name of the key-value pair. For environment variables, this is the name of the environment variable.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-ecs-daemontaskdefinition-keyvaluepair-value"></a>
The value of the key-value pair. For environment variables, this is the value of the environment variable.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
