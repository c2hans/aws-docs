---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CatalogKinesisSource.html
---

# CatalogKinesisSource
<a name="API_CatalogKinesisSource"></a>

Specifies a Kinesis data source in the AWS Glue Data Catalog.

## Contents
<a name="API_CatalogKinesisSource_Contents"></a>

 ** Database **   <a name="Glue-Type-CatalogKinesisSource-Database"></a>
The name of the database to read from.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Name **   <a name="Glue-Type-CatalogKinesisSource-Name"></a>
The name of the data source.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Table **   <a name="Glue-Type-CatalogKinesisSource-Table"></a>
The name of the table in the database to read from.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** DataPreviewOptions **   <a name="Glue-Type-CatalogKinesisSource-DataPreviewOptions"></a>
Additional options for data preview.
Type: [StreamingDataPreviewOptions](API_StreamingDataPreviewOptions.md) object
Required: No

 ** DetectSchema **   <a name="Glue-Type-CatalogKinesisSource-DetectSchema"></a>
Whether to automatically determine the schema from the incoming data.
Type: Boolean
Required: No

 ** StreamingOptions **   <a name="Glue-Type-CatalogKinesisSource-StreamingOptions"></a>
Additional options for the Kinesis streaming data source.
Type: [KinesisStreamingSourceOptions](API_KinesisStreamingSourceOptions.md) object
Required: No

 ** WindowSize **   <a name="Glue-Type-CatalogKinesisSource-WindowSize"></a>
The amount of time to spend processing each micro batch.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_CatalogKinesisSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CatalogKinesisSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CatalogKinesisSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CatalogKinesisSource)
