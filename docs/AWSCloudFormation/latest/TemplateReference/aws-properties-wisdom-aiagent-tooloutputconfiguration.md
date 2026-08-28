---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiagent-tooloutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgent ToolOutputConfiguration
<a name="aws-properties-wisdom-aiagent-tooloutputconfiguration"></a>

Configuration for tool output handling.

## Syntax
<a name="aws-properties-wisdom-aiagent-tooloutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiagent-tooloutputconfiguration-syntax.json"></a>

```
{
  "[OutputVariableNameOverride](#cfn-wisdom-aiagent-tooloutputconfiguration-outputvariablenameoverride)" : {{String}},
  "[SessionDataNamespace](#cfn-wisdom-aiagent-tooloutputconfiguration-sessiondatanamespace)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-aiagent-tooloutputconfiguration-syntax.yaml"></a>

```
  [OutputVariableNameOverride](#cfn-wisdom-aiagent-tooloutputconfiguration-outputvariablenameoverride): {{String}}
  [SessionDataNamespace](#cfn-wisdom-aiagent-tooloutputconfiguration-sessiondatanamespace): {{String}}
```

## Properties
<a name="aws-properties-wisdom-aiagent-tooloutputconfiguration-properties"></a>

`OutputVariableNameOverride`  <a name="cfn-wisdom-aiagent-tooloutputconfiguration-outputvariablenameoverride"></a>
Override the tool output results to different variable name.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SessionDataNamespace`  <a name="cfn-wisdom-aiagent-tooloutputconfiguration-sessiondatanamespace"></a>
The session data namespace for tool output.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
