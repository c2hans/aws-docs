---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_RecommendationSet.html
---

# RecommendationSet
<a name="API_RecommendationSet"></a>

 Contains a recommendation set.

## Contents
<a name="API_RecommendationSet_Contents"></a>

 ** strategy **   <a name="migrationhubstrategy-Type-RecommendationSet-strategy"></a>
 The recommended strategy.
Type: String
Valid Values: `Rehost | Retirement | Refactor | Replatform | Retain | Relocate | Repurchase`
Required: No

 ** targetDestination **   <a name="migrationhubstrategy-Type-RecommendationSet-targetDestination"></a>
 The recommended target destination.
Type: String
Valid Values: `None specified | AWS Elastic BeanStalk | AWS Fargate | Amazon Elastic Cloud Compute (EC2) | Amazon Elastic Container Service (ECS) | Amazon Elastic Kubernetes Service (EKS) | Aurora MySQL | Aurora PostgreSQL | Amazon Relational Database Service on MySQL | Amazon Relational Database Service on PostgreSQL | Amazon DocumentDB | Amazon DynamoDB | Amazon Relational Database Service | Babelfish for Aurora PostgreSQL`
Required: No

 ** transformationTool **   <a name="migrationhubstrategy-Type-RecommendationSet-transformationTool"></a>
 The target destination for the recommendation set.
Type: [TransformationTool](API_TransformationTool.md) object
Required: No

## See Also
<a name="API_RecommendationSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/RecommendationSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/RecommendationSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/RecommendationSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
