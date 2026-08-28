---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_ModelSummary.html
---

# ModelSummary
<a name="API_amazon-q-connect_ModelSummary"></a>

The summary of a model available to an Amazon Q in Connect assistant.

## Contents
<a name="API_amazon-q-connect_ModelSummary_Contents"></a>

 ** displayName **   <a name="connect-Type-amazon-q-connect_ModelSummary-displayName"></a>
The display name of the model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** modelId **   <a name="connect-Type-amazon-q-connect_ModelSummary-modelId"></a>
The identifier of the model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** crossRegionStatus **   <a name="connect-Type-amazon-q-connect_ModelSummary-crossRegionStatus"></a>
The cross-region availability status of the model. `NONE` indicates the model is only available in a single region, `REGIONAL` indicates the model is available through regional inference, and `GLOBAL` indicates the model is available through global cross-region inference.
Type: String
Valid Values: `NONE | REGIONAL | GLOBAL`
Required: No

 ** endOfLifeTimestamp **   <a name="connect-Type-amazon-q-connect_ModelSummary-endOfLifeTimestamp"></a>
The timestamp when the model will reach end of life and no longer be available for use.
Type: Timestamp
Required: No

 ** legacyTimestamp **   <a name="connect-Type-amazon-q-connect_ModelSummary-legacyTimestamp"></a>
The timestamp when the model lifecycle will transition from `ACTIVE` to `LEGACY`.
Type: Timestamp
Required: No

 ** modelLifecycle **   <a name="connect-Type-amazon-q-connect_ModelSummary-modelLifecycle"></a>
The current lifecycle of the model. `ACTIVE` indicates the model is recommended for use and `LEGACY` indicates the model is still usable but is deprecated.
Type: String
Valid Values: `ACTIVE | LEGACY`
Required: No

 ** supportedAIPromptTypes **   <a name="connect-Type-amazon-q-connect_ModelSummary-supportedAIPromptTypes"></a>
The list of AI Prompt types that the model supports.
Type: Array of strings
Valid Values: `ANSWER_GENERATION | INTENT_LABELING_GENERATION | QUERY_REFORMULATION | SELF_SERVICE_PRE_PROCESSING | SELF_SERVICE_ANSWER_GENERATION | EMAIL_RESPONSE | EMAIL_OVERVIEW | EMAIL_GENERATIVE_ANSWER | EMAIL_QUERY_REFORMULATION | ORCHESTRATION | NOTE_TAKING | CASE_SUMMARIZATION`
Required: No

 ** supportsPromptCaching **   <a name="connect-Type-amazon-q-connect_ModelSummary-supportsPromptCaching"></a>
Whether the model supports prompt caching.
Type: Boolean
Required: No

## See Also
<a name="API_amazon-q-connect_ModelSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/ModelSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/ModelSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/ModelSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
