---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_DisconnectParticipant.html
---

# DisconnectParticipant
<a name="API_DisconnectParticipant"></a>

Disconnects a specified participant from a specified stage. If the participant is publishing using an [IngestConfiguration](API_IngestConfiguration.md), DisconnectParticipant also updates the `stageArn` in the IngestConfiguration to be an empty string.

## Request Syntax
<a name="API_DisconnectParticipant_RequestSyntax"></a>

```
POST /DisconnectParticipant HTTP/1.1
Content-type: application/json

{
   "participantId": "{{string}}",
   "reason": "{{string}}",
   "stageArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DisconnectParticipant_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DisconnectParticipant_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [participantId](#API_DisconnectParticipant_RequestSyntax) **   <a name="ivsrealtimeeapireference-DisconnectParticipant-request-participantId"></a>
Identifier of the participant to be disconnected. IVS assigns this; it is returned by [CreateParticipantToken](API_CreateParticipantToken.md) (for streams using WebRTC ingest) or [CreateIngestConfiguration](API_CreateIngestConfiguration.md) (for streams using RTMP ingest).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]*`
Required: Yes

 ** [reason](#API_DisconnectParticipant_RequestSyntax) **   <a name="ivsrealtimeeapireference-DisconnectParticipant-request-reason"></a>
Description of why this participant is being disconnected.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** [stageArn](#API_DisconnectParticipant_RequestSyntax) **   <a name="ivsrealtimeeapireference-DisconnectParticipant-request-stageArn"></a>
ARN of the stage to which the participant is attached.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_DisconnectParticipant_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DisconnectParticipant_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisconnectParticipant_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

 ** exceptionMessage **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** PendingVerification **

 ** exceptionMessage **
 Your account is pending verification.
HTTP Status Code: 403

 ** ResourceNotFoundException **

 ** exceptionMessage **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ValidationException **

 ** exceptionMessage **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DisconnectParticipant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/DisconnectParticipant)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/DisconnectParticipant)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/DisconnectParticipant)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/DisconnectParticipant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/DisconnectParticipant)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/DisconnectParticipant)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/DisconnectParticipant)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/DisconnectParticipant)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/DisconnectParticipant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/DisconnectParticipant)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
