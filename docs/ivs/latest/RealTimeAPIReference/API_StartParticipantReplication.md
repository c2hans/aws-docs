---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StartParticipantReplication.html
---

# StartParticipantReplication
<a name="API_StartParticipantReplication"></a>

Starts replicating a publishing participant from a source stage to a destination stage.

## Request Syntax
<a name="API_StartParticipantReplication_RequestSyntax"></a>

```
POST /StartParticipantReplication HTTP/1.1
Content-type: application/json

{
   "attributes": {
      "{{string}}" : "{{string}}"
   },
   "destinationStageArn": "{{string}}",
   "participantId": "{{string}}",
   "reconnectWindowSeconds": {{number}},
   "sourceStageArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartParticipantReplication_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartParticipantReplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [attributes](#API_StartParticipantReplication_RequestSyntax) **   <a name="ivsrealtimeeapireference-StartParticipantReplication-request-attributes"></a>
Application-provided attributes to set on the replicated participant in the destination stage. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.*
These attributes are merged with any attributes set for this participant when creating the token. If there is overlap in keys, the values in these attributes are replaced.
Type: String to string map
Required: No

 ** [destinationStageArn](#API_StartParticipantReplication_RequestSyntax) **   <a name="ivsrealtimeeapireference-StartParticipantReplication-request-destinationStageArn"></a>
ARN of the stage to which the participant will be replicated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+`
Required: Yes

 ** [participantId](#API_StartParticipantReplication_RequestSyntax) **   <a name="ivsrealtimeeapireference-StartParticipantReplication-request-participantId"></a>
Participant ID of the publisher that will be replicated. This is assigned by IVS and returned by [CreateParticipantToken](API_CreateParticipantToken.md) or the `jti` (JWT ID) used to [create a self signed token](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-distribute-tokens.html#getting-started-distribute-tokens-self-signed).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]*`
Required: Yes

 ** [reconnectWindowSeconds](#API_StartParticipantReplication_RequestSyntax) **   <a name="ivsrealtimeeapireference-StartParticipantReplication-request-reconnectWindowSeconds"></a>
If the participant disconnects and then reconnects within the specified interval, replication will continue to be `ACTIVE`. Default: 0.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 300.
Required: No

 ** [sourceStageArn](#API_StartParticipantReplication_RequestSyntax) **   <a name="ivsrealtimeeapireference-StartParticipantReplication-request-sourceStageArn"></a>
ARN of the stage where the participant is publishing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_StartParticipantReplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Access-Control-Allow-Origin: {{accessControlAllowOrigin}}
Access-Control-Expose-Headers: {{accessControlExposeHeaders}}
Cache-Control: {{cacheControl}}
Content-Security-Policy: {{contentSecurityPolicy}}
Strict-Transport-Security: {{strictTransportSecurity}}
X-Content-Type-Options: {{xContentTypeOptions}}
X-Frame-Options: {{xFrameOptions}}
```

## Response Elements
<a name="API_StartParticipantReplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [accessControlAllowOrigin](#API_StartParticipantReplication_ResponseSyntax) **   <a name="ivsrealtimeeapireference-StartParticipantReplication-response-accessControlAllowOrigin"></a>
See [Access-Control-Allow-Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin) in the MDN Web Docs.

 ** [accessControlExposeHeaders](#API_StartParticipantReplication_ResponseSyntax) **   <a name="ivsrealtimeeapireference-StartParticipantReplication-response-accessControlExposeHeaders"></a>
See [Access-Control-Expose-Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Expose-Headers) in the MDN Web Docs.

 ** [cacheControl](#API_StartParticipantReplication_ResponseSyntax) **   <a name="ivsrealtimeeapireference-StartParticipantReplication-response-cacheControl"></a>
See [Cache-Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control) in the MDN Web Docs.

 ** [contentSecurityPolicy](#API_StartParticipantReplication_ResponseSyntax) **   <a name="ivsrealtimeeapireference-StartParticipantReplication-response-contentSecurityPolicy"></a>
See [Content-Security-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy) in the MDN Web Docs.

 ** [strictTransportSecurity](#API_StartParticipantReplication_ResponseSyntax) **   <a name="ivsrealtimeeapireference-StartParticipantReplication-response-strictTransportSecurity"></a>
See [Strict-Transport-Security](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security) in the MDN Web Docs.

 ** [xContentTypeOptions](#API_StartParticipantReplication_ResponseSyntax) **   <a name="ivsrealtimeeapireference-StartParticipantReplication-response-xContentTypeOptions"></a>
See [X-Content-Type-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Content-Type-Options) in the MDN Web Docs.

 ** [xFrameOptions](#API_StartParticipantReplication_ResponseSyntax) **   <a name="ivsrealtimeeapireference-StartParticipantReplication-response-xFrameOptions"></a>
See [X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options) in the MDN Web Docs.

## Errors
<a name="API_StartParticipantReplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

 ** exceptionMessage **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **

 ** exceptionMessage **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **

 ** exceptionMessage **
Unexpected error during processing of request.
HTTP Status Code: 500

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
<a name="API_StartParticipantReplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/StartParticipantReplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/StartParticipantReplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/StartParticipantReplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/StartParticipantReplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/StartParticipantReplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/StartParticipantReplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/StartParticipantReplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/StartParticipantReplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/StartParticipantReplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/StartParticipantReplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
