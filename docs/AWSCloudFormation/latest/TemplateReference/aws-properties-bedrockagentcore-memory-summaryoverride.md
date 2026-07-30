---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-summaryoverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory SummaryOverride
<a name="aws-properties-bedrockagentcore-memory-summaryoverride"></a>

The memory summary override.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-summaryoverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-summaryoverride-syntax.json"></a>

```
{
  "[Consolidation](#cfn-bedrockagentcore-memory-summaryoverride-consolidation)" : {{SummaryOverrideConsolidationConfigurationInput}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-summaryoverride-syntax.yaml"></a>

```
  [Consolidation](#cfn-bedrockagentcore-memory-summaryoverride-consolidation): {{
    SummaryOverrideConsolidationConfigurationInput}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-summaryoverride-properties"></a>

`Consolidation`  <a name="cfn-bedrockagentcore-memory-summaryoverride-consolidation"></a>
The memory override consolidation.
*Required*: No
*Type*: [SummaryOverrideConsolidationConfigurationInput](aws-properties-bedrockagentcore-memory-summaryoverrideconsolidationconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
