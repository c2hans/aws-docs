---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-expressgatewayservice-keyvaluepair.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::ExpressGatewayService KeyValuePair
<a name="aws-properties-ecs-expressgatewayservice-keyvaluepair"></a>

A key-value pair object.

## Syntax
<a name="aws-properties-ecs-expressgatewayservice-keyvaluepair-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-expressgatewayservice-keyvaluepair-syntax.json"></a>

```
{
  "[Name](#cfn-ecs-expressgatewayservice-keyvaluepair-name)" : {{String}},
  "[Value](#cfn-ecs-expressgatewayservice-keyvaluepair-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-expressgatewayservice-keyvaluepair-syntax.yaml"></a>

```
  [Name](#cfn-ecs-expressgatewayservice-keyvaluepair-name): {{String}}
  [Value](#cfn-ecs-expressgatewayservice-keyvaluepair-value): {{String}}
```

## Properties
<a name="aws-properties-ecs-expressgatewayservice-keyvaluepair-properties"></a>

`Name`  <a name="cfn-ecs-expressgatewayservice-keyvaluepair-name"></a>
The name of the key-value pair. For environment variables, this is the name of the environment variable.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ecs-expressgatewayservice-keyvaluepair-value"></a>
The value of the key-value pair. For environment variables, this is the value of the environment variable.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
