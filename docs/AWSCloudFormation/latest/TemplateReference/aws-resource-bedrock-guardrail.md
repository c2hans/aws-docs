---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-guardrail.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Guardrail
<a name="aws-resource-bedrock-guardrail"></a>

Creates a guardrail to detect and filter harmful content in your generative AI application.

Amazon Bedrock Guardrails provides the following safeguards (also known as policies) to detect and filter harmful content:
+ **Content filters** - Detect and filter harmful text or image content in input prompts or model responses. Filtering is done based on detection of certain predefined harmful content categories: Hate, Insults, Sexual, Violence, Misconduct and Prompt Attack. You also can adjust the filter strength for each of these categories.
+ **Denied topics** - Define a set of topics that are undesirable in the context of your application. The filter will help block them if detected in user queries or model responses.
+ **Word filters** - Configure filters to help block undesirable words, phrases, and profanity (exact match). Such words can include offensive terms, competitor names, etc.
+ **Sensitive information filters** - Configure filters to help block or mask sensitive information, such as personally identifiable information (PII), or custom regex in user inputs and model responses. Blocking or masking is done based on probabilistic detection of sensitive information in standard formats in entities such as SSN number, Date of Birth, address, etc. This also allows configuring regular expression based detection of patterns for identifiers.
+ **Contextual grounding check** - Help detect and filter hallucinations in model responses based on grounding in a source and relevance to the user query.

For more information, see [How Amazon Bedrock Guardrails works](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html).

## Syntax
<a name="aws-resource-bedrock-guardrail-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-guardrail-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::Guardrail",
  "Properties" : {
      "[AutomatedReasoningPolicyConfig](#cfn-bedrock-guardrail-automatedreasoningpolicyconfig)" : {{AutomatedReasoningPolicyConfig}},
      "[BlockedInputMessaging](#cfn-bedrock-guardrail-blockedinputmessaging)" : {{String}},
      "[BlockedOutputsMessaging](#cfn-bedrock-guardrail-blockedoutputsmessaging)" : {{String}},
      "[ContentPolicyConfig](#cfn-bedrock-guardrail-contentpolicyconfig)" : {{ContentPolicyConfig}},
      "[ContextualGroundingPolicyConfig](#cfn-bedrock-guardrail-contextualgroundingpolicyconfig)" : {{ContextualGroundingPolicyConfig}},
      "[CrossRegionConfig](#cfn-bedrock-guardrail-crossregionconfig)" : {{GuardrailCrossRegionConfig}},
      "[Description](#cfn-bedrock-guardrail-description)" : {{String}},
      "[KmsKeyArn](#cfn-bedrock-guardrail-kmskeyarn)" : {{String}},
      "[Name](#cfn-bedrock-guardrail-name)" : {{String}},
      "[SensitiveInformationPolicyConfig](#cfn-bedrock-guardrail-sensitiveinformationpolicyconfig)" : {{SensitiveInformationPolicyConfig}},
      "[Tags](#cfn-bedrock-guardrail-tags)" : {{[ Tag, ... ]}},
      "[TopicPolicyConfig](#cfn-bedrock-guardrail-topicpolicyconfig)" : {{TopicPolicyConfig}},
      "[WordPolicyConfig](#cfn-bedrock-guardrail-wordpolicyconfig)" : {{WordPolicyConfig}}
    }
}
```

### YAML
<a name="aws-resource-bedrock-guardrail-syntax.yaml"></a>

```
Type: AWS::Bedrock::Guardrail
Properties:
  [AutomatedReasoningPolicyConfig](#cfn-bedrock-guardrail-automatedreasoningpolicyconfig): {{
    AutomatedReasoningPolicyConfig}}
  [BlockedInputMessaging](#cfn-bedrock-guardrail-blockedinputmessaging): {{String}}
  [BlockedOutputsMessaging](#cfn-bedrock-guardrail-blockedoutputsmessaging): {{String}}
  [ContentPolicyConfig](#cfn-bedrock-guardrail-contentpolicyconfig): {{
    ContentPolicyConfig}}
  [ContextualGroundingPolicyConfig](#cfn-bedrock-guardrail-contextualgroundingpolicyconfig): {{
    ContextualGroundingPolicyConfig}}
  [CrossRegionConfig](#cfn-bedrock-guardrail-crossregionconfig): {{
    GuardrailCrossRegionConfig}}
  [Description](#cfn-bedrock-guardrail-description): {{String}}
  [KmsKeyArn](#cfn-bedrock-guardrail-kmskeyarn): {{String}}
  [Name](#cfn-bedrock-guardrail-name): {{String}}
  [SensitiveInformationPolicyConfig](#cfn-bedrock-guardrail-sensitiveinformationpolicyconfig): {{
    SensitiveInformationPolicyConfig}}
  [Tags](#cfn-bedrock-guardrail-tags): {{
    - Tag}}
  [TopicPolicyConfig](#cfn-bedrock-guardrail-topicpolicyconfig): {{
    TopicPolicyConfig}}
  [WordPolicyConfig](#cfn-bedrock-guardrail-wordpolicyconfig): {{
    WordPolicyConfig}}
```

## Properties
<a name="aws-resource-bedrock-guardrail-properties"></a>

`AutomatedReasoningPolicyConfig`  <a name="cfn-bedrock-guardrail-automatedreasoningpolicyconfig"></a>
Configuration settings for integrating Automated Reasoning policies with Amazon Bedrock Guardrails.
*Required*: No
*Type*: [AutomatedReasoningPolicyConfig](aws-properties-bedrock-guardrail-automatedreasoningpolicyconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BlockedInputMessaging`  <a name="cfn-bedrock-guardrail-blockedinputmessaging"></a>
The message to return when the guardrail blocks a prompt.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BlockedOutputsMessaging`  <a name="cfn-bedrock-guardrail-blockedoutputsmessaging"></a>
The message to return when the guardrail blocks a model response.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContentPolicyConfig`  <a name="cfn-bedrock-guardrail-contentpolicyconfig"></a>
The content filter policies to configure for the guardrail.
*Required*: No
*Type*: [ContentPolicyConfig](aws-properties-bedrock-guardrail-contentpolicyconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContextualGroundingPolicyConfig`  <a name="cfn-bedrock-guardrail-contextualgroundingpolicyconfig"></a>
Property description not available.
*Required*: No
*Type*: [ContextualGroundingPolicyConfig](aws-properties-bedrock-guardrail-contextualgroundingpolicyconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CrossRegionConfig`  <a name="cfn-bedrock-guardrail-crossregionconfig"></a>
The system-defined guardrail profile that you're using with your guardrail. Guardrail profiles define the destination AWS Regions where guardrail inference requests can be automatically routed. Using guardrail profiles helps maintain guardrail performance and reliability when demand increases.
For more information, see the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region.html).
*Required*: No
*Type*: [GuardrailCrossRegionConfig](aws-properties-bedrock-guardrail-guardrailcrossregionconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-bedrock-guardrail-description"></a>
A description of the guardrail.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-bedrock-guardrail-kmskeyarn"></a>
The ARN of the AWS KMS key that you use to encrypt the guardrail.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrock-guardrail-name"></a>
The name of the guardrail.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-zA-Z-_]+$`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SensitiveInformationPolicyConfig`  <a name="cfn-bedrock-guardrail-sensitiveinformationpolicyconfig"></a>
The sensitive information policy to configure for the guardrail.
*Required*: No
*Type*: [SensitiveInformationPolicyConfig](aws-properties-bedrock-guardrail-sensitiveinformationpolicyconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-bedrock-guardrail-tags"></a>
The tags that you want to attach to the guardrail.
*Required*: No
*Type*: Array of [Tag](aws-properties-bedrock-guardrail-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicPolicyConfig`  <a name="cfn-bedrock-guardrail-topicpolicyconfig"></a>
The topic policies to configure for the guardrail.
*Required*: No
*Type*: [TopicPolicyConfig](aws-properties-bedrock-guardrail-topicpolicyconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WordPolicyConfig`  <a name="cfn-bedrock-guardrail-wordpolicyconfig"></a>
The word policy you configure for the guardrail.
*Required*: No
*Type*: [WordPolicyConfig](aws-properties-bedrock-guardrail-wordpolicyconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrock-guardrail-return-values"></a>

### Ref
<a name="aws-resource-bedrock-guardrail-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrock-guardrail-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrock-guardrail-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Timestamp.

`FailureRecommendations`  <a name="FailureRecommendations-fn::getatt"></a>
Appears if the `status` of the guardrail is `FAILED`. A list of recommendations to carry out before retrying the request.

`GuardrailArn`  <a name="GuardrailArn-fn::getatt"></a>
The ARN of the guardrail.

`GuardrailId`  <a name="GuardrailId-fn::getatt"></a>
The unique identifier of the guardrail.

`Status`  <a name="Status-fn::getatt"></a>
The status of the guardrail.

`StatusReasons`  <a name="StatusReasons-fn::getatt"></a>
Appears if the `status` is `FAILED`. A list of reasons for why the guardrail failed to be created, updated, versioned, or deleted.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
Timestamp.

`Version`  <a name="Version-fn::getatt"></a>
The version of the guardrail that was created. This value will always be `DRAFT`.
