---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RemoveFlowMediaStream.html
---

# RemoveFlowMediaStream
<a name="API_RemoveFlowMediaStream"></a>

 Removes a media stream from a flow. This action is only available if the media stream is not associated with a source or output.

## Request Syntax
<a name="API_RemoveFlowMediaStream_RequestSyntax"></a>

```
DELETE /v1/flows/{{flowArn}}/mediaStreams/{{mediaStreamName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_RemoveFlowMediaStream_RequestParameters"></a>

The request uses the following URI parameters.

 ** [flowArn](#API_RemoveFlowMediaStream_RequestSyntax) **   <a name="mediaconnect-RemoveFlowMediaStream-request-uri-flowArn"></a>
 The Amazon Resource Name (ARN) of the flow that you want to update.
Pattern: `arn:.+:mediaconnect.+:flow:.+`
Required: Yes

 ** [mediaStreamName](#API_RemoveFlowMediaStream_RequestSyntax) **   <a name="mediaconnect-RemoveFlowMediaStream-request-uri-mediaStreamName"></a>
 The name of the media stream that you want to remove.
Required: Yes

## Request Body
<a name="API_RemoveFlowMediaStream_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_RemoveFlowMediaStream_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "flowArn": "string",
   "mediaStreamName": "string"
}
```

## Response Elements
<a name="API_RemoveFlowMediaStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [flowArn](#API_RemoveFlowMediaStream_ResponseSyntax) **   <a name="mediaconnect-RemoveFlowMediaStream-response-flowArn"></a>
 The ARN of the flow that was updated.
Type: String

 ** [mediaStreamName](#API_RemoveFlowMediaStream_ResponseSyntax) **   <a name="mediaconnect-RemoveFlowMediaStream-response-mediaStreamName"></a>
 The name of the media stream that was removed.
Type: String

## Errors
<a name="API_RemoveFlowMediaStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

 ** ForbiddenException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerErrorException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is currently unavailable or busy.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_RemoveFlowMediaStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/RemoveFlowMediaStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/RemoveFlowMediaStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RemoveFlowMediaStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/RemoveFlowMediaStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RemoveFlowMediaStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/RemoveFlowMediaStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/RemoveFlowMediaStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/RemoveFlowMediaStream)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/RemoveFlowMediaStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RemoveFlowMediaStream)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
