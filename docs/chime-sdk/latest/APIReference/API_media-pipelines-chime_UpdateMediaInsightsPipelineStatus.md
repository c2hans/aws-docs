---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_UpdateMediaInsightsPipelineStatus.html
---

# UpdateMediaInsightsPipelineStatus
<a name="API_media-pipelines-chime_UpdateMediaInsightsPipelineStatus"></a>

Updates the status of a media insights pipeline.

## Request Syntax
<a name="API_media-pipelines-chime_UpdateMediaInsightsPipelineStatus_RequestSyntax"></a>

```
PUT /media-insights-pipeline-status/{{identifier}} HTTP/1.1
Content-type: application/json

{
   "UpdateStatus": "{{string}}"
}
```

## URI Request Parameters
<a name="API_media-pipelines-chime_UpdateMediaInsightsPipelineStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [identifier](#API_media-pipelines-chime_UpdateMediaInsightsPipelineStatus_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_UpdateMediaInsightsPipelineStatus-request-uri-Identifier"></a>
The unique identifier of the resource to be updated. Valid values include the ID and ARN of the media insights pipeline.
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_media-pipelines-chime_UpdateMediaInsightsPipelineStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [UpdateStatus](#API_media-pipelines-chime_UpdateMediaInsightsPipelineStatus_RequestSyntax) **   <a name="chimesdk-media-pipelines-chime_UpdateMediaInsightsPipelineStatus-request-UpdateStatus"></a>
The requested status of the media insights pipeline.
Type: String
Valid Values: `Pause | Resume`
Required: Yes

## Response Syntax
<a name="API_media-pipelines-chime_UpdateMediaInsightsPipelineStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_media-pipelines-chime_UpdateMediaInsightsPipelineStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_media-pipelines-chime_UpdateMediaInsightsPipelineStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 400

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 409

 ** ForbiddenException **
The client is permanently forbidden from making the request.
 ** RequestId **
The request id associated with the call responsible for the exception.
HTTP Status Code: 403

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
 ** RequestId **
The request ID associated with the call responsible for the exception.
HTTP Status Code: 404

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
<a name="API_media-pipelines-chime_UpdateMediaInsightsPipelineStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-media-pipelines-2021-07-15/UpdateMediaInsightsPipelineStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-media-pipelines-2021-07-15/UpdateMediaInsightsPipelineStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/UpdateMediaInsightsPipelineStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-media-pipelines-2021-07-15/UpdateMediaInsightsPipelineStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/UpdateMediaInsightsPipelineStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-media-pipelines-2021-07-15/UpdateMediaInsightsPipelineStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-media-pipelines-2021-07-15/UpdateMediaInsightsPipelineStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-media-pipelines-2021-07-15/UpdateMediaInsightsPipelineStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-media-pipelines-2021-07-15/UpdateMediaInsightsPipelineStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/UpdateMediaInsightsPipelineStatus)
