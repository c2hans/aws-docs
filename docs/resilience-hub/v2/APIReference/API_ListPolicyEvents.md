---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListPolicyEvents.html
---

# ListPolicyEvents
<a name="API_ListPolicyEvents"></a>

Lists events for a resilience policy, including services that started or stopped using it, changes to cross-account sharing, and deletion of the policy.

## Request Syntax
<a name="API_ListPolicyEvents_RequestSyntax"></a>

```
GET /v2/list-policy-events?endTime={{endTime}}&eventTypes={{eventTypes}}&maxResults={{maxResults}}&nextToken={{nextToken}}&policyArn={{policyArn}}&startTime={{startTime}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPolicyEvents_RequestParameters"></a>

The request uses the following URI parameters.

 ** [endTime](#API_ListPolicyEvents_RequestSyntax) **   <a name="ngresiliencehub-ListPolicyEvents-request-uri-endTime"></a>
The end time for filtering events.

 ** [eventTypes](#API_ListPolicyEvents_RequestSyntax) **   <a name="ngresiliencehub-ListPolicyEvents-request-uri-eventTypes"></a>
The type of events to include in the results.
Array Members: Minimum number of 0 items. Maximum number of 4 items.
Valid Values: `POLICY_ATTACHED_TO_SERVICE | POLICY_DETACHED_FROM_SERVICE | POLICY_SHARING_REVOKED | POLICY_DELETED`

 ** [maxResults](#API_ListPolicyEvents_RequestSyntax) **   <a name="ngresiliencehub-ListPolicyEvents-request-uri-maxResults"></a>
Pagination page size.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListPolicyEvents_RequestSyntax) **   <a name="ngresiliencehub-ListPolicyEvents-request-uri-nextToken"></a>
Pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

 ** [policyArn](#API_ListPolicyEvents_RequestSyntax) **   <a name="ngresiliencehub-ListPolicyEvents-request-uri-policyArn"></a>
ARN identifier.
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [startTime](#API_ListPolicyEvents_RequestSyntax) **   <a name="ngresiliencehub-ListPolicyEvents-request-uri-startTime"></a>
The start time for filtering events.

## Request Body
<a name="API_ListPolicyEvents_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPolicyEvents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "events": [
      {
         "actor": {
            "accountId": "string",
            "principalId": "string",
            "type": "string",
            "userName": "string"
         },
         "eventDetails": {
            "description": "string",
            "eventMetadata": { ... },
            "title": "string"
         },
         "eventId": "string",
         "eventType": "string",
         "policyArn": "string",
         "timestamp": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListPolicyEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [events](#API_ListPolicyEvents_ResponseSyntax) **   <a name="ngresiliencehub-ListPolicyEvents-response-events"></a>
The list of policy events.
Type: Array of [PolicyEvent](API_PolicyEvent.md) objects

 ** [nextToken](#API_ListPolicyEvents_ResponseSyntax) **   <a name="ngresiliencehub-ListPolicyEvents-response-nextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

## Errors
<a name="API_ListPolicyEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access denied — caller lacks required permissions.
HTTP Status Code: 403

 ** InternalServerException **
Internal service error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource not found.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of the resource that was not found.
HTTP Status Code: 404

 ** ValidationException **
Validation error — invalid input parameters.
 ** fieldList **
The list of fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListPolicyEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/ListPolicyEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/ListPolicyEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ListPolicyEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/ListPolicyEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ListPolicyEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/ListPolicyEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/ListPolicyEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/ListPolicyEvents)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/ListPolicyEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ListPolicyEvents)
