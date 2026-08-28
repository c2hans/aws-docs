---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartLabelDetection.html
---

# StartLabelDetection
<a name="API_StartLabelDetection"></a>

Starts asynchronous detection of labels in a stored video.

Amazon Rekognition Video can detect labels in a video. Labels are instances of real-world entities. This includes objects like flower, tree, and table; events like wedding, graduation, and birthday party; concepts like landscape, evening, and nature; and activities like a person getting out of a car or a person skiing.

The video must be stored in an Amazon S3 bucket. Use [Video](API_Video.md) to specify the bucket name and the filename of the video. `StartLabelDetection` returns a job identifier (`JobId`) which you use to get the results of the operation. When label detection is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in `NotificationChannel`.

To get the results of the label detection operation, first check that the status value published to the Amazon SNS topic is `SUCCEEDED`. If so, call [GetLabelDetection](API_GetLabelDetection.md) and pass the job identifier (`JobId`) from the initial call to `StartLabelDetection`.

 *Optional Parameters*

 `StartLabelDetection` has the `GENERAL_LABELS` Feature applied by default. This feature allows you to provide filtering criteria to the `Settings` parameter. You can filter with sets of individual labels or with label categories. You can specify inclusive filters, exclusive filters, or a combination of inclusive and exclusive filters. For more information on filtering, see [Detecting labels in a video](https://docs.aws.amazon.com/rekognition/latest/dg/labels-detecting-labels-video.html).

You can specify `MinConfidence` to control the confidence threshold for the labels returned. The default is 50.

## Request Syntax
<a name="API_StartLabelDetection_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "Features": [ "{{string}}" ],
   "JobTag": "{{string}}",
   "MinConfidence": {{number}},
   "NotificationChannel": {
      "RoleArn": "{{string}}",
      "SNSTopicArn": "{{string}}"
   },
   "Settings": {
      "GeneralLabels": {
         "LabelCategoryExclusionFilters": [ "{{string}}" ],
         "LabelCategoryInclusionFilters": [ "{{string}}" ],
         "LabelExclusionFilters": [ "{{string}}" ],
         "LabelInclusionFilters": [ "{{string}}" ]
      }
   },
   "Video": {
      "S3Object": {
         "Bucket": "{{string}}",
         "Name": "{{string}}",
         "Version": "{{string}}"
      }
   }
}
```

## Request Parameters
<a name="API_StartLabelDetection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_StartLabelDetection_RequestSyntax) **   <a name="rekognition-StartLabelDetection-request-ClientRequestToken"></a>
Idempotent token used to identify the start request. If you use the same token with multiple `StartLabelDetection` requests, the same `JobId` is returned. Use `ClientRequestToken` to prevent the same job from being accidently started more than once.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: No

 ** [Features](#API_StartLabelDetection_RequestSyntax) **   <a name="rekognition-StartLabelDetection-request-Features"></a>
The features to return after video analysis. You can specify that GENERAL\_LABELS are returned.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Valid Values: `GENERAL_LABELS`
Required: No

 ** [JobTag](#API_StartLabelDetection_RequestSyntax) **   <a name="rekognition-StartLabelDetection-request-JobTag"></a>
An identifier you specify that's returned in the completion notification that's published to your Amazon Simple Notification Service topic. For example, you can use `JobTag` to group related jobs and identify them in the completion notification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9_.\-:+=\/]+`
Required: No

 ** [MinConfidence](#API_StartLabelDetection_RequestSyntax) **   <a name="rekognition-StartLabelDetection-request-MinConfidence"></a>
Specifies the minimum confidence that Amazon Rekognition Video must have in order to return a detected label. Confidence represents how certain Amazon Rekognition is that a label is correctly identified.0 is the lowest confidence. 100 is the highest confidence. Amazon Rekognition Video doesn't return any labels with a confidence level lower than this specified value.
If you don't specify `MinConfidence`, the operation returns labels and bounding boxes (if detected) with confidence values greater than or equal to 50 percent.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NotificationChannel](#API_StartLabelDetection_RequestSyntax) **   <a name="rekognition-StartLabelDetection-request-NotificationChannel"></a>
The Amazon SNS topic ARN you want Amazon Rekognition Video to publish the completion status of the label detection operation to. The Amazon SNS topic must have a topic name that begins with *AmazonRekognition* if you are using the AmazonRekognitionServiceRole permissions policy.
Type: [NotificationChannel](API_NotificationChannel.md) object
Required: No

 ** [Settings](#API_StartLabelDetection_RequestSyntax) **   <a name="rekognition-StartLabelDetection-request-Settings"></a>
The settings for a StartLabelDetection request.Contains the specified parameters for the label detection request of an asynchronous label analysis operation. Settings can include filters for GENERAL\_LABELS.
Type: [LabelDetectionSettings](API_LabelDetectionSettings.md) object
Required: No

 ** [Video](#API_StartLabelDetection_RequestSyntax) **   <a name="rekognition-StartLabelDetection-request-Video"></a>
The video in which you want to detect labels. The video must be stored in an Amazon S3 bucket.
Type: [Video](API_Video.md) object
Required: Yes

## Response Syntax
<a name="API_StartLabelDetection_ResponseSyntax"></a>

```
{
   "JobId": "string"
}
```

## Response Elements
<a name="API_StartLabelDetection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobId](#API_StartLabelDetection_ResponseSyntax) **   <a name="rekognition-StartLabelDetection-response-JobId"></a>
The identifier for the label detection job. Use `JobId` to identify the job in a subsequent call to `GetLabelDetection`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`

## Errors
<a name="API_StartLabelDetection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform the action.
HTTP Status Code: 400

 ** IdempotentParameterMismatchException **
A `ClientRequestToken` input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Rekognition experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterException **
Input parameter violated a constraint. Validate your parameter before calling the API operation again.
HTTP Status Code: 400

 ** InvalidS3ObjectException **
Amazon Rekognition is unable to access the S3 object specified in the request.
HTTP Status Code: 400

 ** LimitExceededException **
An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: `StartLabelDetection`) will raise a `LimitExceededException` exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.
HTTP Status Code: 400

 ** ThrottlingException **
Amazon Rekognition is temporarily unable to process the request. Try your call again.
HTTP Status Code: 500

 ** VideoTooLargeException **
The file size or duration of the supplied media is too large. The maximum file size is 10GB. The maximum duration is 6 hours.
HTTP Status Code: 400

## See Also
<a name="API_StartLabelDetection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/StartLabelDetection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/StartLabelDetection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/StartLabelDetection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/StartLabelDetection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/StartLabelDetection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/StartLabelDetection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/StartLabelDetection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/StartLabelDetection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/StartLabelDetection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/StartLabelDetection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
