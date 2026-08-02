---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ConfiguredTableSummary.html
---

# ConfiguredTableSummary
<a name="API_ConfiguredTableSummary"></a>

The configured table summary for the objects listed by the request.

## Contents
<a name="API_ConfiguredTableSummary_Contents"></a>

 ** analysisMethod **   <a name="API-Type-ConfiguredTableSummary-analysisMethod"></a>
The analysis method for the configured tables.
 `DIRECT_QUERY` allows SQL queries to be run directly on this table.
 `DIRECT_JOB` allows PySpark jobs to be run directly on this table.
 `MULTIPLE` allows both SQL queries and PySpark jobs to be run directly on this table.
Type: String
Valid Values: `DIRECT_QUERY | DIRECT_JOB | MULTIPLE`
Required: Yes

 ** analysisRuleTypes **   <a name="API-Type-ConfiguredTableSummary-analysisRuleTypes"></a>
The types of analysis rules associated with this configured table.
Type: Array of strings
Valid Values: `AGGREGATION | LIST | CUSTOM`
Required: Yes

 ** arn **   <a name="API-Type-ConfiguredTableSummary-arn"></a>
The unique ARN of the configured table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:configuredtable/[\d\w-]+`
Required: Yes

 ** createTime **   <a name="API-Type-ConfiguredTableSummary-createTime"></a>
The time the configured table was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="API-Type-ConfiguredTableSummary-id"></a>
The unique ID of the configured table.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="API-Type-ConfiguredTableSummary-name"></a>
The name of the configured table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** updateTime **   <a name="API-Type-ConfiguredTableSummary-updateTime"></a>
The time the configured table was last updated.
Type: Timestamp
Required: Yes

 ** selectedAnalysisMethods **   <a name="API-Type-ConfiguredTableSummary-selectedAnalysisMethods"></a>
 The selected analysis methods for the configured table summary.
Type: Array of strings
Valid Values: `DIRECT_QUERY | DIRECT_JOB`
Required: No

## See Also
<a name="API_ConfiguredTableSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ConfiguredTableSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ConfiguredTableSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ConfiguredTableSummary)
