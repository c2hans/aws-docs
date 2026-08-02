---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataQualityResultDescription.html
---

# DataQualityResultDescription
<a name="API_DataQualityResultDescription"></a>

Describes a data quality result.

## Contents
<a name="API_DataQualityResultDescription_Contents"></a>

 ** DataSource **   <a name="Glue-Type-DataQualityResultDescription-DataSource"></a>
The table name associated with the data quality result.
Type: [DataSource](API_DataSource.md) object
Required: No

 ** JobName **   <a name="Glue-Type-DataQualityResultDescription-JobName"></a>
The job name associated with the data quality result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** JobRunId **   <a name="Glue-Type-DataQualityResultDescription-JobRunId"></a>
The job run ID associated with the data quality result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** ResultId **   <a name="Glue-Type-DataQualityResultDescription-ResultId"></a>
The unique result ID for this data quality result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** StartedOn **   <a name="Glue-Type-DataQualityResultDescription-StartedOn"></a>
The time that the run started for this data quality result.
Type: Timestamp
Required: No

## See Also
<a name="API_DataQualityResultDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataQualityResultDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataQualityResultDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataQualityResultDescription)
