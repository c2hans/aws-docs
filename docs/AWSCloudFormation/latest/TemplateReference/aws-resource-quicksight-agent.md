---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-agent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Agent
<a name="aws-resource-quicksight-agent"></a>

Creates an agent in Amazon QuickSight.

## Syntax
<a name="aws-resource-quicksight-agent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-agent-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::Agent",
  "Properties" : {
      "[ActionConnectors](#cfn-quicksight-agent-actionconnectors)" : {{[ String, ... ]}},
      "[AgentId](#cfn-quicksight-agent-agentid)" : {{String}},
      "[AgentLifecycle](#cfn-quicksight-agent-agentlifecycle)" : {{String}},
      "[AwsAccountId](#cfn-quicksight-agent-awsaccountid)" : {{String}},
      "[CustomPromptInput](#cfn-quicksight-agent-custompromptinput)" : {{CustomPromptInput}},
      "[Description](#cfn-quicksight-agent-description)" : {{String}},
      "[IconId](#cfn-quicksight-agent-iconid)" : {{String}},
      "[Name](#cfn-quicksight-agent-name)" : {{String}},
      "[Spaces](#cfn-quicksight-agent-spaces)" : {{[ String, ... ]}},
      "[StarterPrompts](#cfn-quicksight-agent-starterprompts)" : {{[ String, ... ]}},
      "[Tags](#cfn-quicksight-agent-tags)" : {{[ AgentTag, ... ]}},
      "[WelcomeMessage](#cfn-quicksight-agent-welcomemessage)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-agent-syntax.yaml"></a>

```
Type: AWS::QuickSight::Agent
Properties:
  [ActionConnectors](#cfn-quicksight-agent-actionconnectors): {{
    - String}}
  [AgentId](#cfn-quicksight-agent-agentid): {{String}}
  [AgentLifecycle](#cfn-quicksight-agent-agentlifecycle): {{String}}
  [AwsAccountId](#cfn-quicksight-agent-awsaccountid): {{String}}
  [CustomPromptInput](#cfn-quicksight-agent-custompromptinput): {{
    CustomPromptInput}}
  [Description](#cfn-quicksight-agent-description): {{String}}
  [IconId](#cfn-quicksight-agent-iconid): {{String}}
  [Name](#cfn-quicksight-agent-name): {{String}}
  [Spaces](#cfn-quicksight-agent-spaces): {{
    - String}}
  [StarterPrompts](#cfn-quicksight-agent-starterprompts): {{
    - String}}
  [Tags](#cfn-quicksight-agent-tags): {{
    - AgentTag}}
  [WelcomeMessage](#cfn-quicksight-agent-welcomemessage): {{String}}
```

## Properties
<a name="aws-resource-quicksight-agent-properties"></a>

`ActionConnectors`  <a name="cfn-quicksight-agent-actionconnectors"></a>
The Amazon Resource Names (ARNs) of the action connectors attached to the agent.
*Required*: No
*Type*: Array of String
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AgentId`  <a name="cfn-quicksight-agent-agentid"></a>
The unique identifier for the agent.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-zA-Z-_.+]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AgentLifecycle`  <a name="cfn-quicksight-agent-agentlifecycle"></a>
The lifecycle state of the agent. Valid values are `PREVIEW` and `PUBLISHED`.
*Required*: No
*Type*: String
*Allowed values*: `PREVIEW | PUBLISHED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AwsAccountId`  <a name="cfn-quicksight-agent-awsaccountid"></a>
The ID of the AWS account that contains the agent.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CustomPromptInput`  <a name="cfn-quicksight-agent-custompromptinput"></a>
The custom prompt configuration for the agent.
*Required*: No
*Type*: [CustomPromptInput](aws-properties-quicksight-agent-custompromptinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-quicksight-agent-description"></a>
A description of the agent.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IconId`  <a name="cfn-quicksight-agent-iconid"></a>
The icon identifier for the agent.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-agent-name"></a>
The name of the agent.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Spaces`  <a name="cfn-quicksight-agent-spaces"></a>
The Amazon Resource Names (ARNs) of the spaces attached to the agent.
*Required*: No
*Type*: Array of String
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StarterPrompts`  <a name="cfn-quicksight-agent-starterprompts"></a>
A list of starter prompts that are displayed to users when they begin interacting with the agent.
*Required*: No
*Type*: Array of String
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-quicksight-agent-tags"></a>
Contains a map of the key-value pairs for the resource tag or tags assigned to the agent.
*Required*: No
*Type*: Array of [AgentTag](aws-properties-quicksight-agent-agenttag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WelcomeMessage`  <a name="cfn-quicksight-agent-welcomemessage"></a>
The welcome message that is displayed when a user starts a conversation with the agent.
*Required*: No
*Type*: String
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-quicksight-agent-return-values"></a>

### Ref
<a name="aws-resource-quicksight-agent-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-agent-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-agent-return-values-fn--getatt-fn--getatt"></a>

`AgentStatus`  <a name="AgentStatus-fn::getatt"></a>
The status of the agent.

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the agent.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time that the agent was created.

`Creator`  <a name="Creator-fn::getatt"></a>
The identity of the user who created the agent.

`ErrorMessage`  <a name="ErrorMessage-fn::getatt"></a>
An error message associated with the agent, if applicable.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time that the agent was last updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
