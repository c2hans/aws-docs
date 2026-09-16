---
source_url: https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_GetQuotaUtilizationReport.html
---

# GetQuotaUtilizationReport
<a name="API_GetQuotaUtilizationReport"></a>

Retrieves the quota utilization report for your AWS account. This operation returns paginated results showing your quota usage across all AWS services, sorted by utilization percentage in descending order (highest utilization first).

You must first initiate a report using the `StartQuotaUtilizationReport` operation. The report generation process is asynchronous and may take several seconds to complete. Poll this operation periodically to check the status and retrieve results when the report is ready.

Each report contains up to 1,000 quota records per page. Use the `NextToken` parameter to retrieve additional pages of results. Reports are automatically deleted after 15 minutes.

**Related Actions**
+  [StartQuotaUtilizationReport](API_StartQuotaUtilizationReport.md)

## Request Syntax
<a name="API_GetQuotaUtilizationReport_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ReportId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetQuotaUtilizationReport_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_GetQuotaUtilizationReport_RequestSyntax) **   <a name="servicequotas-GetQuotaUtilizationReport-request-MaxResults"></a>
The maximum number of results to return per page. The default value is 1,000 and the maximum allowed value is 1,000.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_GetQuotaUtilizationReport_RequestSyntax) **   <a name="servicequotas-GetQuotaUtilizationReport-request-NextToken"></a>
A token that indicates the next page of results to retrieve. This token is returned in the response when there are more results available. Omit this parameter for the first request.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[a-zA-Z0-9/+]*={0,2}$`
Required: No

 ** [ReportId](#API_GetQuotaUtilizationReport_RequestSyntax) **   <a name="servicequotas-GetQuotaUtilizationReport-request-ReportId"></a>
The unique identifier for the quota utilization report. This identifier is returned by the `StartQuotaUtilizationReport` operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[0-9a-zA-Z][a-zA-Z0-9-]{1,128}`
Required: Yes

## Response Syntax
<a name="API_GetQuotaUtilizationReport_ResponseSyntax"></a>

```
{
   "ErrorCode": "string",
   "ErrorMessage": "string",
   "GeneratedAt": number,
   "NextToken": "string",
   "Quotas": [
      {
         "Adjustable": boolean,
         "AppliedValue": number,
         "DefaultValue": number,
         "Namespace": "string",
         "QuotaCode": "string",
         "QuotaName": "string",
         "ServiceCode": "string",
         "ServiceName": "string",
         "Utilization": number
      }
   ],
   "ReportId": "string",
   "Status": "string",
   "TotalCount": number
}
```

## Response Elements
<a name="API_GetQuotaUtilizationReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ErrorCode](#API_GetQuotaUtilizationReport_ResponseSyntax) **   <a name="servicequotas-GetQuotaUtilizationReport-response-ErrorCode"></a>
An error code indicating the reason for failure when the report status is `FAILED`. This field is only present when the status is `FAILED`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z][a-zA-Z0-9]*`

 ** [ErrorMessage](#API_GetQuotaUtilizationReport_ResponseSyntax) **   <a name="servicequotas-GetQuotaUtilizationReport-response-ErrorMessage"></a>
A detailed error message describing the failure when the report status is `FAILED`. This field is only present when the status is `FAILED`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `^.*$`

 ** [GeneratedAt](#API_GetQuotaUtilizationReport_ResponseSyntax) **   <a name="servicequotas-GetQuotaUtilizationReport-response-GeneratedAt"></a>
The timestamp when the report was generated, in ISO 8601 format.
Type: Timestamp

 ** [NextToken](#API_GetQuotaUtilizationReport_ResponseSyntax) **   <a name="servicequotas-GetQuotaUtilizationReport-response-NextToken"></a>
A token that indicates more results are available. Include this token in the next request to retrieve the next page of results. If this field is not present, you have retrieved all available results.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[a-zA-Z0-9/+]*={0,2}$`

 ** [Quotas](#API_GetQuotaUtilizationReport_ResponseSyntax) **   <a name="servicequotas-GetQuotaUtilizationReport-response-Quotas"></a>
A list of quota utilization records, sorted by utilization percentage in descending order. Each record includes the quota code, service code, service name, quota name, namespace, utilization percentage, default value, applied value, and whether the quota is adjustable. Up to 1,000 records are returned per page.
Type: Array of [QuotaUtilizationInfo](API_QuotaUtilizationInfo.md) objects
Array Members: Maximum number of 1000 items.

 ** [ReportId](#API_GetQuotaUtilizationReport_ResponseSyntax) **   <a name="servicequotas-GetQuotaUtilizationReport-response-ReportId"></a>
The unique identifier for the quota utilization report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[0-9a-zA-Z][a-zA-Z0-9-]{1,128}`

 ** [Status](#API_GetQuotaUtilizationReport_ResponseSyntax) **   <a name="servicequotas-GetQuotaUtilizationReport-response-Status"></a>
The current status of the report generation. Possible values are:
+  `PENDING` - The report generation is in progress. Retry this operation after a few seconds.
+  `IN_PROGRESS` - The report is being processed. Continue polling until the status changes to `COMPLETED`.
+  `COMPLETED` - The report is ready and quota utilization data is available in the response.
+  `FAILED` - The report generation failed. Check the `ErrorCode` and `ErrorMessage` fields for details.
Type: String
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED`

 ** [TotalCount](#API_GetQuotaUtilizationReport_ResponseSyntax) **   <a name="servicequotas-GetQuotaUtilizationReport-response-TotalCount"></a>
The total number of quotas included in the report across all pages.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.

## Errors
<a name="API_GetQuotaUtilizationReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permission to perform this action.
HTTP Status Code: 400

 ** IllegalArgumentException **
Invalid input was provided.
HTTP Status Code: 400

 ** InvalidPaginationTokenException **
Invalid input was provided.
HTTP Status Code: 400

 ** NoSuchResourceException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceException **
Something went wrong.
HTTP Status Code: 500

 ** TooManyRequestsException **
Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.
HTTP Status Code: 400

## See Also
<a name="API_GetQuotaUtilizationReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/service-quotas-2019-06-24/GetQuotaUtilizationReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/service-quotas-2019-06-24/GetQuotaUtilizationReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/service-quotas-2019-06-24/GetQuotaUtilizationReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/service-quotas-2019-06-24/GetQuotaUtilizationReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/service-quotas-2019-06-24/GetQuotaUtilizationReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/service-quotas-2019-06-24/GetQuotaUtilizationReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/service-quotas-2019-06-24/GetQuotaUtilizationReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/service-quotas-2019-06-24/GetQuotaUtilizationReport)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/service-quotas-2019-06-24/GetQuotaUtilizationReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/service-quotas-2019-06-24/GetQuotaUtilizationReport)
