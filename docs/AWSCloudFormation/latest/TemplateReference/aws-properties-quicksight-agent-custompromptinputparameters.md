---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-agent-custompromptinputparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Agent CustomPromptInputParameters
<a name="aws-properties-quicksight-agent-custompromptinputparameters"></a>

The parameters for configuring a custom prompt for an agent.

## Syntax
<a name="aws-properties-quicksight-agent-custompromptinputparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-agent-custompromptinputparameters-syntax.json"></a>

```
{
  "[CustomInstructions](#cfn-quicksight-agent-custompromptinputparameters-custominstructions)" : {{String}},
  "[Identity](#cfn-quicksight-agent-custompromptinputparameters-identity)" : {{String}},
  "[OutputStyle](#cfn-quicksight-agent-custompromptinputparameters-outputstyle)" : {{String}},
  "[ResponseLength](#cfn-quicksight-agent-custompromptinputparameters-responselength)" : {{String}},
  "[Tone](#cfn-quicksight-agent-custompromptinputparameters-tone)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-agent-custompromptinputparameters-syntax.yaml"></a>

```
  [CustomInstructions](#cfn-quicksight-agent-custompromptinputparameters-custominstructions): {{String}}
  [Identity](#cfn-quicksight-agent-custompromptinputparameters-identity): {{String}}
  [OutputStyle](#cfn-quicksight-agent-custompromptinputparameters-outputstyle): {{String}}
  [ResponseLength](#cfn-quicksight-agent-custompromptinputparameters-responselength): {{String}}
  [Tone](#cfn-quicksight-agent-custompromptinputparameters-tone): {{String}}
```

## Properties
<a name="aws-properties-quicksight-agent-custompromptinputparameters-properties"></a>

`CustomInstructions`  <a name="cfn-quicksight-agent-custompromptinputparameters-custominstructions"></a>
Custom instructions for the agent's behavior.
*Required*: No
*Type*: String
*Minimum*: `5`
*Maximum*: `350000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Identity`  <a name="cfn-quicksight-agent-custompromptinputparameters-identity"></a>
Instructions that define the agent's identity and persona.
*Required*: No
*Type*: String
*Minimum*: `5`
*Maximum*: `350000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputStyle`  <a name="cfn-quicksight-agent-custompromptinputparameters-outputstyle"></a>
Instructions for the desired output style.
*Required*: No
*Type*: String
*Minimum*: `5`
*Maximum*: `350000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResponseLength`  <a name="cfn-quicksight-agent-custompromptinputparameters-responselength"></a>
Instructions for the desired response length.
*Required*: No
*Type*: String
*Minimum*: `5`
*Maximum*: `350000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tone`  <a name="cfn-quicksight-agent-custompromptinputparameters-tone"></a>
Instructions for the desired tone of responses.
*Required*: No
*Type*: String
*Minimum*: `5`
*Maximum*: `350000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
