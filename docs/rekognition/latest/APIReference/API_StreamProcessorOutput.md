---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessorOutput.html
---

# StreamProcessorOutput
<a name="API_StreamProcessorOutput"></a>

Information about the Amazon Kinesis Data Streams stream to which a Amazon Rekognition Video stream processor streams the results of a video analysis. For more information, see [CreateStreamProcessor](API_CreateStreamProcessor.md).

## Contents
<a name="API_StreamProcessorOutput_Contents"></a>

 ** KinesisDataStream **   <a name="rekognition-Type-StreamProcessorOutput-KinesisDataStream"></a>
The Amazon Kinesis Data Streams stream to which the Amazon Rekognition stream processor streams the analysis results.
Type: [KinesisDataStream](API_KinesisDataStream.md) object
Required: No

 ** S3Destination **   <a name="rekognition-Type-StreamProcessorOutput-S3Destination"></a>
 The Amazon S3 bucket location to which Amazon Rekognition publishes the detailed inference results of a video analysis operation.
Type: [S3Destination](API_S3Destination.md) object
Required: No

## See Also
<a name="API_StreamProcessorOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/StreamProcessorOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/StreamProcessorOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/StreamProcessorOutput)
