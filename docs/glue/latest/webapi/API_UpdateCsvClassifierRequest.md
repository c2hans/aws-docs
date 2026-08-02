---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_UpdateCsvClassifierRequest.html
---

# UpdateCsvClassifierRequest
<a name="API_UpdateCsvClassifierRequest"></a>

Specifies a custom CSV classifier to be updated.

## Contents
<a name="API_UpdateCsvClassifierRequest_Contents"></a>

 ** Name **   <a name="Glue-Type-UpdateCsvClassifierRequest-Name"></a>
The name of the classifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** AllowSingleColumn **   <a name="Glue-Type-UpdateCsvClassifierRequest-AllowSingleColumn"></a>
Enables the processing of files that contain only one column.
Type: Boolean
Required: No

 ** ContainsHeader **   <a name="Glue-Type-UpdateCsvClassifierRequest-ContainsHeader"></a>
Indicates whether the CSV file contains a header.
Type: String
Valid Values: `UNKNOWN | PRESENT | ABSENT`
Required: No

 ** CustomDatatypeConfigured **   <a name="Glue-Type-UpdateCsvClassifierRequest-CustomDatatypeConfigured"></a>
Specifies the configuration of custom datatypes.
Type: Boolean
Required: No

 ** CustomDatatypes **   <a name="Glue-Type-UpdateCsvClassifierRequest-CustomDatatypes"></a>
Specifies a list of supported custom datatypes.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Delimiter **   <a name="Glue-Type-UpdateCsvClassifierRequest-Delimiter"></a>
A custom symbol to denote what separates each column entry in the row.
Type: String
Length Constraints: Fixed length of 1.
Pattern: `[^\r\n]`
Required: No

 ** DisableValueTrimming **   <a name="Glue-Type-UpdateCsvClassifierRequest-DisableValueTrimming"></a>
Specifies not to trim values before identifying the type of column values. The default value is true.
Type: Boolean
Required: No

 ** Header **   <a name="Glue-Type-UpdateCsvClassifierRequest-Header"></a>
A list of strings representing column names.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** QuoteSymbol **   <a name="Glue-Type-UpdateCsvClassifierRequest-QuoteSymbol"></a>
A custom symbol to denote what combines content into a single column value. It must be different from the column delimiter.
Type: String
Length Constraints: Fixed length of 1.
Pattern: `[^\r\n]`
Required: No

 ** Serde **   <a name="Glue-Type-UpdateCsvClassifierRequest-Serde"></a>
Sets the SerDe for processing CSV in the classifier, which will be applied in the Data Catalog. Valid values are `OpenCSVSerDe`, `LazySimpleSerDe`, and `None`. You can specify the `None` value when you want the crawler to do the detection.
Type: String
Valid Values: `OpenCSVSerDe | LazySimpleSerDe | None`
Required: No

## See Also
<a name="API_UpdateCsvClassifierRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/UpdateCsvClassifierRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/UpdateCsvClassifierRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/UpdateCsvClassifierRequest)
