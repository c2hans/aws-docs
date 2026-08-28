---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-customconfigurationinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory CustomConfigurationInput
<a name="aws-properties-bedrockagentcore-memory-customconfigurationinput"></a>

The memory configuration input.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-customconfigurationinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-customconfigurationinput-syntax.json"></a>

```
{
  "[EpisodicOverride](#cfn-bedrockagentcore-memory-customconfigurationinput-episodicoverride)" : {{EpisodicOverride}},
  "[SelfManagedConfiguration](#cfn-bedrockagentcore-memory-customconfigurationinput-selfmanagedconfiguration)" : {{SelfManagedConfiguration}},
  "[SemanticOverride](#cfn-bedrockagentcore-memory-customconfigurationinput-semanticoverride)" : {{SemanticOverride}},
  "[SummaryOverride](#cfn-bedrockagentcore-memory-customconfigurationinput-summaryoverride)" : {{SummaryOverride}},
  "[UserPreferenceOverride](#cfn-bedrockagentcore-memory-customconfigurationinput-userpreferenceoverride)" : {{UserPreferenceOverride}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-customconfigurationinput-syntax.yaml"></a>

```
  [EpisodicOverride](#cfn-bedrockagentcore-memory-customconfigurationinput-episodicoverride): {{
    EpisodicOverride}}
  [SelfManagedConfiguration](#cfn-bedrockagentcore-memory-customconfigurationinput-selfmanagedconfiguration): {{
    SelfManagedConfiguration}}
  [SemanticOverride](#cfn-bedrockagentcore-memory-customconfigurationinput-semanticoverride): {{
    SemanticOverride}}
  [SummaryOverride](#cfn-bedrockagentcore-memory-customconfigurationinput-summaryoverride): {{
    SummaryOverride}}
  [UserPreferenceOverride](#cfn-bedrockagentcore-memory-customconfigurationinput-userpreferenceoverride): {{
    UserPreferenceOverride}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-customconfigurationinput-properties"></a>

`EpisodicOverride`  <a name="cfn-bedrockagentcore-memory-customconfigurationinput-episodicoverride"></a>
The episodic memory strategy override configuration for a custom memory strategy.
*Required*: No
*Type*: [EpisodicOverride](aws-properties-bedrockagentcore-memory-episodicoverride.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelfManagedConfiguration`  <a name="cfn-bedrockagentcore-memory-customconfigurationinput-selfmanagedconfiguration"></a>
The custom configuration input.
*Required*: No
*Type*: [SelfManagedConfiguration](aws-properties-bedrockagentcore-memory-selfmanagedconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SemanticOverride`  <a name="cfn-bedrockagentcore-memory-customconfigurationinput-semanticoverride"></a>
The memory override configuration.
*Required*: No
*Type*: [SemanticOverride](aws-properties-bedrockagentcore-memory-semanticoverride.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SummaryOverride`  <a name="cfn-bedrockagentcore-memory-customconfigurationinput-summaryoverride"></a>
The memory configuration override.
*Required*: No
*Type*: [SummaryOverride](aws-properties-bedrockagentcore-memory-summaryoverride.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserPreferenceOverride`  <a name="cfn-bedrockagentcore-memory-customconfigurationinput-userpreferenceoverride"></a>
The memory user preference override.
*Required*: No
*Type*: [UserPreferenceOverride](aws-properties-bedrockagentcore-memory-userpreferenceoverride.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
