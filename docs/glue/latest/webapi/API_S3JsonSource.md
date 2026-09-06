---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_S3JsonSource.html
---

# S3JsonSource
<a name="API_S3JsonSource"></a>

Specifies a JSON data store stored in Amazon S3.

## Contents
<a name="API_S3JsonSource_Contents"></a>

 ** Name **   <a name="Glue-Type-S3JsonSource-Name"></a>
The name of the data store.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Paths **   <a name="Glue-Type-S3JsonSource-Paths"></a>
A list of the Amazon S3 paths to read from.
Type: Array of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** AdditionalOptions **   <a name="Glue-Type-S3JsonSource-AdditionalOptions"></a>
Specifies additional connection options.
Type: [S3DirectSourceAdditionalOptions](API_S3DirectSourceAdditionalOptions.md) object
Required: No

 ** CompressionType **   <a name="Glue-Type-S3JsonSource-CompressionType"></a>
Specifies how the data is compressed. This is generally not necessary if the data has a standard file extension. Possible values are `"gzip"` and `"bzip"`).
Type: String
Valid Values: `gzip | bzip2`
Required: No

 ** Exclusions **   <a name="Glue-Type-S3JsonSource-Exclusions"></a>
A string containing a JSON list of Unix-style glob patterns to exclude. For example, "[\\"\*\*.pdf\\"]" excludes all PDF files.
Type: Array of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** GroupFiles **   <a name="Glue-Type-S3JsonSource-GroupFiles"></a>
Grouping files is turned on by default when the input contains more than 50,000 files. To turn on grouping with fewer than 50,000 files, set this parameter to "inPartition". To disable grouping when there are more than 50,000 files, set this parameter to `"none"`.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** GroupSize **   <a name="Glue-Type-S3JsonSource-GroupSize"></a>
The target group size in bytes. The default is computed based on the input data size and the size of your cluster. When there are fewer than 50,000 input files, `"groupFiles"` must be set to `"inPartition"` for this to take effect.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** JsonPath **   <a name="Glue-Type-S3JsonSource-JsonPath"></a>
A JsonPath string defining the JSON data.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** MaxBand **   <a name="Glue-Type-S3JsonSource-MaxBand"></a>
This option controls the duration in milliseconds after which the s3 listing is likely to be consistent. Files with modification timestamps falling within the last maxBand milliseconds are tracked specially when using JobBookmarks to account for Amazon S3 eventual consistency. Most users don't need to set this option. The default is 900000 milliseconds, or 15 minutes.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** MaxFilesInBand **   <a name="Glue-Type-S3JsonSource-MaxFilesInBand"></a>
This option specifies the maximum number of files to save from the last maxBand seconds. If this number is exceeded, extra files are skipped and only processed in the next job run.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Multiline **   <a name="Glue-Type-S3JsonSource-Multiline"></a>
A Boolean value that specifies whether a single record can span multiple lines. This can occur when a field contains a quoted new-line character. You must set this option to True if any record spans multiple lines. The default value is `False`, which allows for more aggressive file-splitting during parsing.
Type: Boolean
Required: No

 ** OutputSchemas **   <a name="Glue-Type-S3JsonSource-OutputSchemas"></a>
Specifies the data schema for the S3 JSON source.
Type: Array of [GlueSchema](API_GlueSchema.md) objects
Required: No

 ** Recurse **   <a name="Glue-Type-S3JsonSource-Recurse"></a>
If set to true, recursively reads files in all subdirectories under the specified paths.
Type: Boolean
Required: No

## See Also
<a name="API_S3JsonSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/S3JsonSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/S3JsonSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/S3JsonSource)
