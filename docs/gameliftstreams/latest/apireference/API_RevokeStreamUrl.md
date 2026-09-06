---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_RevokeStreamUrl.html
---

# RevokeStreamUrl
<a name="API_RevokeStreamUrl"></a>

Revokes a stream URL so that it can no longer start new stream sessions. By default, stream sessions that are already running continue until they end on their own. To also end running sessions, set `RevocationMode` to `REVOKE_AND_TERMINATE_SESSIONS`.

Revoking a stream URL is permanent. The status of the stream URL changes to `REVOKED`.

## Request Syntax
<a name="API_RevokeStreamUrl_RequestSyntax"></a>

```
POST /streamgroups/{{Identifier}}/streamurls/{{StreamUrlIdentifier}}/revoke HTTP/1.1
Content-type: application/json

{
   "RevocationMode": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RevokeStreamUrl_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_RevokeStreamUrl_RequestSyntax) **   <a name="gameliftstreams-RevokeStreamUrl-request-uri-Identifier"></a>
An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the stream group resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`. Example ID: `sg-1AB2C3De4`.
This is the stream group that owns the stream URL.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

 ** [StreamUrlIdentifier](#API_RevokeStreamUrl_RequestSyntax) **   <a name="gameliftstreams-RevokeStreamUrl-request-uri-StreamUrlIdentifier"></a>
The unique identifier of the stream URL to revoke. Specify a stream URL ID or Amazon Resource Name (ARN). Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamurl/sg-1AB2C3De4/su-1AB2C3De4`. Example ID: `su-1AB2C3De4`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

## Request Body
<a name="API_RevokeStreamUrl_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [RevocationMode](#API_RevokeStreamUrl_RequestSyntax) **   <a name="gameliftstreams-RevokeStreamUrl-request-RevocationMode"></a>
Controls what happens to running stream sessions when you revoke the stream URL. If you do not specify a value, the default is `REVOKE_URL`. Possible values include the following:
+  `REVOKE_URL`: Stops the stream URL from starting new stream sessions. Running sessions continue until they end.
+  `REVOKE_AND_TERMINATE_SESSIONS`: Stops new stream sessions and ends any running stream sessions.
Type: String
Valid Values: `REVOKE_URL | REVOKE_AND_TERMINATE_SESSIONS`
Required: No

## Response Syntax
<a name="API_RevokeStreamUrl_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_RevokeStreamUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_RevokeStreamUrl_Errors"></a>

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

## Examples
<a name="API_RevokeStreamUrl_Examples"></a>

### Revoke a Stream URL (AWS CLI)
<a name="API_RevokeStreamUrl_Example_1"></a>

The following AWS CLI command revokes a stream URL.

#### Sample Request
<a name="API_RevokeStreamUrl_Example_1_Request"></a>

```
aws gameliftstreams revoke-stream-url \
  --identifier sg-1AB2C3De4 \
  --stream-url-identifier su-1AB2C3De4
```

## See Also
<a name="API_RevokeStreamUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gameliftstreams-2018-05-10/RevokeStreamUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gameliftstreams-2018-05-10/RevokeStreamUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/RevokeStreamUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gameliftstreams-2018-05-10/RevokeStreamUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/RevokeStreamUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gameliftstreams-2018-05-10/RevokeStreamUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gameliftstreams-2018-05-10/RevokeStreamUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gameliftstreams-2018-05-10/RevokeStreamUrl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gameliftstreams-2018-05-10/RevokeStreamUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/RevokeStreamUrl)
