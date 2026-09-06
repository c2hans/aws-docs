---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ListSecurityRequirementPacks.html
---

# ListSecurityRequirementPacks
<a name="API_ListSecurityRequirementPacks"></a>

Lists all security requirement packs in the caller's account.

## Request Syntax
<a name="API_ListSecurityRequirementPacks_RequestSyntax"></a>

```
POST /ListSecurityRequirementPacks HTTP/1.1
Content-type: application/json

{
   "filter": {
      "managementType": "{{string}}",
      "status": "{{string}}"
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListSecurityRequirementPacks_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListSecurityRequirementPacks_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filter](#API_ListSecurityRequirementPacks_RequestSyntax) **   <a name="securityagent-ListSecurityRequirementPacks-request-filter"></a>
The filter criteria for listing security requirement packs.
Type: [ListSecurityRequirementPackFilter](API_ListSecurityRequirementPackFilter.md) object
Required: No

 ** [maxResults](#API_ListSecurityRequirementPacks_RequestSyntax) **   <a name="securityagent-ListSecurityRequirementPacks-request-maxResults"></a>
The maximum number of results to return in a single request.
Type: Integer
Required: No

 ** [nextToken](#API_ListSecurityRequirementPacks_RequestSyntax) **   <a name="securityagent-ListSecurityRequirementPacks-request-nextToken"></a>
The pagination token from a previous request to retrieve the next page of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListSecurityRequirementPacks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "securityRequirementPackSummaries": [
      {
         "createdAt": "string",
         "description": "string",
         "managementType": "string",
         "name": "string",
         "packId": "string",
         "status": "string",
         "updatedAt": "string",
         "vendorName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSecurityRequirementPacks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSecurityRequirementPacks_ResponseSyntax) **   <a name="securityagent-ListSecurityRequirementPacks-response-nextToken"></a>
The pagination token to use in a subsequent request to retrieve the next page of results.
Type: String

 ** [securityRequirementPackSummaries](#API_ListSecurityRequirementPacks_ResponseSyntax) **   <a name="securityagent-ListSecurityRequirementPacks-response-securityRequirementPackSummaries"></a>
The list of security requirement pack summaries.
Type: Array of [SecurityRequirementPackSummary](API_SecurityRequirementPackSummary.md) objects

## Errors
<a name="API_ListSecurityRequirementPacks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** message **
Error description.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during the processing of your request.
 ** message **
Error description.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
 ** message **
Error description.
 ** quotaCode **
Quota code for throttling limit.
 ** serviceCode **
Service code for throttling limit.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fieldList **
A list of specific failures encountered during validation.
 ** message **
A summary of the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListSecurityRequirementPacks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/ListSecurityRequirementPacks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/ListSecurityRequirementPacks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ListSecurityRequirementPacks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/ListSecurityRequirementPacks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ListSecurityRequirementPacks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/ListSecurityRequirementPacks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/ListSecurityRequirementPacks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/ListSecurityRequirementPacks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/ListSecurityRequirementPacks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ListSecurityRequirementPacks)
