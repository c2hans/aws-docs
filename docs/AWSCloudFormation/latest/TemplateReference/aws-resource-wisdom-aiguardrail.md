---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wisdom-aiguardrail.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIGuardrail
<a name="aws-resource-wisdom-aiguardrail"></a>

Creates an Amazon Q in Connect AI Guardrail.

## Syntax
<a name="aws-resource-wisdom-aiguardrail-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wisdom-aiguardrail-syntax.json"></a>

```
{
  "Type" : "AWS::Wisdom::AIGuardrail",
  "Properties" : {
      "[AssistantId](#cfn-wisdom-aiguardrail-assistantid)" : {{String}},
      "[BlockedInputMessaging](#cfn-wisdom-aiguardrail-blockedinputmessaging)" : {{String}},
      "[BlockedOutputsMessaging](#cfn-wisdom-aiguardrail-blockedoutputsmessaging)" : {{String}},
      "[ContentPolicyConfig](#cfn-wisdom-aiguardrail-contentpolicyconfig)" : {{AIGuardrailContentPolicyConfig}},
      "[ContextualGroundingPolicyConfig](#cfn-wisdom-aiguardrail-contextualgroundingpolicyconfig)" : {{AIGuardrailContextualGroundingPolicyConfig}},
      "[Description](#cfn-wisdom-aiguardrail-description)" : {{String}},
      "[Name](#cfn-wisdom-aiguardrail-name)" : {{String}},
      "[SensitiveInformationPolicyConfig](#cfn-wisdom-aiguardrail-sensitiveinformationpolicyconfig)" : {{AIGuardrailSensitiveInformationPolicyConfig}},
      "[Tags](#cfn-wisdom-aiguardrail-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[TopicPolicyConfig](#cfn-wisdom-aiguardrail-topicpolicyconfig)" : {{AIGuardrailTopicPolicyConfig}},
      "[WordPolicyConfig](#cfn-wisdom-aiguardrail-wordpolicyconfig)" : {{AIGuardrailWordPolicyConfig}}
    }
}
```

### YAML
<a name="aws-resource-wisdom-aiguardrail-syntax.yaml"></a>

```
Type: AWS::Wisdom::AIGuardrail
Properties:
  [AssistantId](#cfn-wisdom-aiguardrail-assistantid): {{String}}
  [BlockedInputMessaging](#cfn-wisdom-aiguardrail-blockedinputmessaging): {{String}}
  [BlockedOutputsMessaging](#cfn-wisdom-aiguardrail-blockedoutputsmessaging): {{String}}
  [ContentPolicyConfig](#cfn-wisdom-aiguardrail-contentpolicyconfig): {{
    AIGuardrailContentPolicyConfig}}
  [ContextualGroundingPolicyConfig](#cfn-wisdom-aiguardrail-contextualgroundingpolicyconfig): {{
    AIGuardrailContextualGroundingPolicyConfig}}
  [Description](#cfn-wisdom-aiguardrail-description): {{String}}
  [Name](#cfn-wisdom-aiguardrail-name): {{String}}
  [SensitiveInformationPolicyConfig](#cfn-wisdom-aiguardrail-sensitiveinformationpolicyconfig): {{
    AIGuardrailSensitiveInformationPolicyConfig}}
  [Tags](#cfn-wisdom-aiguardrail-tags): {{
    {{Key}}: {{Value}}}}
  [TopicPolicyConfig](#cfn-wisdom-aiguardrail-topicpolicyconfig): {{
    AIGuardrailTopicPolicyConfig}}
  [WordPolicyConfig](#cfn-wisdom-aiguardrail-wordpolicyconfig): {{
    AIGuardrailWordPolicyConfig}}
```

## Properties
<a name="aws-resource-wisdom-aiguardrail-properties"></a>

`AssistantId`  <a name="cfn-wisdom-aiguardrail-assistantid"></a>
The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BlockedInputMessaging`  <a name="cfn-wisdom-aiguardrail-blockedinputmessaging"></a>
The message to return when the AI Guardrail blocks a prompt.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BlockedOutputsMessaging`  <a name="cfn-wisdom-aiguardrail-blockedoutputsmessaging"></a>
The message to return when the AI Guardrail blocks a model response.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContentPolicyConfig`  <a name="cfn-wisdom-aiguardrail-contentpolicyconfig"></a>
Contains details about how to handle harmful content.
*Required*: No
*Type*: [AIGuardrailContentPolicyConfig](aws-properties-wisdom-aiguardrail-aiguardrailcontentpolicyconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContextualGroundingPolicyConfig`  <a name="cfn-wisdom-aiguardrail-contextualgroundingpolicyconfig"></a>
The policy configuration details for the AI Guardrail's contextual grounding policy.
*Required*: No
*Type*: [AIGuardrailContextualGroundingPolicyConfig](aws-properties-wisdom-aiguardrail-aiguardrailcontextualgroundingpolicyconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-wisdom-aiguardrail-description"></a>
A description of the AI Guardrail.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-wisdom-aiguardrail-name"></a>
The name of the AI Guardrail.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s_.,-]+`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SensitiveInformationPolicyConfig`  <a name="cfn-wisdom-aiguardrail-sensitiveinformationpolicyconfig"></a>
Contains details about PII entities and regular expressions to configure for the AI Guardrail.
*Required*: No
*Type*: [AIGuardrailSensitiveInformationPolicyConfig](aws-properties-wisdom-aiguardrail-aiguardrailsensitiveinformationpolicyconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-wisdom-aiguardrail-tags"></a>
The tags used to organize, track, or control access for this resource.
*Required*: No
*Type*: Object of String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TopicPolicyConfig`  <a name="cfn-wisdom-aiguardrail-topicpolicyconfig"></a>
Contains details about topics that the AI Guardrail should identify and deny.
*Required*: No
*Type*: [AIGuardrailTopicPolicyConfig](aws-properties-wisdom-aiguardrail-aiguardrailtopicpolicyconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WordPolicyConfig`  <a name="cfn-wisdom-aiguardrail-wordpolicyconfig"></a>
Contains details about the word policy to configured for the AI Guardrail.
*Required*: No
*Type*: [AIGuardrailWordPolicyConfig](aws-properties-wisdom-aiguardrail-aiguardrailwordpolicyconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-wisdom-aiguardrail-return-values"></a>

### Ref
<a name="aws-resource-wisdom-aiguardrail-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-wisdom-aiguardrail-return-values-fn--getatt"></a>

####
<a name="aws-resource-wisdom-aiguardrail-return-values-fn--getatt-fn--getatt"></a>

`AIGuardrailArn`  <a name="AIGuardrailArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the AI Guardrail.

`AIGuardrailId`  <a name="AIGuardrailId-fn::getatt"></a>
The identifier of the Amazon Q in Connect AI Guardrail.

`AssistantArn`  <a name="AssistantArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.

`ModifiedTimeSeconds`  <a name="ModifiedTimeSeconds-fn::getatt"></a>
Property description not available.
