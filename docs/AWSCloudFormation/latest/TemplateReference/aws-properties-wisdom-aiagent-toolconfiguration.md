---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiagent-toolconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgent ToolConfiguration
<a name="aws-properties-wisdom-aiagent-toolconfiguration"></a>

Configuration settings for a tool used by AI Agents.

## Syntax
<a name="aws-properties-wisdom-aiagent-toolconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiagent-toolconfiguration-syntax.json"></a>

```
{
  "[Annotations](#cfn-wisdom-aiagent-toolconfiguration-annotations)" : {{Json}},
  "[Description](#cfn-wisdom-aiagent-toolconfiguration-description)" : {{String}},
  "[InputSchema](#cfn-wisdom-aiagent-toolconfiguration-inputschema)" : {{Json}},
  "[Instruction](#cfn-wisdom-aiagent-toolconfiguration-instruction)" : {{ToolInstruction}},
  "[OutputFilters](#cfn-wisdom-aiagent-toolconfiguration-outputfilters)" : {{[ ToolOutputFilter, ... ]}},
  "[OutputSchema](#cfn-wisdom-aiagent-toolconfiguration-outputschema)" : {{Json}},
  "[OverrideInputValues](#cfn-wisdom-aiagent-toolconfiguration-overrideinputvalues)" : {{[ ToolOverrideInputValue, ... ]}},
  "[Title](#cfn-wisdom-aiagent-toolconfiguration-title)" : {{String}},
  "[ToolId](#cfn-wisdom-aiagent-toolconfiguration-toolid)" : {{String}},
  "[ToolName](#cfn-wisdom-aiagent-toolconfiguration-toolname)" : {{String}},
  "[ToolType](#cfn-wisdom-aiagent-toolconfiguration-tooltype)" : {{String}},
  "[UserInteractionConfiguration](#cfn-wisdom-aiagent-toolconfiguration-userinteractionconfiguration)" : {{UserInteractionConfiguration}}
}
```

### YAML
<a name="aws-properties-wisdom-aiagent-toolconfiguration-syntax.yaml"></a>

```
  [Annotations](#cfn-wisdom-aiagent-toolconfiguration-annotations): {{Json}}
  [Description](#cfn-wisdom-aiagent-toolconfiguration-description): {{String}}
  [InputSchema](#cfn-wisdom-aiagent-toolconfiguration-inputschema): {{Json}}
  [Instruction](#cfn-wisdom-aiagent-toolconfiguration-instruction): {{
    ToolInstruction}}
  [OutputFilters](#cfn-wisdom-aiagent-toolconfiguration-outputfilters): {{
    - ToolOutputFilter}}
  [OutputSchema](#cfn-wisdom-aiagent-toolconfiguration-outputschema): {{Json}}
  [OverrideInputValues](#cfn-wisdom-aiagent-toolconfiguration-overrideinputvalues): {{
    - ToolOverrideInputValue}}
  [Title](#cfn-wisdom-aiagent-toolconfiguration-title): {{String}}
  [ToolId](#cfn-wisdom-aiagent-toolconfiguration-toolid): {{String}}
  [ToolName](#cfn-wisdom-aiagent-toolconfiguration-toolname): {{String}}
  [ToolType](#cfn-wisdom-aiagent-toolconfiguration-tooltype): {{String}}
  [UserInteractionConfiguration](#cfn-wisdom-aiagent-toolconfiguration-userinteractionconfiguration): {{
    UserInteractionConfiguration}}
```

## Properties
<a name="aws-properties-wisdom-aiagent-toolconfiguration-properties"></a>

`Annotations`  <a name="cfn-wisdom-aiagent-toolconfiguration-annotations"></a>
Annotations for the tool configuration.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-wisdom-aiagent-toolconfiguration-description"></a>
The description of the tool configuration.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputSchema`  <a name="cfn-wisdom-aiagent-toolconfiguration-inputschema"></a>
The input schema for the tool configuration.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Instruction`  <a name="cfn-wisdom-aiagent-toolconfiguration-instruction"></a>
Instructions for using the tool.
*Required*: No
*Type*: [ToolInstruction](aws-properties-wisdom-aiagent-toolinstruction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputFilters`  <a name="cfn-wisdom-aiagent-toolconfiguration-outputfilters"></a>
Output filters applies to the tool result.
*Required*: No
*Type*: Array of [ToolOutputFilter](aws-properties-wisdom-aiagent-tooloutputfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputSchema`  <a name="cfn-wisdom-aiagent-toolconfiguration-outputschema"></a>
The output schema for the tool configuration.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OverrideInputValues`  <a name="cfn-wisdom-aiagent-toolconfiguration-overrideinputvalues"></a>
Override input values for the tool configuration.
*Required*: No
*Type*: Array of [ToolOverrideInputValue](aws-properties-wisdom-aiagent-tooloverrideinputvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-wisdom-aiagent-toolconfiguration-title"></a>
The title of the tool configuration.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ToolId`  <a name="cfn-wisdom-aiagent-toolconfiguration-toolid"></a>
The identifier of the tool, for example toolName from Model Context Provider server.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ToolName`  <a name="cfn-wisdom-aiagent-toolconfiguration-toolname"></a>
The name of the tool.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ToolType`  <a name="cfn-wisdom-aiagent-toolconfiguration-tooltype"></a>
The type of the tool.
*Required*: Yes
*Type*: String
*Allowed values*: `MODEL_CONTEXT_PROTOCOL | RETURN_TO_CONTROL | CONSTANT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserInteractionConfiguration`  <a name="cfn-wisdom-aiagent-toolconfiguration-userinteractionconfiguration"></a>
Configuration for user interaction with the tool.
*Required*: No
*Type*: [UserInteractionConfiguration](aws-properties-wisdom-aiagent-userinteractionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
