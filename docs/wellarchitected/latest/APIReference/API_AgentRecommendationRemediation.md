---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_AgentRecommendationRemediation.html
---

# AgentRecommendationRemediation
<a name="API_AgentRecommendationRemediation"></a>

The core fields for a remediation.

## Contents
<a name="API_AgentRecommendationRemediation_Contents"></a>

 ** createdAt **   <a name="wellarchitected-Type-AgentRecommendationRemediation-createdAt"></a>
The timestamp when the remediation was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="wellarchitected-Type-AgentRecommendationRemediation-createdBy"></a>
The identifier of the user or system that created this remediation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** recommendationArn **   <a name="wellarchitected-Type-AgentRecommendationRemediation-recommendationArn"></a>
The ARN of the recommendation that this remediation belongs to.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-recommendation/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** steps **   <a name="wellarchitected-Type-AgentRecommendationRemediation-steps"></a>
The procedural steps to perform the remediation.
Type: Array of [RemediationStep](API_RemediationStep.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** type **   <a name="wellarchitected-Type-AgentRecommendationRemediation-type"></a>
The remediation method.
Type: String
Valid Values: `AUTO_REMEDIATION | CONSOLE | CLI | SDK | IAC | MCP`
Required: Yes

 ** lastModifiedAt **   <a name="wellarchitected-Type-AgentRecommendationRemediation-lastModifiedAt"></a>
The timestamp when the remediation was last modified.
Type: Timestamp
Required: No

 ** lastModifiedBy **   <a name="wellarchitected-Type-AgentRecommendationRemediation-lastModifiedBy"></a>
The identifier of the user or system that last modified this remediation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** resourceLinks **   <a name="wellarchitected-Type-AgentRecommendationRemediation-resourceLinks"></a>
External references associated with the steps.
Type: Array of [ResourceLink](API_ResourceLink.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_AgentRecommendationRemediation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/AgentRecommendationRemediation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/AgentRecommendationRemediation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/AgentRecommendationRemediation)
