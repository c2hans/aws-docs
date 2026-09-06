---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_IntermediateTableAnalysisRuleCustom.html
---

# IntermediateTableAnalysisRuleCustom
<a name="API_IntermediateTableAnalysisRuleCustom"></a>

Contains the custom analysis rule configuration for an intermediate table.

## Contents
<a name="API_IntermediateTableAnalysisRuleCustom_Contents"></a>

 ** additionalAnalyses **   <a name="API-Type-IntermediateTableAnalysisRuleCustom-additionalAnalyses"></a>
The setting that controls whether additional analyses are allowed on the intermediate table.
Type: String
Valid Values: `ALLOWED | REQUIRED | NOT_ALLOWED`
Required: No

 ** aggregationThresholds **   <a name="API-Type-IntermediateTableAnalysisRuleCustom-aggregationThresholds"></a>
The aggregation thresholds that each query output group must satisfy. AWS Clean Rooms filters out any group that represents fewer than the specified number of distinct identities. You can specify at most one threshold. You can't use aggregation thresholds with differential privacy, or when `allowedAnalyses` allows only jobs.
Type: Array of [AggregationThreshold](API_AggregationThreshold.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** allowedAdditionalAnalyses **   <a name="API-Type-IntermediateTableAnalysisRuleCustom-allowedAdditionalAnalyses"></a>
The list of allowed additional analyses for the intermediate table.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:([\d]{12}|\*):membership\/[\*\d\w-]+\/configuredaudiencemodelassociation\/[\*\d\w-]+$|^arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:([0-9]{12}|\*):membership\/[\*\d\w-]+\/configured-model-algorithm-association\/([-a-zA-Z0-9_\/.]+|\*)`
Required: No

 ** allowedAnalyses **   <a name="API-Type-IntermediateTableAnalysisRuleCustom-allowedAnalyses"></a>
The list of allowed analyses that can be performed on the intermediate table.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `(ANY_QUERY|ANY_JOB|arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/analysistemplate/[\d\w-]+)`
Required: No

 ** allowedAnalysisProviders **   <a name="API-Type-IntermediateTableAnalysisRuleCustom-allowedAnalysisProviders"></a>
The list of AWS account IDs for the allowed analysis providers.
Type: Array of strings
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

 ** allowedResultReceivers **   <a name="API-Type-IntermediateTableAnalysisRuleCustom-allowedResultReceivers"></a>
The list of AWS account IDs that are allowed to receive results from queries run on the intermediate table.
Type: Array of strings
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

 ** comparisonControls **   <a name="API-Type-IntermediateTableAnalysisRuleCustom-comparisonControls"></a>
The controls that restrict how a query can compare the columns in the intermediate table. You can't use comparison controls with differential privacy, or when `allowedAnalyses` allows only jobs.
Type: [ComparisonControls](API_ComparisonControls.md) object
Required: No

 ** differentialPrivacy **   <a name="API-Type-IntermediateTableAnalysisRuleCustom-differentialPrivacy"></a>
Specifies the unique identifier for your users.
Type: [DifferentialPrivacyConfiguration](API_DifferentialPrivacyConfiguration.md) object
Required: No

 ** disallowedOutputColumns **   <a name="API-Type-IntermediateTableAnalysisRuleCustom-disallowedOutputColumns"></a>
The list of columns that are not allowed in the query output.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: No

## See Also
<a name="API_IntermediateTableAnalysisRuleCustom_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/IntermediateTableAnalysisRuleCustom)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/IntermediateTableAnalysisRuleCustom)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/IntermediateTableAnalysisRuleCustom)
