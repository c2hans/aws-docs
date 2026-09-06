---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_S3ExcelSource.html
---

# S3ExcelSource
<a name="API_S3ExcelSource"></a>

Specifies an S3 Excel data source.

## Contents
<a name="API_S3ExcelSource_Contents"></a>

 ** Name **   <a name="Glue-Type-S3ExcelSource-Name"></a>
The name of the S3 Excel data source.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Paths **   <a name="Glue-Type-S3ExcelSource-Paths"></a>
The S3 paths where the Excel files are located.
Type: Array of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** AdditionalOptions **   <a name="Glue-Type-S3ExcelSource-AdditionalOptions"></a>
Additional configuration options for S3 direct source processing.
Type: [S3DirectSourceAdditionalOptions](API_S3DirectSourceAdditionalOptions.md) object
Required: No

 ** CompressionType **   <a name="Glue-Type-S3ExcelSource-CompressionType"></a>
The compression format used for the Excel files.
Type: String
Valid Values: `snappy | lzo | gzip | brotli | lz4 | uncompressed | none`
Required: No

 ** Exclusions **   <a name="Glue-Type-S3ExcelSource-Exclusions"></a>
Patterns to exclude specific files or paths from processing.
Type: Array of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** GroupFiles **   <a name="Glue-Type-S3ExcelSource-GroupFiles"></a>
Specifies how files should be grouped for processing.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** GroupSize **   <a name="Glue-Type-S3ExcelSource-GroupSize"></a>
Defines the size of file groups for batch processing.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** MaxBand **   <a name="Glue-Type-S3ExcelSource-MaxBand"></a>
The maximum number of processing bands to use.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** MaxFilesInBand **   <a name="Glue-Type-S3ExcelSource-MaxFilesInBand"></a>
The maximum number of files to process in each band.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** NumberRows **   <a name="Glue-Type-S3ExcelSource-NumberRows"></a>
The number of rows to process from each Excel file.
Type: Long
Required: No

 ** OutputSchemas **   <a name="Glue-Type-S3ExcelSource-OutputSchemas"></a>
The AWS Glue schemas to apply to the processed data.
Type: Array of [GlueSchema](API_GlueSchema.md) objects
Required: No

 ** Recurse **   <a name="Glue-Type-S3ExcelSource-Recurse"></a>
Indicates whether to recursively process subdirectories.
Type: Boolean
Required: No

 ** SkipFooter **   <a name="Glue-Type-S3ExcelSource-SkipFooter"></a>
The number of rows to skip at the end of each Excel file.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_S3ExcelSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/S3ExcelSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/S3ExcelSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/S3ExcelSource)
