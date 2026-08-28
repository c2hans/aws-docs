---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-agent-custompromptinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Agent CustomPromptInput
<a name="aws-properties-quicksight-agent-custompromptinput"></a>

The custom prompt input for an agent. This is a union type that can be either an existing prompt profile or new prompt parameters.

## Syntax
<a name="aws-properties-quicksight-agent-custompromptinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-agent-custompromptinput-syntax.json"></a>

```
{
  "[ExistingPrompt](#cfn-quicksight-agent-custompromptinput-existingprompt)" : {{CustomPromptProfile}},
  "[NewPrompt](#cfn-quicksight-agent-custompromptinput-newprompt)" : {{CustomPromptInputParameters}}
}
```

### YAML
<a name="aws-properties-quicksight-agent-custompromptinput-syntax.yaml"></a>

```
  [ExistingPrompt](#cfn-quicksight-agent-custompromptinput-existingprompt): {{
    CustomPromptProfile}}
  [NewPrompt](#cfn-quicksight-agent-custompromptinput-newprompt): {{
    CustomPromptInputParameters}}
```

## Properties
<a name="aws-properties-quicksight-agent-custompromptinput-properties"></a>

`ExistingPrompt`  <a name="cfn-quicksight-agent-custompromptinput-existingprompt"></a>
An existing custom prompt profile to use for the agent.
*Required*: No
*Type*: [CustomPromptProfile](aws-properties-quicksight-agent-custompromptprofile.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NewPrompt`  <a name="cfn-quicksight-agent-custompromptinput-newprompt"></a>
New custom prompt parameters to configure for the agent.
*Required*: No
*Type*: [CustomPromptInputParameters](aws-properties-quicksight-agent-custompromptinputparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
