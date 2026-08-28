---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListFailureModeFindings.html
---

# ListFailureModeFindings
<a name="API_ListFailureModeFindings"></a>

List findings.

## Request Syntax
<a name="API_ListFailureModeFindings_RequestSyntax"></a>

```
GET /v2/list-failure-mode-findings?failureCategory={{failureCategory}}&maxResults={{maxResults}}&nextToken={{nextToken}}&serviceArn={{serviceArn}}&severity={{severity}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListFailureModeFindings_RequestParameters"></a>

The request uses the following URI parameters.

 ** [failureCategory](#API_ListFailureModeFindings_RequestSyntax) **   <a name="ngresiliencehub-ListFailureModeFindings-request-uri-failureCategory"></a>
Filter findings by failure category.
Valid Values: `SHARED_FATE | EXCESSIVE_LOAD | EXCESSIVE_LATENCY | MISCONFIGURATION_AND_BUGS | SINGLE_POINT_OF_FAILURE`

 ** [maxResults](#API_ListFailureModeFindings_RequestSyntax) **   <a name="ngresiliencehub-ListFailureModeFindings-request-uri-maxResults"></a>
Pagination page size.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListFailureModeFindings_RequestSyntax) **   <a name="ngresiliencehub-ListFailureModeFindings-request-uri-nextToken"></a>
Pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

 ** [serviceArn](#API_ListFailureModeFindings_RequestSyntax) **   <a name="ngresiliencehub-ListFailureModeFindings-request-uri-serviceArn"></a>
ARN identifier.
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [severity](#API_ListFailureModeFindings_RequestSyntax) **   <a name="ngresiliencehub-ListFailureModeFindings-request-uri-severity"></a>
Filter findings by severity.
Valid Values: `LOW | MEDIUM | HIGH`

 ** [status](#API_ListFailureModeFindings_RequestSyntax) **   <a name="ngresiliencehub-ListFailureModeFindings-request-uri-status"></a>
Filter findings by status.
Valid Values: `OPEN | RESOLVED | IRRELEVANT`

## Request Body
<a name="API_ListFailureModeFindings_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListFailureModeFindings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "findingsSummary": [
      {
         "description": "string",
         "failureCategory": "string",
         "findingId": "string",
         "name": "string",
         "policyComponent": "string",
         "serviceArn": "string",
         "severity": "string",
         "status": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListFailureModeFindings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [findingsSummary](#API_ListFailureModeFindings_ResponseSyntax) **   <a name="ngresiliencehub-ListFailureModeFindings-response-findingsSummary"></a>
The list of finding summaries.
Type: Array of [FindingSummary](API_FindingSummary.md) objects

 ** [nextToken](#API_ListFailureModeFindings_ResponseSyntax) **   <a name="ngresiliencehub-ListFailureModeFindings-response-nextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

## Errors
<a name="API_ListFailureModeFindings_Errors"></a>

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
<a name="API_ListFailureModeFindings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/ListFailureModeFindings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/ListFailureModeFindings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ListFailureModeFindings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/ListFailureModeFindings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ListFailureModeFindings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/ListFailureModeFindings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/ListFailureModeFindings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/ListFailureModeFindings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/ListFailureModeFindings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ListFailureModeFindings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
