---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-userpreferenceoverrideconsolidationconfigurationinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory UserPreferenceOverrideConsolidationConfigurationInput
<a name="aws-properties-bedrockagentcore-memory-userpreferenceoverrideconsolidationconfigurationinput"></a>

The configuration input.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-userpreferenceoverrideconsolidationconfigurationinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-userpreferenceoverrideconsolidationconfigurationinput-syntax.json"></a>

```
{
  "[AppendToPrompt](#cfn-bedrockagentcore-memory-userpreferenceoverrideconsolidationconfigurationinput-appendtoprompt)" : {{String}},
  "[ModelId](#cfn-bedrockagentcore-memory-userpreferenceoverrideconsolidationconfigurationinput-modelid)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-userpreferenceoverrideconsolidationconfigurationinput-syntax.yaml"></a>

```
  [AppendToPrompt](#cfn-bedrockagentcore-memory-userpreferenceoverrideconsolidationconfigurationinput-appendtoprompt): {{String}}
  [ModelId](#cfn-bedrockagentcore-memory-userpreferenceoverrideconsolidationconfigurationinput-modelid): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-userpreferenceoverrideconsolidationconfigurationinput-properties"></a>

`AppendToPrompt`  <a name="cfn-bedrockagentcore-memory-userpreferenceoverrideconsolidationconfigurationinput-appendtoprompt"></a>
The memory configuration.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `30000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelId`  <a name="cfn-bedrockagentcore-memory-userpreferenceoverrideconsolidationconfigurationinput-modelid"></a>
The memory override configuration model ID.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
