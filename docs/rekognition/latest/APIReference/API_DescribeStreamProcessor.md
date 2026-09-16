---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeStreamProcessor.html
---

# DescribeStreamProcessor
<a name="API_DescribeStreamProcessor"></a>

**Important**
Service availability notice: Streaming Video and Bulk Image Analysis is no longer available to new customers. For more information, see [Rekognition feature availability changes](https://docs.aws.amazon.com/rekognition/latest/dg/rekognition-availability-changes.html).
 **This change does not impact the availability of other Amazon Rekognition features.**

Provides information about a stream processor created by [CreateStreamProcessor](API_CreateStreamProcessor.md). You can get information about the input and output streams, the input parameters for the face recognition being performed, and the current status of the stream processor.

## Request Syntax
<a name="API_DescribeStreamProcessor_RequestSyntax"></a>

```
{
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeStreamProcessor_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_DescribeStreamProcessor_RequestSyntax) **   <a name="rekognition-DescribeStreamProcessor-request-Name"></a>
Name of the stream processor for which you want information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.\-]+`
Required: Yes

## Response Syntax
<a name="API_DescribeStreamProcessor_ResponseSyntax"></a>

```
{
   "CreationTimestamp": number,
   "DataSharingPreference": {
      "OptIn": boolean
   },
   "Input": {
      "KinesisVideoStream": {
         "Arn": "string"
      }
   },
   "KmsKeyId": "string",
   "LastUpdateTimestamp": number,
   "Name": "string",
   "NotificationChannel": {
      "SNSTopicArn": "string"
   },
   "Output": {
      "KinesisDataStream": {
         "Arn": "string"
      },
      "S3Destination": {
         "Bucket": "string",
         "KeyPrefix": "string"
      }
   },
   "RegionsOfInterest": [
      {
         "BoundingBox": {
            "Height": number,
            "Left": number,
            "Top": number,
            "Width": number
         },
         "Polygon": [
            {
               "X": number,
               "Y": number
            }
         ]
      }
   ],
   "RoleArn": "string",
   "Settings": {
      "ConnectedHome": {
         "Labels": [ "string" ],
         "MinConfidence": number
      },
      "FaceSearch": {
         "CollectionId": "string",
         "FaceMatchThreshold": number
      }
   },
   "Status": "string",
   "StatusMessage": "string",
   "StreamProcessorArn": "string"
}
```

## Response Elements
<a name="API_DescribeStreamProcessor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTimestamp](#API_DescribeStreamProcessor_ResponseSyntax) **   <a name="rekognition-DescribeStreamProcessor-response-CreationTimestamp"></a>
Date and time the stream processor was created
Type: Timestamp

 ** [DataSharingPreference](#API_DescribeStreamProcessor_ResponseSyntax) **   <a name="rekognition-DescribeStreamProcessor-response-DataSharingPreference"></a>
 Shows whether you are sharing data with Rekognition to improve model performance. You can choose this option at the account level or on a per-stream basis. Note that if you opt out at the account level this setting is ignored on individual streams.
Type: [StreamProcessorDataSharingPreference](API_StreamProcessorDataSharingPreference.md) object

 ** [Input](#API_DescribeStreamProcessor_ResponseSyntax) **   <a name="rekognition-DescribeStreamProcessor-response-Input"></a>
Kinesis video stream that provides the source streaming video.
Type: [StreamProcessorInput](API_StreamProcessorInput.md) object

 ** [KmsKeyId](#API_DescribeStreamProcessor_ResponseSyntax) **   <a name="rekognition-DescribeStreamProcessor-response-KmsKeyId"></a>
 The identifier for your AWS Key Management Service key (AWS KMS key). This is an optional parameter for label detection stream processors.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`

 ** [LastUpdateTimestamp](#API_DescribeStreamProcessor_ResponseSyntax) **   <a name="rekognition-DescribeStreamProcessor-response-LastUpdateTimestamp"></a>
The time, in Unix format, the stream processor was last updated. For example, when the stream processor moves from a running state to a failed state, or when the user starts or stops the stream processor.
Type: Timestamp

 ** [Name](#API_DescribeStreamProcessor_ResponseSyntax) **   <a name="rekognition-DescribeStreamProcessor-response-Name"></a>
Name of the stream processor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.\-]+`

 ** [NotificationChannel](#API_DescribeStreamProcessor_ResponseSyntax) **   <a name="rekognition-DescribeStreamProcessor-response-NotificationChannel"></a>
The Amazon Simple Notification Service topic to which Amazon Rekognition publishes the object detection results and completion status of a video analysis operation.
Amazon Rekognition publishes a notification the first time an object of interest or a person is detected in the video stream. For example, if Amazon Rekognition detects a person at second 2, a pet at second 4, and a person again at second 5, Amazon Rekognition sends 2 object class detected notifications, one for a person at second 2 and one for a pet at second 4.
Amazon Rekognition also publishes an an end-of-session notification with a summary when the stream processing session is complete.
Type: [StreamProcessorNotificationChannel](API_StreamProcessorNotificationChannel.md) object

 ** [Output](#API_DescribeStreamProcessor_ResponseSyntax) **   <a name="rekognition-DescribeStreamProcessor-response-Output"></a>
Kinesis data stream to which Amazon Rekognition Video puts the analysis results.
Type: [StreamProcessorOutput](API_StreamProcessorOutput.md) object

 ** [RegionsOfInterest](#API_DescribeStreamProcessor_ResponseSyntax) **   <a name="rekognition-DescribeStreamProcessor-response-RegionsOfInterest"></a>
 Specifies locations in the frames where Amazon Rekognition checks for objects or people. This is an optional parameter for label detection stream processors.
Type: Array of [RegionOfInterest](API_RegionOfInterest.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [RoleArn](#API_DescribeStreamProcessor_ResponseSyntax) **   <a name="rekognition-DescribeStreamProcessor-response-RoleArn"></a>
ARN of the IAM role that allows access to the stream processor.
Type: String
Pattern: `arn:aws:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [Settings](#API_DescribeStreamProcessor_ResponseSyntax) **   <a name="rekognition-DescribeStreamProcessor-response-Settings"></a>
Input parameters used in a streaming video analyzed by a stream processor. You can use `FaceSearch` to recognize faces in a streaming video, or you can use `ConnectedHome` to detect labels.
Type: [StreamProcessorSettings](API_StreamProcessorSettings.md) object

 ** [Status](#API_DescribeStreamProcessor_ResponseSyntax) **   <a name="rekognition-DescribeStreamProcessor-response-Status"></a>
Current status of the stream processor.
Type: String
Valid Values: `STOPPED | STARTING | RUNNING | FAILED | STOPPING | UPDATING`

 ** [StatusMessage](#API_DescribeStreamProcessor_ResponseSyntax) **   <a name="rekognition-DescribeStreamProcessor-response-StatusMessage"></a>
Detailed status message about the stream processor.
Type: String

 ** [StreamProcessorArn](#API_DescribeStreamProcessor_ResponseSyntax) **   <a name="rekognition-DescribeStreamProcessor-response-StreamProcessorArn"></a>
ARN of the stream processor.
Type: String
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:streamprocessor\/.+$)`

## Errors
<a name="API_DescribeStreamProcessor_Errors"></a>

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

 ** ResourceNotFoundException **
The resource specified in the request cannot be found.
HTTP Status Code: 400

 ** ThrottlingException **
Amazon Rekognition is temporarily unable to process the request. Try your call again.
HTTP Status Code: 500

## See Also
<a name="API_DescribeStreamProcessor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/DescribeStreamProcessor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/DescribeStreamProcessor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DescribeStreamProcessor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/DescribeStreamProcessor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/DescribeStreamProcessor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/DescribeStreamProcessor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/DescribeStreamProcessor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/DescribeStreamProcessor)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/DescribeStreamProcessor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DescribeStreamProcessor)
