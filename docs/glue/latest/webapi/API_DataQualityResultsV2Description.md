---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataQualityResultsV2Description.html
---

# DataQualityResultsV2Description
<a name="API_DataQualityResultsV2Description"></a>

Describes a data quality result returned by `ListDataQualityResultsV2`.

## Contents
<a name="API_DataQualityResultsV2Description_Contents"></a>

 ** DataQualityEvaluationConfig **   <a name="Glue-Type-DataQualityResultsV2Description-DataQualityEvaluationConfig"></a>
The name of the data quality evaluation configuration that started the evaluation run, returned when `EvaluationRunMode` is `EVALUATION_CONFIG`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** DataSource **   <a name="Glue-Type-DataQualityResultsV2Description-DataSource"></a>
The table associated with the data quality result, if any.
Type: [DataSource](API_DataSource.md) object
Required: No

 ** Descriptors **   <a name="Glue-Type-DataQualityResultsV2Description-Descriptors"></a>
A map of user-provided descriptors that add contextual metadata and configuration to the data quality result, such as database name, table name, team, or environment.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Value Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Dimensions **   <a name="Glue-Type-DataQualityResultsV2Description-Dimensions"></a>
A map of platform-specific identifiers, such as cluster, application, workgroup, or project IDs, that identify where the data quality evaluation ran.
Type: String to string map
Map Entries: Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Value Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** EvaluationContext **   <a name="Glue-Type-DataQualityResultsV2Description-EvaluationContext"></a>
The evaluation context for the data quality result. This value identifies a specific data quality result, or a series of related results, within a run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** EvaluationRunMode **   <a name="Glue-Type-DataQualityResultsV2Description-EvaluationRunMode"></a>
How the evaluation run that produced the result started: `ON_DEMAND` for a run started by `StartDataQualityRulesetEvaluationRun`, or `EVALUATION_CONFIG` for a run started by a data quality evaluation configuration. Not returned for results that no evaluation run produced, such as results from any ETL job.
Type: String
Valid Values: `ON_DEMAND | EVALUATION_CONFIG`
Required: No

 ** ResultId **   <a name="Glue-Type-DataQualityResultsV2Description-ResultId"></a>
The unique result ID for this data quality result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** ResultPublishedOn **   <a name="Glue-Type-DataQualityResultsV2Description-ResultPublishedOn"></a>
The date and time when this data quality result was published.
Type: Timestamp
Required: No

## See Also
<a name="API_DataQualityResultsV2Description_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataQualityResultsV2Description)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataQualityResultsV2Description)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataQualityResultsV2Description)
