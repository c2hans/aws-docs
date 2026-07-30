---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-userpreferenceoverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory UserPreferenceOverride
<a name="aws-properties-bedrockagentcore-memory-userpreferenceoverride"></a>

The memory user preference override.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-userpreferenceoverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-userpreferenceoverride-syntax.json"></a>

```
{
  "[Consolidation](#cfn-bedrockagentcore-memory-userpreferenceoverride-consolidation)" : {{UserPreferenceOverrideConsolidationConfigurationInput}},
  "[Extraction](#cfn-bedrockagentcore-memory-userpreferenceoverride-extraction)" : {{UserPreferenceOverrideExtractionConfigurationInput}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-userpreferenceoverride-syntax.yaml"></a>

```
  [Consolidation](#cfn-bedrockagentcore-memory-userpreferenceoverride-consolidation): {{
    UserPreferenceOverrideConsolidationConfigurationInput}}
  [Extraction](#cfn-bedrockagentcore-memory-userpreferenceoverride-extraction): {{
    UserPreferenceOverrideExtractionConfigurationInput}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-userpreferenceoverride-properties"></a>

`Consolidation`  <a name="cfn-bedrockagentcore-memory-userpreferenceoverride-consolidation"></a>
The memory override consolidation information.
*Required*: No
*Type*: [UserPreferenceOverrideConsolidationConfigurationInput](aws-properties-bedrockagentcore-memory-userpreferenceoverrideconsolidationconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Extraction`  <a name="cfn-bedrockagentcore-memory-userpreferenceoverride-extraction"></a>
The memory user preferences for extraction.
*Required*: No
*Type*: [UserPreferenceOverrideExtractionConfigurationInput](aws-properties-bedrockagentcore-memory-userpreferenceoverrideextractionconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
