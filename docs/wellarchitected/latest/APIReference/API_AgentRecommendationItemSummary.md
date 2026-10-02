---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_AgentRecommendationItemSummary.html
---

# AgentRecommendationItemSummary
<a name="API_AgentRecommendationItemSummary"></a>

Summary of an agent recommendation item, representing an AWS resource or recommendation affected by the optimization recommendation.

## Contents
<a name="API_AgentRecommendationItemSummary_Contents"></a>

 ** createdAt **   <a name="wellarchitected-Type-AgentRecommendationItemSummary-createdAt"></a>
The timestamp when the recommendation item was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="wellarchitected-Type-AgentRecommendationItemSummary-createdBy"></a>
The identifier of the user or system that created this recommendation item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** id **   <a name="wellarchitected-Type-AgentRecommendationItemSummary-id"></a>
The unique identifier of the recommendation item.
Type: String
Required: Yes

 ** metadata **   <a name="wellarchitected-Type-AgentRecommendationItemSummary-metadata"></a>
Metadata containing a snapshot of the resource or recommendation at the time of generation.
Type: JSON value
Required: Yes

 ** recommendationArn **   <a name="wellarchitected-Type-AgentRecommendationItemSummary-recommendationArn"></a>
The Amazon Resource Name (ARN) of the associated recommendation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-recommendation/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** type **   <a name="wellarchitected-Type-AgentRecommendationItemSummary-type"></a>
The type of the recommendation item.
Type: String
Valid Values: `AWS_RESOURCE | RECOMMENDATION`
Required: Yes

 ** autoRemediation **   <a name="wellarchitected-Type-AgentRecommendationItemSummary-autoRemediation"></a>
The optional per-resource auto-remediation for this affected resource, representing an SSM runbook execution. Present only when the item's check is backed by an SSM automation runbook.
Type: [AutoRemediation](API_AutoRemediation.md) object
Required: No

 ** lastModifiedAt **   <a name="wellarchitected-Type-AgentRecommendationItemSummary-lastModifiedAt"></a>
The timestamp when the recommendation item was last modified.
Type: Timestamp
Required: No

 ** lastModifiedBy **   <a name="wellarchitected-Type-AgentRecommendationItemSummary-lastModifiedBy"></a>
The identifier of the user or system that last modified this recommendation item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_AgentRecommendationItemSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/AgentRecommendationItemSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/AgentRecommendationItemSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/AgentRecommendationItemSummary)
