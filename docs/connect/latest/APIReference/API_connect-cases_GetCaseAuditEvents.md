---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetCaseAuditEvents.html
---

# GetCaseAuditEvents
<a name="API_connect-cases_GetCaseAuditEvents"></a>

Returns the audit history about a specific case if it exists.

## Request Syntax
<a name="API_connect-cases_GetCaseAuditEvents_RequestSyntax"></a>

```
POST /domains/{{domainId}}/cases/{{caseId}}/audit-history HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-cases_GetCaseAuditEvents_RequestParameters"></a>

The request uses the following URI parameters.

 ** [caseId](#API_connect-cases_GetCaseAuditEvents_RequestSyntax) **   <a name="connect-connect-cases_GetCaseAuditEvents-request-uri-caseId"></a>
A unique identifier of the case.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [domainId](#API_connect-cases_GetCaseAuditEvents_RequestSyntax) **   <a name="connect-connect-cases_GetCaseAuditEvents-request-uri-domainId"></a>
The unique identifier of the Cases domain.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_connect-cases_GetCaseAuditEvents_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_connect-cases_GetCaseAuditEvents_RequestSyntax) **   <a name="connect-connect-cases_GetCaseAuditEvents-request-maxResults"></a>
The maximum number of audit events to return. When no value is provided, 25 is the default.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_connect-cases_GetCaseAuditEvents_RequestSyntax) **   <a name="connect-connect-cases_GetCaseAuditEvents-request-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 9000.
Required: No

## Response Syntax
<a name="API_connect-cases_GetCaseAuditEvents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "auditEvents": [
      {
         "eventId": "string",
         "fields": [
            {
               "eventFieldId": "string",
               "newValue": { ... },
               "oldValue": { ... }
            }
         ],
         "performedBy": {
            "iamPrincipalArn": "string",
            "user": { ... }
         },
         "performedTime": "string",
         "relatedItemType": "string",
         "type": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_connect-cases_GetCaseAuditEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [auditEvents](#API_connect-cases_GetCaseAuditEvents_ResponseSyntax) **   <a name="connect-connect-cases_GetCaseAuditEvents-response-auditEvents"></a>
A list of case audits where each represents a particular edit of the case.
Type: Array of [AuditEvent](API_connect-cases_AuditEvent.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

 ** [nextToken](#API_connect-cases_GetCaseAuditEvents_ResponseSyntax) **   <a name="connect-connect-cases_GetCaseAuditEvents-response-nextToken"></a>
The token for the next set of results. This is null if there are no more results to return.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 9000.

## Errors
<a name="API_connect-cases_GetCaseAuditEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
We couldn't process your request because of an issue with the server. Try again later.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
We couldn't find the requested resource. Check that your resources exists and were created in the same AWS Region as your request, and try your request again.
 ** resourceId **
Unique identifier of the resource affected.
 ** resourceType **
Type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
The rate has been exceeded for this API. Please try again after a few minutes.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. Check the syntax and try again.
HTTP Status Code: 400

## See Also
<a name="API_connect-cases_GetCaseAuditEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/GetCaseAuditEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/GetCaseAuditEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/GetCaseAuditEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/GetCaseAuditEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/GetCaseAuditEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/GetCaseAuditEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/GetCaseAuditEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/GetCaseAuditEvents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/GetCaseAuditEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/GetCaseAuditEvents)
