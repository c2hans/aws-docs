---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataQualityRulesetFilterCriteria.html
---

# DataQualityRulesetFilterCriteria
<a name="API_DataQualityRulesetFilterCriteria"></a>

The criteria used to filter data quality rulesets.

## Contents
<a name="API_DataQualityRulesetFilterCriteria_Contents"></a>

 ** CreatedAfter **   <a name="Glue-Type-DataQualityRulesetFilterCriteria-CreatedAfter"></a>
Filter on rulesets created after this date.
Type: Timestamp
Required: No

 ** CreatedBefore **   <a name="Glue-Type-DataQualityRulesetFilterCriteria-CreatedBefore"></a>
Filter on rulesets created before this date.
Type: Timestamp
Required: No

 ** Description **   <a name="Glue-Type-DataQualityRulesetFilterCriteria-Description"></a>
The description of the ruleset filter criteria.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** LastModifiedAfter **   <a name="Glue-Type-DataQualityRulesetFilterCriteria-LastModifiedAfter"></a>
Filter on rulesets last modified after this date.
Type: Timestamp
Required: No

 ** LastModifiedBefore **   <a name="Glue-Type-DataQualityRulesetFilterCriteria-LastModifiedBefore"></a>
Filter on rulesets last modified before this date.
Type: Timestamp
Required: No

 ** Name **   <a name="Glue-Type-DataQualityRulesetFilterCriteria-Name"></a>
The name of the ruleset filter criteria.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** TargetTable **   <a name="Glue-Type-DataQualityRulesetFilterCriteria-TargetTable"></a>
The name and database name of the target table.
Type: [DataQualityTargetTable](API_DataQualityTargetTable.md) object
Required: No

## See Also
<a name="API_DataQualityRulesetFilterCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataQualityRulesetFilterCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataQualityRulesetFilterCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataQualityRulesetFilterCriteria)
