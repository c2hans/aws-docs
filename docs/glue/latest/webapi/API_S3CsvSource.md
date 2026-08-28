---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_S3CsvSource.html
---

# S3CsvSource
<a name="API_S3CsvSource"></a>

Specifies a command-separated value (CSV) data store stored in Amazon S3.

## Contents
<a name="API_S3CsvSource_Contents"></a>

 ** Name **   <a name="Glue-Type-S3CsvSource-Name"></a>
The name of the data store.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Paths **   <a name="Glue-Type-S3CsvSource-Paths"></a>
A list of the Amazon S3 paths to read from.
Type: Array of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** QuoteChar **   <a name="Glue-Type-S3CsvSource-QuoteChar"></a>
Specifies the character to use for quoting. The default is a double quote: `'"'`. Set this to `-1` to turn off quoting entirely.
Type: String
Valid Values: `quote | quillemet | single_quote | disabled`
Required: Yes

 ** Separator **   <a name="Glue-Type-S3CsvSource-Separator"></a>
Specifies the delimiter character. The default is a comma: ",", but any other character can be specified.
Type: String
Valid Values: `comma | ctrla | pipe | semicolon | tab`
Required: Yes

 ** AdditionalOptions **   <a name="Glue-Type-S3CsvSource-AdditionalOptions"></a>
Specifies additional connection options.
Type: [S3DirectSourceAdditionalOptions](API_S3DirectSourceAdditionalOptions.md) object
Required: No

 ** CompressionType **   <a name="Glue-Type-S3CsvSource-CompressionType"></a>
Specifies how the data is compressed. This is generally not necessary if the data has a standard file extension. Possible values are `"gzip"` and `"bzip"`).
Type: String
Valid Values: `gzip | bzip2`
Required: No

 ** Escaper **   <a name="Glue-Type-S3CsvSource-Escaper"></a>
Specifies a character to use for escaping. This option is used only when reading CSV files. The default value is `none`. If enabled, the character which immediately follows is used as-is, except for a small set of well-known escapes (`\n`, `\r`, `\t`, and `\0`).
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** Exclusions **   <a name="Glue-Type-S3CsvSource-Exclusions"></a>
A string containing a JSON list of Unix-style glob patterns to exclude. For example, "[\\"\*\*.pdf\\"]" excludes all PDF files.
Type: Array of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** GroupFiles **   <a name="Glue-Type-S3CsvSource-GroupFiles"></a>
Grouping files is turned on by default when the input contains more than 50,000 files. To turn on grouping with fewer than 50,000 files, set this parameter to "inPartition". To disable grouping when there are more than 50,000 files, set this parameter to `"none"`.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** GroupSize **   <a name="Glue-Type-S3CsvSource-GroupSize"></a>
The target group size in bytes. The default is computed based on the input data size and the size of your cluster. When there are fewer than 50,000 input files, `"groupFiles"` must be set to `"inPartition"` for this to take effect.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** MaxBand **   <a name="Glue-Type-S3CsvSource-MaxBand"></a>
This option controls the duration in milliseconds after which the s3 listing is likely to be consistent. Files with modification timestamps falling within the last maxBand milliseconds are tracked specially when using JobBookmarks to account for Amazon S3 eventual consistency. Most users don't need to set this option. The default is 900000 milliseconds, or 15 minutes.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** MaxFilesInBand **   <a name="Glue-Type-S3CsvSource-MaxFilesInBand"></a>
This option specifies the maximum number of files to save from the last maxBand seconds. If this number is exceeded, extra files are skipped and only processed in the next job run.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Multiline **   <a name="Glue-Type-S3CsvSource-Multiline"></a>
A Boolean value that specifies whether a single record can span multiple lines. This can occur when a field contains a quoted new-line character. You must set this option to True if any record spans multiple lines. The default value is `False`, which allows for more aggressive file-splitting during parsing.
Type: Boolean
Required: No

 ** OptimizePerformance **   <a name="Glue-Type-S3CsvSource-OptimizePerformance"></a>
A Boolean value that specifies whether to use the advanced SIMD CSV reader along with Apache Arrow based columnar memory formats. Only available in AWS Glue version 3.0.
Type: Boolean
Required: No

 ** OutputSchemas **   <a name="Glue-Type-S3CsvSource-OutputSchemas"></a>
Specifies the data schema for the S3 CSV source.
Type: Array of [GlueSchema](API_GlueSchema.md) objects
Required: No

 ** Recurse **   <a name="Glue-Type-S3CsvSource-Recurse"></a>
If set to true, recursively reads files in all subdirectories under the specified paths.
Type: Boolean
Required: No

 ** SkipFirst **   <a name="Glue-Type-S3CsvSource-SkipFirst"></a>
A Boolean value that specifies whether to skip the first data line. The default value is `False`.
Type: Boolean
Required: No

 ** WithHeader **   <a name="Glue-Type-S3CsvSource-WithHeader"></a>
A Boolean value that specifies whether to treat the first line as a header. The default value is `False`.
Type: Boolean
Required: No

 ** WriteHeader **   <a name="Glue-Type-S3CsvSource-WriteHeader"></a>
A Boolean value that specifies whether to write the header to output. The default value is `True`.
Type: Boolean
Required: No

## See Also
<a name="API_S3CsvSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/S3CsvSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/S3CsvSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/S3CsvSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
