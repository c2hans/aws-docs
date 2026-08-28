---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-intelligentpromptrouter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::IntelligentPromptRouter
<a name="aws-resource-bedrock-intelligentpromptrouter"></a>

Specifies an intelligent prompt router resource for Amazon Bedrock.

## Syntax
<a name="aws-resource-bedrock-intelligentpromptrouter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-intelligentpromptrouter-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::IntelligentPromptRouter",
  "Properties" : {
      "[Description](#cfn-bedrock-intelligentpromptrouter-description)" : {{String}},
      "[FallbackModel](#cfn-bedrock-intelligentpromptrouter-fallbackmodel)" : {{PromptRouterTargetModel}},
      "[Models](#cfn-bedrock-intelligentpromptrouter-models)" : {{[ PromptRouterTargetModel, ... ]}},
      "[PromptRouterName](#cfn-bedrock-intelligentpromptrouter-promptroutername)" : {{String}},
      "[RoutingCriteria](#cfn-bedrock-intelligentpromptrouter-routingcriteria)" : {{RoutingCriteria}},
      "[Tags](#cfn-bedrock-intelligentpromptrouter-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-bedrock-intelligentpromptrouter-syntax.yaml"></a>

```
Type: AWS::Bedrock::IntelligentPromptRouter
Properties:
  [Description](#cfn-bedrock-intelligentpromptrouter-description): {{String}}
  [FallbackModel](#cfn-bedrock-intelligentpromptrouter-fallbackmodel): {{
    PromptRouterTargetModel}}
  [Models](#cfn-bedrock-intelligentpromptrouter-models): {{
    - PromptRouterTargetModel}}
  [PromptRouterName](#cfn-bedrock-intelligentpromptrouter-promptroutername): {{String}}
  [RoutingCriteria](#cfn-bedrock-intelligentpromptrouter-routingcriteria): {{
    RoutingCriteria}}
  [Tags](#cfn-bedrock-intelligentpromptrouter-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-bedrock-intelligentpromptrouter-properties"></a>

`Description`  <a name="cfn-bedrock-intelligentpromptrouter-description"></a>
An optional description of the prompt router to help identify its purpose.
*Required*: No
*Type*: String
*Pattern*: `^([0-9a-zA-Z:.][ _-]?)+$`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FallbackModel`  <a name="cfn-bedrock-intelligentpromptrouter-fallbackmodel"></a>
The default model to use when the routing criteria is not met.
*Required*: Yes
*Type*: [PromptRouterTargetModel](aws-properties-bedrock-intelligentpromptrouter-promptroutertargetmodel.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Models`  <a name="cfn-bedrock-intelligentpromptrouter-models"></a>
A list of foundation models that the prompt router can route requests to. At least one model must be specified.
*Required*: Yes
*Type*: Array of [PromptRouterTargetModel](aws-properties-bedrock-intelligentpromptrouter-promptroutertargetmodel.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PromptRouterName`  <a name="cfn-bedrock-intelligentpromptrouter-promptroutername"></a>
The name of the prompt router. The name must be unique within your AWS account in the current region.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-zA-Z][ _-]?)+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoutingCriteria`  <a name="cfn-bedrock-intelligentpromptrouter-routingcriteria"></a>
Routing criteria for a prompt router.
*Required*: Yes
*Type*: [RoutingCriteria](aws-properties-bedrock-intelligentpromptrouter-routingcriteria.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-bedrock-intelligentpromptrouter-tags"></a>
An array of key-value pairs to apply to this resource as tags. You can use tags to categorize and manage your AWS resources.
*Required*: No
*Type*: Array of [Tag](aws-properties-bedrock-intelligentpromptrouter-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrock-intelligentpromptrouter-return-values"></a>

### Ref
<a name="aws-resource-bedrock-intelligentpromptrouter-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the intelligent prompt router information.

### Fn::GetAtt
<a name="aws-resource-bedrock-intelligentpromptrouter-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrock-intelligentpromptrouter-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Indicates the time that the prompt router was created.

`PromptRouterArn`  <a name="PromptRouterArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the prompt router.

`Status`  <a name="Status-fn::getatt"></a>
The router's status.

`Type`  <a name="Type-fn::getatt"></a>
The router's type.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
When the router was updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
