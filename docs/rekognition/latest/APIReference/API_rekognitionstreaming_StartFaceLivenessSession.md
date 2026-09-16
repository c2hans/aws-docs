---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_rekognitionstreaming_StartFaceLivenessSession.html
---

# StartFaceLivenessSession
<a name="API_rekognitionstreaming_StartFaceLivenessSession"></a>

Starts a Face Liveness video stream and liveness detection process for a given session.

Requires `sessionId`, `ChallengeVersions`, `VideoWidth`, `VideoHeight` and a `RequestEventStream` as input. The event stream contains information about different events for the session, including the challenge information used for verification.

The maximum video size for Face Liveness is 10 MB. Face Liveness throws a `ValidationException` if the video does not match the necessary formatting and size parameters.

StartFaceLivenessSession supports the websockets and [the AWS SDK for JavaScript](https://aws.amazon.com/sdk-for-javascript/).

## Request Syntax
<a name="API_rekognitionstreaming_StartFaceLivenessSession_RequestSyntax"></a>

```
POST /start-face-liveness-session HTTP/1.1
x-amz-rekognition-streaming-liveness-session-id: {{SessionId}}
x-amz-rekognition-streaming-liveness-video-width: {{VideoWidth}}
x-amz-rekognition-streaming-liveness-video-height: {{VideoHeight}}
x-amz-rekognition-streaming-liveness-challenge-versions: {{ChallengeVersions}}
Content-type: application/json

{
   "ClientSessionInformationEvent": {
      "Challenge": { ... }
   },
   "VideoEvent": {
      "TimestampMillis": {{number}},
      "VideoChunk": {{blob}}
   }
}
```

## URI Request Parameters
<a name="API_rekognitionstreaming_StartFaceLivenessSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChallengeVersions](#API_rekognitionstreaming_StartFaceLivenessSession_RequestSyntax) **   <a name="rekognition-rekognitionstreaming_StartFaceLivenessSession-request-ChallengeVersions"></a>
String containing comma separated list of challenge versions supported by client.
Length Constraints: Minimum length of 15. Maximum length of 150.
Pattern: `^([a-zA-Z]{10,}_\d+\.\d+\.\d+){1}(,[a-zA-Z]{10,}_\d+\.\d+\.\d+)*`
Required: Yes

 ** [SessionId](#API_rekognitionstreaming_StartFaceLivenessSession_RequestSyntax) **   <a name="rekognition-rekognitionstreaming_StartFaceLivenessSession-request-SessionId"></a>
A unique 128-bit UUID. Used to uniquely identify the session and also acta as an idempotency token for all operations associated with the session.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [VideoHeight](#API_rekognitionstreaming_StartFaceLivenessSession_RequestSyntax) **   <a name="rekognition-rekognitionstreaming_StartFaceLivenessSession-request-VideoHeight"></a>
The height of the video object included in a request to start a Face Liveness session.
Length Constraints: Minimum length of 3. Maximum length of 4.
Pattern: `^[0-9]{3,}$`
Required: Yes

 ** [VideoWidth](#API_rekognitionstreaming_StartFaceLivenessSession_RequestSyntax) **   <a name="rekognition-rekognitionstreaming_StartFaceLivenessSession-request-VideoWidth"></a>
The width of the video object included in a request to start a Face Liveness session.
Length Constraints: Minimum length of 3. Maximum length of 4.
Pattern: `^[0-9]{3,}$`
Required: Yes

## Request Body
<a name="API_rekognitionstreaming_StartFaceLivenessSession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientSessionInformationEvent](#API_rekognitionstreaming_StartFaceLivenessSession_RequestSyntax) **   <a name="rekognition-rekognitionstreaming_StartFaceLivenessSession-request-ClientSessionInformationEvent"></a>
Information event for the client session for a given Face Liveness request stream.
Type: [ClientSessionInformationEvent](API_rekognitionstreaming_ClientSessionInformationEvent.md) object
Required: No

 ** [VideoEvent](#API_rekognitionstreaming_StartFaceLivenessSession_RequestSyntax) **   <a name="rekognition-rekognitionstreaming_StartFaceLivenessSession-request-VideoEvent"></a>
Contains video events for a Face Liveness request stream.
Type: [VideoEvent](API_rekognitionstreaming_VideoEvent.md) object
Required: No

## Response Syntax
<a name="API_rekognitionstreaming_StartFaceLivenessSession_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amz-rekognition-streaming-liveness-session-id: {{SessionId}}
Content-type: application/json

{
   "DisconnectionEvent": {
      "TimestampMillis": number
   },
   "InternalServerException": {
   },
   "ServerSessionInformationEvent": {
      "SessionInformation": {
         "Challenge": { ... }
      }
   },
   "ServiceQuotaExceededException": {
   },
   "ServiceUnavailableException": {
   },
   "ThrottlingException": {
   },
   "ValidationException": {
   }
}
```

## Response Elements
<a name="API_rekognitionstreaming_StartFaceLivenessSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [SessionId](#API_rekognitionstreaming_StartFaceLivenessSession_ResponseSyntax) **   <a name="rekognition-rekognitionstreaming_StartFaceLivenessSession-response-SessionId"></a>
The ID that identifies a Face Liveness session.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

The following data is returned in JSON format by the service.

 ** [DisconnectionEvent](#API_rekognitionstreaming_StartFaceLivenessSession_ResponseSyntax) **   <a name="rekognition-rekognitionstreaming_StartFaceLivenessSession-response-DisconnectionEvent"></a>
Notification that disconnection event has occurred to a Face Liveness session.
Type: [DisconnectionEvent](API_rekognitionstreaming_DisconnectionEvent.md) object

 ** [InternalServerException](#API_rekognitionstreaming_StartFaceLivenessSession_ResponseSyntax) **   <a name="rekognition-rekognitionstreaming_StartFaceLivenessSession-response-InternalServerException"></a>
Notification that an InternalServerException occurred during a Face Liveness session.
Type: Exception
HTTP Status Code: 500

 ** [ServerSessionInformationEvent](#API_rekognitionstreaming_StartFaceLivenessSession_ResponseSyntax) **   <a name="rekognition-rekognitionstreaming_StartFaceLivenessSession-response-ServerSessionInformationEvent"></a>
Details for a server session information event.
Type: [ServerSessionInformationEvent](API_rekognitionstreaming_ServerSessionInformationEvent.md) object

 ** [ServiceQuotaExceededException](#API_rekognitionstreaming_StartFaceLivenessSession_ResponseSyntax) **   <a name="rekognition-rekognitionstreaming_StartFaceLivenessSession-response-ServiceQuotaExceededException"></a>
Notification that a ServiceQuotaExceededException occurred during a Face Liveness session.
Type: Exception
HTTP Status Code: 429

 ** [ServiceUnavailableException](#API_rekognitionstreaming_StartFaceLivenessSession_ResponseSyntax) **   <a name="rekognition-rekognitionstreaming_StartFaceLivenessSession-response-ServiceUnavailableException"></a>
Notification that a ServiceUnavailableException occurred during a Face Liveness session.
Type: Exception
HTTP Status Code: 503

 ** [ThrottlingException](#API_rekognitionstreaming_StartFaceLivenessSession_ResponseSyntax) **   <a name="rekognition-rekognitionstreaming_StartFaceLivenessSession-response-ThrottlingException"></a>
Notification that a ThrottlingException occurred during a Face Liveness session.
Type: Exception
HTTP Status Code: 429

 ** [ValidationException](#API_rekognitionstreaming_StartFaceLivenessSession_ResponseSyntax) **   <a name="rekognition-rekognitionstreaming_StartFaceLivenessSession-response-ValidationException"></a>
Notification that a ValidationException occurred during a Face Liveness session.
Type: Exception
HTTP Status Code: 400

## Errors
<a name="API_rekognitionstreaming_StartFaceLivenessSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Occurs when the client isn't authorized to perform the action.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
Occurs when a request would cause a service quota to be exceeded.
HTTP Status Code: 429

 ** ServiceUnavailableException **
Service-wide throttling to recover from an operational event or service is not able to scale.
HTTP Status Code: 503

 ** SessionNotFoundException **
Occurs when the given `sessionId` is not found.
HTTP Status Code: 400

 ** ThrottlingException **
A request was denied due to request throttling. Occurs when too many requests were made by a user (exceeding their service quota), the service isn't able to scale, or a service-wide throttling was done to recover from an operational event.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service. Potential reasons inlcude: video quality or size is invalid, video container format not supported, video does not have enough information - no person detected in video, request couldn't be parsed or is invalid, session has expired or is invalid, S3 bucket is invalid/in another AWS region, KMS Key is invalid.
HTTP Status Code: 400

## See Also
<a name="API_rekognitionstreaming_StartFaceLivenessSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognitionstreaming-2022-05-30/StartFaceLivenessSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognitionstreaming-2022-05-30/StartFaceLivenessSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognitionstreaming-2022-05-30/StartFaceLivenessSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognitionstreaming-2022-05-30/StartFaceLivenessSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognitionstreaming-2022-05-30/StartFaceLivenessSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognitionstreaming-2022-05-30/StartFaceLivenessSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognitionstreaming-2022-05-30/StartFaceLivenessSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognitionstreaming-2022-05-30/StartFaceLivenessSession)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rekognitionstreaming-2022-05-30/StartFaceLivenessSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognitionstreaming-2022-05-30/StartFaceLivenessSession)
