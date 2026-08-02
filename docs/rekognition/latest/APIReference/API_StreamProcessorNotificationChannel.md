---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessorNotificationChannel.html
---

# StreamProcessorNotificationChannel
<a name="API_StreamProcessorNotificationChannel"></a>

The Amazon Simple Notification Service topic to which Amazon Rekognition publishes the object detection results and completion status of a video analysis operation.

Amazon Rekognition publishes a notification the first time an object of interest or a person is detected in the video stream. For example, if Amazon Rekognition detects a person at second 2, a pet at second 4, and a person again at second 5, Amazon Rekognition sends 2 object class detected notifications, one for a person at second 2 and one for a pet at second 4.

Amazon Rekognition also publishes an an end-of-session notification with a summary when the stream processing session is complete.

## Contents
<a name="API_StreamProcessorNotificationChannel_Contents"></a>

 ** SNSTopicArn **   <a name="rekognition-Type-StreamProcessorNotificationChannel-SNSTopicArn"></a>
 The Amazon Resource Number (ARN) of the Amazon Amazon Simple Notification Service topic to which Amazon Rekognition posts the completion status.
Type: String
Pattern: `(^arn:aws:sns:.*:\w{12}:.+$)`
Required: Yes

## See Also
<a name="API_StreamProcessorNotificationChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/StreamProcessorNotificationChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/StreamProcessorNotificationChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/StreamProcessorNotificationChannel)
