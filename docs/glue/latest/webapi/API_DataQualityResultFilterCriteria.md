---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataQualityResultFilterCriteria.html
---

# DataQualityResultFilterCriteria
<a name="API_DataQualityResultFilterCriteria"></a>

Criteria used to return data quality results.

## Contents
<a name="API_DataQualityResultFilterCriteria_Contents"></a>

 ** DataSource **   <a name="Glue-Type-DataQualityResultFilterCriteria-DataSource"></a>
Filter results by the specified data source. For example, retrieving all results for an AWS Glue table.
Type: [DataSource](API_DataSource.md) object
Required: No

 ** JobName **   <a name="Glue-Type-DataQualityResultFilterCriteria-JobName"></a>
Filter results by the specified job name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** JobRunId **   <a name="Glue-Type-DataQualityResultFilterCriteria-JobRunId"></a>
Filter results by the specified job run ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** StartedAfter **   <a name="Glue-Type-DataQualityResultFilterCriteria-StartedAfter"></a>
Filter results by runs that started after this time.
Type: Timestamp
Required: No

 ** StartedBefore **   <a name="Glue-Type-DataQualityResultFilterCriteria-StartedBefore"></a>
Filter results by runs that started before this time.
Type: Timestamp
Required: No

## See Also
<a name="API_DataQualityResultFilterCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataQualityResultFilterCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataQualityResultFilterCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataQualityResultFilterCriteria)
