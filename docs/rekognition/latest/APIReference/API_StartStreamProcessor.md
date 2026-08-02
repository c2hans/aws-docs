---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartStreamProcessor.html
---

# StartStreamProcessor
<a name="API_StartStreamProcessor"></a>

**Important**
Service availability notice: Streaming Video and Bulk Image Analysis is no longer available to new customers. For more information, see [Rekognition feature availability changes](https://docs.aws.amazon.com/rekognition/latest/dg/rekognition-availability-changes.html).
 **This change does not impact the availability of other Amazon Rekognition features.**

Starts processing a stream processor. You create a stream processor by calling [CreateStreamProcessor](API_CreateStreamProcessor.md). To tell `StartStreamProcessor` which stream processor to start, use the value of the `Name` field specified in the call to `CreateStreamProcessor`.

If you are using a label detection stream processor to detect labels, you need to provide a `Start selector` and a `Stop selector` to determine the length of the stream processing time.

## Request Syntax
<a name="API_StartStreamProcessor_RequestSyntax"></a>

```
{
   "Name": "{{string}}",
   "StartSelector": {
      "KVSStreamStartSelector": {
         "FragmentNumber": "{{string}}",
         "ProducerTimestamp": {{number}}
      }
   },
   "StopSelector": {
      "MaxDurationInSeconds": {{number}}
   }
}
```

## Request Parameters
<a name="API_StartStreamProcessor_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_StartStreamProcessor_RequestSyntax) **   <a name="rekognition-StartStreamProcessor-request-Name"></a>
The name of the stream processor to start processing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.\-]+`
Required: Yes

 ** [StartSelector](#API_StartStreamProcessor_RequestSyntax) **   <a name="rekognition-StartStreamProcessor-request-StartSelector"></a>
 Specifies the starting point in the Kinesis stream to start processing. You can use the producer timestamp or the fragment number. If you use the producer timestamp, you must put the time in milliseconds. For more information about fragment numbers, see [Fragment](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_Fragment.html).
This is a required parameter for label detection stream processors and should not be used to start a face search stream processor.
Type: [StreamProcessingStartSelector](API_StreamProcessingStartSelector.md) object
Required: No

 ** [StopSelector](#API_StartStreamProcessor_RequestSyntax) **   <a name="rekognition-StartStreamProcessor-request-StopSelector"></a>
 Specifies when to stop processing the stream. You can specify a maximum amount of time to process the video.
This is a required parameter for label detection stream processors and should not be used to start a face search stream processor.
Type: [StreamProcessingStopSelector](API_StreamProcessingStopSelector.md) object
Required: No

## Response Syntax
<a name="API_StartStreamProcessor_ResponseSyntax"></a>

```
{
   "SessionId": "string"
}
```

## Response Elements
<a name="API_StartStreamProcessor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SessionId](#API_StartStreamProcessor_ResponseSyntax) **   <a name="rekognition-StartStreamProcessor-response-SessionId"></a>
 A unique identifier for the stream processing session.
Type: String

## Errors
<a name="API_StartStreamProcessor_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform the action.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Rekognition experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterException **
Input parameter violated a constraint. Validate your parameter before calling the API operation again.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.
HTTP Status Code: 400

 ** ResourceInUseException **
The specified resource is already being used.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource specified in the request cannot be found.
HTTP Status Code: 400

 ** ThrottlingException **
Amazon Rekognition is temporarily unable to process the request. Try your call again.
HTTP Status Code: 500

## See Also
<a name="API_StartStreamProcessor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/StartStreamProcessor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/StartStreamProcessor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/StartStreamProcessor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/StartStreamProcessor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/StartStreamProcessor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/StartStreamProcessor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/StartStreamProcessor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/StartStreamProcessor)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/StartStreamProcessor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/StartStreamProcessor)
