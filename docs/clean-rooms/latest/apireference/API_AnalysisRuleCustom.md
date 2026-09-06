---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_AnalysisRuleCustom.html
---

# AnalysisRuleCustom
<a name="API_AnalysisRuleCustom"></a>

A type of analysis rule that enables the table owner to approve custom SQL queries on their configured tables. It supports differential privacy, minimum aggregation thresholds, and comparison controls.

## Contents
<a name="API_AnalysisRuleCustom_Contents"></a>

 ** allowedAnalyses **   <a name="API-Type-AnalysisRuleCustom-allowedAnalyses"></a>
The ARN of the analysis templates that are allowed by the custom analysis rule.
Type: Array of strings
Array Members: Minimum number of 0 items.
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `(ANY_QUERY|ANY_JOB|arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/analysistemplate/[\d\w-]+)`
Required: Yes

 ** additionalAnalyses **   <a name="API-Type-AnalysisRuleCustom-additionalAnalyses"></a>
 An indicator as to whether additional analyses (such as AWS Clean Rooms ML) can be applied to the output of the direct query.
Type: String
Valid Values: `ALLOWED | REQUIRED | NOT_ALLOWED`
Required: No

 ** aggregationThresholds **   <a name="API-Type-AnalysisRuleCustom-aggregationThresholds"></a>
The aggregation thresholds that each query output group must satisfy. AWS Clean Rooms filters out any group that represents fewer than the specified number of distinct identities. You can specify at most one threshold. You can't use aggregation thresholds with differential privacy, or when `allowedAnalyses` allows only jobs.
Type: Array of [AggregationThreshold](API_AggregationThreshold.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** allowedAdditionalAnalyses **   <a name="API-Type-AnalysisRuleCustom-allowedAdditionalAnalyses"></a>
The list of allowed additional analyses for the custom analysis rule.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:([\d]{12}|\*):membership\/[\*\d\w-]+\/configuredaudiencemodelassociation\/[\*\d\w-]+$|^arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:([0-9]{12}|\*):membership\/[\*\d\w-]+\/configured-model-algorithm-association\/([-a-zA-Z0-9_\/.]+|\*)`
Required: No

 ** allowedAnalysisProviders **   <a name="API-Type-AnalysisRuleCustom-allowedAnalysisProviders"></a>
The IDs of the AWS accounts that are allowed to query by the custom analysis rule. Required when `allowedAnalyses` is `ANY_QUERY`.
Type: Array of strings
Array Members: Minimum number of 0 items.
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

 ** allowedResultReceivers **   <a name="API-Type-AnalysisRuleCustom-allowedResultReceivers"></a>
The list of AWS account IDs that are allowed to receive results from queries run on the configured table.
Type: Array of strings
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

 ** comparisonControls **   <a name="API-Type-AnalysisRuleCustom-comparisonControls"></a>
The controls that restrict how a query can compare the columns in the configured table. You can't use comparison controls with differential privacy, or when `allowedAnalyses` allows only jobs.
Type: [ComparisonControls](API_ComparisonControls.md) object
Required: No

 ** differentialPrivacy **   <a name="API-Type-AnalysisRuleCustom-differentialPrivacy"></a>
The differential privacy configuration.
Type: [DifferentialPrivacyConfiguration](API_DifferentialPrivacyConfiguration.md) object
Required: No

 ** disallowedOutputColumns **   <a name="API-Type-AnalysisRuleCustom-disallowedOutputColumns"></a>
 A list of columns that aren't allowed to be shown in the query output.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: No

## See Also
<a name="API_AnalysisRuleCustom_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/AnalysisRuleCustom)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/AnalysisRuleCustom)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/AnalysisRuleCustom)
