---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_Recommendation.html
---

# Recommendation
<a name="API_Recommendation"></a>

Represents a recommendation with all its properties and metadata

## Contents
<a name="API_Recommendation_Contents"></a>

 ** agentSpaceArn **   <a name="devopsagent-Type-Recommendation-agentSpaceArn"></a>
ARN of the agent space this recommendation belongs to
Type: String
Required: Yes

 ** content **   <a name="devopsagent-Type-Recommendation-content"></a>
Content of the recommendation
Type: [RecommendationContent](API_RecommendationContent.md) object
Required: Yes

 ** createdAt **   <a name="devopsagent-Type-Recommendation-createdAt"></a>
Timestamp when this recommendation was created
Type: Timestamp
Required: Yes

 ** priority **   <a name="devopsagent-Type-Recommendation-priority"></a>
Priority level of the recommendation
Type: String
Valid Values: `HIGH | MEDIUM | LOW`
Required: Yes

 ** recommendationId **   <a name="devopsagent-Type-Recommendation-recommendationId"></a>
The unique identifier for this recommendation
Type: String
Required: Yes

 ** status **   <a name="devopsagent-Type-Recommendation-status"></a>
Current status of the recommendation
Type: String
Valid Values: `PROPOSED | ACCEPTED | REJECTED | CLOSED | COMPLETED | UPDATE_IN_PROGRESS`
Required: Yes

 ** taskId **   <a name="devopsagent-Type-Recommendation-taskId"></a>
ID of the task that generated the recommendation
Type: String
Required: Yes

 ** title **   <a name="devopsagent-Type-Recommendation-title"></a>
The title of the recommendation
Type: String
Required: Yes

 ** updatedAt **   <a name="devopsagent-Type-Recommendation-updatedAt"></a>
Timestamp when this recommendation was last updated
Type: Timestamp
Required: Yes

 ** version **   <a name="devopsagent-Type-Recommendation-version"></a>
Version number for optimistic locking
Type: Long
Required: Yes

 ** additionalContext **   <a name="devopsagent-Type-Recommendation-additionalContext"></a>
Additional context for recommendation
Type: String
Required: No

 ** goalId **   <a name="devopsagent-Type-Recommendation-goalId"></a>
ID of the goal this recommendation is associated with
Type: String
Required: No

 ** goalVersion **   <a name="devopsagent-Type-Recommendation-goalVersion"></a>
Version of the goal at the time this recommendation was generated
Type: Long
Required: No

 ** rankedAt **   <a name="devopsagent-Type-Recommendation-rankedAt"></a>
Timestamp when the recommendation was last ranked
Type: Timestamp
Required: No

 ** rankPosition **   <a name="devopsagent-Type-Recommendation-rankPosition"></a>
Position in ranked list (1 = highest priority)
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_Recommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/Recommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/Recommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/Recommendation)
