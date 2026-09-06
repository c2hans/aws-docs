---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DBRecommendation.html
---

# DBRecommendation
<a name="API_DBRecommendation"></a>

The recommendation for your DB instances, DB clusters, and DB parameter groups.

## Contents
<a name="API_DBRecommendation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AdditionalInfo **
Additional information about the recommendation. The information might contain markdown.
Type: String
Required: No

 ** Category **
The category of the recommendation.
Valid values:
+  `performance efficiency`
+  `security`
+  `reliability`
+  `cost optimization`
+  `operational excellence`
+  `sustainability`
Type: String
Required: No

 ** CreatedTime **
The time when the recommendation was created. For example, `2023-09-28T01:13:53.931000+00:00`.
Type: Timestamp
Required: No

 ** Description **
A detailed description of the recommendation. The description might contain markdown.
Type: String
Required: No

 ** Detection **
A short description of the issue identified for this recommendation. The description might contain markdown.
Type: String
Required: No

 ** Impact **
A short description that explains the possible impact of an issue.
Type: String
Required: No

 ** IssueDetails **
Details of the issue that caused the recommendation.
Type: [IssueDetails](API_IssueDetails.md) object
Required: No

 ** Links.member.N **
A link to documentation that provides additional information about the recommendation.
Type: Array of [DocLink](API_DocLink.md) objects
Required: No

 ** Reason **
The reason why this recommendation was created. The information might contain markdown.
Type: String
Required: No

 ** Recommendation **
A short description of the recommendation to resolve an issue. The description might contain markdown.
Type: String
Required: No

 ** RecommendationId **
The unique identifier of the recommendation.
Type: String
Required: No

 ** RecommendedActions.member.N **
A list of recommended actions.
Type: Array of [RecommendedAction](API_RecommendedAction.md) objects
Required: No

 ** ResourceArn **
The Amazon Resource Name (ARN) of the RDS resource associated with the recommendation.
Type: String
Required: No

 ** Severity **
The severity level of the recommendation. The severity level can help you decide the urgency with which to address the recommendation.
Valid values:
+  `high`
+  `medium`
+  `low`
+  `informational`
Type: String
Required: No

 ** Source **
The AWS service that generated the recommendations.
Type: String
Required: No

 ** Status **
The current status of the recommendation.
Valid values:
+  `active` - The recommendations which are ready for you to apply.
+  `pending` - The applied or scheduled recommendations which are in progress.
+  `resolved` - The recommendations which are completed.
+  `dismissed` - The recommendations that you dismissed.
Type: String
Required: No

 ** TypeDetection **
A short description of the recommendation type. The description might contain markdown.
Type: String
Required: No

 ** TypeId **
A value that indicates the type of recommendation. This value determines how the description is rendered.
Type: String
Required: No

 ** TypeRecommendation **
A short description that summarizes the recommendation to fix all the issues of the recommendation type. The description might contain markdown.
Type: String
Required: No

 ** UpdatedTime **
The time when the recommendation was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_DBRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBRecommendation)
