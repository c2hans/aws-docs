---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_Recommendation.html
---

# Recommendation
<a name="API_Recommendation"></a>

An Amazon Redshift Advisor recommended action on the Amazon Redshift cluster.

## Contents
<a name="API_Recommendation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ClusterIdentifier **
The unique identifier of the cluster for which the recommendation is returned.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** CreatedAt **
The date and time (UTC) that the recommendation was created.
Type: Timestamp
Required: No

 ** Description **
The description of the recommendation.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** Id **
A unique identifier of the Advisor recommendation.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** ImpactRanking **
The scale of the impact that the Advisor recommendation has to the performance and cost of the cluster.
Type: String
Valid Values: `HIGH | MEDIUM | LOW`
Required: No

 ** NamespaceArn **
The Amazon Redshift cluster namespace ARN for which the recommendations is returned.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** Observation **
The description of what was observed about your cluster.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** RecommendationText **
The description of the recommendation.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** RecommendationType **
The type of Advisor recommendation.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** RecommendedActions.RecommendedAction.N **
List of Amazon Redshift recommended actions.
Type: Array of [RecommendedAction](API_RecommendedAction.md) objects
Required: No

 ** ReferenceLinks.ReferenceLink.N **
List of helpful links for more information about the Advisor recommendation.
Type: Array of [ReferenceLink](API_ReferenceLink.md) objects
Required: No

 ** Title **
The title of the recommendation.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

## See Also
<a name="API_Recommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/Recommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/Recommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/Recommendation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
