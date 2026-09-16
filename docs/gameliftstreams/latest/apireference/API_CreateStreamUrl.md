---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamUrl.html
---

# CreateStreamUrl
<a name="API_CreateStreamUrl"></a>

Creates a stream URL that grants temporary access to a stream session in a web browser without requiring an AWS account or client integration.

You can use the stream URL to start a stream session up to the number of times set by `UsageLimit`, until it expires after `UrlExpiresAfterMinutes`. Each successful use starts a new stream session.

To make the request idempotent, provide a `ClientToken`.

## Request Syntax
<a name="API_CreateStreamUrl_RequestSyntax"></a>

```
POST /streamgroups/{{Identifier}}/streamurls HTTP/1.1
Content-type: application/json

{
   "AdditionalEnvironmentVariables": {
      "{{string}}" : "{{string}}"
   },
   "AdditionalLaunchArgs": [ "{{string}}" ],
   "ApplicationIdentifier": "{{string}}",
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "DisplayConfiguration": {
      "Resolution": {
         "Height": {{number}},
         "Width": {{number}}
      }
   },
   "Locations": [ "{{string}}" ],
   "Protocol": "{{string}}",
   "RoleArn": "{{string}}",
   "SessionLengthSeconds": {{number}},
   "UrlExpiresAfterMinutes": {{number}},
   "UsageLimit": {{number}}
}
```

## URI Request Parameters
<a name="API_CreateStreamUrl_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_CreateStreamUrl_RequestSyntax) **   <a name="gameliftstreams-CreateStreamUrl-request-uri-Identifier"></a>
An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the stream group resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`. Example ID: `sg-1AB2C3De4`.
The stream session runs in this stream group.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

## Request Body
<a name="API_CreateStreamUrl_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApplicationIdentifier](#API_CreateStreamUrl_RequestSyntax) **   <a name="gameliftstreams-CreateStreamUrl-request-ApplicationIdentifier"></a>
An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the application resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`. Example ID: `a-9ZY8X7Wv6`.
This application must be associated with the stream group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

 ** [Locations](#API_CreateStreamUrl_RequestSyntax) **   <a name="gameliftstreams-CreateStreamUrl-request-Locations"></a>
A list of locations, in order of preference, where Amazon GameLift Streams can place the stream session. Specify each location by its AWS Region code, for example `us-east-1`. For a complete list of locations that Amazon GameLift Streams supports, refer to [Regions, quotas, and limitations](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html) in the *Amazon GameLift Streams Developer Guide*.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [Protocol](#API_CreateStreamUrl_RequestSyntax) **   <a name="gameliftstreams-CreateStreamUrl-request-Protocol"></a>
The data transport protocol for the stream session. Amazon GameLift Streams supports `WebRTC`.
Type: String
Valid Values: `WebRTC`
Required: Yes

 ** [UrlExpiresAfterMinutes](#API_CreateStreamUrl_RequestSyntax) **   <a name="gameliftstreams-CreateStreamUrl-request-UrlExpiresAfterMinutes"></a>
The number of minutes after creation that the stream URL remains valid. After this period, the status of the stream URL changes to `EXPIRED` and it can no longer start stream sessions. The minimum is 1 minute. For the maximum, see [Regions, quotas, and limitations](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html) in the *Amazon GameLift Streams Developer Guide*.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** [AdditionalEnvironmentVariables](#API_CreateStreamUrl_RequestSyntax) **   <a name="gameliftstreams-CreateStreamUrl-request-AdditionalEnvironmentVariables"></a>
A set of options that you can use to control the stream session runtime environment, expressed as a set of key-value pairs. You can use this to configure the application or stream session details. You can also provide custom environment variables that Amazon GameLift Streams passes to your game client.
If you want to debug your application with environment variables, we recommend that you do so in a local environment outside of Amazon GameLift Streams. For more information, refer to the Compatibility Guidance in the troubleshooting section of the Developer Guide.
 `AdditionalEnvironmentVariables` and `AdditionalLaunchArgs` have similar purposes. `AdditionalEnvironmentVariables` passes data using environment variables; while `AdditionalLaunchArgs` passes data using command-line arguments.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[_a-zA-Z][_a-zA-Z0-9]*`
Value Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [AdditionalLaunchArgs](#API_CreateStreamUrl_RequestSyntax) **   <a name="gameliftstreams-CreateStreamUrl-request-AdditionalLaunchArgs"></a>
A list of CLI arguments that are sent to the streaming server when a stream session launches. You can use this to configure the application or stream session details. You can also provide custom arguments that Amazon GameLift Streams passes to your game client.
 `AdditionalEnvironmentVariables` and `AdditionalLaunchArgs` have similar purposes. `AdditionalEnvironmentVariables` passes data using environment variables; while `AdditionalLaunchArgs` passes data using command-line arguments.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** [ClientToken](#API_CreateStreamUrl_RequestSyntax) **   <a name="gameliftstreams-CreateStreamUrl-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure this request is idempotent. If you retry a request with the same `ClientToken`, Amazon GameLift Streams returns the original response without performing the operation again.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [Description](#API_CreateStreamUrl_RequestSyntax) **   <a name="gameliftstreams-CreateStreamUrl-request-Description"></a>
A descriptive label for the stream URL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[a-zA-Z0-9-_.!+@/][a-zA-Z0-9-_.!+@/ ]*`
Required: No

 ** [DisplayConfiguration](#API_CreateStreamUrl_RequestSyntax) **   <a name="gameliftstreams-CreateStreamUrl-request-DisplayConfiguration"></a>
The display settings, such as resolution, for stream sessions started from this stream URL.
Type: [DisplayConfiguration](API_DisplayConfiguration.md) object
Required: No

 ** [RoleArn](#API_CreateStreamUrl_RequestSyntax) **   <a name="gameliftstreams-CreateStreamUrl-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that Amazon GameLift Streams assumes during stream sessions started from this stream URL. For more information, see [Provide AWS credentials to your streaming application](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/session-credentials.html) in the *Amazon GameLift Streams Developer Guide*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-zA-Z-]*:iam::\d{12}:role/.+`
Required: No

 ** [SessionLengthSeconds](#API_CreateStreamUrl_RequestSyntax) **   <a name="gameliftstreams-CreateStreamUrl-request-SessionLengthSeconds"></a>
The maximum length of time, in seconds, that a stream session started from this stream URL can run. Valid values are 1-86400 seconds (1 second to 24 hours). The default is 43200 seconds (12 hours).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 86400.
Required: No

 ** [UsageLimit](#API_CreateStreamUrl_RequestSyntax) **   <a name="gameliftstreams-CreateStreamUrl-request-UsageLimit"></a>
The maximum number of times the stream URL can start a stream session. Each successful use reduces the remaining uses by one. The minimum is 1, and the default is 1. For the maximum, see [Regions, quotas, and limitations](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html) in the *Amazon GameLift Streams Developer Guide*.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## Response Syntax
<a name="API_CreateStreamUrl_ResponseSyntax"></a>

```
HTTP/1.1 201
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
   "StreamUrl": "string",
   "StreamUrlId": "string",
   "UsageLimit": number
}
```

## Response Elements
<a name="API_CreateStreamUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamUrl-response-Arn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the stream URL across all AWS Regions. Format is `arn:aws:gameliftstreams:[AWS Region]:[AWS account]:streamurl/[stream group resource ID]/[stream URL resource ID]`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)`

 ** [AdditionalEnvironmentVariables](#API_CreateStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamUrl-response-AdditionalEnvironmentVariables"></a>
The environment variables made available to the application when a stream session starts.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[_a-zA-Z][_a-zA-Z0-9]*`
Value Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [AdditionalLaunchArgs](#API_CreateStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamUrl-response-AdditionalLaunchArgs"></a>
The command-line arguments passed to the application when a stream session starts.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [ApplicationArn](#API_CreateStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamUrl-response-ApplicationArn"></a>
The application that runs in the stream sessions.
This value is an [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the application resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)`

 ** [CreatedAt](#API_CreateStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamUrl-response-CreatedAt"></a>
A timestamp that indicates when this resource was created. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).
Type: Timestamp

 ** [Description](#API_CreateStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamUrl-response-Description"></a>
The descriptive label for the stream URL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[a-zA-Z0-9-_.!+@/][a-zA-Z0-9-_.!+@/ ]*`

 ** [DisplayConfiguration](#API_CreateStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamUrl-response-DisplayConfiguration"></a>
The display settings, such as resolution, for stream sessions started from this stream URL.
Type: [DisplayConfiguration](API_DisplayConfiguration.md) object

 ** [ExpiresAt](#API_CreateStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamUrl-response-ExpiresAt"></a>
The date and time when the stream URL expires and stops accepting new stream sessions. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).
Type: Timestamp

 ** [Locations](#API_CreateStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamUrl-response-Locations"></a>
The list of locations, in order of preference, where Amazon GameLift Streams places the stream session. For a complete list of locations that Amazon GameLift Streams supports, refer to [Regions, quotas, and limitations](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html) in the *Amazon GameLift Streams Developer Guide*.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[a-zA-Z0-9-]+`

 ** [Protocol](#API_CreateStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamUrl-response-Protocol"></a>
The data transport protocol used for stream sessions started from this stream URL.
Type: String
Valid Values: `WebRTC`

 ** [RemainingUses](#API_CreateStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamUrl-response-RemainingUses"></a>
The number of times the stream URL can still be used to start a stream session.
Type: Integer
Valid Range: Minimum value of 0.

 ** [RoleArn](#API_CreateStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamUrl-response-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that Amazon GameLift Streams assumes during stream sessions started from this stream URL. For more information, see [Provide AWS credentials to your streaming application](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/session-credentials.html) in the *Amazon GameLift Streams Developer Guide*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-zA-Z-]*:iam::\d{12}:role/.+`

 ** [SessionLengthSeconds](#API_CreateStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamUrl-response-SessionLengthSeconds"></a>
The maximum length of time, in seconds, that a stream session started from this stream URL can run.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 86400.

 ** [Status](#API_CreateStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamUrl-response-Status"></a>
The current status of the stream URL. Possible statuses include the following:
+  `ACTIVE`: The stream URL is valid and can start stream sessions.
+  `EXPIRED`: The stream URL has passed its expiration time and can no longer start stream sessions.
+  `REVOKED`: The stream URL was revoked and can no longer start stream sessions.
+  `LIMIT_REACHED`: The stream URL has been used the maximum number of times and can no longer start stream sessions.
Type: String
Valid Values: `ACTIVE | EXPIRED | REVOKED | LIMIT_REACHED`

 ** [StatusReason](#API_CreateStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamUrl-response-StatusReason"></a>
Additional information about why the stream URL is in its current status. Amazon GameLift Streams populates this value when the status is `REVOKED`. Possible values include the following:
+  `userRevoked`: You revoked the stream URL.
+  `revokedAndTerminatingSessions`: You revoked the stream URL and Amazon GameLift Streams is ending its running stream sessions.
+  `revokedAndSessionsTerminated`: You revoked the stream URL and its running stream sessions have ended.
+  `streamGroupDeleted`: The stream group was deleted, which revoked the stream URL.
+  `applicationDeleted`: The application was deleted, which revoked the stream URL.
Type: String
Valid Values: `userRevoked | revokedAndTerminatingSessions | revokedAndSessionsTerminated | streamGroupDeleted | applicationDeleted`

 ** [StreamGroupArn](#API_CreateStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamUrl-response-StreamGroupArn"></a>
The stream group that runs the stream sessions.
This value is an [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the stream group resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)`

 ** [StreamUrl](#API_CreateStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamUrl-response-StreamUrl"></a>
The shareable stream URL. Distribute this URL to end users so that they can start and play a stream session in a hosted web player. Treat the stream URL as a secret. Anyone who has it can start a stream session until the stream URL expires, is revoked, or reaches its usage limit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [StreamUrlId](#API_CreateStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamUrl-response-StreamUrlId"></a>
The unique identifier for the stream URL resource, for example `su-1AB2C3De4`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9-]+`

 ** [UsageLimit](#API_CreateStreamUrl_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamUrl-response-UsageLimit"></a>
The maximum number of times the stream URL can start a stream session.
Type: Integer
Valid Range: Minimum value of 1.

## Errors
<a name="API_CreateStreamUrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.
 ** Message **
Description of the error.
HTTP Status Code: 403

 [ConflictException](API_ConflictException.md)
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
 ** Message **
Description of the error.
HTTP Status Code: 409

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

 [ServiceQuotaExceededException](API_ServiceQuotaExceededException.md)
The request would cause the resource to exceed an allowed service quota. Resolve the issue before you try again.
 ** Message **
Description of the error.
HTTP Status Code: 402

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
<a name="API_CreateStreamUrl_Examples"></a>

### Create a Stream URL (AWS CLI)
<a name="API_CreateStreamUrl_Example_1"></a>

The following AWS CLI command creates a stream URL for an application in a stream group.

#### Sample Request
<a name="API_CreateStreamUrl_Example_1_Request"></a>

```
aws gameliftstreams create-stream-url \
  --identifier sg-1AB2C3De4 \
  --application-identifier a-9ZY8X7Wv6 \
  --protocol WebRTC \
  --url-expires-after-minutes 60 \
  --usage-limit 5 \
  --locations us-east-1 us-west-2
```

## See Also
<a name="API_CreateStreamUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gameliftstreams-2018-05-10/CreateStreamUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gameliftstreams-2018-05-10/CreateStreamUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/CreateStreamUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gameliftstreams-2018-05-10/CreateStreamUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/CreateStreamUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gameliftstreams-2018-05-10/CreateStreamUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gameliftstreams-2018-05-10/CreateStreamUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gameliftstreams-2018-05-10/CreateStreamUrl)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gameliftstreams-2018-05-10/CreateStreamUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/CreateStreamUrl)
