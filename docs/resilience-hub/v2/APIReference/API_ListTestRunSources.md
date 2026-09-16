---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListTestRunSources.html
---

# ListTestRunSources
<a name="API_ListTestRunSources"></a>

Lists the monitoring source snapshots captured for a test run, optionally filtered by type.

## Request Syntax
<a name="API_ListTestRunSources_RequestSyntax"></a>

```
GET /v2/test-runs/{{testRunId}}/sources?maxResults={{maxResults}}&nextToken={{nextToken}}&serviceArn={{serviceArn}}&type={{type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTestRunSources_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListTestRunSources_RequestSyntax) **   <a name="ngresiliencehub-ListTestRunSources-request-uri-maxResults"></a>
Pagination page size.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListTestRunSources_RequestSyntax) **   <a name="ngresiliencehub-ListTestRunSources-request-uri-nextToken"></a>
Pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

 ** [serviceArn](#API_ListTestRunSources_RequestSyntax) **   <a name="ngresiliencehub-ListTestRunSources-request-uri-serviceArn"></a>
The ARN of the service the test run belongs to.
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [testRunId](#API_ListTestRunSources_RequestSyntax) **   <a name="ngresiliencehub-ListTestRunSources-request-uri-testRunId"></a>
The identifier of the test run to list sources for.
Length Constraints: Minimum length of 1.
Required: Yes

 ** [type](#API_ListTestRunSources_RequestSyntax) **   <a name="ngresiliencehub-ListTestRunSources-request-uri-type"></a>
Filter sources by type.
Valid Values: `SUCCESS_CRITERIA | OBSERVABILITY`

## Request Body
<a name="API_ListTestRunSources_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTestRunSources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "testRunSources": [
      { ... }
   ]
}
```

## Response Elements
<a name="API_ListTestRunSources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTestRunSources_ResponseSyntax) **   <a name="ngresiliencehub-ListTestRunSources-response-nextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

 ** [testRunSources](#API_ListTestRunSources_ResponseSyntax) **   <a name="ngresiliencehub-ListTestRunSources-response-testRunSources"></a>
The list of monitoring source snapshots.
Type: Array of [TestRunSourceSummary](API_TestRunSourceSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

## Errors
<a name="API_ListTestRunSources_Errors"></a>

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
<a name="API_ListTestRunSources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/ListTestRunSources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/ListTestRunSources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ListTestRunSources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/ListTestRunSources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ListTestRunSources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/ListTestRunSources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/ListTestRunSources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/ListTestRunSources)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/ListTestRunSources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ListTestRunSources)
