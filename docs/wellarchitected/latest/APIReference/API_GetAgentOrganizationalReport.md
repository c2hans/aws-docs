---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAgentOrganizationalReport.html
---

# GetAgentOrganizationalReport
<a name="API_GetAgentOrganizationalReport"></a>

**Important**
This operation is not available during the preview release.

Retrieves metadata and current state for a single Organizational Report. The coverageSummary is populated once the report reaches COMPLETED and is absent for reports still in progress or in a failed state.

## Request Syntax
<a name="API_GetAgentOrganizationalReport_RequestSyntax"></a>

```
GET /api/v1/agent-organizational-reports/{{reportId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAgentOrganizationalReport_RequestParameters"></a>

The request uses the following URI parameters.

 ** [reportId](#API_GetAgentOrganizationalReport_RequestSyntax) **   <a name="wellarchitected-GetAgentOrganizationalReport-request-uri-reportId"></a>
Identifier of the report to retrieve.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_GetAgentOrganizationalReport_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAgentOrganizationalReport_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "coverageSummary": {
      "accountsWithoutProfile": number,
      "accountsWithProfile": number,
      "failedAccountCount": number,
      "failedAccounts": [
         {
            "accountId": "string",
            "reason": "string"
         }
      ],
      "failedOrganizationalUnits": [
         {
            "organizationalUnitId": "string",
            "reason": "string"
         }
      ],
      "recommendationCountByPillar": [
         {
            "count": number,
            "pillar": "string"
         }
      ],
      "recommendationCountByPriority": [
         {
            "count": number,
            "priority": "string"
         }
      ],
      "totalAccountsInScope": number,
      "totalProfiles": number,
      "totalRecommendations": number
   },
   "createdAt": "string",
   "filters": {
      "accountIds": [ "string" ],
      "createdAtRange": {
         "from": "string",
         "to": "string"
      },
      "organizationalUnitIds": [ "string" ],
      "pillars": [ "string" ],
      "priorities": [ "string" ],
      "recommendationTypes": [ "string" ],
      "statuses": [ "string" ],
      "updatedAtRange": {
         "from": "string",
         "to": "string"
      }
   },
   "label": "string",
   "organizationId": "string",
   "ownerAccountId": "string",
   "reportId": "string",
   "state": "string"
}
```

## Response Elements
<a name="API_GetAgentOrganizationalReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [coverageSummary](#API_GetAgentOrganizationalReport_ResponseSyntax) **   <a name="wellarchitected-GetAgentOrganizationalReport-response-coverageSummary"></a>
Coverage and aggregate counts for the report. Present only after the report reaches COMPLETED.
Type: [CoverageSummary](API_CoverageSummary.md) object

 ** [createdAt](#API_GetAgentOrganizationalReport_ResponseSyntax) **   <a name="wellarchitected-GetAgentOrganizationalReport-response-createdAt"></a>
Timestamp at which the report was created.
Type: Timestamp

 ** [filters](#API_GetAgentOrganizationalReport_ResponseSyntax) **   <a name="wellarchitected-GetAgentOrganizationalReport-response-filters"></a>
Filters captured when the report was created. Absent when no filters were supplied (meaning the report covered the whole organization).
Type: [OrganizationalReportFilters](API_OrganizationalReportFilters.md) object

 ** [label](#API_GetAgentOrganizationalReport_ResponseSyntax) **   <a name="wellarchitected-GetAgentOrganizationalReport-response-label"></a>
Optional human-readable label supplied by the caller at creation time.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [organizationId](#API_GetAgentOrganizationalReport_ResponseSyntax) **   <a name="wellarchitected-GetAgentOrganizationalReport-response-organizationId"></a>
Identifier of the AWS Organization the report belongs to. Derived from the caller's authorization context at creation time and not accepted as a client-supplied input.
Type: String

 ** [ownerAccountId](#API_GetAgentOrganizationalReport_ResponseSyntax) **   <a name="wellarchitected-GetAgentOrganizationalReport-response-ownerAccountId"></a>
AWS account ID of the caller that created the report. Only this account or a delegated administrator of the same organization may retrieve or delete the report.
Type: String
Pattern: `\d{12}`

 ** [reportId](#API_GetAgentOrganizationalReport_ResponseSyntax) **   <a name="wellarchitected-GetAgentOrganizationalReport-response-reportId"></a>
Unique identifier of the Organizational Report assigned by the service at creation time.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [state](#API_GetAgentOrganizationalReport_ResponseSyntax) **   <a name="wellarchitected-GetAgentOrganizationalReport-response-state"></a>
Current lifecycle state of the report.
Type: String
Valid Values: `DISCOVERING | SNAPSHOTTING | AGGREGATING | COMPRESSING | COMPLETED | FAILED | DELETING`

## Errors
<a name="API_GetAgentOrganizationalReport_Errors"></a>

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

 ** ResourceNotFoundException **
The requested resource was not found.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 404

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
<a name="API_GetAgentOrganizationalReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/GetAgentOrganizationalReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/GetAgentOrganizationalReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/GetAgentOrganizationalReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/GetAgentOrganizationalReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/GetAgentOrganizationalReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/GetAgentOrganizationalReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/GetAgentOrganizationalReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/GetAgentOrganizationalReport)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/GetAgentOrganizationalReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/GetAgentOrganizationalReport)
