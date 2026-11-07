---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataQualityResultsV2FilterCriteria.html
---

# DataQualityResultsV2FilterCriteria
<a name="API_DataQualityResultsV2FilterCriteria"></a>

Describes the criteria used to filter the data quality results returned by `ListDataQualityResultsV2`.

## Contents
<a name="API_DataQualityResultsV2FilterCriteria_Contents"></a>

 ** DataSource **   <a name="Glue-Type-DataQualityResultsV2FilterCriteria-DataSource"></a>
The data source used to filter the results. For example, you can retrieve all results for an AWS Glue table. `DatabaseName` and `TableName` are required. If you omit `CatalogId`, the catalog of the calling account is used.
When you filter by data source, a page of results can be empty but still include a `NextToken`. Keep requesting pages until `NextToken` is absent.
Type: [DataSource](API_DataSource.md) object
Required: No

 ** Dimensions **   <a name="Glue-Type-DataQualityResultsV2FilterCriteria-Dimensions"></a>
The platform dimensions to filter results by.
Type: String to string map
Map Entries: Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Value Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** EvaluationContext **   <a name="Glue-Type-DataQualityResultsV2FilterCriteria-EvaluationContext"></a>
The evaluation context to filter results by.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** PublishedAfter **   <a name="Glue-Type-DataQualityResultsV2FilterCriteria-PublishedAfter"></a>
The time after which to include published results.
Type: Timestamp
Required: No

 ** PublishedBefore **   <a name="Glue-Type-DataQualityResultsV2FilterCriteria-PublishedBefore"></a>
The time before which to include published results.
Type: Timestamp
Required: No

## See Also
<a name="API_DataQualityResultsV2FilterCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataQualityResultsV2FilterCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataQualityResultsV2FilterCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataQualityResultsV2FilterCriteria)
