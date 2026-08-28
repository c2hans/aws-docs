---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListServiceEvents.html
---

# ListServiceEvents
<a name="API_ListServiceEvents"></a>

Lists events for a service.

## Request Syntax
<a name="API_ListServiceEvents_RequestSyntax"></a>

```
GET /v2/list-service-events?endTime={{endTime}}&eventTypes={{eventTypes}}&maxResults={{maxResults}}&nextToken={{nextToken}}&serviceArn={{serviceArn}}&startTime={{startTime}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListServiceEvents_RequestParameters"></a>

The request uses the following URI parameters.

 ** [endTime](#API_ListServiceEvents_RequestSyntax) **   <a name="ngresiliencehub-ListServiceEvents-request-uri-endTime"></a>
The end time for filtering events.

 ** [eventTypes](#API_ListServiceEvents_RequestSyntax) **   <a name="ngresiliencehub-ListServiceEvents-request-uri-eventTypes"></a>
Filter events by type.
Valid Values: `SERVICE_CREATED | SERVICE_DELETED | SERVICE_SYSTEM_ASSOCIATED | SERVICE_SYSTEM_DISASSOCIATED | SERVICE_RESOURCES_ASSOCIATED | SERVICE_RESOURCES_DISASSOCIATED | SERVICE_WORKFLOW_UPDATED | SERVICE_INPUT_SOURCES_UPDATED | SERVICE_POLICY_ASSOCIATED | SERVICE_POLICY_DISASSOCIATED | SERVICE_FUNCTION_CREATED | SERVICE_FUNCTION_UPDATED | SERVICE_FUNCTION_DELETED | SERVICE_FUNCTION_RESOURCES_ADDED | SERVICE_FUNCTION_RESOURCES_REMOVED | SERVICE_ACHIEVABILITY_UPDATED | ASSERTION_CREATED | ASSERTION_UPDATED | ASSERTION_DELETED`

 ** [maxResults](#API_ListServiceEvents_RequestSyntax) **   <a name="ngresiliencehub-ListServiceEvents-request-uri-maxResults"></a>
Pagination page size.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListServiceEvents_RequestSyntax) **   <a name="ngresiliencehub-ListServiceEvents-request-uri-nextToken"></a>
Pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

 ** [serviceArn](#API_ListServiceEvents_RequestSyntax) **   <a name="ngresiliencehub-ListServiceEvents-request-uri-serviceArn"></a>
ARN identifier.
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [startTime](#API_ListServiceEvents_RequestSyntax) **   <a name="ngresiliencehub-ListServiceEvents-request-uri-startTime"></a>
The start time for filtering events.

## Request Body
<a name="API_ListServiceEvents_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListServiceEvents_ResponseSyntax"></a>

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
         "serviceArn": "string",
         "timestamp": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListServiceEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [events](#API_ListServiceEvents_ResponseSyntax) **   <a name="ngresiliencehub-ListServiceEvents-response-events"></a>
The list of service events.
Type: Array of [ServiceEvent](API_ServiceEvent.md) objects

 ** [nextToken](#API_ListServiceEvents_ResponseSyntax) **   <a name="ngresiliencehub-ListServiceEvents-response-nextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

## Errors
<a name="API_ListServiceEvents_Errors"></a>

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
<a name="API_ListServiceEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/ListServiceEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/ListServiceEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ListServiceEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/ListServiceEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ListServiceEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/ListServiceEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/ListServiceEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/ListServiceEvents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/ListServiceEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ListServiceEvents)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
