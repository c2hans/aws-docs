---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-agentalias.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::AgentAlias
<a name="aws-resource-bedrock-agentalias"></a>

Specifies an agent alias as a resource in a top-level template. Minimally, you must specify the following properties:
+ AgentAliasName – Specify a name for the alias.

For more information about creating aliases for an agent in Amazon Bedrock, see [Deploy an Amazon Bedrock agent](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-deploy.html).

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrock-agentalias-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-agentalias-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::AgentAlias",
  "Properties" : {
      "[AgentAliasName](#cfn-bedrock-agentalias-agentaliasname)" : {{String}},
      "[AgentId](#cfn-bedrock-agentalias-agentid)" : {{String}},
      "[Description](#cfn-bedrock-agentalias-description)" : {{String}},
      "[RoutingConfiguration](#cfn-bedrock-agentalias-routingconfiguration)" : {{[ AgentAliasRoutingConfigurationListItem, ... ]}},
      "[Tags](#cfn-bedrock-agentalias-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-bedrock-agentalias-syntax.yaml"></a>

```
Type: AWS::Bedrock::AgentAlias
Properties:
  [AgentAliasName](#cfn-bedrock-agentalias-agentaliasname): {{String}}
  [AgentId](#cfn-bedrock-agentalias-agentid): {{String}}
  [Description](#cfn-bedrock-agentalias-description): {{String}}
  [RoutingConfiguration](#cfn-bedrock-agentalias-routingconfiguration): {{
    - AgentAliasRoutingConfigurationListItem}}
  [Tags](#cfn-bedrock-agentalias-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-bedrock-agentalias-properties"></a>

`AgentAliasName`  <a name="cfn-bedrock-agentalias-agentaliasname"></a>
The name of the alias of the agent.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-zA-Z][_-]?){1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AgentId`  <a name="cfn-bedrock-agentalias-agentid"></a>
The unique identifier of the agent.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-zA-Z]{10}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-bedrock-agentalias-description"></a>
The description of the alias of the agent.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoutingConfiguration`  <a name="cfn-bedrock-agentalias-routingconfiguration"></a>
Contains details about the routing configuration of the alias.
*Required*: No
*Type*: Array of [AgentAliasRoutingConfigurationListItem](aws-properties-bedrock-agentalias-agentaliasroutingconfigurationlistitem.md)
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-bedrock-agentalias-tags"></a>
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
<a name="aws-resource-bedrock-agentalias-return-values"></a>

### Ref
<a name="aws-resource-bedrock-agentalias-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the agent ID and the agent alias ID, separated by a pipe (`|`).

For example, `{ "Ref": "myAgentAlias" }` could return the value `"AGENT12345|ALIAS12345"`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-bedrock-agentalias-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrock-agentalias-return-values-fn--getatt-fn--getatt"></a>

`AgentAliasArn`  <a name="AgentAliasArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the alias of the agent.

`AgentAliasHistoryEvents`  <a name="AgentAliasHistoryEvents-fn::getatt"></a>
Contains details about the history of the alias.

`AgentAliasId`  <a name="AgentAliasId-fn::getatt"></a>
The unique identifier of the alias of the agent.

`AgentAliasStatus`  <a name="AgentAliasStatus-fn::getatt"></a>
The status of the alias of the agent and whether it is ready for use. The following statuses are possible:
+ CREATING – The agent alias is being created.
+ PREPARED – The agent alias is finished being created or updated and is ready to be invoked.
+ FAILED – The agent alias API operation failed.
+ UPDATING – The agent alias is being updated.
+ DELETING – The agent alias is being deleted.
+ DISSOCIATED - The agent alias has no version associated with it.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time at which the alias of the agent was created.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The time at which the alias was last updated.

## Examples
<a name="aws-resource-bedrock-agentalias--examples"></a>

### Create an alias for an agent
<a name="aws-resource-bedrock-agentalias--examples--Create_an_alias_for_an_agent"></a>

The following example creates an alias that points to version 1 of an agent.

#### YAML
<a name="aws-resource-bedrock-agentalias--examples--Create_an_alias_for_an_agent--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: "CFN stack for creating an AgentAlias"
Resources:
  ExampleAgentAliasResource:
    Type: AWS::Bedrock::AgentAlias
    Properties:
      AgentId: "1234567890"
      AgentAliasName: "TestAlias"
      Description: "Alias for testing"
      RoutingConfiguration:
        - AgentVersion: "1"
```

#### JSON
<a name="aws-resource-bedrock-agentalias--examples--Create_an_alias_for_an_agent--json"></a>

```
{
   "AWSTemplateFormatVersion": "2010-09-09",
   "Description": "CFN stack for creating an AgentAlias",
   "Resources": {
      "ExampleAgentAliasResource": {
         "Type": "AWS::Bedrock::AgentAlias",
         "Properties": {
            "AgentId": "1234567890",
            "AgentAliasName": "TestAlias",
            "Description": "Alias for testing",
            "RoutingConfiguration": {
               "AgentVersion": "1"
            }
         }
      }
   }
}
```
