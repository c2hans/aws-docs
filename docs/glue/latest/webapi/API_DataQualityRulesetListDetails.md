---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataQualityRulesetListDetails.html
---

# DataQualityRulesetListDetails
<a name="API_DataQualityRulesetListDetails"></a>

Describes a data quality ruleset returned by `GetDataQualityRuleset`.

## Contents
<a name="API_DataQualityRulesetListDetails_Contents"></a>

 ** CreatedOn **   <a name="Glue-Type-DataQualityRulesetListDetails-CreatedOn"></a>
The date and time the data quality ruleset was created.
Type: Timestamp
Required: No

 ** Description **   <a name="Glue-Type-DataQualityRulesetListDetails-Description"></a>
A description of the data quality ruleset.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** LastModifiedOn **   <a name="Glue-Type-DataQualityRulesetListDetails-LastModifiedOn"></a>
The date and time the data quality ruleset was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="Glue-Type-DataQualityRulesetListDetails-Name"></a>
The name of the data quality ruleset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** RecommendationRunId **   <a name="Glue-Type-DataQualityRulesetListDetails-RecommendationRunId"></a>
When a ruleset was created from a recommendation run, this run ID is generated to link the two together.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** RuleCount **   <a name="Glue-Type-DataQualityRulesetListDetails-RuleCount"></a>
The number of rules in the ruleset.
Type: Integer
Required: No

 ** TargetTable **   <a name="Glue-Type-DataQualityRulesetListDetails-TargetTable"></a>
An object representing an AWS Glue table.
Type: [DataQualityTargetTable](API_DataQualityTargetTable.md) object
Required: No

## See Also
<a name="API_DataQualityRulesetListDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataQualityRulesetListDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataQualityRulesetListDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataQualityRulesetListDetails)
