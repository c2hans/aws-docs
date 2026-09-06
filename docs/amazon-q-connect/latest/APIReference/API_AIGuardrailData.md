---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_AIGuardrailData.html
---

# AIGuardrailData
<a name="API_amazon-q-connect_AIGuardrailData"></a>

The data for the AI Guardrail

## Contents
<a name="API_amazon-q-connect_AIGuardrailData_Contents"></a>

 ** aiGuardrailArn **   <a name="connect-Type-amazon-q-connect_AIGuardrailData-aiGuardrailArn"></a>
The Amazon Resource Name (ARN) of the AI Guardrail.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** aiGuardrailId **   <a name="connect-Type-amazon-q-connect_AIGuardrailData-aiGuardrailId"></a>
The identifier of the Amazon Q in Connect AI Guardrail.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** assistantArn **   <a name="connect-Type-amazon-q-connect_AIGuardrailData-assistantArn"></a>
The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** assistantId **   <a name="connect-Type-amazon-q-connect_AIGuardrailData-assistantId"></a>
The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** blockedInputMessaging **   <a name="connect-Type-amazon-q-connect_AIGuardrailData-blockedInputMessaging"></a>
The message to return when the AI Guardrail blocks a prompt.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** blockedOutputsMessaging **   <a name="connect-Type-amazon-q-connect_AIGuardrailData-blockedOutputsMessaging"></a>
The message to return when the AI Guardrail blocks a model response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** name **   <a name="connect-Type-amazon-q-connect_AIGuardrailData-name"></a>
The name of the AI Guardrail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: Yes

 ** visibilityStatus **   <a name="connect-Type-amazon-q-connect_AIGuardrailData-visibilityStatus"></a>
The visibility status of the AI Guardrail.
Type: String
Valid Values: `SAVED | PUBLISHED`
Required: Yes

 ** contentPolicyConfig **   <a name="connect-Type-amazon-q-connect_AIGuardrailData-contentPolicyConfig"></a>
Contains details about how to handle harmful content.
Type: [AIGuardrailContentPolicyConfig](API_amazon-q-connect_AIGuardrailContentPolicyConfig.md) object
Required: No

 ** contextualGroundingPolicyConfig **   <a name="connect-Type-amazon-q-connect_AIGuardrailData-contextualGroundingPolicyConfig"></a>
The policy configuration details for the AI Guardrail's contextual grounding policy.
Type: [AIGuardrailContextualGroundingPolicyConfig](API_amazon-q-connect_AIGuardrailContextualGroundingPolicyConfig.md) object
Required: No

 ** description **   <a name="connect-Type-amazon-q-connect_AIGuardrailData-description"></a>
A description of the AI Guardrail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** modifiedTime **   <a name="connect-Type-amazon-q-connect_AIGuardrailData-modifiedTime"></a>
The time the AI Guardrail was last modified.
Type: Timestamp
Required: No

 ** sensitiveInformationPolicyConfig **   <a name="connect-Type-amazon-q-connect_AIGuardrailData-sensitiveInformationPolicyConfig"></a>
Contains details about PII entities and regular expressions to configure for the AI Guardrail.
Type: [AIGuardrailSensitiveInformationPolicyConfig](API_amazon-q-connect_AIGuardrailSensitiveInformationPolicyConfig.md) object
Required: No

 ** status **   <a name="connect-Type-amazon-q-connect_AIGuardrailData-status"></a>
The status of the AI Guardrail.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED | ACTIVE | DELETE_IN_PROGRESS | DELETE_FAILED | DELETED`
Required: No

 ** tags **   <a name="connect-Type-amazon-q-connect_AIGuardrailData-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** topicPolicyConfig **   <a name="connect-Type-amazon-q-connect_AIGuardrailData-topicPolicyConfig"></a>
Contains details about topics that the AI Guardrail should identify and deny.
Type: [AIGuardrailTopicPolicyConfig](API_amazon-q-connect_AIGuardrailTopicPolicyConfig.md) object
Required: No

 ** wordPolicyConfig **   <a name="connect-Type-amazon-q-connect_AIGuardrailData-wordPolicyConfig"></a>
Contains details about the word policy to configured for the AI Guardrail.
Type: [AIGuardrailWordPolicyConfig](API_amazon-q-connect_AIGuardrailWordPolicyConfig.md) object
Required: No

## See Also
<a name="API_amazon-q-connect_AIGuardrailData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/AIGuardrailData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/AIGuardrailData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/AIGuardrailData)
