---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateAgentOrganizationalReport.html
---

# CreateAgentOrganizationalReport
<a name="API_CreateAgentOrganizationalReport"></a>

**Important**
This operation is not available during the preview release.

Creates an Organizational Report, which is an asynchronously-materialized, point-in-time snapshot of recommendations across all Agent Profiles within the caller's AWS Organization. You can optionally narrow the scope with filters. The operation is idempotent on the caller-supplied clientToken. The AWS Organization the report belongs to is inferred from the caller's authorization context. Reports are retained for 90 days from creation, after which they are automatically deleted. Use DeleteAgentOrganizationalReport to delete a report earlier.

## Request Syntax
<a name="API_CreateAgentOrganizationalReport_RequestSyntax"></a>

```
POST /api/v1/agent-organizational-reports HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "filters": {
      "accountIds": [ "{{string}}" ],
      "createdAtRange": {
         "from": "{{string}}",
         "to": "{{string}}"
      },
      "organizationalUnitIds": [ "{{string}}" ],
      "pillars": [ "{{string}}" ],
      "priorities": [ "{{string}}" ],
      "recommendationTypes": [ "{{string}}" ],
      "statuses": [ "{{string}}" ],
      "updatedAtRange": {
         "from": "{{string}}",
         "to": "{{string}}"
      }
   },
   "label": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateAgentOrganizationalReport_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAgentOrganizationalReport_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateAgentOrganizationalReport_RequestSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalReport-request-clientToken"></a>
A caller-supplied idempotency token. Two create calls sharing the same token within the service's idempotency window return the same reportId.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [filters](#API_CreateAgentOrganizationalReport_RequestSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalReport-request-filters"></a>
Optional filters narrowing the report's scope. Absent means the report covers the whole organization.
Type: [OrganizationalReportFilters](API_OrganizationalReportFilters.md) object
Required: No

 ** [label](#API_CreateAgentOrganizationalReport_RequestSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalReport-request-label"></a>
Optional human-readable label (1-500 characters) that helps callers distinguish reports created with the same filters. Carried through list and get responses.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

## Response Syntax
<a name="API_CreateAgentOrganizationalReport_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "reportId": "string",
   "state": "string"
}
```

## Response Elements
<a name="API_CreateAgentOrganizationalReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [reportId](#API_CreateAgentOrganizationalReport_ResponseSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalReport-response-reportId"></a>
Unique identifier assigned to the newly-created report.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [state](#API_CreateAgentOrganizationalReport_ResponseSyntax) **   <a name="wellarchitected-CreateAgentOrganizationalReport-response-state"></a>
Lifecycle state of the report at the moment the create call returned. For a freshly-created report this is typically DISCOVERING.
Type: String
Valid Values: `DISCOVERING | SNAPSHOTTING | AGGREGATING | COMPRESSING | COMPLETED | FAILED | DELETING`

## Errors
<a name="API_CreateAgentOrganizationalReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** ConflictException **
The resource has already been processed, was deleted, or is too large.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 409

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The user has reached their resource quota.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 402

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
<a name="API_CreateAgentOrganizationalReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/CreateAgentOrganizationalReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/CreateAgentOrganizationalReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/CreateAgentOrganizationalReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/CreateAgentOrganizationalReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/CreateAgentOrganizationalReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/CreateAgentOrganizationalReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/CreateAgentOrganizationalReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/CreateAgentOrganizationalReport)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/CreateAgentOrganizationalReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/CreateAgentOrganizationalReport)
