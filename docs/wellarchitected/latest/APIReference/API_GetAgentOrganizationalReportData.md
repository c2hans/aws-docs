---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAgentOrganizationalReportData.html
---

# GetAgentOrganizationalReportData
<a name="API_GetAgentOrganizationalReportData"></a>

**Important**
This operation is not available during the preview release.

Retrieves the data artifact for a completed Organizational Report as a short-lived presigned S3 URL. The response contains the URL in downloadUrl and its expiration in expiresAt. To have the service write the artifact directly into a caller-owned bucket instead, use SendAgentOrganizationalReportDataToS3.

## Request Syntax
<a name="API_GetAgentOrganizationalReportData_RequestSyntax"></a>

```
GET /api/v1/agent-organizational-reports/{{reportId}}/data?format={{format}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAgentOrganizationalReportData_RequestParameters"></a>

The request uses the following URI parameters.

 ** [format](#API_GetAgentOrganizationalReportData_RequestSyntax) **   <a name="wellarchitected-GetAgentOrganizationalReportData-request-uri-format"></a>
Format of the returned artifact (CSV, JSON, or PARQUET).
Valid Values: `CSV | JSON | PARQUET`
Required: Yes

 ** [reportId](#API_GetAgentOrganizationalReportData_RequestSyntax) **   <a name="wellarchitected-GetAgentOrganizationalReportData-request-uri-reportId"></a>
Identifier of the report whose data is being retrieved.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_GetAgentOrganizationalReportData_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAgentOrganizationalReportData_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "downloadUrl": "string",
   "expiresAt": "string"
}
```

## Response Elements
<a name="API_GetAgentOrganizationalReportData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [downloadUrl](#API_GetAgentOrganizationalReportData_ResponseSyntax) **   <a name="wellarchitected-GetAgentOrganizationalReportData-response-downloadUrl"></a>
Presigned URL that can be used to download the artifact.
Type: String

 ** [expiresAt](#API_GetAgentOrganizationalReportData_ResponseSyntax) **   <a name="wellarchitected-GetAgentOrganizationalReportData-response-expiresAt"></a>
Expiration time of downloadUrl.
Type: Timestamp

## Errors
<a name="API_GetAgentOrganizationalReportData_Errors"></a>

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
<a name="API_GetAgentOrganizationalReportData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/GetAgentOrganizationalReportData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/GetAgentOrganizationalReportData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/GetAgentOrganizationalReportData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/GetAgentOrganizationalReportData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/GetAgentOrganizationalReportData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/GetAgentOrganizationalReportData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/GetAgentOrganizationalReportData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/GetAgentOrganizationalReportData)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/GetAgentOrganizationalReportData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/GetAgentOrganizationalReportData)
