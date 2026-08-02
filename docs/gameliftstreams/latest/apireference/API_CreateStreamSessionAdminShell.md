---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamSessionAdminShell.html
---

# CreateStreamSessionAdminShell
<a name="API_CreateStreamSessionAdminShell"></a>

Creates an administrative terminal session with full access to the live runtime environment of the Amazon GameLift Streams stream session. Use the returned credentials (`SessionId`, `StreamUrl` and `TokenValue`) with the AWS Systems Manager [Session Manager plugin](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html) for the AWS CLI to access the terminal session.

The stream session must be in one of the following statuses: `ACTIVE`, `CONNECTED`, `PENDING_CLIENT_RECONNECTION`, or `RECONNECTING`.

The `StreamUrl` is valid for 60 seconds. After it expires, call this operation again to get a new URL.

**Important**
The returned credentials grant full access to the live runtime environment of the Amazon GameLift Streams stream session. The operator who connects to the terminal session has the same level of access that your Amazon GameLift Streams applications have, including potentially user input, screen images, and application data files. Grant permissions to call this operation only to trusted IAM identities that require live runtime environment access.

## Request Syntax
<a name="API_CreateStreamSessionAdminShell_RequestSyntax"></a>

```
POST /streamgroups/{{Identifier}}/streamsessions/{{StreamSessionIdentifier}}/access HTTP/1.1
```

## URI Request Parameters
<a name="API_CreateStreamSessionAdminShell_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_CreateStreamSessionAdminShell_RequestSyntax) **   <a name="gameliftstreams-CreateStreamSessionAdminShell-request-uri-Identifier"></a>
The stream group that runs this stream session.
This value is an [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the stream group resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`. Example ID: `sg-1AB2C3De4`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

 ** [StreamSessionIdentifier](#API_CreateStreamSessionAdminShell_RequestSyntax) **   <a name="gameliftstreams-CreateStreamSessionAdminShell-request-uri-StreamSessionIdentifier"></a>
An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the stream session resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamsession/sg-1AB2C3De4/ABC123def4567`. Example ID: `ABC123def4567`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

## Request Body
<a name="API_CreateStreamSessionAdminShell_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CreateStreamSessionAdminShell_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "SessionId": "string",
   "StreamUrl": "string",
   "TokenValue": "string"
}
```

## Response Elements
<a name="API_CreateStreamSessionAdminShell_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SessionId](#API_CreateStreamSessionAdminShell_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamSessionAdminShell-response-SessionId"></a>
An AWS Systems Manager session identifier that uniquely identifies the requested terminal session. Use this value with the AWS Systems Manager Session Manager plugin.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [StreamUrl](#API_CreateStreamSessionAdminShell_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamSessionAdminShell-response-StreamUrl"></a>
An AWS Systems Manager WebSocket connection endpoint for the requested terminal session.
Type: String

 ** [TokenValue](#API_CreateStreamSessionAdminShell_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamSessionAdminShell-response-TokenValue"></a>
An AWS Systems Manager authentication token that authenticates your access to the session ID and WebSocket URL. This token must be treated with the same level of security as other user credentials. The token value is only valid for establishing a new connection within 60 seconds of generation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

## Errors
<a name="API_CreateStreamSessionAdminShell_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.
 ** Message **
Description of the error.
HTTP Status Code: 403

 [InternalServerException](API_InternalServerException.md)
The service encountered an internal error and is unable to complete the request.
 ** Message **
Description of the error.
HTTP Status Code: 500

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
The resource specified in the request was not found. Correct the request before you try again.
 ** Message **
Description of the error.
HTTP Status Code: 404

 [StreamSessionAccessNotReadyException](API_StreamSessionAccessNotReadyException.md)
The terminal connection to the stream session is not yet available. Wait before retrying the request.
 ** Message **
Description of the error.
HTTP Status Code: 409

 [ThrottlingException](API_ThrottlingException.md)
The request was denied due to request throttling. Retry the request after the suggested wait time.
 ** Message **
Description of the error.
HTTP Status Code: 429

 [ValidationException](API_ValidationException.md)
One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.
 ** Message **
Description of the error.
HTTP Status Code: 400

## See Also
<a name="API_CreateStreamSessionAdminShell_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gameliftstreams-2018-05-10/CreateStreamSessionAdminShell)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gameliftstreams-2018-05-10/CreateStreamSessionAdminShell)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/CreateStreamSessionAdminShell)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gameliftstreams-2018-05-10/CreateStreamSessionAdminShell)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/CreateStreamSessionAdminShell)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gameliftstreams-2018-05-10/CreateStreamSessionAdminShell)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gameliftstreams-2018-05-10/CreateStreamSessionAdminShell)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gameliftstreams-2018-05-10/CreateStreamSessionAdminShell)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gameliftstreams-2018-05-10/CreateStreamSessionAdminShell)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/CreateStreamSessionAdminShell)
