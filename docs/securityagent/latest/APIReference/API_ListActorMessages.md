---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ListActorMessages.html
---

# ListActorMessages
<a name="API_ListActorMessages"></a>

Returns a paginated list of the email MFA messages received for an actor at its server-generated email address, most recent first.

## Request Syntax
<a name="API_ListActorMessages_RequestSyntax"></a>

```
POST /ListActorMessages HTTP/1.1
Content-type: application/json

{
   "actorIdentifier": "{{string}}",
   "agentSpaceId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "pentestId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListActorMessages_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListActorMessages_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actorIdentifier](#API_ListActorMessages_RequestSyntax) **   <a name="securityagent-ListActorMessages-request-actorIdentifier"></a>
The identifier of the actor whose messages to list. The identifier is case-insensitive.
Type: String
Required: Yes

 ** [agentSpaceId](#API_ListActorMessages_RequestSyntax) **   <a name="securityagent-ListActorMessages-request-agentSpaceId"></a>
The unique identifier of the agent space that owns the pentest.
Type: String
Required: Yes

 ** [maxResults](#API_ListActorMessages_RequestSyntax) **   <a name="securityagent-ListActorMessages-request-maxResults"></a>
The maximum number of results to return in a single call.
Type: Integer
Required: No

 ** [nextToken](#API_ListActorMessages_RequestSyntax) **   <a name="securityagent-ListActorMessages-request-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.
Type: String
Required: No

 ** [pentestId](#API_ListActorMessages_RequestSyntax) **   <a name="securityagent-ListActorMessages-request-pentestId"></a>
The unique identifier of the pentest that the actor belongs to.
Type: String
Required: Yes

## Response Syntax
<a name="API_ListActorMessages_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "messages": [
      {
         "body": "string",
         "receivedAt": "string",
         "sender": "string",
         "subject": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListActorMessages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [messages](#API_ListActorMessages_ResponseSyntax) **   <a name="securityagent-ListActorMessages-response-messages"></a>
The list of messages received for the actor, most recent first.
Type: Array of [ActorMessage](API_ActorMessage.md) objects

 ** [nextToken](#API_ListActorMessages_ResponseSyntax) **   <a name="securityagent-ListActorMessages-response-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.
Type: String

## Errors
<a name="API_ListActorMessages_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListActorMessages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/ListActorMessages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/ListActorMessages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ListActorMessages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/ListActorMessages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ListActorMessages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/ListActorMessages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/ListActorMessages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/ListActorMessages)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/ListActorMessages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ListActorMessages)
