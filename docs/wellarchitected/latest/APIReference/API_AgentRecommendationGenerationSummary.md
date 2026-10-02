---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_AgentRecommendationGenerationSummary.html
---

# AgentRecommendationGenerationSummary
<a name="API_AgentRecommendationGenerationSummary"></a>

Summary of a recommendation generation process initiated through the agent API.

## Contents
<a name="API_AgentRecommendationGenerationSummary_Contents"></a>

 ** createdAt **   <a name="wellarchitected-Type-AgentRecommendationGenerationSummary-createdAt"></a>
The timestamp when the generation was started.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="wellarchitected-Type-AgentRecommendationGenerationSummary-createdBy"></a>
The identifier of the user or system that started this generation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** id **   <a name="wellarchitected-Type-AgentRecommendationGenerationSummary-id"></a>
The unique identifier of the recommendation generation.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** profileArn **   <a name="wellarchitected-Type-AgentRecommendationGenerationSummary-profileArn"></a>
The Amazon Resource Name (ARN) of the profile used for this generation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`
Required: Yes

 ** status **   <a name="wellarchitected-Type-AgentRecommendationGenerationSummary-status"></a>
The current status of the recommendation generation.
Type: String
Valid Values: `QUEUED | IN_PROGRESS | COMPLETED | ERROR`
Required: Yes

 ** estimatedCompletionTime **   <a name="wellarchitected-Type-AgentRecommendationGenerationSummary-estimatedCompletionTime"></a>
The estimated time for the generation to complete.
Type: Timestamp
Required: No

 ** lastModifiedAt **   <a name="wellarchitected-Type-AgentRecommendationGenerationSummary-lastModifiedAt"></a>
The timestamp when the generation was last modified.
Type: Timestamp
Required: No

 ** lastModifiedBy **   <a name="wellarchitected-Type-AgentRecommendationGenerationSummary-lastModifiedBy"></a>
The identifier of the user or system that last modified this generation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** name **   <a name="wellarchitected-Type-AgentRecommendationGenerationSummary-name"></a>
The name of the recommendation generation.
Type: String
Required: No

## See Also
<a name="API_AgentRecommendationGenerationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/AgentRecommendationGenerationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/AgentRecommendationGenerationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/AgentRecommendationGenerationSummary)
