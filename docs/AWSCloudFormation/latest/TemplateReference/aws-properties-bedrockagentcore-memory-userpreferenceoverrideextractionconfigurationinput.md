---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-userpreferenceoverrideextractionconfigurationinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory UserPreferenceOverrideExtractionConfigurationInput
<a name="aws-properties-bedrockagentcore-memory-userpreferenceoverrideextractionconfigurationinput"></a>

The memory override configuration.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-userpreferenceoverrideextractionconfigurationinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-userpreferenceoverrideextractionconfigurationinput-syntax.json"></a>

```
{
  "[AppendToPrompt](#cfn-bedrockagentcore-memory-userpreferenceoverrideextractionconfigurationinput-appendtoprompt)" : {{String}},
  "[ModelId](#cfn-bedrockagentcore-memory-userpreferenceoverrideextractionconfigurationinput-modelid)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-userpreferenceoverrideextractionconfigurationinput-syntax.yaml"></a>

```
  [AppendToPrompt](#cfn-bedrockagentcore-memory-userpreferenceoverrideextractionconfigurationinput-appendtoprompt): {{String}}
  [ModelId](#cfn-bedrockagentcore-memory-userpreferenceoverrideextractionconfigurationinput-modelid): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-userpreferenceoverrideextractionconfigurationinput-properties"></a>

`AppendToPrompt`  <a name="cfn-bedrockagentcore-memory-userpreferenceoverrideextractionconfigurationinput-appendtoprompt"></a>
The extraction configuration.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `30000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelId`  <a name="cfn-bedrockagentcore-memory-userpreferenceoverrideextractionconfigurationinput-modelid"></a>
The memory override for the model ID.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
