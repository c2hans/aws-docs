---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-flowalias.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowAlias
<a name="aws-resource-bedrock-flowalias"></a>

Creates an alias of a flow for deployment. For more information, see [Deploy a flow in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-deploy.html) in the Amazon Bedrock User Guide.

## Syntax
<a name="aws-resource-bedrock-flowalias-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-flowalias-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::FlowAlias",
  "Properties" : {
      "[ConcurrencyConfiguration](#cfn-bedrock-flowalias-concurrencyconfiguration)" : {{FlowAliasConcurrencyConfiguration}},
      "[Description](#cfn-bedrock-flowalias-description)" : {{String}},
      "[FlowArn](#cfn-bedrock-flowalias-flowarn)" : {{String}},
      "[Name](#cfn-bedrock-flowalias-name)" : {{String}},
      "[RoutingConfiguration](#cfn-bedrock-flowalias-routingconfiguration)" : {{[ FlowAliasRoutingConfigurationListItem, ... ]}},
      "[Tags](#cfn-bedrock-flowalias-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-bedrock-flowalias-syntax.yaml"></a>

```
Type: AWS::Bedrock::FlowAlias
Properties:
  [ConcurrencyConfiguration](#cfn-bedrock-flowalias-concurrencyconfiguration): {{
    FlowAliasConcurrencyConfiguration}}
  [Description](#cfn-bedrock-flowalias-description): {{String}}
  [FlowArn](#cfn-bedrock-flowalias-flowarn): {{String}}
  [Name](#cfn-bedrock-flowalias-name): {{String}}
  [RoutingConfiguration](#cfn-bedrock-flowalias-routingconfiguration): {{
    - FlowAliasRoutingConfigurationListItem}}
  [Tags](#cfn-bedrock-flowalias-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-bedrock-flowalias-properties"></a>

`ConcurrencyConfiguration`  <a name="cfn-bedrock-flowalias-concurrencyconfiguration"></a>
The configuration that specifies how nodes in the flow are executed concurrently.
*Required*: No
*Type*: [FlowAliasConcurrencyConfiguration](aws-properties-bedrock-flowalias-flowaliasconcurrencyconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-bedrock-flowalias-description"></a>
A description of the alias.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FlowArn`  <a name="cfn-bedrock-flowalias-flowarn"></a>
The Amazon Resource Name (ARN) of the alias.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-bedrock-flowalias-name"></a>
The name of the alias.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-zA-Z][_-]?){1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoutingConfiguration`  <a name="cfn-bedrock-flowalias-routingconfiguration"></a>
A list of configurations about the versions that the alias maps to. Currently, you can only specify one.
*Required*: Yes
*Type*: Array of [FlowAliasRoutingConfigurationListItem](aws-properties-bedrock-flowalias-flowaliasroutingconfigurationlistitem.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-bedrock-flowalias-tags"></a>
Metadata that you can assign to a resource as key-value pairs. For more information, see the following resources:
+  [Tag naming limits and requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions)
+  [Tagging best practices](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices)
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrock-flowalias-return-values"></a>

### Ref
<a name="aws-resource-bedrock-flowalias-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Number (ARN) of the flow and the Amazon Resource Name (ARN) of its alias, separated by a pipe (`|`).

For example, `{ "Ref": "myFlowAlias" }` could return the value `"arn:aws:bedrock:us-east-1:123456789012:flow/FLOW12345|arn:aws:bedrock:us-east-1:123456789012:flow/FLOW12345/alias/ALIAS12345"`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-bedrock-flowalias-return-values-fn--getatt"></a>

####
<a name="aws-resource-bedrock-flowalias-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the alias.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time at which the alias was created.

`FlowId`  <a name="FlowId-fn::getatt"></a>
The unique identifier of the flow.

`Id`  <a name="Id-fn::getatt"></a>
The unique identifier of the alias of the flow.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The time at which the alias was last updated.
