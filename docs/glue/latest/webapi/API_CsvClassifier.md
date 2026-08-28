---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CsvClassifier.html
---

# CsvClassifier
<a name="API_CsvClassifier"></a>

A classifier for custom `CSV` content.

## Contents
<a name="API_CsvClassifier_Contents"></a>

 ** Name **   <a name="Glue-Type-CsvClassifier-Name"></a>
The name of the classifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** AllowSingleColumn **   <a name="Glue-Type-CsvClassifier-AllowSingleColumn"></a>
Enables the processing of files that contain only one column.
Type: Boolean
Required: No

 ** ContainsHeader **   <a name="Glue-Type-CsvClassifier-ContainsHeader"></a>
Indicates whether the CSV file contains a header.
Type: String
Valid Values: `UNKNOWN | PRESENT | ABSENT`
Required: No

 ** CreationTime **   <a name="Glue-Type-CsvClassifier-CreationTime"></a>
The time that this classifier was registered.
Type: Timestamp
Required: No

 ** CustomDatatypeConfigured **   <a name="Glue-Type-CsvClassifier-CustomDatatypeConfigured"></a>
Enables the custom datatype to be configured.
Type: Boolean
Required: No

 ** CustomDatatypes **   <a name="Glue-Type-CsvClassifier-CustomDatatypes"></a>
A list of custom datatypes including "BINARY", "BOOLEAN", "DATE", "DECIMAL", "DOUBLE", "FLOAT", "INT", "LONG", "SHORT", "STRING", "TIMESTAMP".
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Delimiter **   <a name="Glue-Type-CsvClassifier-Delimiter"></a>
A custom symbol to denote what separates each column entry in the row.
Type: String
Length Constraints: Fixed length of 1.
Pattern: `[^\r\n]`
Required: No

 ** DisableValueTrimming **   <a name="Glue-Type-CsvClassifier-DisableValueTrimming"></a>
Specifies not to trim values before identifying the type of column values. The default value is `true`.
Type: Boolean
Required: No

 ** Header **   <a name="Glue-Type-CsvClassifier-Header"></a>
A list of strings representing column names.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** LastUpdated **   <a name="Glue-Type-CsvClassifier-LastUpdated"></a>
The time that this classifier was last updated.
Type: Timestamp
Required: No

 ** QuoteSymbol **   <a name="Glue-Type-CsvClassifier-QuoteSymbol"></a>
A custom symbol to denote what combines content into a single column value. It must be different from the column delimiter.
Type: String
Length Constraints: Fixed length of 1.
Pattern: `[^\r\n]`
Required: No

 ** Serde **   <a name="Glue-Type-CsvClassifier-Serde"></a>
Sets the SerDe for processing CSV in the classifier, which will be applied in the Data Catalog. Valid values are `OpenCSVSerDe`, `LazySimpleSerDe`, and `None`. You can specify the `None` value when you want the crawler to do the detection.
Type: String
Valid Values: `OpenCSVSerDe | LazySimpleSerDe | None`
Required: No

 ** Version **   <a name="Glue-Type-CsvClassifier-Version"></a>
The version of this classifier.
Type: Long
Required: No

## See Also
<a name="API_CsvClassifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CsvClassifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CsvClassifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CsvClassifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
