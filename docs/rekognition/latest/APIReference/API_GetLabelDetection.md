---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetLabelDetection.html
---

# GetLabelDetection
<a name="API_GetLabelDetection"></a>

Gets the label detection results of a Amazon Rekognition Video analysis started by [StartLabelDetection](API_StartLabelDetection.md).

The label detection operation is started by a call to [StartLabelDetection](API_StartLabelDetection.md) which returns a job identifier (`JobId`). When the label detection operation finishes, Amazon Rekognition publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to `StartlabelDetection`.

To get the results of the label detection operation, first check that the status value published to the Amazon SNS topic is `SUCCEEDED`. If so, call [GetLabelDetection](#API_GetLabelDetection) and pass the job identifier (`JobId`) from the initial call to `StartLabelDetection`.

 `GetLabelDetection` returns an array of detected labels (`Labels`) sorted by the time the labels were detected. You can also sort by the label name by specifying `NAME` for the `SortBy` input parameter. If there is no `NAME` specified, the default sort is by timestamp.

You can select how results are aggregated by using the `AggregateBy` input parameter. The default aggregation method is `TIMESTAMPS`. You can also aggregate by `SEGMENTS`, which aggregates all instances of labels detected in a given segment.

The returned Labels array may include the following attributes:
+ Name - The name of the detected label.
+ Confidence - The level of confidence in the label assigned to a detected object.
+ Parents - The ancestor labels for a detected label. GetLabelDetection returns a hierarchical taxonomy of detected labels. For example, a detected car might be assigned the label car. The label car has two parent labels: Vehicle (its parent) and Transportation (its grandparent). The response includes the all ancestors for a label, where every ancestor is a unique label. In the previous example, Car, Vehicle, and Transportation are returned as unique labels in the response.
+  Aliases - Possible Aliases for the label.
+ Categories - The label categories that the detected label belongs to.
+ BoundingBox — Bounding boxes are described for all instances of detected common object labels, returned in an array of Instance objects. An Instance object contains a BoundingBox object, describing the location of the label on the input image. It also includes the confidence for the accuracy of the detected bounding box.
+ Timestamp - Time, in milliseconds from the start of the video, that the label was detected. For aggregation by `SEGMENTS`, the `StartTimestampMillis`, `EndTimestampMillis`, and `DurationMillis` structures are what define a segment. Although the “Timestamp” structure is still returned with each label, its value is set to be the same as `StartTimestampMillis`.

Timestamp and Bounding box information are returned for detected Instances, only if aggregation is done by `TIMESTAMPS`. If aggregating by `SEGMENTS`, information about detected instances isn’t returned.

The version of the label model used for the detection is also returned.

 **Note `DominantColors` isn't returned for `Instances`, although it is shown as part of the response in the sample seen below.**

Use `MaxResults` parameter to limit the number of labels returned. If there are more results than specified in `MaxResults`, the value of `NextToken` in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call `GetlabelDetection` and populate the `NextToken` request parameter with the token value returned from the previous call to `GetLabelDetection`.

If you are retrieving results while using the Amazon Simple Notification Service, note that you will receive an "ERROR" notification if the job encounters an issue.

## Request Syntax
<a name="API_GetLabelDetection_RequestSyntax"></a>

```
{
   "AggregateBy": "{{string}}",
   "JobId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortBy": "{{string}}"
}
```

## Request Parameters
<a name="API_GetLabelDetection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AggregateBy](#API_GetLabelDetection_RequestSyntax) **   <a name="rekognition-GetLabelDetection-request-AggregateBy"></a>
Defines how to aggregate the returned results. Results can be aggregated by timestamps or segments.
Type: String
Valid Values: `TIMESTAMPS | SEGMENTS`
Required: No

 ** [JobId](#API_GetLabelDetection_RequestSyntax) **   <a name="rekognition-GetLabelDetection-request-JobId"></a>
Job identifier for the label detection operation for which you want results returned. You get the job identifer from an initial call to `StartlabelDetection`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: Yes

 ** [MaxResults](#API_GetLabelDetection_RequestSyntax) **   <a name="rekognition-GetLabelDetection-request-MaxResults"></a>
Maximum number of results to return per paginated call. The largest value you can specify is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned. The default value is 1000.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_GetLabelDetection_RequestSyntax) **   <a name="rekognition-GetLabelDetection-request-NextToken"></a>
If the previous response was incomplete (because there are more labels to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of labels.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** [SortBy](#API_GetLabelDetection_RequestSyntax) **   <a name="rekognition-GetLabelDetection-request-SortBy"></a>
Sort to use for elements in the `Labels` array. Use `TIMESTAMP` to sort array elements by the time labels are detected. Use `NAME` to alphabetically group elements for a label together. Within each label group, the array element are sorted by detection confidence. The default sort is by `TIMESTAMP`.
Type: String
Valid Values: `NAME | TIMESTAMP`
Required: No

## Response Syntax
<a name="API_GetLabelDetection_ResponseSyntax"></a>

```
{
   "GetRequestMetadata": {
      "AggregateBy": "string",
      "SortBy": "string"
   },
   "JobId": "string",
   "JobStatus": "string",
   "JobTag": "string",
   "LabelModelVersion": "string",
   "Labels": [
      {
         "DurationMillis": number,
         "EndTimestampMillis": number,
         "Label": {
            "Aliases": [
               {
                  "Name": "string"
               }
            ],
            "Categories": [
               {
                  "Name": "string"
               }
            ],
            "Confidence": number,
            "Instances": [
               {
                  "BoundingBox": {
                     "Height": number,
                     "Left": number,
                     "Top": number,
                     "Width": number
                  },
                  "Confidence": number,
                  "DominantColors": [
                     {
                        "Blue": number,
                        "CSSColor": "string",
                        "Green": number,
                        "HexCode": "string",
                        "PixelPercent": number,
                        "Red": number,
                        "SimplifiedColor": "string"
                     }
                  ]
               }
            ],
            "Name": "string",
            "Parents": [
               {
                  "Name": "string"
               }
            ]
         },
         "StartTimestampMillis": number,
         "Timestamp": number
      }
   ],
   "NextToken": "string",
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
<a name="API_GetLabelDetection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GetRequestMetadata](#API_GetLabelDetection_ResponseSyntax) **   <a name="rekognition-GetLabelDetection-response-GetRequestMetadata"></a>
Information about the paramters used when getting a response. Includes information on aggregation and sorting methods.
Type: [GetLabelDetectionRequestMetadata](API_GetLabelDetectionRequestMetadata.md) object

 ** [JobId](#API_GetLabelDetection_ResponseSyntax) **   <a name="rekognition-GetLabelDetection-response-JobId"></a>
Job identifier for the label detection operation for which you want to obtain results. The job identifer is returned by an initial call to StartLabelDetection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`

 ** [JobStatus](#API_GetLabelDetection_ResponseSyntax) **   <a name="rekognition-GetLabelDetection-response-JobStatus"></a>
The current status of the label detection job.
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED | FAILED`

 ** [JobTag](#API_GetLabelDetection_ResponseSyntax) **   <a name="rekognition-GetLabelDetection-response-JobTag"></a>
A job identifier specified in the call to StartLabelDetection and returned in the job completion notification sent to your Amazon Simple Notification Service topic.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9_.\-:+=\/]+`

 ** [LabelModelVersion](#API_GetLabelDetection_ResponseSyntax) **   <a name="rekognition-GetLabelDetection-response-LabelModelVersion"></a>
Version number of the label detection model that was used to detect labels.
Type: String

 ** [Labels](#API_GetLabelDetection_ResponseSyntax) **   <a name="rekognition-GetLabelDetection-response-Labels"></a>
An array of labels detected in the video. Each element contains the detected label and the time, in milliseconds from the start of the video, that the label was detected.
Type: Array of [LabelDetection](API_LabelDetection.md) objects

 ** [NextToken](#API_GetLabelDetection_ResponseSyntax) **   <a name="rekognition-GetLabelDetection-response-NextToken"></a>
If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of labels.
Type: String
Length Constraints: Maximum length of 255.

 ** [StatusMessage](#API_GetLabelDetection_ResponseSyntax) **   <a name="rekognition-GetLabelDetection-response-StatusMessage"></a>
If the job fails, `StatusMessage` provides a descriptive error message.
Type: String

 ** [Video](#API_GetLabelDetection_ResponseSyntax) **   <a name="rekognition-GetLabelDetection-response-Video"></a>
Video file stored in an Amazon S3 bucket. Amazon Rekognition video start operations such as [StartLabelDetection](API_StartLabelDetection.md) use `Video` to specify a video for analysis. The supported file formats are .mp4, .mov and .avi.
Type: [Video](API_Video.md) object

 ** [VideoMetadata](#API_GetLabelDetection_ResponseSyntax) **   <a name="rekognition-GetLabelDetection-response-VideoMetadata"></a>
Information about a video that Amazon Rekognition Video analyzed. `Videometadata` is returned in every page of paginated responses from a Amazon Rekognition video operation.
Type: [VideoMetadata](API_VideoMetadata.md) object

## Errors
<a name="API_GetLabelDetection_Errors"></a>

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
<a name="API_GetLabelDetection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/GetLabelDetection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/GetLabelDetection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/GetLabelDetection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/GetLabelDetection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/GetLabelDetection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/GetLabelDetection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/GetLabelDetection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/GetLabelDetection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/GetLabelDetection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/GetLabelDetection)
