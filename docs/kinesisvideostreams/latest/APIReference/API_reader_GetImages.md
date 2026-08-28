---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_reader_GetImages.html
---

# GetImages
<a name="API_reader_GetImages"></a>

Managed support for images provides a fully managed way to get images from the video data streamed and stored in Kinesis Video Streams. You can use images to run machine learning (ML) workloads such as person, pet, or vehicle detection. Images can also be used to add interactive elements to playback, such as image previews for motion events and scrubbing for a video clip.

GetImages also retrieves a list of images corresponding to each timestamp for a given time range, sampling interval, and image format configuration.

**Note**
You must first call the `GetDataEndpoint` API to get an endpoint. Then send the `GetImages` requests to this endpoint using the [--endpoint-url parameter](https://docs.aws.amazon.com/cli/latest/reference/).

 [Video playback track requirements](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/video-playback-requirements.html).

## Request Syntax
<a name="API_reader_GetImages_RequestSyntax"></a>

```
POST /getImages HTTP/1.1
Content-type: application/json

{
   "EndTimestamp": {{number}},
   "Format": "{{string}}",
   "FormatConfig": {
      "{{string}}" : "{{string}}"
   },
   "HeightPixels": {{number}},
   "ImageSelectorType": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SamplingInterval": {{number}},
   "StartTimestamp": {{number}},
   "StreamARN": "{{string}}",
   "StreamName": "{{string}}",
   "WidthPixels": {{number}}
}
```

## URI Request Parameters
<a name="API_reader_GetImages_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_reader_GetImages_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EndTimestamp](#API_reader_GetImages_RequestSyntax) **   <a name="KinesisVideo-reader_GetImages-request-EndTimestamp"></a>
The end timestamp for the range of images to be generated. If the time range between `StartTimestamp` and `EndTimestamp` is more than 300 seconds above `StartTimestamp`, you will receive an `IllegalArgumentException`.
Type: Timestamp
Required: Yes

 ** [Format](#API_reader_GetImages_RequestSyntax) **   <a name="KinesisVideo-reader_GetImages-request-Format"></a>
The format that will be used to encode the image.
Type: String
Valid Values: `JPEG | PNG`
Required: Yes

 ** [FormatConfig](#API_reader_GetImages_RequestSyntax) **   <a name="KinesisVideo-reader_GetImages-request-FormatConfig"></a>
The list of a key-value pair structure that contains extra parameters that can be applied when the image is generated. The `FormatConfig` key is the `JPEGQuality`, which indicates the JPEG quality key to be used to generate the image. The `FormatConfig` value accepts ints from 1 to 100. If the value is 1, the image will be generated with less quality and the best compression. If the value is 100, the image will be generated with the best quality and less compression. If no value is provided, the default value of the `JPEGQuality` key will be set to 80.
Type: String to string map
Map Entries: Maximum number of 1 item.
Valid Keys: `JPEGQuality`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^[a-zA-Z_0-9]+`
Required: No

 ** [HeightPixels](#API_reader_GetImages_RequestSyntax) **   <a name="KinesisVideo-reader_GetImages-request-HeightPixels"></a>
The height of the output image that is used in conjunction with the `WidthPixels` parameter. When both `HeightPixels` and `WidthPixels` parameters are provided, the image will be stretched to fit the specified aspect ratio. If only the `HeightPixels` parameter is provided, its original aspect ratio will be used to calculate the `WidthPixels` ratio. If neither parameter is provided, the original image size will be returned.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2160.
Required: No

 ** [ImageSelectorType](#API_reader_GetImages_RequestSyntax) **   <a name="KinesisVideo-reader_GetImages-request-ImageSelectorType"></a>
The origin of the Server or Producer timestamps to use to generate the images.
Type: String
Valid Values: `PRODUCER_TIMESTAMP | SERVER_TIMESTAMP`
Required: Yes

 ** [MaxResults](#API_reader_GetImages_RequestSyntax) **   <a name="KinesisVideo-reader_GetImages-request-MaxResults"></a>
The maximum number of images to be returned by the API.
The default limit is 25 images per API response. Providing a `MaxResults` greater than this value will result in a page size of 25. Any additional results will be paginated.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_reader_GetImages_RequestSyntax) **   <a name="KinesisVideo-reader_GetImages-request-NextToken"></a>
A token that specifies where to start paginating the next set of Images. This is the `GetImages:NextToken` from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[a-zA-Z0-9+/]+={0,2}`
Required: No

 ** [SamplingInterval](#API_reader_GetImages_RequestSyntax) **   <a name="KinesisVideo-reader_GetImages-request-SamplingInterval"></a>
The time interval in milliseconds (ms) at which the images need to be generated from the stream. The minimum value that can be provided is 200 ms (5 images per second). If the timestamp range is less than the sampling interval, the image from the `startTimestamp` will be returned if available.
Type: Integer
Required: No

 ** [StartTimestamp](#API_reader_GetImages_RequestSyntax) **   <a name="KinesisVideo-reader_GetImages-request-StartTimestamp"></a>
The starting point from which the images should be generated. This `StartTimestamp` must be within an inclusive range of timestamps for an image to be returned.
Type: Timestamp
Required: Yes

 ** [StreamARN](#API_reader_GetImages_RequestSyntax) **   <a name="KinesisVideo-reader_GetImages-request-StreamARN"></a>
The Amazon Resource Name (ARN) of the stream from which to retrieve the images. You must specify either the `StreamName` or the `StreamARN`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`
Required: No

 ** [StreamName](#API_reader_GetImages_RequestSyntax) **   <a name="KinesisVideo-reader_GetImages-request-StreamName"></a>
The name of the stream from which to retrieve the images. You must specify either the `StreamName` or the `StreamARN`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** [WidthPixels](#API_reader_GetImages_RequestSyntax) **   <a name="KinesisVideo-reader_GetImages-request-WidthPixels"></a>
The width of the output image that is used in conjunction with the `HeightPixels` parameter. When both `WidthPixels` and `HeightPixels` parameters are provided, the image will be stretched to fit the specified aspect ratio. If only the `WidthPixels` parameter is provided or if only the `HeightPixels` is provided, a `ValidationException` will be thrown. If neither parameter is provided, the original image size from the stream will be returned.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 3840.
Required: No

## Response Syntax
<a name="API_reader_GetImages_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Images": [
      {
         "Error": "string",
         "ImageContent": "string",
         "TimeStamp": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_reader_GetImages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Images](#API_reader_GetImages_ResponseSyntax) **   <a name="KinesisVideo-reader_GetImages-response-Images"></a>
The list of images generated from the video stream. If there is no media available for the given timestamp, the `NO_MEDIA` error will be listed in the output. If an error occurs while the image is being generated, the `MEDIA_ERROR` will be listed in the output as the cause of the missing image.
Type: Array of [Image](API_reader_Image.md) objects

 ** [NextToken](#API_reader_GetImages_ResponseSyntax) **   <a name="KinesisVideo-reader_GetImages-response-NextToken"></a>
The encrypted token that was used in the request to get more images.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[a-zA-Z0-9+/]+={0,2}`

## Errors
<a name="API_reader_GetImages_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClientLimitExceededException **
Kinesis Video Streams has throttled the request because you have exceeded a limit. Try making the call later. For information about limits, see [Kinesis Video Streams quotas](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/limits.html).
HTTP Status Code: 400

 ** InvalidArgumentException **
A specified parameter exceeds its restrictions, is not supported, or can't be used.
HTTP Status Code: 400

 ** NoDataRetentionException **
 `GetImages` was requested for a stream that does not retain data (that is, has a `DataRetentionInHours` of 0).
HTTP Status Code: 400

 ** NotAuthorizedException **
Status Code: 403, The caller is not authorized to perform an operation on the given stream, or the token has expired.
HTTP Status Code: 401

 ** ResourceNotFoundException **
 `GetImages` will throw this error when Kinesis Video Streams can't find the stream that you specified.
 `GetHLSStreamingSessionURL` and `GetDASHStreamingSessionURL` throw this error if a session with a `PlaybackMode` of `ON_DEMAND` or `LIVE_REPLAY` is requested for a stream that has no fragments within the requested time range, or if a session with a `PlaybackMode` of `LIVE` is requested for a stream that has no fragments within the last 30 seconds.
HTTP Status Code: 404

## See Also
<a name="API_reader_GetImages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-video-reader-data-2017-09-30/GetImages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-video-reader-data-2017-09-30/GetImages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-video-reader-data-2017-09-30/GetImages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-video-reader-data-2017-09-30/GetImages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-video-reader-data-2017-09-30/GetImages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-video-reader-data-2017-09-30/GetImages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-video-reader-data-2017-09-30/GetImages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-video-reader-data-2017-09-30/GetImages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesis-video-reader-data-2017-09-30/GetImages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-video-reader-data-2017-09-30/GetImages)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
