---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAgentOrganizationalReports.html
---

# ListAgentOrganizationalReports
<a name="API_ListAgentOrganizationalReports"></a>

**Important**
This operation is not available during the preview release.

Lists Organizational Reports owned by the caller's account within the caller's AWS Organization, ordered by most recently created first. Supports pagination and an optional state filter.

## Request Syntax
<a name="API_ListAgentOrganizationalReports_RequestSyntax"></a>

```
GET /api/v1/agent-organizational-reports?maxResults={{maxResults}}&nextToken={{nextToken}}&state={{state}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAgentOrganizationalReports_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListAgentOrganizationalReports_RequestSyntax) **   <a name="wellarchitected-ListAgentOrganizationalReports-request-uri-maxResults"></a>
The maximum number of results to return for this request.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListAgentOrganizationalReports_RequestSyntax) **   <a name="wellarchitected-ListAgentOrganizationalReports-request-uri-nextToken"></a>
The token to use to retrieve the next set of results.
Length Constraints: Minimum length of 1.
Pattern: `[A-Za-z0-9+\/=_-]+`

 ** [state](#API_ListAgentOrganizationalReports_RequestSyntax) **   <a name="wellarchitected-ListAgentOrganizationalReports-request-uri-state"></a>
Optional filter restricting the response to reports in a single lifecycle state.
Valid Values: `DISCOVERING | SNAPSHOTTING | AGGREGATING | COMPRESSING | COMPLETED | FAILED | DELETING`

## Request Body
<a name="API_ListAgentOrganizationalReports_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAgentOrganizationalReports_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "createdAt": "string",
         "label": "string",
         "organizationId": "string",
         "ownerAccountId": "string",
         "reportId": "string",
         "state": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAgentOrganizationalReports_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListAgentOrganizationalReports_ResponseSyntax) **   <a name="wellarchitected-ListAgentOrganizationalReports-response-items"></a>
Page of report summaries, most-recently-created first.
Type: Array of [OrganizationalReportSummary](API_OrganizationalReportSummary.md) objects

 ** [nextToken](#API_ListAgentOrganizationalReports_ResponseSyntax) **   <a name="wellarchitected-ListAgentOrganizationalReports-response-nextToken"></a>
The token to use to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[A-Za-z0-9+\/=_-]+`

## Errors
<a name="API_ListAgentOrganizationalReports_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ThrottlingException **
Request was denied due to request throttling.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 429

 ** ValidationException **
The user input is not valid.
 ** Fields **
The fields that caused the error, if applicable.
 ** Message **
Description of the error.
 ** Reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListAgentOrganizationalReports_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/ListAgentOrganizationalReports)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/ListAgentOrganizationalReports)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ListAgentOrganizationalReports)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/ListAgentOrganizationalReports)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ListAgentOrganizationalReports)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/ListAgentOrganizationalReports)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/ListAgentOrganizationalReports)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/ListAgentOrganizationalReports)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/ListAgentOrganizationalReports)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ListAgentOrganizationalReports)
