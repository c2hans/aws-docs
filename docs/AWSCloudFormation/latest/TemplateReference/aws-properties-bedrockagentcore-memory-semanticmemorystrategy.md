---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-semanticmemorystrategy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory SemanticMemoryStrategy
<a name="aws-properties-bedrockagentcore-memory-semanticmemorystrategy"></a>

The memory strategy.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-semanticmemorystrategy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-semanticmemorystrategy-syntax.json"></a>

```
{
  "[CreatedAt](#cfn-bedrockagentcore-memory-semanticmemorystrategy-createdat)" : {{String}},
  "[Description](#cfn-bedrockagentcore-memory-semanticmemorystrategy-description)" : {{String}},
  "[MemoryRecordSchema](#cfn-bedrockagentcore-memory-semanticmemorystrategy-memoryrecordschema)" : {{MemoryRecordSchema}},
  "[Name](#cfn-bedrockagentcore-memory-semanticmemorystrategy-name)" : {{String}},
  "[Namespaces](#cfn-bedrockagentcore-memory-semanticmemorystrategy-namespaces)" : {{[ String, ... ]}},
  "[NamespaceTemplates](#cfn-bedrockagentcore-memory-semanticmemorystrategy-namespacetemplates)" : {{[ String, ... ]}},
  "[Status](#cfn-bedrockagentcore-memory-semanticmemorystrategy-status)" : {{String}},
  "[StrategyId](#cfn-bedrockagentcore-memory-semanticmemorystrategy-strategyid)" : {{String}},
  "[Type](#cfn-bedrockagentcore-memory-semanticmemorystrategy-type)" : {{String}},
  "[UpdatedAt](#cfn-bedrockagentcore-memory-semanticmemorystrategy-updatedat)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-semanticmemorystrategy-syntax.yaml"></a>

```
  [CreatedAt](#cfn-bedrockagentcore-memory-semanticmemorystrategy-createdat): {{String}}
  [Description](#cfn-bedrockagentcore-memory-semanticmemorystrategy-description): {{String}}
  [MemoryRecordSchema](#cfn-bedrockagentcore-memory-semanticmemorystrategy-memoryrecordschema): {{
    MemoryRecordSchema}}
  [Name](#cfn-bedrockagentcore-memory-semanticmemorystrategy-name): {{String}}
  [Namespaces](#cfn-bedrockagentcore-memory-semanticmemorystrategy-namespaces): {{
    - String}}
  [NamespaceTemplates](#cfn-bedrockagentcore-memory-semanticmemorystrategy-namespacetemplates): {{
    - String}}
  [Status](#cfn-bedrockagentcore-memory-semanticmemorystrategy-status): {{String}}
  [StrategyId](#cfn-bedrockagentcore-memory-semanticmemorystrategy-strategyid): {{String}}
  [Type](#cfn-bedrockagentcore-memory-semanticmemorystrategy-type): {{String}}
  [UpdatedAt](#cfn-bedrockagentcore-memory-semanticmemorystrategy-updatedat): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-semanticmemorystrategy-properties"></a>

`CreatedAt`  <a name="cfn-bedrockagentcore-memory-semanticmemorystrategy-createdat"></a>
The memory strategy creation date and time.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-bedrockagentcore-memory-semanticmemorystrategy-description"></a>
The memory strategy description.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MemoryRecordSchema`  <a name="cfn-bedrockagentcore-memory-semanticmemorystrategy-memoryrecordschema"></a>
Property description not available.
*Required*: No
*Type*: [MemoryRecordSchema](aws-properties-bedrockagentcore-memory-memoryrecordschema.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrockagentcore-memory-semanticmemorystrategy-name"></a>
The memory strategy name.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_]{0,47}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Namespaces`  <a name="cfn-bedrockagentcore-memory-semanticmemorystrategy-namespaces"></a>
The memory strategy namespaces.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NamespaceTemplates`  <a name="cfn-bedrockagentcore-memory-semanticmemorystrategy-namespacetemplates"></a>
The namespaceTemplates associated with the semantic memory strategy.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-bedrockagentcore-memory-semanticmemorystrategy-status"></a>
The memory strategy status.
*Required*: No
*Type*: String
*Allowed values*: `CREATING | ACTIVE | DELETING | FAILED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StrategyId`  <a name="cfn-bedrockagentcore-memory-semanticmemorystrategy-strategyid"></a>
The memory strategy ID.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}$`
*Minimum*: `12`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrockagentcore-memory-semanticmemorystrategy-type"></a>
The memory strategy type.
*Required*: No
*Type*: String
*Allowed values*: `SEMANTIC | SUMMARIZATION | USER_PREFERENCE | CUSTOM | EPISODIC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdatedAt`  <a name="cfn-bedrockagentcore-memory-semanticmemorystrategy-updatedat"></a>
The timestamp when the semantic memory strategy was last updated.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
