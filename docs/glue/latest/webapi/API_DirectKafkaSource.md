---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DirectKafkaSource.html
---

# DirectKafkaSource
<a name="API_DirectKafkaSource"></a>

Specifies an Apache Kafka data store.

## Contents
<a name="API_DirectKafkaSource_Contents"></a>

 ** Name **   <a name="Glue-Type-DirectKafkaSource-Name"></a>
The name of the data store.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** DataPreviewOptions **   <a name="Glue-Type-DirectKafkaSource-DataPreviewOptions"></a>
Specifies options related to data preview for viewing a sample of your data.
Type: [StreamingDataPreviewOptions](API_StreamingDataPreviewOptions.md) object
Required: No

 ** DetectSchema **   <a name="Glue-Type-DirectKafkaSource-DetectSchema"></a>
Whether to automatically determine the schema from the incoming data.
Type: Boolean
Required: No

 ** StreamingOptions **   <a name="Glue-Type-DirectKafkaSource-StreamingOptions"></a>
Specifies the streaming options.
Type: [KafkaStreamingSourceOptions](API_KafkaStreamingSourceOptions.md) object
Required: No

 ** WindowSize **   <a name="Glue-Type-DirectKafkaSource-WindowSize"></a>
The amount of time to spend processing each micro batch.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_DirectKafkaSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DirectKafkaSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DirectKafkaSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DirectKafkaSource)
