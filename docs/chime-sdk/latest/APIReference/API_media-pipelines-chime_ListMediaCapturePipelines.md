---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ListMediaCapturePipelines.html
---

# ListMediaCapturePipelines
<a name="API_media-pipelines-chime_ListMediaCapturePipelines"></a>

Returns a list of media pipelines.

## Request Syntax
<a name="API_media-pipelines-chime_ListMediaCapturePipelines_RequestSyntax"></a>

```
GET /sdk-media-capture-pipelines?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_media-pipelines-chime_ListMediaCapturePipelines_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_media-pipelines-chime_ListMediaCapturePipelines_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_ListMediaCapturePipelines-request-uri-MaxResults"></a>
The maximum number of results to return in a single call. Valid Range: 1 - 99.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_media-pipelines-chime_ListMediaCapturePipelines_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_ListMediaCapturePipelines-request-uri-NextToken"></a>
The token used to retrieve the next page of results.
Length Constraints: Maximum length of 4096.
Pattern: `.*`

## Request Body
<a name="API_media-pipelines-chime_ListMediaCapturePipelines_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_media-pipelines-chime_ListMediaCapturePipelines_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MediaCapturePipelines": [
      {
         "MediaPipelineArn": "string",
         "MediaPipelineId": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_media-pipelines-chime_ListMediaCapturePipelines_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MediaCapturePipelines](#API_media-pipelines-chime_ListMediaCapturePipelines_ResponseSyntax) **   <a name="chimesdk-media-pipelines-chime_ListMediaCapturePipelines-response-MediaCapturePipelines"></a>
The media pipeline objects in the list.
Type: Array of [MediaCapturePipelineSummary](API_media-pipelines-chime_MediaCapturePipelineSummary.md) objects

 ** [NextToken](#API_media-pipelines-chime_ListMediaCapturePipelines_ResponseSyntax) **   <a name="chimesdk-media-pipelines-chime_ListMediaCapturePipelines-response-NextToken"></a>
The token used to retrieve the next page of results.
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `.*`

## Errors
<a name="API_media-pipelines-chime_ListMediaCapturePipelines_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
 ** RequestId **
The request id associated with the call responsible for the exception.
HTTP Status Code: 403

 ** ResourceLimitExceededException **
The request exceeds the resource limit.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 400

 ** ServiceFailureException **
The service encountered an unexpected error.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 503

 ** ThrottledClientException **
The client exceeded its request rate limit.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client is not currently authorized to make the request.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 401

## See Also
<a name="API_media-pipelines-chime_ListMediaCapturePipelines_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-media-pipelines-2021-07-15/ListMediaCapturePipelines)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-media-pipelines-2021-07-15/ListMediaCapturePipelines)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/ListMediaCapturePipelines)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-media-pipelines-2021-07-15/ListMediaCapturePipelines)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/ListMediaCapturePipelines)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-media-pipelines-2021-07-15/ListMediaCapturePipelines)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-media-pipelines-2021-07-15/ListMediaCapturePipelines)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-media-pipelines-2021-07-15/ListMediaCapturePipelines)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-media-pipelines-2021-07-15/ListMediaCapturePipelines)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/ListMediaCapturePipelines)
