---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListParticipantReplicas.html
---

# ListParticipantReplicas
<a name="API_ListParticipantReplicas"></a>

Lists all the replicas for a participant from a source stage.

## Request Syntax
<a name="API_ListParticipantReplicas_RequestSyntax"></a>

```
POST /ListParticipantReplicas HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "participantId": "{{string}}",
   "sourceStageArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListParticipantReplicas_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListParticipantReplicas_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListParticipantReplicas_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListParticipantReplicas-request-maxResults"></a>
Maximum number of results to return. Default: 50.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_ListParticipantReplicas_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListParticipantReplicas-request-nextToken"></a>
The first participant to retrieve. This is used for pagination; see the `nextToken` response field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`
Required: No

 ** [participantId](#API_ListParticipantReplicas_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListParticipantReplicas-request-participantId"></a>
Participant ID of the publisher that has been replicated. This is assigned by IVS and returned by [CreateParticipantToken](API_CreateParticipantToken.md) or the `jti` (JWT ID) used to [create a self signed token](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-distribute-tokens.html#getting-started-distribute-tokens-self-signed).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]*`
Required: Yes

 ** [sourceStageArn](#API_ListParticipantReplicas_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListParticipantReplicas-request-sourceStageArn"></a>
ARN of the stage where the participant is publishing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_ListParticipantReplicas_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "replicas": [
      {
         "destinationSessionId": "string",
         "destinationStageArn": "string",
         "participantId": "string",
         "replicationState": "string",
         "sourceSessionId": "string",
         "sourceStageArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListParticipantReplicas_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListParticipantReplicas_ResponseSyntax) **   <a name="ivsrealtimeeapireference-ListParticipantReplicas-response-nextToken"></a>
If there are more participants than `maxResults`, use `nextToken` in the request to get the next set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`

 ** [replicas](#API_ListParticipantReplicas_ResponseSyntax) **   <a name="ivsrealtimeeapireference-ListParticipantReplicas-response-replicas"></a>
List of all participant replicas.
Type: Array of [ParticipantReplica](API_ParticipantReplica.md) objects

## Errors
<a name="API_ListParticipantReplicas_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListParticipantReplicas_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/ListParticipantReplicas)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/ListParticipantReplicas)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/ListParticipantReplicas)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/ListParticipantReplicas)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/ListParticipantReplicas)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/ListParticipantReplicas)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/ListParticipantReplicas)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/ListParticipantReplicas)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/ListParticipantReplicas)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/ListParticipantReplicas)
