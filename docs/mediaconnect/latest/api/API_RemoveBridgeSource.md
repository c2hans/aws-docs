---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RemoveBridgeSource.html
---

# RemoveBridgeSource
<a name="API_RemoveBridgeSource"></a>

 Removes a source from a bridge.

## Request Syntax
<a name="API_RemoveBridgeSource_RequestSyntax"></a>

```
DELETE /v1/bridges/{{bridgeArn}}/sources/{{sourceName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_RemoveBridgeSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [bridgeArn](#API_RemoveBridgeSource_RequestSyntax) **   <a name="mediaconnect-RemoveBridgeSource-request-uri-bridgeArn"></a>
 The Amazon Resource Name (ARN) of the bridge that you want to update.
Pattern: `arn:.+:mediaconnect.+:bridge:.+`
Required: Yes

 ** [sourceName](#API_RemoveBridgeSource_RequestSyntax) **   <a name="mediaconnect-RemoveBridgeSource-request-uri-sourceName"></a>
 The name of the bridge source that you want to remove.
Required: Yes

## Request Body
<a name="API_RemoveBridgeSource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_RemoveBridgeSource_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "bridgeArn": "string",
   "sourceName": "string"
}
```

## Response Elements
<a name="API_RemoveBridgeSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [bridgeArn](#API_RemoveBridgeSource_ResponseSyntax) **   <a name="mediaconnect-RemoveBridgeSource-response-bridgeArn"></a>
 The ARN of the bridge from which the source was removed.
Type: String

 ** [sourceName](#API_RemoveBridgeSource_ResponseSyntax) **   <a name="mediaconnect-RemoveBridgeSource-response-sourceName"></a>
 The name of the bridge source that was removed.
Type: String

## Errors
<a name="API_RemoveBridgeSource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
HTTP Status Code: 409

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
<a name="API_RemoveBridgeSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/RemoveBridgeSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/RemoveBridgeSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RemoveBridgeSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/RemoveBridgeSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RemoveBridgeSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/RemoveBridgeSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/RemoveBridgeSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/RemoveBridgeSource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/RemoveBridgeSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RemoveBridgeSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
