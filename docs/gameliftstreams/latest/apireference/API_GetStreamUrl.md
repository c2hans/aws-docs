---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamUrl.html
---

# GetStreamUrl
<a name="API_GetStreamUrl"></a>

Retrieves properties for a stream URL, including its current status, usage, and the stream sessions started through it.

If you delete the stream group or application that backs the stream URL, this operation updates the status of the stream URL to `REVOKED`.

## Request Syntax
<a name="API_GetStreamUrl_RequestSyntax"></a>

```
GET /streamgroups/{{Identifier}}/streamurls/{{StreamUrlIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetStreamUrl_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_GetStreamUrl_RequestSyntax) **   <a name="gameliftstreams-GetStreamUrl-request-uri-Identifier"></a>
An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the stream group resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`. Example ID: `sg-1AB2C3De4`.
This is the stream group that owns the stream URL.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

 ** [StreamUrlIdentifier](#API_GetStreamUrl_RequestSyntax) **   <a name="gameliftstreams-GetStreamUrl-request-uri-StreamUrlIdentifier"></a>
The unique identifier of the stream URL. Specify a stream URL ID or Amazon Resource Name (ARN). Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamurl/sg-1AB2C3De4/su-1AB2C3De4`. Example ID: `su-1AB2C3De4`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

## Request Body
<a name="API_GetStreamUrl_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetStreamUrl_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AdditionalEnvironmentVariables": {
      "string" : "string"
   },
   "AdditionalLaunchArgs": [ "string" ],
   "ApplicationArn": "string",
   "Arn": "string",
   "CreatedAt": number,
   "Description": "string",
   "DisplayConfiguration": {
      "Resolution": {
         "Height": number,
         "Width": number
      }
   },
   "ExpiresAt": number,
   "Locations": [ "string" ],
   "Protocol": "string",
   "RemainingUses": number,
   "RoleArn": "string",
   "SessionLengthSeconds": number,
   "Status": "string",
   "StatusReason": "string",
   "StreamGroupArn": "string",
   "StreamSessions": [
      {
         "ApplicationArn": "string",
         "Arn": "string",
         "CreatedAt": number,
         "ExportFilesMetadata": {
            "OutputUri": "string",
            "Status": "string",
            "StatusReason": "string"
         },
         "LastUpdatedAt": number,
         "Location": "string",
         "Protocol": "string",
         "RoleArn": "string",
         "Status": "string",
         "StatusReason": "string",
         "UserId": "string"
      }
   ],
   "StreamUrl": "string",
   "StreamUrlId": "string",
   "UsageLimit": number
}
```

## Response Elements
<a name="API_GetStreamUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-GetStreamUrl-response-Arn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the stream URL across all AWS Regions. Format is `arn:aws:gameliftstreams:[AWS Region]:[AWS account]:streamurl/[stream group resource ID]/[stream URL resource ID]`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)`

 ** [AdditionalEnvironmentVariables](#API_GetStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-GetStreamUrl-response-AdditionalEnvironmentVariables"></a>
The environment variables made available to the application when a stream session starts.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[_a-zA-Z][_a-zA-Z0-9]*`
Value Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [AdditionalLaunchArgs](#API_GetStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-GetStreamUrl-response-AdditionalLaunchArgs"></a>
The command-line arguments passed to the application when a stream session starts.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [ApplicationArn](#API_GetStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-GetStreamUrl-response-ApplicationArn"></a>
The application that runs in the stream sessions.
This value is an [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the application resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)`

 ** [CreatedAt](#API_GetStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-GetStreamUrl-response-CreatedAt"></a>
A timestamp that indicates when this resource was created. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).
Type: Timestamp

 ** [Description](#API_GetStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-GetStreamUrl-response-Description"></a>
The descriptive label for the stream URL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[a-zA-Z0-9-_.!+@/][a-zA-Z0-9-_.!+@/ ]*`

 ** [DisplayConfiguration](#API_GetStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-GetStreamUrl-response-DisplayConfiguration"></a>
The display settings, such as resolution, for stream sessions started from this stream URL.
Type: [DisplayConfiguration](API_DisplayConfiguration.md) object

 ** [ExpiresAt](#API_GetStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-GetStreamUrl-response-ExpiresAt"></a>
The date and time when the stream URL expires and stops accepting new stream sessions. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).
Type: Timestamp

 ** [Locations](#API_GetStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-GetStreamUrl-response-Locations"></a>
The list of locations, in order of preference, where Amazon GameLift Streams places the stream session. For a complete list of locations that Amazon GameLift Streams supports, refer to [Regions, quotas, and limitations](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html) in the *Amazon GameLift Streams Developer Guide*.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[a-zA-Z0-9-]+`

 ** [Protocol](#API_GetStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-GetStreamUrl-response-Protocol"></a>
The data transport protocol used for stream sessions started from this stream URL.
Type: String
Valid Values: `WebRTC`

 ** [RemainingUses](#API_GetStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-GetStreamUrl-response-RemainingUses"></a>
The number of times the stream URL can still be used to start a stream session.
Type: Integer
Valid Range: Minimum value of 0.

 ** [RoleArn](#API_GetStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-GetStreamUrl-response-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that Amazon GameLift Streams assumes during stream sessions started from this stream URL. For more information, see [Provide AWS credentials to your streaming application](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/session-credentials.html) in the *Amazon GameLift Streams Developer Guide*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-zA-Z-]*:iam::\d{12}:role/.+`

 ** [SessionLengthSeconds](#API_GetStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-GetStreamUrl-response-SessionLengthSeconds"></a>
The maximum length of time, in seconds, that a stream session started from this stream URL can run.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 86400.

 ** [Status](#API_GetStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-GetStreamUrl-response-Status"></a>
The current status of the stream URL. Possible statuses include the following:
+  `ACTIVE`: The stream URL is valid and can start stream sessions.
+  `EXPIRED`: The stream URL has passed its expiration time and can no longer start stream sessions.
+  `REVOKED`: The stream URL was revoked and can no longer start stream sessions.
+  `LIMIT_REACHED`: The stream URL has been used the maximum number of times and can no longer start stream sessions.
Type: String
Valid Values: `ACTIVE | EXPIRED | REVOKED | LIMIT_REACHED`

 ** [StatusReason](#API_GetStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-GetStreamUrl-response-StatusReason"></a>
Additional information about why the stream URL is in its current status. Amazon GameLift Streams populates this value when the status is `REVOKED`. Possible values include the following:
+  `userRevoked`: You revoked the stream URL.
+  `revokedAndTerminatingSessions`: You revoked the stream URL and Amazon GameLift Streams is ending its running stream sessions.
+  `revokedAndSessionsTerminated`: You revoked the stream URL and its running stream sessions have ended.
+  `streamGroupDeleted`: The stream group was deleted, which revoked the stream URL.
+  `applicationDeleted`: The application was deleted, which revoked the stream URL.
Type: String
Valid Values: `userRevoked | revokedAndTerminatingSessions | revokedAndSessionsTerminated | streamGroupDeleted | applicationDeleted`

 ** [StreamGroupArn](#API_GetStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-GetStreamUrl-response-StreamGroupArn"></a>
The stream group that runs the stream sessions.
This value is an [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the stream group resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)`

 ** [StreamSessions](#API_GetStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-GetStreamUrl-response-StreamSessions"></a>
A list of the stream sessions that have been started through this stream URL.
Type: Array of [StreamSessionSummary](API_StreamSessionSummary.md) objects

 ** [StreamUrl](#API_GetStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-GetStreamUrl-response-StreamUrl"></a>
The shareable stream URL. Distribute this URL to end users so that they can start and play a stream session in a hosted web player. Treat the stream URL as a secret. Anyone who has it can start a stream session until the stream URL expires, is revoked, or reaches its usage limit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [StreamUrlId](#API_GetStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-GetStreamUrl-response-StreamUrlId"></a>
The unique identifier for the stream URL resource, for example `su-1AB2C3De4`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9-]+`

 ** [UsageLimit](#API_GetStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-GetStreamUrl-response-UsageLimit"></a>
The maximum number of times the stream URL can start a stream session.
Type: Integer
Valid Range: Minimum value of 1.

## Errors
<a name="API_GetStreamUrl_Errors"></a>

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
<a name="API_GetStreamUrl_Examples"></a>

### Get details for a Stream URL (AWS CLI)
<a name="API_GetStreamUrl_Example_1"></a>

The following AWS CLI command retrieves properties for a stream URL.

#### Sample Request
<a name="API_GetStreamUrl_Example_1_Request"></a>

```
aws gameliftstreams get-stream-url \
  --identifier sg-1AB2C3De4 \
  --stream-url-identifier su-1AB2C3De4
```

## See Also
<a name="API_GetStreamUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gameliftstreams-2018-05-10/GetStreamUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gameliftstreams-2018-05-10/GetStreamUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/GetStreamUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gameliftstreams-2018-05-10/GetStreamUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/GetStreamUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gameliftstreams-2018-05-10/GetStreamUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gameliftstreams-2018-05-10/GetStreamUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gameliftstreams-2018-05-10/GetStreamUrl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gameliftstreams-2018-05-10/GetStreamUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/GetStreamUrl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftstreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
