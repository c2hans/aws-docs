---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DirectKinesisSource.html
---

# DirectKinesisSource
<a name="API_DirectKinesisSource"></a>

Specifies a direct Amazon Kinesis data source.

## Contents
<a name="API_DirectKinesisSource_Contents"></a>

 ** Name **   <a name="Glue-Type-DirectKinesisSource-Name"></a>
The name of the data source.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** DataPreviewOptions **   <a name="Glue-Type-DirectKinesisSource-DataPreviewOptions"></a>
Additional options for data preview.
Type: [StreamingDataPreviewOptions](API_StreamingDataPreviewOptions.md) object
Required: No

 ** DetectSchema **   <a name="Glue-Type-DirectKinesisSource-DetectSchema"></a>
Whether to automatically determine the schema from the incoming data.
Type: Boolean
Required: No

 ** StreamingOptions **   <a name="Glue-Type-DirectKinesisSource-StreamingOptions"></a>
Additional options for the Kinesis streaming data source.
Type: [KinesisStreamingSourceOptions](API_KinesisStreamingSourceOptions.md) object
Required: No

 ** WindowSize **   <a name="Glue-Type-DirectKinesisSource-WindowSize"></a>
The amount of time to spend processing each micro batch.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_DirectKinesisSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DirectKinesisSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DirectKinesisSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DirectKinesisSource)
