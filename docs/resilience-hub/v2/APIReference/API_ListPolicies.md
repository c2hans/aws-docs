---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListPolicies.html
---

# ListPolicies
<a name="API_ListPolicies"></a>

Lists resilience policies.

## Request Syntax
<a name="API_ListPolicies_RequestSyntax"></a>

```
GET /v2/list-policies?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPolicies_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListPolicies_RequestSyntax) **   <a name="ngresiliencehub-ListPolicies-request-uri-maxResults"></a>
Pagination page size.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListPolicies_RequestSyntax) **   <a name="ngresiliencehub-ListPolicies-request-uri-nextToken"></a>
Pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

## Request Body
<a name="API_ListPolicies_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPolicies_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "policySummaries": [
      {
         "associatedServiceCount": number,
         "availabilitySlo": {
            "target": number
         },
         "createdAt": number,
         "dataRecovery": {
            "timeBetweenBackupsInMinutes": number
         },
         "multiAz": {
            "disasterRecoveryApproach": "string",
            "rpoInMinutes": number,
            "rtoInMinutes": number
         },
         "multiRegion": {
            "disasterRecoveryApproach": "string",
            "rpoInMinutes": number,
            "rtoInMinutes": number
         },
         "name": "string",
         "policyArn": "string",
         "updatedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_ListPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPolicies_ResponseSyntax) **   <a name="ngresiliencehub-ListPolicies-response-nextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

 ** [policySummaries](#API_ListPolicies_ResponseSyntax) **   <a name="ngresiliencehub-ListPolicies-response-policySummaries"></a>
The list of policy summaries.
Type: Array of [PolicySummary](API_PolicySummary.md) objects

## Errors
<a name="API_ListPolicies_Errors"></a>

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
<a name="API_ListPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/ListPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/ListPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ListPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/ListPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ListPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/ListPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/ListPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/ListPolicies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/ListPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ListPolicies)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
