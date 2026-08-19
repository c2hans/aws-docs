---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-metadataschemaentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory MetadataSchemaEntry
<a name="aws-properties-bedrockagentcore-memory-metadataschemaentry"></a>

A metadata field definition within a strategy's schema.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-metadataschemaentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-metadataschemaentry-syntax.json"></a>

```
{
  "[ExtractionConfig](#cfn-bedrockagentcore-memory-metadataschemaentry-extractionconfig)" : {{ExtractionConfig}},
  "[ExtractionType](#cfn-bedrockagentcore-memory-metadataschemaentry-extractiontype)" : {{String}},
  "[Key](#cfn-bedrockagentcore-memory-metadataschemaentry-key)" : {{String}},
  "[Type](#cfn-bedrockagentcore-memory-metadataschemaentry-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-metadataschemaentry-syntax.yaml"></a>

```
  [ExtractionConfig](#cfn-bedrockagentcore-memory-metadataschemaentry-extractionconfig): {{
    ExtractionConfig}}
  [ExtractionType](#cfn-bedrockagentcore-memory-metadataschemaentry-extractiontype): {{String}}
  [Key](#cfn-bedrockagentcore-memory-metadataschemaentry-key): {{String}}
  [Type](#cfn-bedrockagentcore-memory-metadataschemaentry-type): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-metadataschemaentry-properties"></a>

`ExtractionConfig`  <a name="cfn-bedrockagentcore-memory-metadataschemaentry-extractionconfig"></a>
Configuration for extracting this metadata value from conversational content. Applicable only if extractionType is LLM inferred.
*Required*: No
*Type*: [ExtractionConfig](aws-properties-bedrockagentcore-memory-extractionconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExtractionType`  <a name="cfn-bedrockagentcore-memory-metadataschemaentry-extractiontype"></a>
Specifies whether the metadata value is extracted by the LLM or passed through deterministically from the event.
*Required*: No
*Type*: String
*Allowed values*: `LLM_INFERRED | STRICTLY_CONSISTENT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-bedrockagentcore-memory-metadataschemaentry-key"></a>
The metadata field name. Must match an indexed key to be queryable via metadata filters.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrockagentcore-memory-metadataschemaentry-type"></a>
The MetadataValueType.
*Required*: No
*Type*: String
*Allowed values*: `STRING | STRINGLIST | NUMBER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
