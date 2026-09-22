---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-memory.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory
<a name="aws-resource-bedrockagentcore-memory"></a>

Memory allows AI agents to maintain both immediate and long-term knowledge, enabling context-aware and personalized interactions.

For more information about using Memory in Amazon Bedrock AgentCore, see [Host agent or tools with Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-getting-started.html).

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrockagentcore-memory-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-memory-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::Memory",
  "Properties" : {
      "[Description](#cfn-bedrockagentcore-memory-description)" : {{String}},
      "[EncryptionKeyArn](#cfn-bedrockagentcore-memory-encryptionkeyarn)" : {{String}},
      "[EventExpiryDuration](#cfn-bedrockagentcore-memory-eventexpiryduration)" : {{Integer}},
      "[IndexedKeys](#cfn-bedrockagentcore-memory-indexedkeys)" : {{[ IndexedKey, ... ]}},
      "[MemoryExecutionRoleArn](#cfn-bedrockagentcore-memory-memoryexecutionrolearn)" : {{String}},
      "[MemoryStrategies](#cfn-bedrockagentcore-memory-memorystrategies)" : {{[ MemoryStrategy, ... ]}},
      "[Name](#cfn-bedrockagentcore-memory-name)" : {{String}},
      "[NamespaceKeys](#cfn-bedrockagentcore-memory-namespacekeys)" : {{[ NamespaceKeyEntry, ... ]}},
      "[StreamDeliveryResources](#cfn-bedrockagentcore-memory-streamdeliveryresources)" : {{StreamDeliveryResources}},
      "[Tags](#cfn-bedrockagentcore-memory-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-memory-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::Memory
Properties:
  [Description](#cfn-bedrockagentcore-memory-description): {{String}}
  [EncryptionKeyArn](#cfn-bedrockagentcore-memory-encryptionkeyarn): {{String}}
  [EventExpiryDuration](#cfn-bedrockagentcore-memory-eventexpiryduration): {{Integer}}
  [IndexedKeys](#cfn-bedrockagentcore-memory-indexedkeys): {{
    - IndexedKey}}
  [MemoryExecutionRoleArn](#cfn-bedrockagentcore-memory-memoryexecutionrolearn): {{String}}
  [MemoryStrategies](#cfn-bedrockagentcore-memory-memorystrategies): {{
    - MemoryStrategy}}
  [Name](#cfn-bedrockagentcore-memory-name): {{String}}
  [NamespaceKeys](#cfn-bedrockagentcore-memory-namespacekeys): {{
    - NamespaceKeyEntry}}
  [StreamDeliveryResources](#cfn-bedrockagentcore-memory-streamdeliveryresources): {{
    StreamDeliveryResources}}
  [Tags](#cfn-bedrockagentcore-memory-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-bedrockagentcore-memory-properties"></a>

`Description`  <a name="cfn-bedrockagentcore-memory-description"></a>
The description of the memory.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionKeyArn`  <a name="cfn-bedrockagentcore-memory-encryptionkeyarn"></a>
The ARN of the KMS key used to encrypt the memory.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws(?:-cn|-us-gov|-iso(?:-[bef])?)?):[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EventExpiryDuration`  <a name="cfn-bedrockagentcore-memory-eventexpiryduration"></a>
The number of days after which memory events will expire.
*Required*: Yes
*Type*: Integer
*Minimum*: `3`
*Maximum*: `365`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IndexedKeys`  <a name="cfn-bedrockagentcore-memory-indexedkeys"></a>
The indexed metadata keys for this memory. Only indexed keys can be used in metadata filters.
*Required*: No
*Type*: Array of [IndexedKey](aws-properties-bedrockagentcore-memory-indexedkey.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MemoryExecutionRoleArn`  <a name="cfn-bedrockagentcore-memory-memoryexecutionrolearn"></a>
The ARN of the IAM role that provides permissions for the memory.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws(?:-cn|-us-gov|-iso(?:-[bef])?)?):[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MemoryStrategies`  <a name="cfn-bedrockagentcore-memory-memorystrategies"></a>
The list of memory strategies associated with this memory.
*Required*: No
*Type*: Array of [MemoryStrategy](aws-properties-bedrockagentcore-memory-memorystrategy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrockagentcore-memory-name"></a>
The name of the memory.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_]{0,47}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NamespaceKeys`  <a name="cfn-bedrockagentcore-memory-namespacekeys"></a>
The namespace variable key definitions for this memory. Namespace keys define custom variables used in `namespaceTemplates` with optional validation rules.
*Required*: No
*Type*: Array of [NamespaceKeyEntry](aws-properties-bedrockagentcore-memory-namespacekeyentry.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamDeliveryResources`  <a name="cfn-bedrockagentcore-memory-streamdeliveryresources"></a>
Configuration for streaming memory record data to external resources.
*Required*: No
*Type*: [StreamDeliveryResources](aws-properties-bedrockagentcore-memory-streamdeliveryresources.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-bedrockagentcore-memory-tags"></a>
A map of tag keys and values to assign to an AgentCore Memory. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]{1,128}$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrockagentcore-memory-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-memory-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the memory. For example:

 `arn:aws:bedrock-agentcore:us-east-1:123456789012:memory/MyMemory-a1b2c3d4e5`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-memory-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrockagentcore-memory-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the memory was created.

`FailureReason`  <a name="FailureReason-fn::getatt"></a>
The reason for failure if the memory is in a failed state.

`MemoryArn`  <a name="MemoryArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the memory.

`MemoryId`  <a name="MemoryId-fn::getatt"></a>
The unique identifier of the memory.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the memory.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the memory was last updated.
