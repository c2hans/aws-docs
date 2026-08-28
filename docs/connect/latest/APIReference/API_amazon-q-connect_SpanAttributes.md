---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_SpanAttributes.html
---

# SpanAttributes
<a name="API_amazon-q-connect_SpanAttributes"></a>

Contextual attributes capturing operation details, LLM configuration, usage metrics, and conversation data

## Contents
<a name="API_amazon-q-connect_SpanAttributes_Contents"></a>

 ** agentId **   <a name="connect-Type-amazon-q-connect_SpanAttributes-agentId"></a>
Amazon Connect agent ID
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** aiAgentArn **   <a name="connect-Type-amazon-q-connect_SpanAttributes-aiAgentArn"></a>
AI agent ARN
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}(:[A-Z0-9_$]+){0,1}`
Required: No

 ** aiAgentId **   <a name="connect-Type-amazon-q-connect_SpanAttributes-aiAgentId"></a>
AI agent identifier
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** aiAgentInvoker **   <a name="connect-Type-amazon-q-connect_SpanAttributes-aiAgentInvoker"></a>
Entity that invoked the AI agent
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** aiAgentName **   <a name="connect-Type-amazon-q-connect_SpanAttributes-aiAgentName"></a>
AI agent name
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: No

 ** aiAgentOrchestratorUseCase **   <a name="connect-Type-amazon-q-connect_SpanAttributes-aiAgentOrchestratorUseCase"></a>
AI agent orchestrator use case
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** aiAgentType **   <a name="connect-Type-amazon-q-connect_SpanAttributes-aiAgentType"></a>
AI agent type
Type: String
Valid Values: `MANUAL_SEARCH | ANSWER_RECOMMENDATION | SELF_SERVICE | EMAIL_RESPONSE | EMAIL_OVERVIEW | EMAIL_GENERATIVE_ANSWER | ORCHESTRATION | NOTE_TAKING | CASE_SUMMARIZATION`
Required: No

 ** aiAgentVersion **   <a name="connect-Type-amazon-q-connect_SpanAttributes-aiAgentVersion"></a>
AI agent version number
Type: Integer
Required: No

 ** cacheReadInputTokens **   <a name="connect-Type-amazon-q-connect_SpanAttributes-cacheReadInputTokens"></a>
Number of input tokens that were retrieved from cache
Type: Integer
Required: No

 ** cacheWriteInputTokens **   <a name="connect-Type-amazon-q-connect_SpanAttributes-cacheWriteInputTokens"></a>
Number of input tokens that were written to cache in this request
Type: Integer
Required: No

 ** contactId **   <a name="connect-Type-amazon-q-connect_SpanAttributes-contactId"></a>
Amazon Connect contact identifier
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** errorType **   <a name="connect-Type-amazon-q-connect_SpanAttributes-errorType"></a>
Error classification if span failed (e.g., throttle, timeout)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** guardrailAssessments **   <a name="connect-Type-amazon-q-connect_SpanAttributes-guardrailAssessments"></a>
Guardrail assessments for the inference span. Absent on other span types and when no AI Guardrail is attached to the AI Agent.
Type: Array of [SpanGuardrailAssessment](API_amazon-q-connect_SpanGuardrailAssessment.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** initialContactId **   <a name="connect-Type-amazon-q-connect_SpanAttributes-initialContactId"></a>
Amazon Connect contact identifier
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** inputMessages **   <a name="connect-Type-amazon-q-connect_SpanAttributes-inputMessages"></a>
Input message collection sent to LLM
Type: Array of [SpanMessage](API_amazon-q-connect_SpanMessage.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** instanceArn **   <a name="connect-Type-amazon-q-connect_SpanAttributes-instanceArn"></a>
Amazon Connect instance ARN
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z-]+?:[a-z-]+?:[a-z0-9-]*?:([0-9]{12})?:[a-zA-Z0-9-:/]+`
Required: No

 ** operationName **   <a name="connect-Type-amazon-q-connect_SpanAttributes-operationName"></a>
Action being performed
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** outputMessages **   <a name="connect-Type-amazon-q-connect_SpanAttributes-outputMessages"></a>
Output message collection received from LLM
Type: Array of [SpanMessage](API_amazon-q-connect_SpanMessage.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** promptArn **   <a name="connect-Type-amazon-q-connect_SpanAttributes-promptArn"></a>
AI prompt ARN
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}(:[A-Z0-9_$]+){0,1}`
Required: No

 ** promptId **   <a name="connect-Type-amazon-q-connect_SpanAttributes-promptId"></a>
AI prompt identifier
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** promptName **   <a name="connect-Type-amazon-q-connect_SpanAttributes-promptName"></a>
AI prompt name
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: No

 ** promptType **   <a name="connect-Type-amazon-q-connect_SpanAttributes-promptType"></a>
AI prompt type
Type: String
Valid Values: `ANSWER_GENERATION | INTENT_LABELING_GENERATION | QUERY_REFORMULATION | SELF_SERVICE_PRE_PROCESSING | SELF_SERVICE_ANSWER_GENERATION | EMAIL_RESPONSE | EMAIL_OVERVIEW | EMAIL_GENERATIVE_ANSWER | EMAIL_QUERY_REFORMULATION | ORCHESTRATION | NOTE_TAKING | CASE_SUMMARIZATION`
Required: No

 ** promptVersion **   <a name="connect-Type-amazon-q-connect_SpanAttributes-promptVersion"></a>
AI prompt version number
Type: Integer
Required: No

 ** providerName **   <a name="connect-Type-amazon-q-connect_SpanAttributes-providerName"></a>
Model provider identifier (e.g., aws.bedrock)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** requestMaxTokens **   <a name="connect-Type-amazon-q-connect_SpanAttributes-requestMaxTokens"></a>
Maximum tokens configured for generation
Type: Integer
Required: No

 ** requestModel **   <a name="connect-Type-amazon-q-connect_SpanAttributes-requestModel"></a>
LLM model ID for request (e.g., anthropic.claude-3-sonnet)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** responseFinishReasons **   <a name="connect-Type-amazon-q-connect_SpanAttributes-responseFinishReasons"></a>
Generation termination reasons (e.g., stop, max\_tokens)
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** responseModel **   <a name="connect-Type-amazon-q-connect_SpanAttributes-responseModel"></a>
Actual model used for response (usually matches requestModel)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** sessionName **   <a name="connect-Type-amazon-q-connect_SpanAttributes-sessionName"></a>
Session name
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** systemInstructions **   <a name="connect-Type-amazon-q-connect_SpanAttributes-systemInstructions"></a>
System prompt instructions
Type: Array of [SpanMessageValue](API_amazon-q-connect_SpanMessageValue.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** temperature **   <a name="connect-Type-amazon-q-connect_SpanAttributes-temperature"></a>
Sampling temperature for generation
Type: Float
Valid Range: Minimum value of 0.0. Maximum value of 1.0.
Required: No

 ** timeToFirstTokenMs **   <a name="connect-Type-amazon-q-connect_SpanAttributes-timeToFirstTokenMs"></a>
Time to first token in milliseconds, measured from when Amazon Bedrock was invoked to when the first token was returned
Type: Integer
Required: No

 ** topP **   <a name="connect-Type-amazon-q-connect_SpanAttributes-topP"></a>
Top-p sampling parameter for generation
Type: Float
Valid Range: Minimum value of 0.0. Maximum value of 1.0.
Required: No

 ** usageInputTokens **   <a name="connect-Type-amazon-q-connect_SpanAttributes-usageInputTokens"></a>
Number of input tokens in prompt
Type: Integer
Required: No

 ** usageOutputTokens **   <a name="connect-Type-amazon-q-connect_SpanAttributes-usageOutputTokens"></a>
Number of output tokens in response
Type: Integer
Required: No

 ** usageTotalTokens **   <a name="connect-Type-amazon-q-connect_SpanAttributes-usageTotalTokens"></a>
Total tokens consumed (input \+ output)
Type: Integer
Required: No

## See Also
<a name="API_amazon-q-connect_SpanAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/SpanAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/SpanAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/SpanAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
