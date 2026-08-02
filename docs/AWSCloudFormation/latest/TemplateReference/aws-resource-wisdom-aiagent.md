---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wisdom-aiagent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgent
<a name="aws-resource-wisdom-aiagent"></a>

Creates an Amazon Q in Connect AI Agent.

## Syntax
<a name="aws-resource-wisdom-aiagent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wisdom-aiagent-syntax.json"></a>

```
{
  "Type" : "AWS::Wisdom::AIAgent",
  "Properties" : {
      "[AssistantId](#cfn-wisdom-aiagent-assistantid)" : {{String}},
      "[Configuration](#cfn-wisdom-aiagent-configuration)" : {{AIAgentConfiguration}},
      "[Description](#cfn-wisdom-aiagent-description)" : {{String}},
      "[Name](#cfn-wisdom-aiagent-name)" : {{String}},
      "[Tags](#cfn-wisdom-aiagent-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Type](#cfn-wisdom-aiagent-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-wisdom-aiagent-syntax.yaml"></a>

```
Type: AWS::Wisdom::AIAgent
Properties:
  [AssistantId](#cfn-wisdom-aiagent-assistantid): {{String}}
  [Configuration](#cfn-wisdom-aiagent-configuration): {{
    AIAgentConfiguration}}
  [Description](#cfn-wisdom-aiagent-description): {{String}}
  [Name](#cfn-wisdom-aiagent-name): {{String}}
  [Tags](#cfn-wisdom-aiagent-tags): {{
    {{Key}}: {{Value}}}}
  [Type](#cfn-wisdom-aiagent-type): {{String}}
```

## Properties
<a name="aws-resource-wisdom-aiagent-properties"></a>

`AssistantId`  <a name="cfn-wisdom-aiagent-assistantid"></a>
The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Configuration`  <a name="cfn-wisdom-aiagent-configuration"></a>
Configuration for the AI Agent.
*Required*: Yes
*Type*: [AIAgentConfiguration](aws-properties-wisdom-aiagent-aiagentconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-wisdom-aiagent-description"></a>
The description of the AI Agent.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s_.,-]+`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-wisdom-aiagent-name"></a>
The name of the AI Agent.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s_.,-]+`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-wisdom-aiagent-tags"></a>
The tags used to organize, track, or control access for this resource.
*Required*: No
*Type*: Object of String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-wisdom-aiagent-type"></a>
The type of the AI Agent.
*Required*: Yes
*Type*: String
*Allowed values*: `MANUAL_SEARCH | ANSWER_RECOMMENDATION | SELF_SERVICE | EMAIL_RESPONSE | EMAIL_OVERVIEW | EMAIL_GENERATIVE_ANSWER | ORCHESTRATION | NOTE_TAKING | CASE_SUMMARIZATION`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-wisdom-aiagent-return-values"></a>

### Ref
<a name="aws-resource-wisdom-aiagent-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-wisdom-aiagent-return-values-fn--getatt"></a>

####
<a name="aws-resource-wisdom-aiagent-return-values-fn--getatt-fn--getatt"></a>

`AIAgentArn`  <a name="AIAgentArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the AI agent.

`AIAgentId`  <a name="AIAgentId-fn::getatt"></a>
The identifier of the AI Agent.

`AssistantArn`  <a name="AssistantArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.

`ModifiedTimeSeconds`  <a name="ModifiedTimeSeconds-fn::getatt"></a>
Property description not available.
