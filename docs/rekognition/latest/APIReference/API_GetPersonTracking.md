---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetPersonTracking.html
---

# GetPersonTracking
<a name="API_GetPersonTracking"></a>

**Note**
 *End of support notice:* On October 31, 2025, AWS will discontinue support for Amazon Rekognition People Pathing. After October 31, 2025, you will no longer be able to use the Rekognition People Pathing capability. For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/transitioning-from-amazon-rekognition-people-pathing-exploring-other-alternatives/).

Gets the path tracking results of a Amazon Rekognition Video analysis started by [StartPersonTracking](API_StartPersonTracking.md).

The person path tracking operation is started by a call to `StartPersonTracking` which returns a job identifier (`JobId`). When the operation finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to `StartPersonTracking`.

To get the results of the person path tracking operation, first check that the status value published to the Amazon SNS topic is `SUCCEEDED`. If so, call [GetPersonTracking](#API_GetPersonTracking) and pass the job identifier (`JobId`) from the initial call to `StartPersonTracking`.

 `GetPersonTracking` returns an array, `Persons`, of tracked persons and the time(s) their paths were tracked in the video.

**Note**
 `GetPersonTracking` only returns the default facial attributes (`BoundingBox`, `Confidence`, `Landmarks`, `Pose`, and `Quality`). The other facial attributes listed in the `Face` object of the following response syntax are not returned.
For more information, see [FaceDetail](API_FaceDetail.md).

By default, the array is sorted by the time(s) a person's path is tracked in the video. You can sort by tracked persons by specifying `INDEX` for the `SortBy` input parameter.

Use the `MaxResults` parameter to limit the number of items returned. If there are more results than specified in `MaxResults`, the value of `NextToken` in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call `GetPersonTracking` and populate the `NextToken` request parameter with the token value returned from the previous call to `GetPersonTracking`.

## Request Syntax
<a name="API_GetPersonTracking_RequestSyntax"></a>

```
{
   "JobId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortBy": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPersonTracking_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobId](#API_GetPersonTracking_RequestSyntax) **   <a name="rekognition-GetPersonTracking-request-JobId"></a>
The identifier for a job that tracks persons in a video. You get the `JobId` from a call to `StartPersonTracking`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: Yes

 ** [MaxResults](#API_GetPersonTracking_RequestSyntax) **   <a name="rekognition-GetPersonTracking-request-MaxResults"></a>
Maximum number of results to return per paginated call. The largest value you can specify is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned. The default value is 1000.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_GetPersonTracking_RequestSyntax) **   <a name="rekognition-GetPersonTracking-request-NextToken"></a>
If the previous response was incomplete (because there are more persons to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of persons.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** [SortBy](#API_GetPersonTracking_RequestSyntax) **   <a name="rekognition-GetPersonTracking-request-SortBy"></a>
Sort to use for elements in the `Persons` array. Use `TIMESTAMP` to sort array elements by the time persons are detected. Use `INDEX` to sort by the tracked persons. If you sort by `INDEX`, the array elements for each person are sorted by detection confidence. The default sort is by `TIMESTAMP`.
Type: String
Valid Values: `INDEX | TIMESTAMP`
Required: No

## Response Syntax
<a name="API_GetPersonTracking_ResponseSyntax"></a>

```
{
   "JobId": "string",
   "JobStatus": "string",
   "JobTag": "string",
   "NextToken": "string",
   "Persons": [
      {
         "Person": {
            "BoundingBox": {
               "Height": number,
               "Left": number,
               "Top": number,
               "Width": number
            },
            "Face": {
               "AgeRange": {
                  "High": number,
                  "Low": number
               },
               "Beard": {
                  "Confidence": number,
                  "Value": boolean
               },
               "BoundingBox": {
                  "Height": number,
                  "Left": number,
                  "Top": number,
                  "Width": number
               },
               "Confidence": number,
               "Emotions": [
                  {
                     "Confidence": number,
                     "Type": "string"
                  }
               ],
               "EyeDirection": {
                  "Confidence": number,
                  "Pitch": number,
                  "Yaw": number
               },
               "Eyeglasses": {
                  "Confidence": number,
                  "Value": boolean
               },
               "EyesOpen": {
                  "Confidence": number,
                  "Value": boolean
               },
               "FaceOccluded": {
                  "Confidence": number,
                  "Value": boolean
               },
               "Gender": {
                  "Confidence": number,
                  "Value": "string"
               },
               "Landmarks": [
                  {
                     "Type": "string",
                     "X": number,
                     "Y": number
                  }
               ],
               "MouthOpen": {
                  "Confidence": number,
                  "Value": boolean
               },
               "Mustache": {
                  "Confidence": number,
                  "Value": boolean
               },
               "Pose": {
                  "Pitch": number,
                  "Roll": number,
                  "Yaw": number
               },
               "Quality": {
                  "Brightness": number,
                  "Sharpness": number
               },
               "Smile": {
                  "Confidence": number,
                  "Value": boolean
               },
               "Sunglasses": {
                  "Confidence": number,
                  "Value": boolean
               }
            },
            "Index": number
         },
         "Timestamp": number
      }
   ],
   "StatusMessage": "string",
   "Video": {
      "S3Object": {
         "Bucket": "string",
         "Name": "string",
         "Version": "string"
      }
   },
   "VideoMetadata": {
      "Codec": "string",
      "ColorRange": "string",
      "DurationMillis": number,
      "Format": "string",
      "FrameHeight": number,
      "FrameRate": number,
      "FrameWidth": number
   }
}
```

## Response Elements
<a name="API_GetPersonTracking_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobId](#API_GetPersonTracking_ResponseSyntax) **   <a name="rekognition-GetPersonTracking-response-JobId"></a>
Job identifier for the person tracking operation for which you want to obtain results. The job identifer is returned by an initial call to StartPersonTracking.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`

 ** [JobStatus](#API_GetPersonTracking_ResponseSyntax) **   <a name="rekognition-GetPersonTracking-response-JobStatus"></a>
The current status of the person tracking job.
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED | FAILED`

 ** [JobTag](#API_GetPersonTracking_ResponseSyntax) **   <a name="rekognition-GetPersonTracking-response-JobTag"></a>
A job identifier specified in the call to StartCelebrityRecognition and returned in the job completion notification sent to your Amazon Simple Notification Service topic.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9_.\-:+=\/]+`

 ** [NextToken](#API_GetPersonTracking_ResponseSyntax) **   <a name="rekognition-GetPersonTracking-response-NextToken"></a>
If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of persons.
Type: String
Length Constraints: Maximum length of 255.

 ** [Persons](#API_GetPersonTracking_ResponseSyntax) **   <a name="rekognition-GetPersonTracking-response-Persons"></a>
An array of the persons detected in the video and the time(s) their path was tracked throughout the video. An array element will exist for each time a person's path is tracked.
Type: Array of [PersonDetection](API_PersonDetection.md) objects

 ** [StatusMessage](#API_GetPersonTracking_ResponseSyntax) **   <a name="rekognition-GetPersonTracking-response-StatusMessage"></a>
If the job fails, `StatusMessage` provides a descriptive error message.
Type: String

 ** [Video](#API_GetPersonTracking_ResponseSyntax) **   <a name="rekognition-GetPersonTracking-response-Video"></a>
Video file stored in an Amazon S3 bucket. Amazon Rekognition video start operations such as [StartLabelDetection](API_StartLabelDetection.md) use `Video` to specify a video for analysis. The supported file formats are .mp4, .mov and .avi.
Type: [Video](API_Video.md) object

 ** [VideoMetadata](#API_GetPersonTracking_ResponseSyntax) **   <a name="rekognition-GetPersonTracking-response-VideoMetadata"></a>
Information about a video that Amazon Rekognition Video analyzed. `Videometadata` is returned in every page of paginated responses from a Amazon Rekognition Video operation.
Type: [VideoMetadata](API_VideoMetadata.md) object

## Errors
<a name="API_GetPersonTracking_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform the action.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Rekognition experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidPaginationTokenException **
Pagination token in the request is not valid.
HTTP Status Code: 400

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
<a name="API_GetPersonTracking_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/GetPersonTracking)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/GetPersonTracking)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/GetPersonTracking)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/GetPersonTracking)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/GetPersonTracking)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/GetPersonTracking)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/GetPersonTracking)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/GetPersonTracking)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/GetPersonTracking)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/GetPersonTracking)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
