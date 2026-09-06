---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-semanticoverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory SemanticOverride
<a name="aws-properties-bedrockagentcore-memory-semanticoverride"></a>

The memory override.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-semanticoverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-semanticoverride-syntax.json"></a>

```
{
  "[Consolidation](#cfn-bedrockagentcore-memory-semanticoverride-consolidation)" : {{SemanticOverrideConsolidationConfigurationInput}},
  "[Extraction](#cfn-bedrockagentcore-memory-semanticoverride-extraction)" : {{SemanticOverrideExtractionConfigurationInput}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-semanticoverride-syntax.yaml"></a>

```
  [Consolidation](#cfn-bedrockagentcore-memory-semanticoverride-consolidation): {{
    SemanticOverrideConsolidationConfigurationInput}}
  [Extraction](#cfn-bedrockagentcore-memory-semanticoverride-extraction): {{
    SemanticOverrideExtractionConfigurationInput}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-semanticoverride-properties"></a>

`Consolidation`  <a name="cfn-bedrockagentcore-memory-semanticoverride-consolidation"></a>
The memory override consolidation.
*Required*: No
*Type*: [SemanticOverrideConsolidationConfigurationInput](aws-properties-bedrockagentcore-memory-semanticoverrideconsolidationconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Extraction`  <a name="cfn-bedrockagentcore-memory-semanticoverride-extraction"></a>
The memory override extraction.
*Required*: No
*Type*: [SemanticOverrideExtractionConfigurationInput](aws-properties-bedrockagentcore-memory-semanticoverrideextractionconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
