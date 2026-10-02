---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_AgentRecommendationSummary.html
---

# AgentRecommendationSummary
<a name="API_AgentRecommendationSummary"></a>

Summary of an agent optimization recommendation returned by list operations.

## Contents
<a name="API_AgentRecommendationSummary_Contents"></a>

 ** createdAt **   <a name="wellarchitected-Type-AgentRecommendationSummary-createdAt"></a>
The timestamp when the recommendation was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="wellarchitected-Type-AgentRecommendationSummary-createdBy"></a>
The identifier of the user or system that created this recommendation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** description **   <a name="wellarchitected-Type-AgentRecommendationSummary-description"></a>
A description of the recommendation.
Type: String
Length Constraints: Minimum length of 80. Maximum length of 500.
Required: Yes

 ** effort **   <a name="wellarchitected-Type-AgentRecommendationSummary-effort"></a>
The effort required to implement the recommendation.
Type: String
Valid Values: `LARGE | MEDIUM | SMALL`
Required: Yes

 ** impact **   <a name="wellarchitected-Type-AgentRecommendationSummary-impact"></a>
The severity of the recommendation's impact.
Type: String
Valid Values: `HIGH | MEDIUM | LOW`
Required: Yes

 ** pillar **   <a name="wellarchitected-Type-AgentRecommendationSummary-pillar"></a>
The AWS Well-Architected Framework pillar that the recommendation addresses.
Type: String
Valid Values: `COST_OPTIMIZATION | SECURITY | RESILIENCE | PERFORMANCE | OPERATIONAL_EXCELLENCE`
Required: Yes

 ** priority **   <a name="wellarchitected-Type-AgentRecommendationSummary-priority"></a>
The priority of the recommendation.
Type: String
Valid Values: `HIGH | MEDIUM | LOW`
Required: Yes

 ** profileArn **   <a name="wellarchitected-Type-AgentRecommendationSummary-profileArn"></a>
The Amazon Resource Name (ARN) of the associated profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`
Required: Yes

 ** recommendationArn **   <a name="wellarchitected-Type-AgentRecommendationSummary-recommendationArn"></a>
The Amazon Resource Name (ARN) of the recommendation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-recommendation/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** roi **   <a name="wellarchitected-Type-AgentRecommendationSummary-roi"></a>
The return on investment estimate for the recommendation.
Type: [Roi](API_Roi.md) object
Required: Yes

 ** state **   <a name="wellarchitected-Type-AgentRecommendationSummary-state"></a>
The current state of the recommendation.
Type: String
Valid Values: `OPEN | CLOSED`
Required: Yes

 ** status **   <a name="wellarchitected-Type-AgentRecommendationSummary-status"></a>
The current status of the recommendation.
Type: String
Valid Values: `ACTIVE | SUPPRESSED | COMPLETED`
Required: Yes

 ** title **   <a name="wellarchitected-Type-AgentRecommendationSummary-title"></a>
The title of the recommendation.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 120.
Required: Yes

 ** type **   <a name="wellarchitected-Type-AgentRecommendationSummary-type"></a>
The type of the recommendation.
Type: String
Valid Values: `RESOURCE | ARCHITECTURE | APPLICATION`
Required: Yes

 ** applications **   <a name="wellarchitected-Type-AgentRecommendationSummary-applications"></a>
The applications that the recommendation targets.
Type: Array of strings
Required: No

 ** awsServices **   <a name="wellarchitected-Type-AgentRecommendationSummary-awsServices"></a>
The AWS services that the recommendation applies to.
Type: Array of strings
Required: No

 ** businessUnits **   <a name="wellarchitected-Type-AgentRecommendationSummary-businessUnits"></a>
The business units that own the affected resources.
Type: Array of strings
Required: No

 ** generationId **   <a name="wellarchitected-Type-AgentRecommendationSummary-generationId"></a>
The identifier of the generation that produced this recommendation.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** lastModifiedAt **   <a name="wellarchitected-Type-AgentRecommendationSummary-lastModifiedAt"></a>
The timestamp when the recommendation was last modified.
Type: Timestamp
Required: No

 ** lastModifiedBy **   <a name="wellarchitected-Type-AgentRecommendationSummary-lastModifiedBy"></a>
The identifier of the user or system that last modified this recommendation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** numberOfResources **   <a name="wellarchitected-Type-AgentRecommendationSummary-numberOfResources"></a>
The number of AWS resources this recommendation affects.
Type: Integer
Required: No

 ** updateReason **   <a name="wellarchitected-Type-AgentRecommendationSummary-updateReason"></a>
The free-text reason associated with the recommendation's most recent status update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_AgentRecommendationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/AgentRecommendationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/AgentRecommendationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/AgentRecommendationSummary)
