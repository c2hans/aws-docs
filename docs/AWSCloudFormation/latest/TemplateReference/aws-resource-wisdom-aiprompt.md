---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wisdom-aiprompt.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIPrompt
<a name="aws-resource-wisdom-aiprompt"></a>

Creates an Amazon Q in Connect AI Prompt.

## Syntax
<a name="aws-resource-wisdom-aiprompt-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wisdom-aiprompt-syntax.json"></a>

```
{
  "Type" : "AWS::Wisdom::AIPrompt",
  "Properties" : {
      "[ApiFormat](#cfn-wisdom-aiprompt-apiformat)" : {{String}},
      "[AssistantId](#cfn-wisdom-aiprompt-assistantid)" : {{String}},
      "[Description](#cfn-wisdom-aiprompt-description)" : {{String}},
      "[ModelId](#cfn-wisdom-aiprompt-modelid)" : {{String}},
      "[Name](#cfn-wisdom-aiprompt-name)" : {{String}},
      "[Tags](#cfn-wisdom-aiprompt-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[TemplateConfiguration](#cfn-wisdom-aiprompt-templateconfiguration)" : {{AIPromptTemplateConfiguration}},
      "[TemplateType](#cfn-wisdom-aiprompt-templatetype)" : {{String}},
      "[Type](#cfn-wisdom-aiprompt-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-wisdom-aiprompt-syntax.yaml"></a>

```
Type: AWS::Wisdom::AIPrompt
Properties:
  [ApiFormat](#cfn-wisdom-aiprompt-apiformat): {{String}}
  [AssistantId](#cfn-wisdom-aiprompt-assistantid): {{String}}
  [Description](#cfn-wisdom-aiprompt-description): {{String}}
  [ModelId](#cfn-wisdom-aiprompt-modelid): {{String}}
  [Name](#cfn-wisdom-aiprompt-name): {{String}}
  [Tags](#cfn-wisdom-aiprompt-tags): {{
    {{Key}}: {{Value}}}}
  [TemplateConfiguration](#cfn-wisdom-aiprompt-templateconfiguration): {{
    AIPromptTemplateConfiguration}}
  [TemplateType](#cfn-wisdom-aiprompt-templatetype): {{String}}
  [Type](#cfn-wisdom-aiprompt-type): {{String}}
```

## Properties
<a name="aws-resource-wisdom-aiprompt-properties"></a>

`ApiFormat`  <a name="cfn-wisdom-aiprompt-apiformat"></a>
The API format used for this AI Prompt.
*Required*: Yes
*Type*: String
*Allowed values*: `ANTHROPIC_CLAUDE_MESSAGES | ANTHROPIC_CLAUDE_TEXT_COMPLETIONS | MESSAGES | TEXT_COMPLETIONS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AssistantId`  <a name="cfn-wisdom-aiprompt-assistantid"></a>
The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
*Required*: No
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-wisdom-aiprompt-description"></a>
The description of the AI Prompt.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s_.,-]+`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelId`  <a name="cfn-wisdom-aiprompt-modelid"></a>
The identifier of the model used for this AI Prompt. The following model Ids are supported:
+  `anthropic.claude-3-haiku--v1:0`
+  `apac.amazon.nova-lite-v1:0`
+  `apac.amazon.nova-micro-v1:0`
+  `apac.amazon.nova-pro-v1:0`
+  `apac.anthropic.claude-3-5-sonnet--v2:0`
+  `apac.anthropic.claude-3-haiku-20240307-v1:0`
+  `eu.amazon.nova-lite-v1:0`
+  `eu.amazon.nova-micro-v1:0`
+  `eu.amazon.nova-pro-v1:0`
+  `eu.anthropic.claude-3-7-sonnet-20250219-v1:0`
+  `eu.anthropic.claude-3-haiku-20240307-v1:0`
+  `us.amazon.nova-lite-v1:0`
+  `us.amazon.nova-micro-v1:0`
+  `us.amazon.nova-pro-v1:0`
+  `us.anthropic.claude-3-5-haiku-20241022-v1:0`
+  `us.anthropic.claude-3-7-sonnet-20250219-v1:0`
+  `us.anthropic.claude-3-haiku-20240307-v1:0`
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-wisdom-aiprompt-name"></a>
The name of the AI Prompt
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s_.,-]+`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-wisdom-aiprompt-tags"></a>
The tags used to organize, track, or control access for this resource.
*Required*: No
*Type*: Object of String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TemplateConfiguration`  <a name="cfn-wisdom-aiprompt-templateconfiguration"></a>
The configuration of the prompt template for this AI Prompt.
*Required*: Yes
*Type*: [AIPromptTemplateConfiguration](aws-properties-wisdom-aiprompt-aiprompttemplateconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateType`  <a name="cfn-wisdom-aiprompt-templatetype"></a>
The type of the prompt template for this AI Prompt.
*Required*: Yes
*Type*: String
*Allowed values*: `TEXT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-wisdom-aiprompt-type"></a>
The type of this AI Prompt.
*Required*: Yes
*Type*: String
*Allowed values*: `ANSWER_GENERATION | INTENT_LABELING_GENERATION | QUERY_REFORMULATION | SELF_SERVICE_PRE_PROCESSING | SELF_SERVICE_ANSWER_GENERATION | EMAIL_RESPONSE | EMAIL_OVERVIEW | EMAIL_GENERATIVE_ANSWER | EMAIL_QUERY_REFORMULATION | ORCHESTRATION | NOTE_TAKING | CASE_SUMMARIZATION`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-wisdom-aiprompt-return-values"></a>

### Ref
<a name="aws-resource-wisdom-aiprompt-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-wisdom-aiprompt-return-values-fn--getatt"></a>

####
<a name="aws-resource-wisdom-aiprompt-return-values-fn--getatt-fn--getatt"></a>

`AIPromptArn`  <a name="AIPromptArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the AI Prompt.

`AIPromptId`  <a name="AIPromptId-fn::getatt"></a>
The identifier of the Amazon Q in Connect AI prompt.

`AssistantArn`  <a name="AssistantArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.

`ModifiedTimeSeconds`  <a name="ModifiedTimeSeconds-fn::getatt"></a>
Property description not available.
