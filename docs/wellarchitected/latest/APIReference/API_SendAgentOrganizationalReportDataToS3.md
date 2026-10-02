---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_SendAgentOrganizationalReportDataToS3.html
---

# SendAgentOrganizationalReportDataToS3
<a name="API_SendAgentOrganizationalReportDataToS3"></a>

**Important**
This operation is not available during the preview release.

Writes the data artifact for a completed Organizational Report directly into a caller-owned S3 bucket. The artifact is written in the requested format to the supplied bucketArn and objectKey, and the resulting S3 location is returned in deliveredTo. This operation creates an S3 object and should not be retried indiscriminately. To download the artifact through a short-lived presigned URL instead, use GetAgentOrganizationalReportData.

## Request Syntax
<a name="API_SendAgentOrganizationalReportDataToS3_RequestSyntax"></a>

```
POST /api/v1/agent-organizational-reports/{{reportId}}/send-to-s3 HTTP/1.1
Content-type: application/json

{
   "bucketArn": "{{string}}",
   "format": "{{string}}",
   "objectKey": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SendAgentOrganizationalReportDataToS3_RequestParameters"></a>

The request uses the following URI parameters.

 ** [reportId](#API_SendAgentOrganizationalReportDataToS3_RequestSyntax) **   <a name="wellarchitected-SendAgentOrganizationalReportDataToS3-request-uri-reportId"></a>
Identifier of the report whose data is being delivered.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_SendAgentOrganizationalReportDataToS3_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [bucketArn](#API_SendAgentOrganizationalReportDataToS3_RequestSyntax) **   <a name="wellarchitected-SendAgentOrganizationalReportDataToS3-request-bucketArn"></a>
ARN of the caller-owned S3 bucket that will receive the artifact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[^:]+:s3:::.+`
Required: Yes

 ** [format](#API_SendAgentOrganizationalReportDataToS3_RequestSyntax) **   <a name="wellarchitected-SendAgentOrganizationalReportDataToS3-request-format"></a>
Format of the delivered artifact (CSV, JSON, or PARQUET).
Type: String
Valid Values: `CSV | JSON | PARQUET`
Required: Yes

 ** [objectKey](#API_SendAgentOrganizationalReportDataToS3_RequestSyntax) **   <a name="wellarchitected-SendAgentOrganizationalReportDataToS3-request-objectKey"></a>
S3 object key under bucketArn where the artifact will be written.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## Response Syntax
<a name="API_SendAgentOrganizationalReportDataToS3_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "deliveredTo": "string"
}
```

## Response Elements
<a name="API_SendAgentOrganizationalReportDataToS3_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deliveredTo](#API_SendAgentOrganizationalReportDataToS3_ResponseSyntax) **   <a name="wellarchitected-SendAgentOrganizationalReportDataToS3-response-deliveredTo"></a>
S3 URI (format s3://bucket/key) where the artifact was written.
Type: String

## Errors
<a name="API_SendAgentOrganizationalReportDataToS3_Errors"></a>

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
<a name="API_SendAgentOrganizationalReportDataToS3_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/SendAgentOrganizationalReportDataToS3)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/SendAgentOrganizationalReportDataToS3)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/SendAgentOrganizationalReportDataToS3)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/SendAgentOrganizationalReportDataToS3)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/SendAgentOrganizationalReportDataToS3)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/SendAgentOrganizationalReportDataToS3)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/SendAgentOrganizationalReportDataToS3)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/SendAgentOrganizationalReportDataToS3)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/SendAgentOrganizationalReportDataToS3)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/SendAgentOrganizationalReportDataToS3)
