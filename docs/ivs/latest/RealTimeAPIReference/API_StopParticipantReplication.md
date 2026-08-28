---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StopParticipantReplication.html
---

# StopParticipantReplication
<a name="API_StopParticipantReplication"></a>

Stops a replicated participant session.

## Request Syntax
<a name="API_StopParticipantReplication_RequestSyntax"></a>

```
POST /StopParticipantReplication HTTP/1.1
Content-type: application/json

{
   "destinationStageArn": "{{string}}",
   "participantId": "{{string}}",
   "sourceStageArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StopParticipantReplication_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StopParticipantReplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [destinationStageArn](#API_StopParticipantReplication_RequestSyntax) **   <a name="ivsrealtimeeapireference-StopParticipantReplication-request-destinationStageArn"></a>
ARN of the stage where the participant has been replicated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+`
Required: Yes

 ** [participantId](#API_StopParticipantReplication_RequestSyntax) **   <a name="ivsrealtimeeapireference-StopParticipantReplication-request-participantId"></a>
Participant ID of the publisher that has been replicated. This is assigned by IVS and returned by [CreateParticipantToken](API_CreateParticipantToken.md) or the `jti` (JWT ID) used to [ create a self signed token](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-distribute-tokens.html#getting-started-distribute-tokens-self-signed).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]*`
Required: Yes

 ** [sourceStageArn](#API_StopParticipantReplication_RequestSyntax) **   <a name="ivsrealtimeeapireference-StopParticipantReplication-request-sourceStageArn"></a>
ARN of the stage where the participant is publishing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_StopParticipantReplication_ResponseSyntax"></a>

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
<a name="API_StopParticipantReplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [accessControlAllowOrigin](#API_StopParticipantReplication_ResponseSyntax) **   <a name="ivsrealtimeeapireference-StopParticipantReplication-response-accessControlAllowOrigin"></a>
See [Access-Control-Allow-Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin) in the MDN Web Docs.

 ** [accessControlExposeHeaders](#API_StopParticipantReplication_ResponseSyntax) **   <a name="ivsrealtimeeapireference-StopParticipantReplication-response-accessControlExposeHeaders"></a>
See [Access-Control-Expose-Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Expose-Headers) in the MDN Web Docs.

 ** [cacheControl](#API_StopParticipantReplication_ResponseSyntax) **   <a name="ivsrealtimeeapireference-StopParticipantReplication-response-cacheControl"></a>
See [Cache-Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control) in the MDN Web Docs.

 ** [contentSecurityPolicy](#API_StopParticipantReplication_ResponseSyntax) **   <a name="ivsrealtimeeapireference-StopParticipantReplication-response-contentSecurityPolicy"></a>
See [Content-Security-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy) in the MDN Web Docs.

 ** [strictTransportSecurity](#API_StopParticipantReplication_ResponseSyntax) **   <a name="ivsrealtimeeapireference-StopParticipantReplication-response-strictTransportSecurity"></a>
See [Strict-Transport-Security](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security) in the MDN Web Docs.

 ** [xContentTypeOptions](#API_StopParticipantReplication_ResponseSyntax) **   <a name="ivsrealtimeeapireference-StopParticipantReplication-response-xContentTypeOptions"></a>
See [X-Content-Type-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Content-Type-Options) in the MDN Web Docs.

 ** [xFrameOptions](#API_StopParticipantReplication_ResponseSyntax) **   <a name="ivsrealtimeeapireference-StopParticipantReplication-response-xFrameOptions"></a>
See [X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options) in the MDN Web Docs.

## Errors
<a name="API_StopParticipantReplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

 ** exceptionMessage **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **

 ** exceptionMessage **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **

 ** exceptionMessage **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ValidationException **

 ** exceptionMessage **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_StopParticipantReplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/StopParticipantReplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/StopParticipantReplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/StopParticipantReplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/StopParticipantReplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/StopParticipantReplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/StopParticipantReplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/StopParticipantReplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/StopParticipantReplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/StopParticipantReplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/StopParticipantReplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
