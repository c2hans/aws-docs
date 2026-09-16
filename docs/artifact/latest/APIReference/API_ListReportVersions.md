---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_ListReportVersions.html
---

# ListReportVersions
<a name="API_ListReportVersions"></a>

List available report versions for a given report.

## Request Syntax
<a name="API_ListReportVersions_RequestSyntax"></a>

```
GET /v1/report/listVersions?maxResults={{maxResults}}&nextToken={{nextToken}}&reportId={{reportId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListReportVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListReportVersions_RequestSyntax) **   <a name="artifact-ListReportVersions-request-uri-maxResults"></a>
Maximum number of resources to return in the paginated response.
Valid Range: Minimum value of 1. Maximum value of 300.

 ** [nextToken](#API_ListReportVersions_RequestSyntax) **   <a name="artifact-ListReportVersions-request-uri-nextToken"></a>
Pagination token to request the next page of resources.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [reportId](#API_ListReportVersions_RequestSyntax) **   <a name="artifact-ListReportVersions-request-uri-reportId"></a>
Unique resource ID for the report resource.
Pattern: `report-[a-zA-Z0-9]{16}`
Required: Yes

## Request Body
<a name="API_ListReportVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListReportVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "reports": [
      {
         "acceptanceType": "string",
         "arn": "string",
         "category": "string",
         "companyName": "string",
         "description": "string",
         "id": "string",
         "name": "string",
         "periodEnd": "string",
         "periodStart": "string",
         "productName": "string",
         "series": "string",
         "state": "string",
         "statusMessage": "string",
         "uploadState": "string",
         "version": number
      }
   ]
}
```

## Response Elements
<a name="API_ListReportVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListReportVersions_ResponseSyntax) **   <a name="artifact-ListReportVersions-response-nextToken"></a>
Pagination token to request the next page of resources.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [reports](#API_ListReportVersions_ResponseSyntax) **   <a name="artifact-ListReportVersions-response-reports"></a>
List of report resources.
Type: Array of [ReportSummary](API_ReportSummary.md) objects

## Errors
<a name="API_ListReportVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unknown server exception has occurred.
 ** retryAfterSeconds **
Number of seconds in which the caller can retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
Identifier of the affected resource.
 ** resourceType **
Type of the affected resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
 ** quotaCode **
Code for the affected quota.
 ** resourceId **
Identifier of the affected resource.
 ** resourceType **
Type of the affected resource.
 ** serviceCode **
Code for the affected service.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
 ** quotaCode **
Code for the affected quota.
 ** retryAfterSeconds **
Number of seconds in which the caller can retry the request.
 ** serviceCode **
Code for the affected service.
HTTP Status Code: 429

 ** ValidationException **
Request fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The field that caused the error, if applicable.
 ** reason **
Reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListReportVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/artifact-2018-05-10/ListReportVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/artifact-2018-05-10/ListReportVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/ListReportVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/artifact-2018-05-10/ListReportVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/ListReportVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/artifact-2018-05-10/ListReportVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/artifact-2018-05-10/ListReportVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/artifact-2018-05-10/ListReportVersions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/artifact-2018-05-10/ListReportVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/ListReportVersions)
