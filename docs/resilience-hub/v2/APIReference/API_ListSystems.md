---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListSystems.html
---

# ListSystems
<a name="API_ListSystems"></a>

Lists systems.

## Request Syntax
<a name="API_ListSystems_RequestSyntax"></a>

```
GET /v2/list-systems?maxResults={{maxResults}}&nextToken={{nextToken}}&ouId={{ouId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSystems_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListSystems_RequestSyntax) **   <a name="ngresiliencehub-ListSystems-request-uri-maxResults"></a>
Pagination page size.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListSystems_RequestSyntax) **   <a name="ngresiliencehub-ListSystems-request-uri-nextToken"></a>
Pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

 ** [ouId](#API_ListSystems_RequestSyntax) **   <a name="ngresiliencehub-ListSystems-request-uri-ouId"></a>
Filter systems by organizational unit (OU) identifier.
Length Constraints: Minimum length of 16. Maximum length of 68.
Pattern: `ou-[a-z0-9]{4,32}-[a-z0-9]{8,32}`

## Request Body
<a name="API_ListSystems_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSystems_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "systemSummaries": [
      {
         "createdAt": number,
         "name": "string",
         "organizationId": "string",
         "ouId": "string",
         "servicesCount": number,
         "systemArn": "string",
         "systemId": "string",
         "updatedAt": number,
         "userJourneysCount": number
      }
   ]
}
```

## Response Elements
<a name="API_ListSystems_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSystems_ResponseSyntax) **   <a name="ngresiliencehub-ListSystems-response-nextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

 ** [systemSummaries](#API_ListSystems_ResponseSyntax) **   <a name="ngresiliencehub-ListSystems-response-systemSummaries"></a>
The list of system summaries.
Type: Array of [SystemSummary](API_SystemSummary.md) objects

## Errors
<a name="API_ListSystems_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access denied — caller lacks required permissions.
HTTP Status Code: 403

 ** InternalServerException **
Internal service error.
HTTP Status Code: 500

 ** ValidationException **
Validation error — invalid input parameters.
 ** fieldList **
The list of fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListSystems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/ListSystems)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/ListSystems)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ListSystems)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/ListSystems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ListSystems)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/ListSystems)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/ListSystems)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/ListSystems)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/ListSystems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ListSystems)
