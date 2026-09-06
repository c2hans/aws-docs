---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_InputProcessingConfiguration.html
---

# InputProcessingConfiguration
<a name="API_InputProcessingConfiguration"></a>

For a SQL-based Kinesis Data Analytics application, describes a processor that is used to preprocess the records in the stream before being processed by your application code. Currently, the only input processor available is [Amazon Lambda](https://docs.aws.amazon.com/lambda/).

## Contents
<a name="API_InputProcessingConfiguration_Contents"></a>

 ** InputLambdaProcessor **   <a name="APIReference-Type-InputProcessingConfiguration-InputLambdaProcessor"></a>
The [InputLambdaProcessor](API_InputLambdaProcessor.md) that is used to preprocess the records in the stream before being processed by your application code.
Type: [InputLambdaProcessor](API_InputLambdaProcessor.md) object
Required: Yes

## See Also
<a name="API_InputProcessingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/InputProcessingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/InputProcessingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/InputProcessingConfiguration)
