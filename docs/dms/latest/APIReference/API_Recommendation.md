---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_Recommendation.html
---

# Recommendation
<a name="API_Recommendation"></a>

Provides information that describes a recommendation of a target engine.

A *recommendation* is a set of possible AWS target engines that you can choose to migrate your source on-premises database. In this set, Fleet Advisor suggests a single target engine as the right sized migration destination. To determine this rightsized migration destination, Fleet Advisor uses the inventory metadata and metrics from data collector. You can use recommendations before the start of migration to save costs and reduce risks.

With recommendations, you can explore different target options and compare metrics, so you can make an informed decision when you choose the migration target.

## Contents
<a name="API_Recommendation_Contents"></a>

 ** CreatedDate **   <a name="DMS-Type-Recommendation-CreatedDate"></a>
The date when Fleet Advisor created the target engine recommendation.
Type: String
Required: No

 ** Data **   <a name="DMS-Type-Recommendation-Data"></a>
The recommendation of a target engine for the specified source database.
Type: [RecommendationData](API_RecommendationData.md) object
Required: No

 ** DatabaseId **   <a name="DMS-Type-Recommendation-DatabaseId"></a>
The identifier of the source database for which Fleet Advisor provided this recommendation.
Type: String
Required: No

 ** EngineName **   <a name="DMS-Type-Recommendation-EngineName"></a>
The name of the target engine. Valid values include `"rds-aurora-mysql"`, `"rds-aurora-postgresql"`, `"rds-mysql"`, `"rds-oracle"`, `"rds-sql-server"`, and `"rds-postgresql"`.
Type: String
Required: No

 ** Preferred **   <a name="DMS-Type-Recommendation-Preferred"></a>
Indicates that this target is the rightsized migration destination.
Type: Boolean
Required: No

 ** Settings **   <a name="DMS-Type-Recommendation-Settings"></a>
The settings in JSON format for the preferred target engine parameters. These parameters include capacity, resource utilization, and the usage type (production, development, or testing).
Type: [RecommendationSettings](API_RecommendationSettings.md) object
Required: No

 ** Status **   <a name="DMS-Type-Recommendation-Status"></a>
The status of the target engine recommendation. Valid values include `"alternate"`, `"in-progress"`, `"not-viable"`, and `"recommended"`.
Type: String
Required: No

## See Also
<a name="API_Recommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/Recommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/Recommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/Recommendation)
