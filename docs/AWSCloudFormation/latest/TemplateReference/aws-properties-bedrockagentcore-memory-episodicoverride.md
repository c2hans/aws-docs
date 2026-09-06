---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-episodicoverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory EpisodicOverride
<a name="aws-properties-bedrockagentcore-memory-episodicoverride"></a>

The configuration to override the episodic memory strategy.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-episodicoverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-episodicoverride-syntax.json"></a>

```
{
  "[Consolidation](#cfn-bedrockagentcore-memory-episodicoverride-consolidation)" : {{EpisodicOverrideConsolidationConfigurationInput}},
  "[Extraction](#cfn-bedrockagentcore-memory-episodicoverride-extraction)" : {{EpisodicOverrideExtractionConfigurationInput}},
  "[Reflection](#cfn-bedrockagentcore-memory-episodicoverride-reflection)" : {{EpisodicOverrideReflectionConfigurationInput}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-episodicoverride-syntax.yaml"></a>

```
  [Consolidation](#cfn-bedrockagentcore-memory-episodicoverride-consolidation): {{
    EpisodicOverrideConsolidationConfigurationInput}}
  [Extraction](#cfn-bedrockagentcore-memory-episodicoverride-extraction): {{
    EpisodicOverrideExtractionConfigurationInput}}
  [Reflection](#cfn-bedrockagentcore-memory-episodicoverride-reflection): {{
    EpisodicOverrideReflectionConfigurationInput}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-episodicoverride-properties"></a>

`Consolidation`  <a name="cfn-bedrockagentcore-memory-episodicoverride-consolidation"></a>
Contains configurations for overriding the consolidation step of the episodic memory strategy.
*Required*: No
*Type*: [EpisodicOverrideConsolidationConfigurationInput](aws-properties-bedrockagentcore-memory-episodicoverrideconsolidationconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Extraction`  <a name="cfn-bedrockagentcore-memory-episodicoverride-extraction"></a>
Contains configurations for overriding the extraction step of the episodic memory strategy.
*Required*: No
*Type*: [EpisodicOverrideExtractionConfigurationInput](aws-properties-bedrockagentcore-memory-episodicoverrideextractionconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Reflection`  <a name="cfn-bedrockagentcore-memory-episodicoverride-reflection"></a>
Contains configurations for overriding the reflection step of the episodic memory strategy.
*Required*: No
*Type*: [EpisodicOverrideReflectionConfigurationInput](aws-properties-bedrockagentcore-memory-episodicoverridereflectionconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
