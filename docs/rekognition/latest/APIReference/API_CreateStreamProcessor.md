---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor.html
---

# CreateStreamProcessor
<a name="API_CreateStreamProcessor"></a>

**Important**
Service availability notice: Streaming Video and Bulk Image Analysis is no longer available to new customers. For more information, see [Rekognition feature availability changes](https://docs.aws.amazon.com/rekognition/latest/dg/rekognition-availability-changes.html).
 **This change does not impact the availability of other Amazon Rekognition features.**

Creates an Amazon Rekognition stream processor that you can use to detect and recognize faces or to detect labels in a streaming video.

Amazon Rekognition Video is a consumer of live video from Amazon Kinesis Video Streams. There are two different settings for stream processors in Amazon Rekognition: detecting faces and detecting labels.
+ If you are creating a stream processor for detecting faces, you provide as input a Kinesis video stream (`Input`) and a Kinesis data stream (`Output`) stream for receiving the output. You must use the `FaceSearch` option in `Settings`, specifying the collection that contains the faces you want to recognize. After you have finished analyzing a streaming video, use [StopStreamProcessor](API_StopStreamProcessor.md) to stop processing.
+ If you are creating a stream processor to detect labels, you provide as input a Kinesis video stream (`Input`), Amazon S3 bucket information (`Output`), and an Amazon SNS topic ARN (`NotificationChannel`). You can also provide a KMS key ID to encrypt the data sent to your Amazon S3 bucket. You specify what you want to detect by using the `ConnectedHome` option in settings, and selecting one of the following: `PERSON`, `PET`, `PACKAGE`, `ALL` You can also specify where in the frame you want Amazon Rekognition to monitor with `RegionsOfInterest`. When you run the [StartStreamProcessor](API_StartStreamProcessor.md) operation on a label detection stream processor, you input start and stop information to determine the length of the processing time.

 Use `Name` to assign an identifier for the stream processor. You use `Name` to manage the stream processor. For example, you can start processing the source video by calling [StartStreamProcessor](API_StartStreamProcessor.md) with the `Name` field.

This operation requires permissions to perform the `rekognition:CreateStreamProcessor` action. If you want to tag your stream processor, you also require permission to perform the `rekognition:TagResource` operation.

## Request Syntax
<a name="API_CreateStreamProcessor_RequestSyntax"></a>

```
{
   "DataSharingPreference": {
      "OptIn": {{boolean}}
   },
   "Input": {
      "KinesisVideoStream": {
         "Arn": "{{string}}"
      }
   },
   "KmsKeyId": "{{string}}",
   "Name": "{{string}}",
   "NotificationChannel": {
      "SNSTopicArn": "{{string}}"
   },
   "Output": {
      "KinesisDataStream": {
         "Arn": "{{string}}"
      },
      "S3Destination": {
         "Bucket": "{{string}}",
         "KeyPrefix": "{{string}}"
      }
   },
   "RegionsOfInterest": [
      {
         "BoundingBox": {
            "Height": {{number}},
            "Left": {{number}},
            "Top": {{number}},
            "Width": {{number}}
         },
         "Polygon": [
            {
               "X": {{number}},
               "Y": {{number}}
            }
         ]
      }
   ],
   "RoleArn": "{{string}}",
   "Settings": {
      "ConnectedHome": {
         "Labels": [ "{{string}}" ],
         "MinConfidence": {{number}}
      },
      "FaceSearch": {
         "CollectionId": "{{string}}",
         "FaceMatchThreshold": {{number}}
      }
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateStreamProcessor_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DataSharingPreference](#API_CreateStreamProcessor_RequestSyntax) **   <a name="rekognition-CreateStreamProcessor-request-DataSharingPreference"></a>
 Shows whether you are sharing data with Rekognition to improve model performance. You can choose this option at the account level or on a per-stream basis. Note that if you opt out at the account level this setting is ignored on individual streams.
Type: [StreamProcessorDataSharingPreference](API_StreamProcessorDataSharingPreference.md) object
Required: No

 ** [Input](#API_CreateStreamProcessor_RequestSyntax) **   <a name="rekognition-CreateStreamProcessor-request-Input"></a>
Kinesis video stream stream that provides the source streaming video. If you are using the AWS CLI, the parameter name is `StreamProcessorInput`. This is required for both face search and label detection stream processors.
Type: [StreamProcessorInput](API_StreamProcessorInput.md) object
Required: Yes

 ** [KmsKeyId](#API_CreateStreamProcessor_RequestSyntax) **   <a name="rekognition-CreateStreamProcessor-request-KmsKeyId"></a>
 The identifier for your AWS Key Management Service key (AWS KMS key). This is an optional parameter for label detection stream processors and should not be used to create a face search stream processor. You can supply the Amazon Resource Name (ARN) of your KMS key, the ID of your KMS key, an alias for your KMS key, or an alias ARN. The key is used to encrypt results and data published to your Amazon S3 bucket, which includes image frames and hero images. Your source images are unaffected.

Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`
Required: No

 ** [Name](#API_CreateStreamProcessor_RequestSyntax) **   <a name="rekognition-CreateStreamProcessor-request-Name"></a>
An identifier you assign to the stream processor. You can use `Name` to manage the stream processor. For example, you can get the current status of the stream processor by calling [DescribeStreamProcessor](API_DescribeStreamProcessor.md). `Name` is idempotent. This is required for both face search and label detection stream processors.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.\-]+`
Required: Yes

 ** [NotificationChannel](#API_CreateStreamProcessor_RequestSyntax) **   <a name="rekognition-CreateStreamProcessor-request-NotificationChannel"></a>
The Amazon Simple Notification Service topic to which Amazon Rekognition publishes the object detection results and completion status of a video analysis operation.
Amazon Rekognition publishes a notification the first time an object of interest or a person is detected in the video stream. For example, if Amazon Rekognition detects a person at second 2, a pet at second 4, and a person again at second 5, Amazon Rekognition sends 2 object class detected notifications, one for a person at second 2 and one for a pet at second 4.
Amazon Rekognition also publishes an an end-of-session notification with a summary when the stream processing session is complete.
Type: [StreamProcessorNotificationChannel](API_StreamProcessorNotificationChannel.md) object
Required: No

 ** [Output](#API_CreateStreamProcessor_RequestSyntax) **   <a name="rekognition-CreateStreamProcessor-request-Output"></a>
Kinesis data stream stream or Amazon S3 bucket location to which Amazon Rekognition Video puts the analysis results. If you are using the AWS CLI, the parameter name is `StreamProcessorOutput`. This must be a [S3Destination](API_S3Destination.md) of an Amazon S3 bucket that you own for a label detection stream processor or a Kinesis data stream ARN for a face search stream processor.
Type: [StreamProcessorOutput](API_StreamProcessorOutput.md) object
Required: Yes

 ** [RegionsOfInterest](#API_CreateStreamProcessor_RequestSyntax) **   <a name="rekognition-CreateStreamProcessor-request-RegionsOfInterest"></a>
 Specifies locations in the frames where Amazon Rekognition checks for objects or people. You can specify up to 10 regions of interest, and each region has either a polygon or a bounding box. This is an optional parameter for label detection stream processors and should not be used to create a face search stream processor.
Type: Array of [RegionOfInterest](API_RegionOfInterest.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [RoleArn](#API_CreateStreamProcessor_RequestSyntax) **   <a name="rekognition-CreateStreamProcessor-request-RoleArn"></a>
The Amazon Resource Number (ARN) of the IAM role that allows access to the stream processor. The IAM role provides Rekognition read permissions for a Kinesis stream. It also provides write permissions to an Amazon S3 bucket and Amazon Simple Notification Service topic for a label detection stream processor. This is required for both face search and label detection stream processors.
Type: String
Pattern: `arn:aws:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [Settings](#API_CreateStreamProcessor_RequestSyntax) **   <a name="rekognition-CreateStreamProcessor-request-Settings"></a>
Input parameters used in a streaming video analyzed by a stream processor. You can use `FaceSearch` to recognize faces in a streaming video, or you can use `ConnectedHome` to detect labels.
Type: [StreamProcessorSettings](API_StreamProcessorSettings.md) object
Required: Yes

 ** [Tags](#API_CreateStreamProcessor_RequestSyntax) **   <a name="rekognition-CreateStreamProcessor-request-Tags"></a>
 A set of tags (key-value pairs) that you want to attach to the stream processor.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## Response Syntax
<a name="API_CreateStreamProcessor_ResponseSyntax"></a>

```
{
   "StreamProcessorArn": "string"
}
```

## Response Elements
<a name="API_CreateStreamProcessor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StreamProcessorArn](#API_CreateStreamProcessor_ResponseSyntax) **   <a name="rekognition-CreateStreamProcessor-response-StreamProcessorArn"></a>
Amazon Resource Number for the newly created stream processor.
Type: String
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:streamprocessor\/.+$)`

## Errors
<a name="API_CreateStreamProcessor_Errors"></a>

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

 ** LimitExceededException **
An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: `StartLabelDetection`) will raise a `LimitExceededException` exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.
HTTP Status Code: 400

 ** ResourceInUseException **
The specified resource is already being used.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **

The size of the resource exceeds the allowed limit. For more information, see [Guidelines and quotas in Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/limits.html).
HTTP Status Code: 400

 ** ThrottlingException **
Amazon Rekognition is temporarily unable to process the request. Try your call again.
HTTP Status Code: 500

## See Also
<a name="API_CreateStreamProcessor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/CreateStreamProcessor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/CreateStreamProcessor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/CreateStreamProcessor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/CreateStreamProcessor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/CreateStreamProcessor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/CreateStreamProcessor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/CreateStreamProcessor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/CreateStreamProcessor)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/CreateStreamProcessor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/CreateStreamProcessor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
