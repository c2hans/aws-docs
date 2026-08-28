---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateParticipantToken.html
---

# CreateParticipantToken
<a name="API_CreateParticipantToken"></a>

Creates an additional token for a specified stage. This can be done after stage creation or when tokens expire. Tokens always are scoped to the stage for which they are created.

Encryption keys are owned by Amazon IVS and never used directly by your application.

## Request Syntax
<a name="API_CreateParticipantToken_RequestSyntax"></a>

```
POST /CreateParticipantToken HTTP/1.1
Content-type: application/json

{
   "attributes": {
      "{{string}}" : "{{string}}"
   },
   "capabilities": [ "{{string}}" ],
   "duration": {{number}},
   "stageArn": "{{string}}",
   "userId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateParticipantToken_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateParticipantToken_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [attributes](#API_CreateParticipantToken_RequestSyntax) **   <a name="ivsrealtimeeapireference-CreateParticipantToken-request-attributes"></a>
Application-provided attributes to encode into the token and attach to a stage. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.*
Type: String to string map
Required: No

 ** [capabilities](#API_CreateParticipantToken_RequestSyntax) **   <a name="ivsrealtimeeapireference-CreateParticipantToken-request-capabilities"></a>
Set of capabilities that the user is allowed to perform in the stage. Default: `PUBLISH, SUBSCRIBE`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `PUBLISH | SUBSCRIBE`
Required: No

 ** [duration](#API_CreateParticipantToken_RequestSyntax) **   <a name="ivsrealtimeeapireference-CreateParticipantToken-request-duration"></a>
Duration (in minutes), after which the token expires. Default: 720 (12 hours).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20160.
Required: No

 ** [stageArn](#API_CreateParticipantToken_RequestSyntax) **   <a name="ivsrealtimeeapireference-CreateParticipantToken-request-stageArn"></a>
ARN of the stage to which this token is scoped.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+`
Required: Yes

 ** [userId](#API_CreateParticipantToken_RequestSyntax) **   <a name="ivsrealtimeeapireference-CreateParticipantToken-request-userId"></a>
Name that can be specified to help identify the token. This can be any UTF-8 encoded text. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.*
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

## Response Syntax
<a name="API_CreateParticipantToken_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "participantToken": {
      "attributes": {
         "string" : "string"
      },
      "capabilities": [ "string" ],
      "duration": number,
      "expirationTime": "string",
      "participantId": "string",
      "token": "string",
      "userId": "string"
   }
}
```

## Response Elements
<a name="API_CreateParticipantToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [participantToken](#API_CreateParticipantToken_ResponseSyntax) **   <a name="ivsrealtimeeapireference-CreateParticipantToken-response-participantToken"></a>
The participant token that was created.
Type: [ParticipantToken](API_ParticipantToken.md) object

## Errors
<a name="API_CreateParticipantToken_Errors"></a>

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

 ** ServiceQuotaExceededException **

 ** exceptionMessage **
Request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ValidationException **

 ** exceptionMessage **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateParticipantToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/CreateParticipantToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/CreateParticipantToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/CreateParticipantToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/CreateParticipantToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/CreateParticipantToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/CreateParticipantToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/CreateParticipantToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/CreateParticipantToken)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/CreateParticipantToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/CreateParticipantToken)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
