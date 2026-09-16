---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListTestRunEvents.html
---

# ListTestRunEvents
<a name="API_ListTestRunEvents"></a>

Lists the events in a test run's timeline.

## Request Syntax
<a name="API_ListTestRunEvents_RequestSyntax"></a>

```
GET /v2/test-runs/{{testRunId}}/events?endedAt={{endedAt}}&maxResults={{maxResults}}&nextToken={{nextToken}}&serviceArn={{serviceArn}}&startedAt={{startedAt}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTestRunEvents_RequestParameters"></a>

The request uses the following URI parameters.

 ** [endedAt](#API_ListTestRunEvents_RequestSyntax) **   <a name="ngresiliencehub-ListTestRunEvents-request-uri-endedAt"></a>
Return events at or before this timestamp.

 ** [maxResults](#API_ListTestRunEvents_RequestSyntax) **   <a name="ngresiliencehub-ListTestRunEvents-request-uri-maxResults"></a>
Pagination page size.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListTestRunEvents_RequestSyntax) **   <a name="ngresiliencehub-ListTestRunEvents-request-uri-nextToken"></a>
Pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

 ** [serviceArn](#API_ListTestRunEvents_RequestSyntax) **   <a name="ngresiliencehub-ListTestRunEvents-request-uri-serviceArn"></a>
The ARN of the service the test run belongs to.
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [startedAt](#API_ListTestRunEvents_RequestSyntax) **   <a name="ngresiliencehub-ListTestRunEvents-request-uri-startedAt"></a>
Return events at or after this timestamp.

 ** [testRunId](#API_ListTestRunEvents_RequestSyntax) **   <a name="ngresiliencehub-ListTestRunEvents-request-uri-testRunId"></a>
The identifier of the test run to list events for.
Length Constraints: Minimum length of 1.
Required: Yes

## Request Body
<a name="API_ListTestRunEvents_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTestRunEvents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "events": [
      {
         "attributes": {
            "string" : "string"
         },
         "eventId": "string",
         "eventType": "string",
         "message": "string",
         "timestamp": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListTestRunEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [events](#API_ListTestRunEvents_ResponseSyntax) **   <a name="ngresiliencehub-ListTestRunEvents-response-events"></a>
The list of test run events.
Type: Array of [TestRunEvent](API_TestRunEvent.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [nextToken](#API_ListTestRunEvents_ResponseSyntax) **   <a name="ngresiliencehub-ListTestRunEvents-response-nextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

## Errors
<a name="API_ListTestRunEvents_Errors"></a>

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
<a name="API_ListTestRunEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/ListTestRunEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/ListTestRunEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ListTestRunEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/ListTestRunEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ListTestRunEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/ListTestRunEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/ListTestRunEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/ListTestRunEvents)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/ListTestRunEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ListTestRunEvents)
