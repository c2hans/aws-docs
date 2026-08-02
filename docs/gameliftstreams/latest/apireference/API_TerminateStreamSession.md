---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TerminateStreamSession.html
---

# TerminateStreamSession
<a name="API_TerminateStreamSession"></a>

Permanently terminates an active stream session. When called, the stream session status changes to `TERMINATING`. You can terminate a stream session in any status except `ACTIVATING`. If the stream session is in `ACTIVATING` status, an exception is thrown.

## Request Syntax
<a name="API_TerminateStreamSession_RequestSyntax"></a>

```
DELETE /streamgroups/{{Identifier}}/streamsessions/{{StreamSessionIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_TerminateStreamSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_TerminateStreamSession_RequestSyntax) **   <a name="gameliftstreams-TerminateStreamSession-request-uri-Identifier"></a>
 [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the stream group resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`. Example ID: `sg-1AB2C3De4`.
The stream group that runs this stream session.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

 ** [StreamSessionIdentifier](#API_TerminateStreamSession_RequestSyntax) **   <a name="gameliftstreams-TerminateStreamSession-request-uri-StreamSessionIdentifier"></a>
 [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the stream session resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamsession/sg-1AB2C3De4/ABC123def4567`. Example ID: `ABC123def4567`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

## Request Body
<a name="API_TerminateStreamSession_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_TerminateStreamSession_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_TerminateStreamSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_TerminateStreamSession_Errors"></a>

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
<a name="API_TerminateStreamSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gameliftstreams-2018-05-10/TerminateStreamSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gameliftstreams-2018-05-10/TerminateStreamSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/TerminateStreamSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gameliftstreams-2018-05-10/TerminateStreamSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/TerminateStreamSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gameliftstreams-2018-05-10/TerminateStreamSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gameliftstreams-2018-05-10/TerminateStreamSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gameliftstreams-2018-05-10/TerminateStreamSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gameliftstreams-2018-05-10/TerminateStreamSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/TerminateStreamSession)
