---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_AIPromptData.html
---

# AIPromptData
<a name="API_amazon-q-connect_AIPromptData"></a>

The data for the AI Prompt

## Contents
<a name="API_amazon-q-connect_AIPromptData_Contents"></a>

 ** aiPromptArn **   <a name="connect-Type-amazon-q-connect_AIPromptData-aiPromptArn"></a>
The Amazon Resource Name (ARN) of the AI Prompt.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** aiPromptId **   <a name="connect-Type-amazon-q-connect_AIPromptData-aiPromptId"></a>
The identifier of the Amazon Q in Connect AI prompt.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** apiFormat **   <a name="connect-Type-amazon-q-connect_AIPromptData-apiFormat"></a>
The API format used for this AI Prompt.
Type: String
Valid Values: `ANTHROPIC_CLAUDE_MESSAGES | ANTHROPIC_CLAUDE_TEXT_COMPLETIONS | MESSAGES | TEXT_COMPLETIONS`
Required: Yes

 ** assistantArn **   <a name="connect-Type-amazon-q-connect_AIPromptData-assistantArn"></a>
The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** assistantId **   <a name="connect-Type-amazon-q-connect_AIPromptData-assistantId"></a>
The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** modelId **   <a name="connect-Type-amazon-q-connect_AIPromptData-modelId"></a>
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
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** name **   <a name="connect-Type-amazon-q-connect_AIPromptData-name"></a>
The name of the AI Prompt
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: Yes

 ** templateConfiguration **   <a name="connect-Type-amazon-q-connect_AIPromptData-templateConfiguration"></a>
The configuration of the prompt template for this AI Prompt.
Type: [AIPromptTemplateConfiguration](API_amazon-q-connect_AIPromptTemplateConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** templateType **   <a name="connect-Type-amazon-q-connect_AIPromptData-templateType"></a>
The type of the prompt template for this AI Prompt.
Type: String
Valid Values: `TEXT`
Required: Yes

 ** type **   <a name="connect-Type-amazon-q-connect_AIPromptData-type"></a>
The type of this AI Prompt.
Type: String
Valid Values: `ANSWER_GENERATION | INTENT_LABELING_GENERATION | QUERY_REFORMULATION | SELF_SERVICE_PRE_PROCESSING | SELF_SERVICE_ANSWER_GENERATION | EMAIL_RESPONSE | EMAIL_OVERVIEW | EMAIL_GENERATIVE_ANSWER | EMAIL_QUERY_REFORMULATION | ORCHESTRATION | NOTE_TAKING | CASE_SUMMARIZATION`
Required: Yes

 ** visibilityStatus **   <a name="connect-Type-amazon-q-connect_AIPromptData-visibilityStatus"></a>
The visibility status of the AI Prompt.
Type: String
Valid Values: `SAVED | PUBLISHED`
Required: Yes

 ** description **   <a name="connect-Type-amazon-q-connect_AIPromptData-description"></a>
The description of the AI Prompt.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: No

 ** inferenceConfiguration **   <a name="connect-Type-amazon-q-connect_AIPromptData-inferenceConfiguration"></a>
The configuration for inference parameters when using the AI Prompt.
Type: [AIPromptInferenceConfiguration](API_amazon-q-connect_AIPromptInferenceConfiguration.md) object
Required: No

 ** modifiedTime **   <a name="connect-Type-amazon-q-connect_AIPromptData-modifiedTime"></a>
The time the AI Prompt was last modified.
Type: Timestamp
Required: No

 ** origin **   <a name="connect-Type-amazon-q-connect_AIPromptData-origin"></a>
The origin of the AI Prompt. `SYSTEM` for a default AI Prompt created by Q in Connect or `CUSTOMER` for an AI Prompt created by calling AI Prompt creation APIs.
Type: String
Valid Values: `SYSTEM | CUSTOMER`
Required: No

 ** status **   <a name="connect-Type-amazon-q-connect_AIPromptData-status"></a>
The status of the AI Prompt.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED | ACTIVE | DELETE_IN_PROGRESS | DELETE_FAILED | DELETED`
Required: No

 ** tags **   <a name="connect-Type-amazon-q-connect_AIPromptData-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_amazon-q-connect_AIPromptData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/AIPromptData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/AIPromptData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/AIPromptData)
